"""Profile assets. Run: python3 scripts/generate_assets.py assets
Hallmark · macrostructure: Map/Diagram · theme: Terminal (mono) · tone: technical · anchor hue: green 150
Hallmark · pre-emit critique: P4 H4 E4 S5 R4 V4
Logos: Simple Icons (CC0), scripts/icons."""
import sys, html, os, glob, re
out = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(f"{out}/*.svg"): os.remove(f)
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
W = 880
T = {
 'dark':  dict(fg='#e6ebe7', body='#aab3ad', mut='#6f7a73', rule='#2a3330', acc='#5fc48f', node='#0f1512'),
 'light': dict(fg='#171d1a', body='#424c46', mut='#6f7a73', rule='#d6ddd9', acc='#1f7a4a', node='#f6f8f7'),
}
LANG = {'JavaScript':'#f1e05a','TypeScript':'#3178c6','Docker':'#384d54','Kotlin':'#A97BFF'}
e = html.escape
def w(n, s): open(f"{out}/{n}", 'w').write(s)
def icon(slug): return re.search(r' d="([^"]+)"', open(f"{here}/icons/{slug}.svg").read()).group(1)
def logo(slug, x, y, size, fill): return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24"><path fill="{fill}" d="{icon(slug)}"/></svg>'
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important;opacity:1!important}}"

G = {  # 24px stroke pictograms, one stroke weight
 'db': '<ellipse cx="12" cy="5.5" rx="7" ry="2.8"/><path d="M5 5.5v13c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8v-13M5 12c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8"/>',
 'bug': '<rect x="7" y="7" width="10" height="13" rx="5"/><path d="M12 11v9M3 13h4M17 13h4M4 7l3 2M20 7l-3 2M4 19l3-2M20 19l-3-2M9 7.5a3 3 0 0 1 6 0"/>',
 'box': '<path d="M12 2.5 20.5 7v10L12 21.5 3.5 17V7Z M3.5 7 12 11.5 20.5 7M12 11.5v10"/>',
 'relay': '<path d="M3 8h13l-3-3M21 16H8l3 3"/>',
 'tv': '<rect x="2.5" y="5" width="19" height="13" rx="2"/><path d="M8 21h8M9 2l3 3 3-3"/>',
 'frame': '<path d="M6 2v16h16M2 6h16v16"/>',
 'cc': '<rect x="2.5" y="4" width="19" height="16" rx="2"/><path d="M6 15h12M6 11h4"/>',
}

