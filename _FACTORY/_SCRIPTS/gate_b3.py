#!/usr/bin/env python3
"""
gate_b3.py — Gate B3 : validation distracteurs
Usage: python gate_b3.py <B3_LIGNE.xlsx> <LIGNE>

Checks :
  B3-1  Prérequis B2 = GO
  B3-2  Champs obligatoires (Q_ID, D1, D2, D3, NIVEAU_CONFIRMÉ, ÉCART_CIBLE)
  B3-3  D1 / D2 / D3 présents
  B3-4  Unicité intra-question (D1 ≠ D2 ≠ D3 ≠ RÉPONSE)
  B3-5  Collision distracteur = réponse ailleurs (inter-questions)
  B3-6  ÉCART_CIBLE renseigné
  B3-7  Format homogénéité basique (casse initiale cohérente)
  B3-8  Distribution NIVEAU_CONFIRMÉ (N1/N2/N3 — warning si déséquilibre)

GO → déverrouille B5 | NO_GO → B5 LOCKED
"""
import sys
import re
import argparse
from pathlib import Path
from collections import Counter, defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from gate_utils import (already_evaluated, update_gate, update_dashboard,
                        header, footer, load_sheet, load_state)

def check_prereq_b2(ligne):
    state = load_state()
    try:
        status = state["lignes"][ligne]["gates"]["B2"]["status"]
        if status != "GO":
            return f"B3-1 : Gate B2 = {status} — B3 ne peut pas être validée"
    except (KeyError, TypeError):
        return "B3-1 : Gate B2 non évaluée"
    return None

def normalize(s):
    return s.strip().lower() if s else ""

def check_distracteurs(rows):
    fails    = []
    warnings = []

    # Index réponses pour collision inter-questions
    rep_index = defaultdict(list)
    for r in rows:
        rep = normalize(r.get("RÉPONSE",""))
        if rep:
            rep_index[rep].append(r.get("Q_ID","?"))

    niveau_counts = Counter()

    for r in rows:
        qid  = r.get("Q_ID","?")
        rep  = r.get("RÉPONSE","")
        d1   = r.get("D1","")
        d2   = r.get("D2","")
        d3   = r.get("D3","")
        niv  = r.get("NIVEAU_CONFIRMÉ","")
        ecar = r.get("ÉCART_CIBLE","")

        # B3-3 présence
        if not d1: fails.append(f"B3-3 D1 absent — {qid}")
        if not d2: fails.append(f"B3-3 D2 absent — {qid}")
        if not d3: fails.append(f"B3-3 D3 absent — {qid}")

        # B3-6 champs
        if not niv:  fails.append(f"B3-2 NIVEAU_CONFIRMÉ absent — {qid}")
        if not ecar: fails.append(f"B3-6 ÉCART_CIBLE absent — {qid}")
        else:
            niveau_counts[niv] += 1

        if not (d1 and d2 and d3):
            continue

        # B3-4 unicité intra-question
        vals = [normalize(d1), normalize(d2), normalize(d3)]
        if len(vals) != len(set(vals)):
            fails.append(f"B3-4 distracteurs non uniques — {qid}: D1={d1} D2={d2} D3={d3}")
        rep_n = normalize(rep)
        for dx, dv in [("D1",d1),("D2",d2),("D3",d3)]:
            if normalize(dv) == rep_n and rep_n:
                fails.append(f"B3-4 {dx}=RÉPONSE — {qid}: '{dv}'")

        # B3-5 collision distracteur = réponse ailleurs
        for dx, dv in [("D1",d1),("D2",d2),("D3",d3)]:
            dv_n = normalize(dv)
            if dv_n and dv_n in rep_index:
                others = [x for x in rep_index[dv_n] if x != qid]
                if others:
                    fails.append(f"B3-5 {dx}='{dv}' est réponse de {others} — {qid}")

        # B3-7 format homogénéité (casse initiale)
        def starts_upper(s): return s and s[0].isupper()
        ref_case = starts_upper(rep)
        for dx, dv in [("D1",d1),("D2",d2),("D3",d3)]:
            if dv and starts_upper(dv) != ref_case:
                warnings.append(f"B3-7 casse incohérente {dx}='{dv}' vs RÉPONSE='{rep}' — {qid}")
                break

    # B3-8 distribution niveaux
    total_niv = sum(niveau_counts.values())
    if total_niv > 0:
        for niv, count in niveau_counts.items():
            pct = count / total_niv * 100
            if pct < 20 or pct > 50:
                warnings.append(f"B3-8 distribution {niv}={count} ({pct:.0f}%) — cible 30/40/30 ±10%")

    return fails, warnings

def run(fichier, ligne):
    path = Path(fichier)
    if not path.exists():
        print(f"ERREUR : fichier introuvable — {fichier}"); sys.exit(2)

    cached, mtime = already_evaluated(fichier, ligne, "B3")
    if cached:
        state = load_state()
        verdict = state["lignes"][ligne]["gates"]["B3"]["status"]
        print(f"\nGATE B3 [{ligne}] — déjà évalué\nVERDICT : {verdict} (inchangé)\n")
        return verdict

    header("B3", ligne, fichier)
    fails = []
    warnings = []

    prereq = check_prereq_b2(ligne)
    if prereq:
        fails.append(prereq)

    rows, err = load_sheet(path, "DISTRACTEURS")
    if err:
        fails.append(f"LECTURE : {err}")
    else:
        print(f"Distracteurs chargés : {len(rows)}\n")
        f2, w2 = check_distracteurs(rows)
        fails    += f2
        warnings += w2

    for f in fails:    print(f"  ✗ {f}")
    for w in warnings: print(f"  ⚠ {w}")

    verdict = "NO_GO" if fails else "GO"
    footer("B3", ligne, verdict, "B5")
    update_gate(ligne, "B3", fichier, mtime, verdict, fails, next_etape="B5")
    update_dashboard(ligne, "B3", verdict, fails)
    return verdict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gate B3 — Distracteurs")
    parser.add_argument("fichier"); parser.add_argument("ligne")
    args = parser.parse_args()
    verdict = run(args.fichier, args.ligne)
    sys.exit(0 if verdict == "GO" else 1)
