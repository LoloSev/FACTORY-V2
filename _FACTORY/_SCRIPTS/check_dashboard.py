"""
check_dashboard.py
Vérifie si les dashboards ont besoin d'être rafraîchis.
Détecte aussi les xlsx de pipeline modifiés et déclenche les gates correspondantes.
Retourne REFRESH_NEEDED ou NO_OP.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT       = Path(__file__).parent.parent
STATE_FILE = ROOT / "_STATE" / "DASHBOARD_STATE.json"
STAMP_FILE = ROOT / "_STATE" / ".dashboard_stamp.json"
PIPE_STATE = ROOT / "_STATE" / "pipeline_state.json"
LIGNES_DIR = ROOT / "_LIGNES"

# Mapping étape → script gate + pattern fichier
GATE_MAP = {
    "A4": {
        "script":  ROOT / "_SCRIPTS" / "gate_a4.py",
        "pattern": "A4_POOLS/A4_*.xlsx",
    },
    "B2": {
        "script":  ROOT / "_SCRIPTS" / "gate_b2.py",
        "pattern": "B2_GENERATION/B2_*.xlsx",
    },
    "B3": {
        "script":  ROOT / "_SCRIPTS" / "gate_b3.py",
        "pattern": "B3_DISTRACTEURS/B3_*.xlsx",
    },
    "B5": {
        "script":  ROOT / "_SCRIPTS" / "gate_b5.py",
        "pattern": "B5_AUDIT/B5_*.xlsx",
    },
    "EXPORT": {
        "script":  ROOT / "_SCRIPTS" / "gate_export.py",
        "pattern": "EXPORT/QUIZ_*_EXPORT.xlsx",
    },
}

def load_pipe_state():
    if not PIPE_STATE.exists():
        return {}
    try:
        return json.loads(PIPE_STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}

def get_prev_mtime(pipe_state, ligne, etape):
    try:
        return pipe_state["lignes"][ligne]["gates"][etape]["fichier_mtime"]
    except (KeyError, TypeError):
        return None

def detect_ligne(path, etape):
    """Extrait le code ligne depuis le nom de fichier : A4_MAYENNE.xlsx → MAYENNE"""
    prefix = etape + "_"
    stem = path.stem  # ex: A4_MAYENNE
    if stem.upper().startswith(prefix):
        return stem[len(prefix):].upper()
    # Fallback : nom du dossier grand-parent
    return path.parent.parent.name.lstrip("_").upper()

def scan_and_run_gates():
    """Scanne les xlsx de pipeline, déclenche les gates si fichier modifié."""
    if not LIGNES_DIR.exists():
        return False

    pipe_state = load_pipe_state()
    gate_triggered = False

    for ligne_dir in sorted(LIGNES_DIR.iterdir()):
        if not ligne_dir.is_dir():
            continue
        # Les lignes factory sont nommées avec un préfixe "_" (_CDM, _MAYENNE, etc.).
        # Ne pas les ignorer, sinon les gates ne tournent jamais.
        if ligne_dir.name.upper() in {"_TEMPLATE", "_ARCHIVE"} or ligne_dir.name.startswith("."):
            continue
        ligne = ligne_dir.name.lstrip("_").upper()

        for etape, cfg in GATE_MAP.items():
            script = cfg["script"]
            if not script.exists():
                continue  # gate pas encore codée

            # Trouver le xlsx correspondant
            xlsx_files = list(ligne_dir.glob(cfg["pattern"]))
            if not xlsx_files:
                continue

            xlsx = max(xlsx_files, key=lambda f: f.stat().st_mtime)
            mtime = xlsx.stat().st_mtime
            prev_mtime = get_prev_mtime(pipe_state, ligne, etape)

            if mtime == prev_mtime:
                continue  # pas modifié

            # Fichier modifié → lancer la gate
            print(f"  → Gate {etape} [{ligne}] : {xlsx.name} modifié — lancement gate_{etape.lower()}.py")
            result = subprocess.run(
                [sys.executable, str(script), str(xlsx), ligne],
                capture_output=True, text=True
            )
            if result.stdout:
                print(result.stdout)
            if result.returncode == 0:
                print(f"     ✓ Gate {etape} [{ligne}] : GO")
            else:
                print(f"     ✗ Gate {etape} [{ligne}] : NO_GO — voir dashboard")

            gate_triggered = True
            # Recharger pipe_state après mise à jour par le script gate
            pipe_state = load_pipe_state()

    return gate_triggered

def run():
    # 1. Scanner et déclencher gates si xlsx modifiés
    gate_triggered = scan_and_run_gates()

    # 2. Vérifier si dashboard doit être rafraîchi
    if not STATE_FILE.exists():
        print("REFRESH_NEEDED (state absent)")
        return

    state_mtime = os.path.getmtime(STATE_FILE)

    if STAMP_FILE.exists() and not gate_triggered:
        try:
            stamp = json.loads(STAMP_FILE.read_text())
            if stamp.get("state_mtime") == state_mtime:
                print("NO_OP")
                return
        except Exception:
            pass

    state = json.loads(STATE_FILE.read_text())
    if gate_triggered:
        print(f"REFRESH_NEEDED (gates déclenchées)")
    else:
        print(f"REFRESH_NEEDED (état mis à jour le {state.get('last_updated','?')})")

if __name__ == "__main__":
    run()