for m, c in T.items():
    # ---------- opening ----------
    w(f"open-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="120" viewBox="0 0 {W} 120" font-family="{MONO}">
<style>.l{{opacity:0;animation:l .5s cubic-bezier(.2,.8,.2,1) forwards}}@keyframes l{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:none}}}}{RM}</style>
<text class="l" x="0" y="34" font-size="26" font-weight="600" fill="{c['fg']}">Ajeeth Kumar</text>
<text class="l" style="animation-delay:.08s" x="0" y="70" font-size="15" fill="{c['body']}">Developer tools for SAP BTP, and the AI agents that use them.</text>
<text class="l" style="animation-delay:.16s" x="0" y="106" font-size="13" fill="{c['mut']}"><tspan fill="{c['acc']}">●</tspan> now: MCP servers for SAP HANA · open to collaboration</text>
</svg>''')

    # ---------- system diagram (the hero image) ----------
    H = 330
    def node(x, y, wd, label, slug=None, mono=False, delay=0):
        s = f'<g class="n" style="animation-delay:{delay}s"><rect x="{x}" y="{y}" width="{wd}" height="40" rx="6" fill="{c["node"]}" stroke="{c["rule"]}"/>'
        tx = x + 14
        if slug: s += logo(slug, x+12, y+11, 18, c['fg']); tx = x + 40
        s += f'<text x="{tx}" y="{y+25}" font-size="12.5" font-weight="{600 if mono else 500}" fill="{c["fg"]}">{e(label)}</text></g>'
        return s
    # columns
    L, Mx, R = 0, 300, 640
    nodes = ''
    nodes += node(L, 40, 180, 'Claude Code', 'claude', delay=.1)
    nodes += node(L, 130, 180, 'Cursor', 'cursor', delay=.15)
    nodes += node(L, 220, 180, 'Codex', 'openai', delay=.2)
    nodes += node(Mx, 20, 240, 'hana-mcp-server', mono=True, delay=.3)
    nodes += node(Mx, 95, 240, 'agent-sandbox', mono=True, delay=.35)
    nodes += node(Mx, 170, 240, 'ccproxy  → Claude', mono=True, delay=.4)
    nodes += node(Mx, 245, 240, 'sap-cap-debugger', mono=True, delay=.45)
    nodes += node(R, 20, 240, 'SAP HANA Cloud', 'sap', delay=.55)
    nodes += node(R, 95, 240, 'GitHub', 'github', delay=.6)
    nodes += node(R, 245, 240, 'Cloud Foundry', 'cloudfoundry', delay=.65)
    # edges (x1,y1 -> x2,y2) with gentle curves
    def edge(x1, y1, x2, y2, label=None, back=False):
        mx = (x1 + x2) / 2
        d = f"M{x1} {y1} C{mx} {y1} {mx} {y2} {x2} {y2}"
        s = f'<path d="{d}" class="e" fill="none" stroke="{c["rule"]}" stroke-width="1.2"/>'
        s += f'<circle r="2.5" fill="{c["acc"]}"><animateMotion dur="2.6s" begin="{abs(y1+x1)%7*0.3:.1f}s" repeatCount="indefinite" path="{d}" keyPoints="{"1;0" if back else "0;1"}" keyTimes="0;1" calcMode="linear"/></circle>'
        if label: s += f'<text x="{mx}" y="{(y1+y2)/2-6}" text-anchor="middle" font-size="10.5" fill="{c["mut"]}">{e(label)}</text>'
        return s
    edges = ''
    edges += edge(180, 60, Mx, 40, 'MCP')          # Claude -> hana-mcp
    edges += edge(180, 60, Mx, 115)                 # Claude -> sandbox
    edges += edge(180, 150, Mx, 190)                # Cursor -> ccproxy
    edges += edge(180, 240, Mx, 190)                # Codex -> ccproxy
    edges += edge(Mx+240, 40, R, 40, 'SQL')          # hana-mcp -> HANA
    edges += edge(Mx+240, 115, R, 115, 'PRs')        # sandbox -> GitHub
    edges += edge(Mx+240, 265, R, 265, 'cf ssh')     # debugger -> CF
    w(f"diagram-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}">
<style>
.n{{opacity:0;animation:n .5s cubic-bezier(.2,.8,.2,1) forwards}}@keyframes n{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:none}}}}
.e{{stroke-dasharray:600;stroke-dashoffset:600;animation:e 1.2s .5s ease-out forwards}}@keyframes e{{to{{stroke-dashoffset:0}}}}
{RM}</style>
<text x="{L}" y="12" font-size="11" fill="{c['mut']}">agents</text>
<text x="{Mx}" y="12" font-size="11" fill="{c['mut']}">what I build</text>
<text x="{R}" y="12" font-size="11" fill="{c['mut']}">systems</text>
{edges}{nodes}
<text x="0" y="{H-6}" font-size="11" fill="{c['mut']}">How the pieces fit: agents reach SAP and GitHub through tools I maintain. Dots are requests.</text>
</svg>''')

    # ---------- section heads & rows ----------
    def head(key, label):
        w(f"head-{key}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="44" viewBox="0 0 {W} 44" font-family="{MONO}">
<text x="0" y="24" font-size="13" font-weight="600" fill="{c['fg']}">{e(label)}</text>
<rect x="0" y="43" width="{W}" height="1" fill="{c['rule']}"/></svg>''')
    head('sap', 'SAP × AI'); head('tools', 'Developer tools'); head('side', 'Side projects'); head('stack', 'Stack')
    def row(name, g, desc, lang):
        w(f"row-{name}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="58" viewBox="0 0 {W} 58" font-family="{MONO}">
<g transform="translate(0 20) scale(.75)" fill="none" stroke="{c['mut']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{G[g]}</g>
<text x="32" y="23" font-size="15" font-weight="600" fill="{c['fg']}">{e(name)}</text>
<text x="32" y="44" font-size="13" fill="{c['body']}">{e(desc)}</text>
<circle cx="{W-len(lang)*7.8-14}" cy="19" r="4" fill="{LANG[lang]}"/>
<text x="{W}" y="23" text-anchor="end" font-size="12" fill="{c['mut']}">{lang}</text>
<text x="{W}" y="44" text-anchor="end" font-size="13" fill="{c['acc']}">→</text>
<rect x="0" y="57" width="{W}" height="1" fill="{c['rule']}"/></svg>''')
    row('hana-mcp-server','db','MCP server for SAP HANA and HANA Cloud. Schema discovery and guarded SQL for AI clients.','JavaScript')
    row('sap-cap-debugger','bug','npx sap-cap-debugger my-app: attach VS Code or DevTools to a CAP app running on Cloud Foundry.','TypeScript')
    row('agent-sandbox','box','Throwaway sandboxes for coding agents. Hosted with a free trial, or self-host.','TypeScript')
    row('ccproxy','relay','Self-hosted HTTPS gateway that runs Cursor and Codex against a Claude subscription.','Docker')
    row('screenxshot','frame','Client-side screenshot beautifier and annotator. Nothing leaves the browser.','JavaScript')
    row('flix-launcher','tv','Android TV launcher: Home is one click from the episode you were halfway through.','Kotlin')
    row('AISubs','cc','Stremio addon that fetches subtitles and translates them with an LLM.','JavaScript')

    # ---------- monochrome logo wall ----------
    WALL = [('sap','SAP BTP'),('nodedotjs','Node.js'),('typescript','TypeScript'),('javascript','JavaScript'),('cloudfoundry','Cloud Foundry'),('claude','Claude / MCP'),('postgresql','PostgreSQL'),
            ('redis','Redis'),('docker','Docker'),('amazonwebservices','AWS'),('githubactions','GitHub Actions'),('python','Python'),('kotlin','Kotlin'),('github','GitHub')]
    cols, cw, rh = 7, W/7, 78
    cells = ''
    for i,(slug,lab) in enumerate(WALL):
        x = (i % cols) * cw; y = (i // cols) * rh
        cells += logo(slug, x + cw/2 - 14, y + 10, 28, c['body']) + f'<text x="{x+cw/2}" y="{y+60}" text-anchor="middle" font-size="11" fill="{c["mut"]}">{e(lab)}</text>'
    w(f"wall-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{rh*2}" viewBox="0 0 {W} {rh*2}" font-family="{MONO}">{cells}</svg>''')

    # ---------- social ----------
    for slug, lab in [('linkedin','LinkedIn'),('x','X'),('instagram','Instagram')]:
        wd = 30 + len(lab)*8
        w(f"soc-{slug}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{wd}" height="24" viewBox="0 0 {wd} 24" font-family="{MONO}">{logo(slug,0,4,16,c['body'])}<text x="24" y="17" font-size="13" fill="{c['body']}">{lab}</text></svg>''')
print("ok")
