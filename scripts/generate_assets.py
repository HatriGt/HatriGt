"""Cinematic profile assets. Run: python3 scripts/generate_assets.py assets
Brand logos in scripts/icons are from Simple Icons (CC0)."""
import sys, html, os, glob, re, math
out = sys.argv[1]; here = os.path.dirname(__file__)
for f in glob.glob(f"{out}/*.svg"): os.remove(f)
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
BG, BG2, FG, MUT, RULE = '#05070d', '#0b0f1a', '#f5f7fb', '#8b93a7', '#1c2333'
A, B, C_ = '#ff6a3d', '#ff2d8a', '#7c5cff'   # ember → magenta → violet
e = html.escape
def w(n, s): open(f"{out}/{n}", 'w').write(s)
def icon(slug): return re.search(r' d="([^"]+)"', open(f"{here}/icons/{slug}.svg").read()).group(1)
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
DEFS = f'''<linearGradient id="grad" x1="0" x2="1"><stop offset="0" stop-color="{A}"/><stop offset=".5" stop-color="{B}"/><stop offset="1" stop-color="{C_}"/></linearGradient>
<linearGradient id="shine" x1="0" x2="1"><stop offset="0" stop-color="{FG}"/><stop offset=".45" stop-color="{FG}"/><stop offset=".5" stop-color="#fff"/><stop offset=".55" stop-color="{FG}"/><stop offset="1" stop-color="{FG}"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glow2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>'''

