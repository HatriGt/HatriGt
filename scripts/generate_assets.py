"""Profile assets. Run: python3 scripts/generate_assets.py assets"""
import sys, html, os, glob
out = sys.argv[1]
for f in glob.glob(f"{out}/*.svg"): os.remove(f)
SERIF = "'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
T = {  # transparent bg; text tuned to GitHub's canvases
 'dark':  dict(fg='#f0f3f6', body='#c9d1d9', mut='#7d8590', rule='#30363d', acc='#e8805a'),
 'light': dict(fg='#1f2328', body='#3d444d', mut='#6e7781', rule='#d8dee4', acc='#b5431b'),
}
e = html.escape
def w(n, s): open(f"{out}/{n}", 'w').write(s)

ROWS = [
 ('hana-mcp-server', 'MCP server for SAP HANA and HANA Cloud — schema discovery and guarded SQL for AI clients.', 'JavaScript'),
 ('sap-cap-debugger', 'Attach VS Code or DevTools to a live CAP app on Cloud Foundry, in one command.', 'TypeScript'),
 ('agent-sandbox', 'Disposable sandboxes for coding agents. Delegate the task, keep the control.', 'TypeScript'),
 ('ccproxy', 'Self-hosted gateway that runs Cursor and Codex on a Claude subscription.', 'Docker'),
 ('flix-launcher', 'A quiet Android TV launcher. Home is one click from what you’re watching.', 'Kotlin'),
 ('screenxshot', 'Client-side screenshot beautifier and annotator. Nothing leaves the browser.', 'JavaScript'),
]

for m, c in T.items():
    w(f"header-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="230" viewBox="0 0 880 230">
<text x="0" y="22" font-family="{MONO}" font-size="12.5" letter-spacing="1.5" fill="{c['mut']}">HATRIGT<tspan fill="{c['acc']}"> ●</tspan> SOFTWARE DEVELOPER</text>
<text x="-2" y="100" font-family="{SERIF}" font-size="60" fill="{c['fg']}" letter-spacing="-1.2">Ajeeth Kumar</text>
<text font-family="{SANS}" font-size="20" fill="{c['body']}">
 <tspan x="0" y="150">I build developer tools for SAP BTP and the AI agents</tspan>
 <tspan x="0" y="180">that work alongside them<tspan fill="{c['acc']}">.</tspan></tspan>
</text>
<rect x="0" y="222" width="880" height="1" fill="{c['rule']}"/>
</svg>''')
    for key, label in [('work','Selected work'),('about','About')]:
        w(f"label-{key}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="40" viewBox="0 0 880 40">
<text x="0" y="26" font-family="{MONO}" font-size="12.5" letter-spacing="1.5" fill="{c['mut']}">{label.upper()}</text></svg>''')
    for i, (name, desc, lang) in enumerate(ROWS, 1):
        w(f"row-{name}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="84" viewBox="0 0 880 84">
<text x="0" y="34" font-family="{MONO}" font-size="12.5" fill="{c['mut']}">{i:02d}</text>
<text x="44" y="35" font-family="{SERIF}" font-size="24" fill="{c['fg']}">{e(name)}</text>
<text x="880" y="34" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{c['mut']}">{lang}  <tspan fill="{c['acc']}">→</tspan></text>
<text x="44" y="62" font-family="{SANS}" font-size="15" fill="{c['body']}">{e(desc)}</text>
<rect x="0" y="83" width="880" height="1" fill="{c['rule']}"/>
</svg>''')
print("ok")
