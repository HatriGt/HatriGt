"""Profile assets. Run: python3 scripts/generate_assets.py assets
Brand logos in scripts/icons are from Simple Icons (CC0)."""
import sys, html, os, glob, re
out = sys.argv[1]; here = os.path.dirname(__file__)
for f in glob.glob(f"{out}/*.svg"): os.remove(f)
SERIF = "'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
T = {
 'dark':  dict(fg='#f0f3f6', body='#c9d1d9', mut='#7d8590', rule='#30363d', acc='#e8805a', tile='#161b22'),
 'light': dict(fg='#1f2328', body='#3d444d', mut='#6e7781', rule='#d8dee4', acc='#b5431b', tile='#f6f8fa'),
}
e = html.escape
def w(n, s): open(f"{out}/{n}", 'w').write(s)
def icon(slug): return re.search(r' d="([^"]+)"', open(f"{here}/icons/{slug}.svg").read()).group(1)
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

# ---------------- header ----------------
for m, c in T.items():
    sat = [('HANA', 600, 62), ('CAP', 830, 58), ('Cloud Foundry', 815, 204), ('Git', 615, 200)]
    hub = (720, 128)
    lines = packets = nodes = ''
    for i, (lab, x, y) in enumerate(sat):
        p = f"M{hub[0]} {hub[1]} L{x} {y}"
        lines += f'<path d="{p}" class="ln" style="animation-delay:{.6+i*.15}s"/>'
        packets += f'<circle r="2.6" fill="{c["acc"]}" opacity="0"><animateMotion dur="{2.4+i*.35}s" begin="{1.4+i*.4}s" repeatCount="indefinite" path="{p if i%2 else f"M{x} {y} L{hub[0]} {hub[1]}"}"/><animate attributeName="opacity" values="0;1;1;0" dur="{2.4+i*.35}s" begin="{1.4+i*.4}s" repeatCount="indefinite"/></circle>'
        ly = y - 12 if y < hub[1] else y + 20
        nodes += f'<g class="pop" style="animation-delay:{.9+i*.15}s"><circle cx="{x}" cy="{y}" r="5" fill="{c["tile"]}" stroke="{c["mut"]}" stroke-width="1.2"/><text x="{x}" y="{ly}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{c["mut"]}">{lab}</text></g>'
    w(f"header-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="250" viewBox="0 0 880 250" overflow="hidden">
<style>
.name{{fill:transparent;stroke:{c['fg']};stroke-width:.8;stroke-dasharray:420;stroke-dashoffset:420;animation:draw 1.6s ease-out forwards,fill .6s 1.2s ease-out forwards}}
@keyframes draw{{to{{stroke-dashoffset:0}}}} @keyframes fill{{to{{fill:{c['fg']};stroke-width:0}}}}
.up{{opacity:0;animation:up .7s ease-out forwards}} @keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.ln{{fill:none;stroke:{c['rule']};stroke-width:1.2;stroke-dasharray:200;stroke-dashoffset:200;animation:draw 1s ease-out forwards}}
.pop{{opacity:0;animation:up .5s ease-out forwards}}
.ring{{transform-origin:{hub[0]}px {hub[1]}px;animation:ring 2.6s ease-out infinite}}
@keyframes ring{{from{{transform:scale(1);opacity:.55}}to{{transform:scale(2.6);opacity:0}}}}
.dot{{animation:blink 2s ease-in-out infinite}} @keyframes blink{{50%{{opacity:.25}}}}
{RM}
</style>
<text x="0" y="22" font-family="{MONO}" font-size="12.5" letter-spacing="1.5" fill="{c['mut']}" class="up">HATRIGT<tspan class="dot" fill="{c['acc']}"> ●</tspan> SOFTWARE DEVELOPER</text>
<text x="-2" y="100" font-family="{SERIF}" font-size="60" letter-spacing="-1.2" class="name">Ajeeth Kumar</text>
<g font-family="{SANS}" font-size="20" fill="{c['body']}" class="up" style="animation-delay:.9s">
 <text x="0" y="150">I build developer tools for SAP BTP</text>
 <text x="0" y="180">and the AI agents that work alongside them<tspan fill="{c['acc']}">.</tspan></text>
</g>
{lines}{packets}
<circle cx="{hub[0]}" cy="{hub[1]}" r="14" fill="none" stroke="{c['acc']}" class="ring"/>
<g class="pop" style="animation-delay:.5s"><circle cx="{hub[0]}" cy="{hub[1]}" r="14" fill="{c['acc']}"/>
<text x="{hub[0]}" y="{hub[1]+4}" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="700" fill="{c['tile']}">AI</text></g>
{nodes}
<rect x="0" y="242" width="880" height="1" fill="{c['rule']}"/>
</svg>''')

# ---------------- labels ----------------
    for key, label in [('work','Selected work'),('stack','Stack'),('about','About')]:
        w(f"label-{key}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="40" viewBox="0 0 880 40">
<style>.l{{stroke-dasharray:24;stroke-dashoffset:24;animation:d .8s .2s ease-out forwards}}@keyframes d{{to{{stroke-dashoffset:0}}}}{RM}</style>
<path class="l" d="M0 21 H18" stroke="{c['acc']}" stroke-width="1.5"/>
<text x="28" y="26" font-family="{MONO}" font-size="12.5" letter-spacing="1.5" fill="{c['mut']}">{label.upper()}</text></svg>''')

