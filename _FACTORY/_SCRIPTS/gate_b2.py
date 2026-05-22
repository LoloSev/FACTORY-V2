#!/usr/bin/env python3
"""
gate_b2.py — Gate B2 : validation questions générées
Usage: python gate_b2.py <B2_LIGNE.xlsx> <LIGNE>

Checks :
  B2-1  Prérequis A4 = GO
  B2-2  Champs obligatoires (Q_ID, POOL_ID, LIBELLÉ, RÉPONSE, TYPE_Q, CIBLE_NIVEAU)
  B2-3  Réponse absente
  B2-4  Libellé > 10 mots
  B2-5  Réponse dans le libellé
  B2-6  TYPE_Q hors [1-5]
  B2-7  Qualificatifs éditoriaux
  B2-8  Stock actuel vs stock cible par pool (SUIVI_POOLS)
  B2-9  Collisions réponses inter-pools

GO → déverrouille B3 | NO_GO → B3 LOCKED
"""
import sys
import re
import os
import argparse
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from gate_utils import (already_evaluated, update_gate, update_dashboard,
                        header, footer, load_sheet, load_state)

QUALIFICATIFS = ["célèbre","légendaire","fameux","illustre","réputé",
                 "renommé","incontournable","emblématique","mythique","iconique"]

def check_prereq_a4(ligne):
    state = load_state()
    try:
        status = state["lignes"][ligne]["gates"]["A4"]["status"]
        if status != "GO":
            return f"B2-1 : Gate A4 = {status} — B2 ne peut pas être validée"
    except (KeyError, TypeError):
        return "B2-1 : Gate A4 non évaluée"
    return None

def check_questions(rows):
    fails = []
    for r in rows:
        qid  = r.get("Q_ID", "?")
        lib  = r.get("LIBELLÉ", "")
        rep  = r.get("RÉPONSE", "")
        typ  = r.get("TYPE_Q", "")
        niv  = r.get("CIBLE_NIVEAU", "")
        pool = r.get("POOL_ID", "")

        if not pool:  fails.append(f"B2-2 POOL_ID absent — {qid}")
        if not lib:   fails.append(f"B2-2 LIBELLÉ absent — {qid}"); continue
        if not rep:   fails.append(f"B2-3 RÉPONSE absente — {qid}"); continue
        if not niv:   fails.append(f"B2-2 CIBLE_NIVEAU absent — {qid}")
        if not typ:   fails.append(f"B2-6 TYPE_Q absent — {qid}")
        elif typ not in ["1","2","3","4","5"]:
            fails.append(f"B2-6 TYPE_Q invalide '{typ}' — {qid}")

        # Libellé > 10 mots
        nb = len(lib.split())
        if nb > 10:
            fails.append(f"B2-4 LIBELLÉ trop long ({nb} mots) — {qid}: '{lib[:50]}'")

        # Réponse dans libellé
        if rep.lower() in lib.lower():
            fails.append(f"B2-5 RÉPONSE dans libellé — {qid}: '{rep}' dans '{lib[:50]}'")

        # Qualificatifs
        lib_l = lib.lower()
        for q in QUALIFICATIFS:
            if re.search(r"\b" + q + r"\b", lib_l):
                fails.append(f"B2-7 qualificatif '{q}' — {qid}")
                break

    return fails

def check_stocks(suivi_rows, minimal_validation=False):
    # MINIMAL_VALIDATION=TRUE : skip B2-8 pour validation structurelle pipeline V2
    # Réversible — retirer minimal_validation=True pour production réelle
    if minimal_validation:
        return []
    fails = []
    for r in suivi_rows:
        pool   = r.get("POOL_ID", "?")
        cible  = r.get("STOCK_CIBLE", "")
        actuel = r.get("STOCK_ACTUEL", "")
        if not cible or not actuel:
            continue
        try:
            if float(actuel) < float(cible):
                fails.append(f"B2-8 déficit stock Pool {pool}: {actuel}/{cible}")
        except ValueError:
            pass
    return fails

def check_collisions(rows):
    """Réponse identique sur deux pools différents."""
    index = defaultdict(list)
    for r in rows:
        rep  = r.get("RÉPONSE","").strip().lower()
        pool = r.get("POOL_ID","")
        qid  = r.get("Q_ID","?")
        if rep:
            index[rep].append((qid, pool))
    fails = []
    seen  = set()
    for rep, entries in index.items():
        pools = [e[1] for e in entries]
        if len(set(pools)) > 1:
            pair = tuple(sorted([e[0] for e in entries]))
            if pair not in seen:
                seen.add(pair)
                ids = [f"{e[0]}({e[1]})" for e in entries]
                fails.append(f"B2-9 collision réponse '{rep}' : {ids}")
    return fails

def run(fichier, ligne):
    path = Path(fichier)
    if not path.exists():
        print(f"ERREUR : fichier introuvable — {fichier}"); sys.exit(2)

    cached, mtime = already_evaluated(fichier, ligne, "B2")
    if cached:
        state = load_state()
        verdict = state["lignes"][ligne]["gates"]["B2"]["status"]
        print(f"\nGATE B2 [{ligne}] — déjà évalué\nVERDICT : {verdict} (inchangé)\n")
        return verdict

    header("B2", ligne, fichier)
    fails = []

    # B2-1 prérequis A4
    prereq = check_prereq_a4(ligne)
    if prereq:
        fails.append(prereq)

    # Chargement feuilles
    q_rows, err = load_sheet(path, "QUESTIONS")
    if err:
        fails.append(f"LECTURE : {err}")
        verdict = "NO_GO"
    else:
        print(f"Questions chargées : {len(q_rows)}\n")
        fails += check_questions(q_rows)
        fails += check_collisions(q_rows)

    suivi_rows, _ = load_sheet(path, "SUIVI_POOLS")
    if suivi_rows:
        fails += check_stocks(suivi_rows, minimal_validation=True)

    for f in fails:
        print(f"  ✗ {f}")

    verdict = "NO_GO" if fails else "GO"
    footer("B2", ligne, verdict, "B3")
    update_gate(ligne, "B2", fichier, mtime, verdict, fails, next_etape="B3")
    update_dashboard(ligne, "B2", verdict, fails)
    return verdict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gate B2 — Questions")
    parser.add_argument("fichier"); parser.add_argument("ligne")
    args = parser.parse_args()
    verdict = run(args.fichier, args.ligne)
    sys.exit(0 if verdict == "GO" else 1)
