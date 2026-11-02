"""Profile assets (website style). Run: python3 scripts/generate_assets.py assets
Logos: Simple Icons (CC0) in scripts/icons."""
import sys, html, os, glob, re
out = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(f"{out}/*.svg"): os.remove(f)
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
e = html.escape
def w(n, s): open(f"{out}/{n}", 'w').write(s)
def icon(slug): return re.search(r' d="([^"]+)"', open(f"{here}/icons/{slug}.svg").read()).group(1)
def logo(slug, x, y, size, fill): return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24"><path fill="{fill}" d="{icon(slug)}"/></svg>'
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important;opacity:1!important}}"
NAVY, NAVY2, WHITE, SOFT = '#0b2545', '#13315c', '#ffffff', '#b8c7e0'
W = 1000

# ---------- banner ----------
dots = ''.join(f'<circle cx="{x}" cy="{y}" r="1.2" fill="#fff" opacity=".12"/>' for x in range(20, W, 24) for y in range(20, 220, 24))
chips = ''
for i,(slug,col,lab) in enumerate([('sap','#0FAAFF','SAP BTP'),('nodedotjs','#5FA04E','Node.js'),('typescript','#3178C6','TypeScript'),('claude','#D97757','Claude / MCP'),('cloudfoundry','#0C9ED5','Cloud Foundry'),('docker','#2496ED','Docker')]):
    x = 60 + i*150
    chips += f'<g class="c" style="animation-delay:{.6+i*.08}s"><rect x="{x}" y="166" width="138" height="34" rx="17" fill="#ffffff14" stroke="#ffffff22"/>{logo(slug,x+12,y:=174,18,col)}<text x="{x+38}" y="188" font-family="{SANS}" font-size="12.5" fill="{WHITE}">{lab}</text></g>'
