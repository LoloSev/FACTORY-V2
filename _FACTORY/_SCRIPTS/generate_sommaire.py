"""
generate_sommaire.py
ROLE    : Compute SOMMAIRE from POOLS + QUESTIONS + QA TSV files.
INPUT   : _FACTORY/_LIGNES/[THEME]/ (POOLS.tsv, QUESTIONS.tsv, QA.tsv)
OUTPUT  : stdout table + optional SOMMAIRE.tsv
TRIGGER : On demand
"""

import sys
import csv
from pathlib import Path
from collections import defaultdict


def read_tsv(path):
    if not path.exists():
        return []
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def generate(theme_dir: Path, write_tsv: bool = False):
    pools      = read_tsv(theme_dir / 'POOLS.tsv')
    questions  = read_tsv(theme_dir / 'QUESTIONS.tsv')
    qa_rows    = read_tsv(theme_dir / 'QA.tsv')

    # Index QA by Q_ID
    qa_index = {r['Q_ID']: r for r in qa_rows if r.get('Q_ID')}

    # Count questions and QA status per pool
    q_per_pool   = defaultdict(list)
    for q in questions:
        pid = q.get('POOL_ID', '')
        if pid:
            q_per_pool[pid].append(q.get('Q_ID', ''))

    qa_counts = defaultdict(lambda: {'PASS': 0, 'WARNING': 0, 'FAIL': 0, 'DRAFT': 0})
    for qid, row in qa_index.items():
        pid    = row.get('POOL_ID', '')
        status = row.get('QA_STATUS', 'DRAFT').upper()
        if status == 'PASS':
            qa_counts[pid]['PASS'] += 1
        elif status in ('WARNING', 'WARN'):
            qa_counts[pid]['WARNING'] += 1
        elif status == 'FAIL':
            qa_counts[pid]['FAIL'] += 1
        else:
            qa_counts[pid]['DRAFT'] += 1

    headers = ['POOL_ID', 'TYPE', 'POSITION_QUIZ', 'THEME_LABEL', 'MODE',
               'COUVERTURE_NIVEAU', 'STOCK_CIBLE', 'STOCK_ACTUEL',
               'Q_PASS', 'Q_WARNING', 'Q_FAIL', 'PCT_COMPLET']

    rows = []
    for p in pools:
        pid          = p.get('POOL_ID', '')
        stock_cible  = int(p.get('STOCK_CIBLE', 0) or 0)
        stock_actuel = len(q_per_pool.get(pid, []))
        counts       = qa_counts.get(pid, {'PASS': 0, 'WARNING': 0, 'FAIL': 0, 'DRAFT': 0})
        pct          = f"{(stock_actuel / stock_cible * 100):.0f}%" if stock_cible else 'N/A'
        rows.append({
            'POOL_ID':           pid,
            'TYPE':              p.get('TYPE', ''),
            'POSITION_QUIZ':     p.get('POSITION_QUIZ', ''),
            'THEME_LABEL':       p.get('THEME_LABEL', ''),
            'MODE':              p.get('MODE', ''),
            'COUVERTURE_NIVEAU': p.get('COUVERTURE_NIVEAU', ''),
            'STOCK_CIBLE':       stock_cible,
            'STOCK_ACTUEL':      stock_actuel,
            'Q_PASS':            counts['PASS'],
            'Q_WARNING':         counts['WARNING'],
            'Q_FAIL':            counts['FAIL'],
            'PCT_COMPLET':       pct,
        })

    # Print table
    col_w = {h: max(len(h), max((len(str(r[h])) for r in rows), default=0)) for h in headers}
    sep = '+' + '+'.join('-' * (col_w[h] + 2) for h in headers) + '+'
    print(sep)
    print('|' + '|'.join(f' {h:<{col_w[h]}} ' for h in headers) + '|')
    print(sep)
    for row in rows:
        print('|' + '|'.join(f' {str(row[h]):<{col_w[h]}} ' for h in headers) + '|')
    print(sep)
    print(f'\nSTOCK_TOTAL: {sum(r["STOCK_ACTUEL"] for r in rows)} / {sum(r["STOCK_CIBLE"] for r in rows)}')

    # Optional TSV output
    if write_tsv:
        out = theme_dir / 'SOMMAIRE.tsv'
        with open(out, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(rows)
        print(f'SOMMAIRE.tsv written: {out}')

    return rows


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python generate_sommaire.py [THEME_DIR] [--write-tsv]')
        print('Example: python generate_sommaire.py ../_LIGNES/MAYENNE --write-tsv')
        sys.exit(1)
    theme_dir  = Path(sys.argv[1])
    write_tsv  = '--write-tsv' in sys.argv
    if not theme_dir.is_dir():
        print(f'ERROR: directory not found: {theme_dir}')
        sys.exit(1)
    generate(theme_dir, write_tsv)