# ---------------- project rows ----------------
G = {  # 24x24 line glyphs
 'db': '<ellipse cx="12" cy="5.5" rx="7" ry="2.8"/><path d="M5 5.5v13c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8v-13M5 12c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8"/>',
 'bug': '<rect x="7" y="7" width="10" height="13" rx="5"/><path d="M12 11v9M3 13h4M17 13h4M4 7l3 2M20 7l-3 2M4 19l3-2M20 19l-3-2M9 7.5a3 3 0 0 1 6 0"/>',
 'box': '<path d="M12 2.5 20.5 7v10L12 21.5 3.5 17V7Z M3.5 7 12 11.5 20.5 7M12 11.5v10"/>',
 'relay': '<path d="M3 8h13l-3-3M21 16H8l3 3"/>',
 'tv': '<rect x="2.5" y="5" width="19" height="13" rx="2"/><path d="M8 21h8M9 2l3 3 3-3"/>',
 'frame': '<path d="M6 2v16h16M2 6h16v16"/>',
}
ROWS = [
 ('hana-mcp-server','db','MCP server for SAP HANA and HANA Cloud — schema discovery and guarded SQL for AI clients.','JavaScript'),
 ('sap-cap-debugger','bug','Attach VS Code or DevTools to a live CAP app on Cloud Foundry, in one command.','TypeScript'),
 ('agent-sandbox','box','Disposable sandboxes for coding agents. Delegate the task, keep the control.','TypeScript'),
 ('ccproxy','relay','Self-hosted gateway that runs Cursor and Codex on a Claude subscription.','Docker'),
 ('flix-launcher','tv','A quiet Android TV launcher. Home is one click from what you’re watching.','Kotlin'),
 ('screenxshot','frame','Client-side screenshot beautifier and annotator. Nothing leaves the browser.','JavaScript'),
]
for m, c in T.items():
    for i, (name, g, desc, lang) in enumerate(ROWS):
        d = .15 + i * .12
        w(f"row-{name}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="88" viewBox="0 0 880 88">
<style>
.r{{opacity:0;animation:in .7s {d}s ease-out forwards}} @keyframes in{{from{{opacity:0;transform:translateX(-10px)}}to{{opacity:1;transform:none}}}}
.ic path,.ic rect,.ic ellipse{{stroke-dasharray:80;stroke-dashoffset:80;animation:dr 1.4s {d+.2}s ease-out forwards}} @keyframes dr{{to{{stroke-dashoffset:0}}}}
.rule{{transform-origin:0 0;transform:scaleX(0);animation:sx 1s {d}s ease-out forwards}} @keyframes sx{{to{{transform:scaleX(1)}}}}
.ar{{animation:nudge 2.2s {2+i*.3}s ease-in-out infinite}} @keyframes nudge{{0%,70%,100%{{transform:none}}80%{{transform:translateX(4px)}}}}
{RM}
</style>
<g class="r">
 <rect x="0" y="16" width="44" height="44" rx="10" fill="{c['tile']}" stroke="{c['rule']}"/>
 <g class="ic" transform="translate(10 26)" fill="none" stroke="{c['acc']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{G[g]}</g>
 <text x="64" y="37" font-family="{SERIF}" font-size="24" fill="{c['fg']}">{e(name)}</text>
 <text x="64" y="63" font-family="{SANS}" font-size="15" fill="{c['body']}">{e(desc)}</text>
 <text x="852" y="36" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{c['mut']}">{lang}</text>
 <g class="ar"><text x="880" y="36" text-anchor="end" font-family="{MONO}" font-size="13" fill="{c['acc']}">→</text></g>
</g>
<rect class="rule" x="0" y="87" width="880" height="1" fill="{c['rule']}"/>
</svg>''')

# ---------------- stack marquee ----------------
STACK = [('sap','SAP BTP','0FAAFF'),('nodedotjs','Node.js','5FA04E'),('typescript','TypeScript','3178C6'),('javascript','JavaScript','F7DF1E'),
 ('anthropic','MCP / Claude',None),('cloudfoundry','Cloud Foundry','0C9ED5'),('postgresql','PostgreSQL','4169E1'),('redis','Redis','FF4438'),
 ('docker','Docker','2496ED'),('amazonwebservices','AWS','FF9900'),('githubactions','Actions','2088FF'),('vercel','Vercel',None),
 ('python','Python','3776AB'),('fastapi','FastAPI','009688'),('kotlin','Kotlin','7F52FF'),('adobelightroom','Lightroom','31A8FF')]
for m, c in T.items():
    items, x = '', 0
    for slug, lab, col in STACK:
        tw = len(lab) * 7.4
        items += f'<g transform="translate({x} 0)"><svg x="0" y="14" width="22" height="22" viewBox="0 0 24 24"><path fill="#{col}" d="{icon(slug)}"/></svg><text x="32" y="30" font-family="{SANS}" font-size="14" fill="{c["body"]}">{e(lab)}</text></g>'.replace('fill="#None"', f'fill="{c["fg"]}"')
        x += 32 + tw + 44
    total = x
    w(f"stack-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="50" viewBox="0 0 880 50">
<defs><linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".08" stop-color="#fff"/><stop offset=".92" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="m"><rect width="880" height="50" fill="url(#f)"/></mask></defs>
<style>.t{{animation:mq {total/40:.0f}s linear infinite}} @keyframes mq{{to{{transform:translateX(-{total}px)}}}}{RM}</style>
<g mask="url(#m)"><g class="t">{items}<g transform="translate({total} 0)">{items}</g></g></g>
</svg>''')
print("ok")
