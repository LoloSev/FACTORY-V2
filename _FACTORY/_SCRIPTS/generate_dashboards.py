"""
generate_dashboards.py
Génère un dashboard unifié depuis DASHBOARD_STATE.json + pipeline_state.json.
Output : .dashboard_factory_main.html  (unique)
"""
import json, os
from pathlib import Path
from datetime import date

ROOT       = Path(__file__).parent.parent
STATE_FILE = ROOT / "_STATE" / "DASHBOARD_STATE.json"
PIPE_FILE  = ROOT / "_STATE" / "pipeline_state.json"
STAMP_FILE = ROOT / "_STATE" / ".dashboard_stamp.json"
OUT_MAIN   = ROOT / "_STATE" / ".dashboard_factory_main.html"

state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
pipe  = json.loads(PIPE_FILE.read_text(encoding="utf-8")) if PIPE_FILE.exists() else {}

lignes       = state.get("lignes", {})
pipe_lignes  = pipe.get("lignes", {})
tasks_open   = state.get("tasks_open", [])
tasks_wait   = state.get("tasks_en_attente", [])
tasks_done   = state.get("tasks_done_session", [])
alertes      = state.get("alertes_glossaire", [])
incoherences = state.get("incerences_v1_v2", [])
updated      = state.get("last_updated", str(date.today()))

STADE_COLOR = {
    "A2": "#3b82f6", "A3": "#6366f1", "A4": "#8b5cf6",
    "B2": "#f59e0b", "B3": "#f97316", "B5": "#ef4444",
    "EXPORT": "#22c55e"
}
GATE_COLOR = {
    "GO":      "#22c55e",
    "NO_GO":   "#ef4444",
    "LOCKED":  "#475569",
    "UNKNOWN": "#64748b",
}
GATE_STEPS = ["A4", "B2", "B3", "B5", "EXPORT"]

def sc(stade):
    return STADE_COLOR.get(stade, "#64748b")

def prio_color(p):
    return {"haute": "#ef4444", "normale": "#3b82f6", "basse": "#64748b"}.get(p, "#64748b")

def gate_pills(ligne_name):
    gates = pipe_lignes.get(ligne_name, {}).get("gates", {})
    pills = ""
    for step in GATE_STEPS:
        g      = gates.get(step, {})
        status = g.get("status", "UNKNOWN") if g else "UNKNOWN"
        color  = GATE_COLOR.get(status, "#64748b")
        icon   = {"GO": "✓", "NO_GO": "✗", "LOCKED": "🔒", "UNKNOWN": "?"}.get(status, "?")
        n_fail = len(g.get("fails", [])) if g else 0
        tip    = f"{step}: {status}" + (f" ({n_fail} fails)" if n_fail else "")
        pills += (
            f'<span title="{tip}" style="background:{color}22;color:{color};'
            f'border:1px solid {color}55;padding:1px 6px;border-radius:3px;'
            f'font-size:9px;font-weight:700;margin-right:3px">{step} {icon}</span>'
        )
    return pills

# ── LIGNE CARDS ───────────────────────────────────────────────────────────────
ligne_cards = ""
for name, info in lignes.items():
    stade  = info.get("stade", "?")
    note   = info.get("note", "")
    bloque = info.get("bloque", False)
    color  = "#ef4444" if bloque else sc(stade)
    warn   = ' <span style="color:#ef4444;font-size:9px">⚠ BLOQUÉ</span>' if bloque else ""
    pills  = gate_pills(name)
    ligne_cards += (
        f'<div style="background:#1a1d27;border:1px solid {"#ef444444" if bloque else "#2a2d3a"};'
        f'border-radius:8px;padding:12px 16px">'
        f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:8px">'
        f'<div style="width:44px;height:44px;border-radius:8px;background:{color}22;border:2px solid {color};'
        f'display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:800;'
        f'color:{color};flex-shrink:0">{stade}</div>'
        f'<div style="flex:1">'
        f'<div style="font-weight:700;color:#e2e8f0;font-size:13px">{name}{warn}</div>'
        f'<div style="font-size:10px;color:#64748b;margin-top:2px">{note}</div>'
        f'</div></div>'
        f'<div style="padding-top:6px;border-top:1px solid #2a2d3a">{pills}</div>'
        f'</div>'
    )

# ── TASKS ─────────────────────────────────────────────────────────────────────
open_rows = ""
for t in tasks_open:
    pc = prio_color(t.get("priorite", "normale"))
    open_rows += (
        f'<div class="task"><span class="ticon io">○</span>'
        f'<span class="ttitle">{t["titre"]}</span>'
        f'<span class="tbadge bo">OUVERT</span>'
        f'<span class="tbadge" style="background:{pc}22;color:{pc}">{t.get("priorite","")}</span></div>'
    )

wait_rows = ""
for t in tasks_wait:
    wait_rows += (
        f'<div class="task"><span class="ticon iw">⏸</span>'
        f'<span class="ttitle">{t["titre"]}</span>'
        f'<span class="tbadge bw">EN ATTENTE</span>'
        f'<span class="tmt">{t.get("note","")}</span></div>'
    )