# ================= HERO =================
W, H = 1000, 420
cx, cy = 760, 210
ORBIT = [  # (slug, color, radius, period, start angle)
 ('sap','0FAAFF',70,14,0),('nodedotjs','5FA04E',70,14,120),('typescript','3178C6',70,14,240),
 ('anthropic','ffffff',118,22,30),('cloudfoundry','0C9ED5',118,22,120),('docker','2496ED',118,22,210),('postgresql','4169E1',118,22,300),
]
orbits = ''
for slug, col, r, per, a0 in ORBIT:
    orbits += f'''<g transform="rotate({a0} {cx} {cy})"><g style="transform-origin:{cx}px {cy}px;animation:spin {per}s linear infinite">
<g transform="translate({cx+r} {cy})"><g style="transform-origin:0 0;animation:spin {per}s linear infinite reverse"><g transform="rotate({-a0})">
<circle r="19" fill="{BG2}" stroke="{RULE}" stroke-width="1.2"/><svg x="-11" y="-11" width="22" height="22" viewBox="0 0 24 24"><path fill="#{col}" d="{icon(slug)}"/></svg></g></g></g></g></g>'''
stars = ''.join(f'<circle cx="{(i*367)%W}" cy="{(i*229)%H}" r="{0.6+(i%3)*.4}" fill="#fff" opacity=".{3+i%5}" style="animation:tw {2+i%4}s {i%7*.3}s ease-in-out infinite"/>' for i in range(70))
title = "AJEETH"; title2 = "KUMAR"
def letters(txt, x, y, size, d0):
    s=''; 
    for i,ch in enumerate(txt):
        s+=f'<tspan class="L" style="animation-delay:{d0+i*.06:.2f}s">{ch}</tspan>'
    return f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" font-weight="800" letter-spacing="-3" fill="url(#shine)">{s}</text>'
w("hero.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{DEFS}
<radialGradient id="neb1" cx=".78" cy=".5" r=".5"><stop offset="0" stop-color="{C_}" stop-opacity=".55"/><stop offset="1" stop-color="{C_}" stop-opacity="0"/></radialGradient>
<radialGradient id="neb2" cx=".15" cy="1" r=".6"><stop offset="0" stop-color="{A}" stop-opacity=".35"/><stop offset="1" stop-color="{A}" stop-opacity="0"/></radialGradient>
<radialGradient id="core" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="{A}"/><stop offset="1" stop-color="{B}" stop-opacity="0"/></radialGradient>
<clipPath id="clip"><rect width="{W}" height="{H}" rx="24"/></clipPath>
<style>
.L{{opacity:0;animation:drop .7s cubic-bezier(.2,.8,.2,1) forwards}} @keyframes drop{{from{{opacity:0;transform:translateY(40px)}}to{{opacity:1;transform:none}}}}
.up{{opacity:0;animation:up .8s ease-out forwards}} @keyframes up{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes tw{{50%{{opacity:.05}}}}
.pulse{{transform-origin:{cx}px {cy}px;animation:pulse 3s ease-in-out infinite}} @keyframes pulse{{50%{{transform:scale(1.15)}}}}
.ring{{transform-origin:{cx}px {cy}px;animation:ring 3s ease-out infinite}} @keyframes ring{{from{{transform:scale(.6);opacity:.8}}to{{transform:scale(2.2);opacity:0}}}}
.sweep{{animation:sweep 6s linear infinite}} @keyframes sweep{{from{{transform:translateX(-{W}px)}}to{{transform:translateX({W}px)}}}}
.bar{{stroke-dasharray:1000;stroke-dashoffset:1000;animation:bar 1.6s .8s ease-out forwards}} @keyframes bar{{to{{stroke-dashoffset:0}}}}
{RM}
</style></defs>
<g clip-path="url(#clip)">
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="url(#neb1)"/><rect width="{W}" height="{H}" fill="url(#neb2)"/>
{stars}
<!-- orbit rings -->
<circle cx="{cx}" cy="{cy}" r="70" fill="none" stroke="{RULE}" stroke-dasharray="2 6"/>
<circle cx="{cx}" cy="{cy}" r="118" fill="none" stroke="{RULE}" stroke-dasharray="2 6"/>
<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="{RULE}" opacity=".5"/>
<circle class="ring" cx="{cx}" cy="{cy}" r="40" fill="none" stroke="{A}" stroke-width="1.5"/>
<circle class="pulse" cx="{cx}" cy="{cy}" r="60" fill="url(#core)" filter="url(#glow2)" opacity=".9"/>
<circle class="pulse" cx="{cx}" cy="{cy}" r="26" fill="url(#core)"/>
<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" fill="{BG}">AI</text>
{orbits}
<!-- type -->
<g class="up"><text x="60" y="92" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{A}">● SAP BTP · AI AGENTS · DEV TOOLS</text></g>
{letters(title, 56, 200, 112, .2)}
{letters(title2, 56, 300, 112, .55)}
<line x1="60" y1="325" x2="420" y2="325" stroke="url(#grad)" stroke-width="3" class="bar" stroke-linecap="round" filter="url(#glow)"/>
<g class="up" style="animation-delay:1.1s"><text x="60" y="362" font-family="{SANS}" font-size="20" fill="{FG}" opacity=".9">Building the tools that let AI agents do real work on SAP systems.</text></g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="24" fill="none" stroke="{RULE}"/>
</g></svg>''')

# ================= SECTION TITLE =================
def section(key, label, num):
    for mode, fg in [('dark', FG), ('light', '#1f2328')]:
        w(f"section-{key}-{mode}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="70" viewBox="0 0 1000 70">
<defs>{DEFS}<style>.u{{opacity:0;animation:u .8s ease-out forwards}}@keyframes u{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.b{{transform-origin:0 0;transform:scaleX(0);animation:s 1.2s .3s cubic-bezier(.2,.8,.2,1) forwards}}@keyframes s{{to{{transform:scaleX(1)}}}}{RM}</style></defs>
<g class="u"><text x="0" y="22" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{A}">{num}</text>
<text x="0" y="56" font-family="{SANS}" font-size="30" font-weight="800" letter-spacing="-1" fill="{fg}">{label}</text></g>
<rect class="b" x="0" y="66" width="1000" height="2" fill="url(#grad)"/></svg>''')
for k,l,n in [('work','Featured Work','01 — PROJECTS'),('stack','Arsenal','02 — STACK'),('stats','Activity','03 — GITHUB'),('about','Behind the code','04 — ABOUT')]: section(k,l,n)

# ================= PROJECT TILES =================
G = {
 'db': '<ellipse cx="12" cy="5.5" rx="7" ry="2.8"/><path d="M5 5.5v13c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8v-13M5 12c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8"/>',
 'bug': '<rect x="7" y="7" width="10" height="13" rx="5"/><path d="M12 11v9M3 13h4M17 13h4M4 7l3 2M20 7l-3 2M4 19l3-2M20 19l-3-2M9 7.5a3 3 0 0 1 6 0"/>',
 'box': '<path d="M12 2.5 20.5 7v10L12 21.5 3.5 17V7Z M3.5 7 12 11.5 20.5 7M12 11.5v10"/>',
 'relay': '<path d="M3 8h13l-3-3M21 16H8l3 3"/>',
 'tv': '<rect x="2.5" y="5" width="19" height="13" rx="2"/><path d="M8 21h8M9 2l3 3 3-3"/>',
 'frame': '<path d="M6 2v16h16M2 6h16v16"/>',
}
P = [
 ('hana-mcp-server','db','MCP server for SAP HANA','Schema discovery and guarded SQL','for AI clients, out of the box.','JavaScript','f1e05a',A),
 ('sap-cap-debugger','bug','Debug CAP apps live on BTP','VS Code or DevTools attached to a','running Cloud Foundry container.','TypeScript','3178c6',B),
 ('agent-sandbox','box','Sandboxes for coding agents','Delegate the task in a throwaway','environment. Keep the control.','TypeScript','3178c6',C_),
 ('ccproxy','relay','Cursor & Codex on Claude','Self-hosted HTTPS gateway for','your favourite agent harness.','Docker','2496ED',C_),
 ('flix-launcher','tv','A calmer Android TV','Home is one click from the film','you were halfway through.','Kotlin','7F52FF',B),
 ('screenxshot','frame','Beautiful screenshots, instantly','Client-side beautifier & annotator.','Nothing leaves the browser.','JavaScript','f1e05a',A),
]
for i,(name,g,h1,l1,l2,lang,lc,acc) in enumerate(P):
    d=i*.12
    w(f"tile-{name}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="230" viewBox="0 0 320 230">
<defs>{DEFS}
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient>
<radialGradient id="tglow" cx=".1" cy=".05" r=".8"><stop offset="0" stop-color="{acc}" stop-opacity=".35"/><stop offset="1" stop-color="{acc}" stop-opacity="0"/></radialGradient>
<linearGradient id="border" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{acc}"/><stop offset=".6" stop-color="{RULE}"/><stop offset="1" stop-color="{RULE}"/></linearGradient>
<clipPath id="c"><rect width="320" height="230" rx="18"/></clipPath>
<style>.in{{opacity:0;animation:in .8s {d}s cubic-bezier(.2,.8,.2,1) forwards}}@keyframes in{{from{{opacity:0;transform:translateY(18px) scale(.97)}}to{{opacity:1;transform:none}}}}
.ic path,.ic rect,.ic ellipse{{stroke-dasharray:90;stroke-dashoffset:90;animation:dr 1.4s {d+.3}s ease-out forwards}}@keyframes dr{{to{{stroke-dashoffset:0}}}}
.sh{{animation:sh 5s {d*3}s ease-in-out infinite}}@keyframes sh{{0%,100%{{transform:translateX(-340px)}}60%,100%{{transform:translateX(340px)}}}}
.ar{{animation:ar 2.4s {1+d}s ease-in-out infinite}}@keyframes ar{{0%,70%,100%{{transform:none}}80%{{transform:translate(3px,-3px)}}}}
{RM}</style></defs>
<g class="in" clip-path="url(#c)">
<rect width="320" height="230" rx="18" fill="url(#tg)"/><rect width="320" height="230" fill="url(#tglow)"/>
<rect class="sh" x="0" y="0" width="80" height="230" fill="#fff" opacity=".05" transform="skewX(-20)"/>
<rect x=".75" y=".75" width="318.5" height="228.5" rx="17.5" fill="none" stroke="url(#border)" stroke-width="1.5"/>
<rect x="24" y="24" width="46" height="46" rx="12" fill="{BG}" stroke="{RULE}"/>
<g class="ic" transform="translate(35 35)" fill="none" stroke="{acc}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)">{G[g]}</g>
<g class="ar"><text x="296" y="46" text-anchor="end" font-family="{SANS}" font-size="20" fill="{acc}">↗</text></g>
<text x="24" y="112" font-family="{SANS}" font-size="19" font-weight="700" fill="{FG}" letter-spacing="-.3">{e(h1)}</text>
<text x="24" y="138" font-family="{SANS}" font-size="13.5" fill="{MUT}">{e(l1)}</text>
<text x="24" y="157" font-family="{SANS}" font-size="13.5" fill="{MUT}">{e(l2)}</text>
<text x="24" y="201" font-family="{MONO}" font-size="12" fill="{acc}">{e(name)}</text>
<circle cx="{296-len(lang)*6.4-9}" cy="197" r="4" fill="#{lc}"/><text x="296" y="201" text-anchor="end" font-family="{MONO}" font-size="11.5" fill="{MUT}">{lang}</text>
</g></svg>''')

# ================= STACK MARQUEE (two rows, opposite directions) =================
ROW1 = [('sap','SAP BTP','0FAAFF'),('nodedotjs','Node.js','5FA04E'),('typescript','TypeScript','3178C6'),('javascript','JavaScript','F7DF1E'),('anthropic','Claude / MCP','ffffff'),('cloudfoundry','Cloud Foundry','0C9ED5'),('python','Python','3776AB'),('fastapi','FastAPI','009688')]
ROW2 = [('postgresql','PostgreSQL','4169E1'),('redis','Redis','FF4438'),('docker','Docker','2496ED'),('amazonwebservices','AWS','FF9900'),('githubactions','GitHub Actions','2088FF'),('vercel','Vercel','ffffff'),('kotlin','Kotlin','7F52FF'),('adobelightroom','Lightroom','31A8FF')]
def chips(row):
    s, x = '', 0
    for slug, lab, col in row:
        wd = 58 + len(lab)*8.2
        s += f'<g transform="translate({x} 0)"><rect width="{wd}" height="44" rx="22" fill="{BG2}" stroke="{RULE}"/><svg x="14" y="12" width="20" height="20" viewBox="0 0 24 24"><path fill="#{col}" d="{icon(slug)}"/></svg><text x="44" y="28" font-family="{SANS}" font-size="14" font-weight="600" fill="{FG}">{e(lab)}</text></g>'
        x += wd + 14
    return s, x
c1, t1 = chips(ROW1); c2, t2 = chips(ROW2)
w("stack.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="130" viewBox="0 0 1000 130">
<defs>{DEFS}<linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".1" stop-color="#fff"/><stop offset=".9" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="m"><rect width="1000" height="130" fill="url(#f)"/></mask><clipPath id="c"><rect width="1000" height="130" rx="18"/></clipPath>
<style>.a{{animation:a {t1/45:.0f}s linear infinite}}@keyframes a{{to{{transform:translateX(-{t1}px)}}}}
.b{{animation:b {t2/45:.0f}s linear infinite}}@keyframes b{{from{{transform:translateX(-{t2}px)}}to{{transform:none}}}}{RM}</style></defs>
<g clip-path="url(#c)"><rect width="1000" height="130" fill="{BG}"/>
<g mask="url(#m)"><g transform="translate(0 16)"><g class="a">{c1}<g transform="translate({t1} 0)">{c1}</g></g></g>
<g transform="translate(0 74)"><g class="b">{c2}<g transform="translate({t2} 0)">{c2}</g></g></g></g>
<rect x=".5" y=".5" width="999" height="129" rx="18" fill="none" stroke="{RULE}"/></g></svg>''')

# ================= ABOUT PANEL =================
w("about.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="200" viewBox="0 0 1000 200">
<defs>{DEFS}<clipPath id="c"><rect width="1000" height="200" rx="18"/></clipPath>
<radialGradient id="n" cx="1" cy="0" r=".7"><stop offset="0" stop-color="{B}" stop-opacity=".3"/><stop offset="1" stop-color="{B}" stop-opacity="0"/></radialGradient>
<style>.t{{opacity:0;animation:t .9s ease-out forwards}}@keyframes t{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
.q{{font-family:Georgia,serif;font-size:120px;fill:url(#grad);opacity:.25}}{RM}</style></defs>
<g clip-path="url(#c)"><rect width="1000" height="200" fill="{BG2}"/><rect width="1000" height="200" fill="url(#n)"/>
<text class="q" x="28" y="120">“</text>
<g font-family="{SANS}" fill="{FG}">
<text class="t" x="90" y="70" font-size="21" font-weight="600" style="animation-delay:.1s">Most of my day is spent on SAP BTP: CAP services, HANA Cloud and Cloud Foundry.</text>
<text class="t" x="90" y="104" font-size="17" fill="{MUT}" style="animation-delay:.3s">Lately that means MCP servers and agent infrastructure — the plumbing that lets an LLM do real work</text>
<text class="t" x="90" y="130" font-size="17" fill="{MUT}" style="animation-delay:.4s">against enterprise systems without being dangerous. Off the clock I shoot photos and edit in Lightroom.</text>
<text class="t" x="90" y="170" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{A}" style="animation-delay:.6s">OPEN TO COLLABORATING ON SAP × AI TOOLING</text>
</g><rect x=".5" y=".5" width="999" height="199" rx="18" fill="none" stroke="{RULE}"/></g></svg>''')
print("ok")