w("banner.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="230" viewBox="0 0 {W} 230">
<defs><clipPath id="c"><rect width="{W}" height="230" rx="16"/></clipPath>
<style>.t{{opacity:0;animation:t .6s cubic-bezier(.2,.8,.2,1) forwards}}.c{{opacity:0;animation:t .5s ease-out forwards}}@keyframes t{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.cur{{animation:b 1s steps(1) infinite}}@keyframes b{{50%{{opacity:0}}}}{RM}</style></defs>
<g clip-path="url(#c)"><rect width="{W}" height="230" fill="{NAVY}"/><rect x="620" width="{W}" height="230" fill="{NAVY2}" transform="skewX(-18)"/>{dots}
<text class="t" x="60" y="72" font-family="{SANS}" font-size="38" font-weight="700" fill="{WHITE}">Hi, I'm Ajeeth Kumar</text>
<text class="t" style="animation-delay:.15s" x="60" y="106" font-family="{SANS}" font-size="18" fill="{SOFT}">SAP BTP developer · building AI agent tooling and developer tools</text>
<text class="t" style="animation-delay:.3s" x="60" y="138" font-family="{MONO}" font-size="14" fill="#7fd1a8">$ npx sap-cap-debugger my-app<tspan class="cur">▍</tspan></text>
{chips}</g></svg>''')

# ---------- project cards ----------
G = {
 'db': '<ellipse cx="12" cy="5.5" rx="7" ry="2.8"/><path d="M5 5.5v13c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8v-13M5 12c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8"/>',
 'bug': '<rect x="7" y="7" width="10" height="13" rx="5"/><path d="M12 11v9M3 13h4M17 13h4M4 7l3 2M20 7l-3 2M4 19l3-2M20 19l-3-2M9 7.5a3 3 0 0 1 6 0"/>',
 'box': '<path d="M12 2.5 20.5 7v10L12 21.5 3.5 17V7Z M3.5 7 12 11.5 20.5 7M12 11.5v10"/>',
 'relay': '<path d="M3 8h13l-3-3M21 16H8l3 3"/>',
 'tv': '<rect x="2.5" y="5" width="19" height="13" rx="2"/><path d="M8 21h8M9 2l3 3 3-3"/>',
 'frame': '<path d="M6 2v16h16M2 6h16v16"/>',
}
CARDS = [
 ('hana-mcp-server','db','#0F6CBD','MCP server for SAP HANA','Lets Claude, Cursor and other AI clients discover schemas','and run guarded SQL on HANA Cloud.',['sap','claude','nodedotjs']),
 ('sap-cap-debugger','bug','#C2410C','Debug CAP apps live on BTP','One command attaches VS Code or Chrome DevTools to a','CAP app running on Cloud Foundry. No redeploy.',['sap','cloudfoundry','typescript']),
 ('agent-sandbox','box','#6D28D9','Sandboxes for coding agents','Hand a task to an agent in a throwaway environment.','Hosted with a free trial, or self-host for free.',['claude','docker','github']),
 ('ccproxy','relay','#0F766E','Cursor & Codex on your Claude plan','Self-hosted HTTPS gateway so Cursor and OpenAI Codex','run on a Claude Pro / Max subscription.',['cursor','openai','docker']),
 ('screenxshot','frame','#BE185D','Beautiful screenshots, instantly','Privacy-first, client-side screenshot beautifier','and annotator. Nothing leaves the browser.',['javascript']),
 ('flix-launcher','tv','#B45309','A calmer Android TV launcher','Home is one click from the episode you were halfway','through. Works on BRAVIA, Shield, Chromecast and more.',['kotlin']),
]
for name,g,col,title,l1,l2,logos in CARDS:
    lg = ''.join(logo(s, 400-24-i*30, 24, 20, '#ffffffcc') for i,s in enumerate(reversed(logos)))
    w(f"card-{name}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="200" viewBox="0 0 440 200">
<defs><clipPath id="c"><rect width="440" height="200" rx="14"/></clipPath></defs>
<g clip-path="url(#c)"><rect width="440" height="200" fill="{col}"/><rect x="0" y="0" width="440" height="200" fill="#000" opacity=".08"/><rect x="0" y="70" width="440" height="130" fill="#000" opacity=".22"/>
<rect x="24" y="22" width="40" height="40" rx="10" fill="#ffffff22"/><g transform="translate(32 30)" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{G[g]}</g>
{lg}
<text x="24" y="104" font-family="{SANS}" font-size="19" font-weight="700" fill="#fff">{e(title)}</text>
<text x="24" y="130" font-family="{SANS}" font-size="13" fill="#ffffffd9">{e(l1)}</text>
<text x="24" y="149" font-family="{SANS}" font-size="13" fill="#ffffffd9">{e(l2)}</text>
<text x="24" y="181" font-family="{MONO}" font-size="12" fill="#ffffffb3">github.com/HatriGt/{name}</text>
<text x="416" y="181" text-anchor="end" font-family="{SANS}" font-size="16" fill="#fff">→</text>
</g></svg>''')

# ---------- footer ----------
w("footer.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="90" viewBox="0 0 {W} 90">
<defs><clipPath id="c"><rect width="{W}" height="90" rx="16"/></clipPath></defs>
<g clip-path="url(#c)"><rect width="{W}" height="90" fill="{NAVY}"/>
<text x="60" y="40" font-family="{SANS}" font-size="18" font-weight="600" fill="#fff">Working on SAP × AI tooling? Let's talk.</text>
<text x="60" y="64" font-family="{SANS}" font-size="13" fill="{SOFT}">Open to collaboration and interesting problems on SAP BTP, MCP and agent infrastructure.</text>
<rect x="{W-230}" y="27" width="170" height="36" rx="18" fill="#fff"/><text x="{W-145}" y="50" text-anchor="middle" font-family="{SANS}" font-size="14" font-weight="600" fill="{NAVY}">Connect on LinkedIn</text>
</g></svg>''')
print("ok")
