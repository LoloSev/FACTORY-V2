#!/usr/bin/env python3
"""
gate_b5.py — Gate B5 : validation audit QA
Usage: python gate_b5.py <B5_LIGNE.xlsx> <LIGNE>

Checks :
  B5-1  Prérequis B3 = GO
  B5-2  QA_STATUS renseigné pour toutes les questions
  B5-3  QA_STATUS = FAIL count → bloquant si > 0 non résolu
  B5-4  DÉCISION renseignée (CONSERVER/MODIFIER/REJETER/DÉPLACER)
  B5-5  Synthèse : DÉCISION_GATE renseignée sur tous les pools
  B5-6  Stock total (feuille SYNTHÈSE : somme PASS ≥ 90% total)
  B5-7  FICHE_VEILLE présente dans le dossier de la ligne
  B5-8  Marqueurs veille détectés dans libellés (warning)

GO → déverrouille EXPORT | NO_GO → EXPORT LOCKED
"""
import sys
import re
import argparse
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))
from gate_utils import (already_evaluated, update_gate, update_dashboard,
                        header, footer, load_sheet, load_state)

MARQUEURS_VEILLE = [
    "dernier","dernière","premier","première","jamais","encore jamais",
    "seul","unique","record","recordman","recordwoman",
    "plus grand","plus petit","plus rapide","meilleur","pire","à ce jour",
]

def check_prereq_b3(ligne):
    state = load_state()
    try:
        status = state["lignes"][ligne]["gates"]["B3"]["status"]
        if status != "GO":
            return f"B5-1 : Gate B3 = {status} — B5 ne peut pas être validée"
    except (KeyError, TypeError):
        return "B5-1 : Gate B3 non évaluée"
    return None

def check_qa_rows(rows):
    fails    = []
    warnings = []

    statuts = Counter()
    for r in rows:
        qid     = r.get("Q_ID","?")
        status  = r.get("QA_STATUS","")
        decision= r.get("DÉCISION","")
        libelle = r.get("LIBELLÉ_Q","")

        # B5-2 QA_STATUS renseigné
        if not status:
            fails.append(f"B5-2 QA_STATUS absent — {qid}")
            continue
        statuts[status] += 1

        # B5-3 FAIL non résolu
        if status == "FAIL":
            fails.append(f"B5-3 QA_STATUS=FAIL non résolu — {qid}")

        # B5-4 DÉCISION renseignée
        if not decision:
            fails.append(f"B5-4 DÉCISION absente — {qid}")

        # B5-8 marqueurs veille
        lib_l = libelle.lower()
        for m in MARQUEURS_VEILLE:
            if m in lib_l:
                warnings.append(f"B5-8 marqueur veille '{m}' — {qid}: '{libelle[:60]}'")
                break

    return fails, warnings, statuts

def check_synthese(rows):
    fails = []
    for r in rows:
        pool = r.get("POOL_ID","?")
        gate = r.get("DÉCISION_GATE","")
        if not gate:
            fails.append(f"B5-5 DÉCISION_GATE absente — pool {pool}")
    return fails

def check_fiche_veille(fichier, ligne):
    """Cherche FICHE_VEILLE dans le dossier de la ligne."""
    ligne_dir = Path(fichier).parent.parent
    patterns  = ["*FICHE_VEILLE*", "*VEILLE*", "*veille*"]
    for pat in patterns:
        if list(ligne_dir.rglob(pat)):
            return None
    return f"B5-7 FICHE_VEILLE introuvable dans {ligne_dir.name}"

def run(fichier, ligne):
    path = Path(fichier)
    if not path.exists():
        print(f"ERREUR : fichier introuvable — {fichier}"); sys.exit(2)

    cached, mtime = already_evaluated(fichier, ligne, "B5")
    if cached:
        state = load_state()
        verdict = state["lignes"][ligne]["gates"]["B5"]["status"]
        print(f"\nGATE B5 [{ligne}] — déjà évalué\nVERDICT : {verdict} (inchangé)\n")
        return verdict

    header("B5", ligne, fichier)
    fails    = []
    warnings = []

    prereq = check_prereq_b3(ligne)
    if prereq:
        fails.append(prereq)

    # Feuille QA
    qa_rows, err = load_sheet(path, "QA")
    if err:
        fails.append(f"LECTURE QA : {err}")
    else:
        print(f"Questions QA chargées : {len(qa_rows)}\n")
        f2, w2, statuts = check_qa_rows(qa_rows)
        fails    += f2
        warnings += w2
        print(f"  Distribution QA_STATUS : {dict(statuts)}")

    # Feuille SYNTHÈSE
    synth_rows, err2 = load_sheet(path, "SYNTHÈSE")
    if err2:
        warnings.append(f"LECTURE SYNTHÈSE : {err2}")
    elif synth_rows:
        fails += check_synthese(synth_rows)

        # B5-6 stock PASS
        total_pass  = sum(int(r.get("PASS","0") or 0) for r in synth_rows)
        total_q     = sum(int(r.get("TOTAL_Q","0") or 0) for r in synth_rows)
        if total_q > 0:
            taux = total_pass / total_q * 100
            print(f"  PASS : {total_pass}/{total_q} ({taux:.0f}%)")
            if taux < 90:
                fails.append(f"B5-6 taux PASS {taux:.0f}% < 90% — {total_pass}/{total_q} questions")

    # B5-7 FICHE_VEILLE
    fv_fail = check_fiche_veille(fichier, ligne)
    if fv_fail:
        fails.append(fv_fail)

    for f in fails:    print(f"  ✗ {f}")
    for w in warnings: print(f"  ⚠ {w}")

    verdict = "NO_GO" if fails else "GO"
    footer("B5", ligne, verdict, "EXPORT")
    update_gate(ligne, "B5", fichier, mtime, verdict, fails, next_etape="EXPORT")
    update_dashboard(ligne, "B5", verdict, fails)
    return verdict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gate B5 — Audit QA")
    parser.add_argument("fichier"); parser.add_argument("ligne")
    args = parser.parse_args()
    verdict = run(args.fichier, args.ligne)
    sys.exit(0 if verdict == "GO" else 1)