done_rows = ""
for t in tasks_done:
    done_rows += (
        f'<div class="task"><span class="ticon id">✓</span>'
        f'<span class="ttitle">{t}</span>'
        f'<span class="tbadge bd">DONE</span></div>'
    )

n_open = len(tasks_open)
n_wait = len(tasks_wait)
n_done = len(tasks_done)

tasks_section = ""
if wait_rows:
    tasks_section += '<div class="stitle" style="margin-top:10px">En attente</div>' + wait_rows
if open_rows:
    tasks_section += '<div class="stitle" style="margin-top:10px">Ouvertes</div>' + open_rows
if done_rows:
    tasks_section += f'<div class="stitle" style="margin-top:10px">Complétées — {updated}</div>' + done_rows

# ── ALERTES / INCOHÉRENCES ────────────────────────────────────────────────────
alert_rows = "".join(
    f'<div class="arow">⚠ {a}</div>' for a in alertes
) or '<div style="color:#22c55e;font-size:11px">Aucune alerte</div>'

inco_rows = "".join(
    f'<div class="irow">⚡ {i}</div>' for i in incoherences
) or '<div style="color:#22c55e;font-size:11px">Aucune incohérence</div>'

# ── HTML ──────────────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<script type="application/json" id="cowork-artifact-meta">
{{"name":"Factory Dashboard","schemaVersion":1,"description":"Dashboard unifié — pipeline, tâches, alertes."}}
</script>
<html lang="fr"><head><meta charset="UTF-8"><title>Factory Dashboard</title>
<style>
:root{{--bg:#0f1117;--sf:#1a1d27;--bd:#2a2d3a;--tx:#e2e8f0;--mt:#64748b}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--tx);font-family:'Segoe UI',system-ui,sans-serif;font-size:13px;padding:20px}}
h1{{font-size:18px;font-weight:700;color:#fff;margin-bottom:3px}}
.sub{{color:var(--mt);font-size:11px;margin-bottom:20px}}
.section{{margin-bottom:18px}}
.stitle{{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--mt);margin-bottom:8px}}
.lgrid{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}
.card{{background:var(--sf);border:1px solid var(--bd);border-radius:10px;padding:16px}}
.ctitle{{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--mt);margin-bottom:10px}}
.sumgrid{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:10px}}
.scard{{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:10px 12px}}
.sval{{font-size:20px;font-weight:800}}.slbl{{font-size:10px;color:var(--mt);margin-top:2px}}
.task{{background:var(--sf);border:1px solid var(--bd);border-radius:6px;padding:8px 12px;margin-bottom:5px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.ticon{{width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:9px;flex-shrink:0}}
.id{{background:#14532d44;color:#22c55e}}.iw{{background:#78350f44;color:#f59e0b}}.io{{background:#1e293b;color:var(--mt)}}
.ttitle{{font-weight:600;color:#e2e8f0;flex:1}}.tmt{{font-size:10px;color:var(--mt);width:100%;padding-left:26px}}
.tbadge{{display:inline-block;padding:1px 6px;border-radius:4px;font-size:9px;font-weight:700;margin-left:4px}}
.bd{{background:#14532d44;color:#22c55e}}.bw{{background:#78350f44;color:#f59e0b}}.bo{{background:#1e293b;color:var(--mt)}}
.row2{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.arow{{color:#fbbf24;font-size:11px;padding:3px 0;border-bottom:1px solid #2a2d3a55}}
.irow{{color:#f97316;font-size:11px;padding:3px 0;border-bottom:1px solid #2a2d3a55}}
@media(max-width:600px){{.lgrid,.row2,.sumgrid{{grid-template-columns:1fr}}}}
</style></head><body>
<h1>Quizzz Factory — Dashboard</h1>
<p class="sub">Mis à jour le {updated} · {len(lignes)} lignes · {n_open+n_wait+n_done} tâches actives</p>

<div class="section">
  <div class="stitle">Pipeline — État des lignes</div>
  <div class="lgrid">{ligne_cards}</div>
</div>

<div class="section">
  <div class="stitle">Tâches</div>
  <div class="sumgrid">
    <div class="scard"><div class="sval" style="color:#22c55e">{n_done}</div><div class="slbl">Complétées</div></div>
    <div class="scard"><div class="sval" style="color:#f59e0b">{n_wait}</div><div class="slbl">En attente</div></div>
    <div class="scard"><div class="sval" style="color:var(--mt)">{n_open}</div><div class="slbl">Ouvertes</div></div>
    <div class="scard"><div class="sval" style="color:#fff">{n_open+n_wait+n_done}</div><div class="slbl">Total actif</div></div>
  </div>
  {tasks_section}
</div>

<div class="row2">
  <div class="card">
    <div class="ctitle">⚠ Alertes glossaire ({len(alertes)})</div>
    {alert_rows}
  </div>
  <div class="card">
    <div class="ctitle">⚡ Incohérences V1/V2 ({len(incoherences)})</div>
    {inco_rows}
  </div>
</div>
</body></html>"""

OUT_MAIN.write_text(html, encoding="utf-8")

# Stamp
STAMP_FILE.write_text(json.dumps({"state_mtime": os.path.getmtime(STATE_FILE)}))

print(f"OK DASHBOARD GENERATED -- {OUT_MAIN.name}")
