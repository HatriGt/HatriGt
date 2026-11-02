"""Profile assets. Run: python3 scripts/generate_assets.py assets
Hallmark · macrostructure: Index-First · theme: Terminal (mono-only) · tone: technical · anchor hue: green 150
Hallmark · pre-emit critique: P4 H4 E4 S4 R5 V4
"""
import sys, html, os, glob
out = sys.argv[1]
for f in glob.glob(f"{out}/*.svg"): os.remove(f)
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
W = 880
# tokens — tinted neutrals, one accent, transparent paper (GitHub supplies it)
T = {
 'dark':  dict(fg='#e6ebe7', body='#aab3ad', mut='#6f7a73', rule='#2a3330', acc='#5fc48f'),
 'light': dict(fg='#171d1a', body='#424c46', mut='#6f7a73', rule='#d6ddd9', acc='#1f7a4a'),
}
LANG = {'JavaScript':'#f1e05a','TypeScript':'#3178c6','Docker':'#384d54','Kotlin':'#A97BFF','Python':'#3572A5'}
e = html.escape
def w(n, s): open(f"{out}/{n}", 'w').write(s)
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important;opacity:1!important}}"

for m, c in T.items():
    # opening — one short paragraph, no display type, the only animation on the page
    w(f"open-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="150" viewBox="0 0 {W} 150" font-family="{MONO}">
<style>.l{{opacity:0;animation:l .5s cubic-bezier(.2,.8,.2,1) forwards}}@keyframes l{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:none}}}}{RM}</style>
<text class="l" x="0" y="34" font-size="26" font-weight="600" fill="{c['fg']}">Ajeeth Kumar</text>
<text class="l" style="animation-delay:.08s" x="0" y="72" font-size="15" fill="{c['body']}">Developer tools for SAP BTP, and the AI agents that use them.</text>
<text class="l" style="animation-delay:.16s" x="0" y="96" font-size="15" fill="{c['body']}">CAP · HANA Cloud · Cloud Foundry · MCP · Node.js</text>
<text class="l" style="animation-delay:.24s" x="0" y="134" font-size="13" fill="{c['mut']}"><tspan fill="{c['acc']}">●</tspan> now: MCP servers for SAP HANA · open to collaboration</text>
</svg>''')

    def head(key, label):
        w(f"head-{key}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="44" viewBox="0 0 {W} 44" font-family="{MONO}">
<text x="0" y="24" font-size="13" font-weight="600" fill="{c['fg']}">{e(label)}</text>
<rect x="0" y="43" width="{W}" height="1" fill="{c['rule']}"/></svg>''')
    head('sap', 'SAP × AI')
    head('tools', 'Developer tools')
    head('side', 'Side projects')

    def row(name, desc, lang):
        lc = LANG[lang]
        w(f"row-{name}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="58" viewBox="0 0 {W} 58" font-family="{MONO}">
<text x="0" y="23" font-size="15" font-weight="600" fill="{c['fg']}">{e(name)}</text>
<text x="0" y="44" font-size="13" fill="{c['body']}">{e(desc)}</text>
<circle cx="{W-len(lang)*7.8-14}" cy="19" r="4" fill="{lc}"/>
<text x="{W}" y="23" text-anchor="end" font-size="12" fill="{c['mut']}">{lang}</text>
<text x="{W}" y="44" text-anchor="end" font-size="13" fill="{c['acc']}">→</text>
<rect x="0" y="57" width="{W}" height="1" fill="{c['rule']}"/></svg>''')
    row('hana-mcp-server', 'MCP server for SAP HANA and HANA Cloud. Schema discovery and guarded SQL for AI clients.', 'JavaScript')
    row('sap-cap-debugger', 'npx sap-cap-debugger my-app: attach VS Code or DevTools to a CAP app running on Cloud Foundry.', 'TypeScript')
    row('agent-sandbox', 'Throwaway sandboxes for coding agents. Hosted with a free trial, or self-host.', 'TypeScript')
    row('ccproxy', 'Self-hosted HTTPS gateway that runs Cursor and Codex against a Claude subscription.', 'Docker')
    row('screenxshot', 'Client-side screenshot beautifier and annotator. Nothing leaves the browser.', 'JavaScript')
    row('flix-launcher', 'Android TV launcher: Home is one click from the episode you were halfway through.', 'Kotlin')
    row('AISubs', 'Stremio addon that fetches subtitles and translates them with an LLM.', 'JavaScript')

    w(f"stack-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="76" viewBox="0 0 {W} 76" font-family="{MONO}" font-size="13">
<text x="0" y="22" fill="{c['mut']}">daily</text><text x="110" y="22" fill="{c['body']}">SAP CAP · HANA Cloud · Cloud Foundry · Node.js · TypeScript · PostgreSQL · Redis</text>
<text x="0" y="46" fill="{c['mut']}">also</text><text x="110" y="46" fill="{c['body']}">Python · FastAPI · Docker · AWS · GitHub Actions · Kotlin</text>
<text x="0" y="70" fill="{c['mut']}">off-hours</text><text x="110" y="70" fill="{c['body']}">photography · Lightroom</text>
</svg>''')
print("ok")
