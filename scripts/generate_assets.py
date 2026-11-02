import sys, html
out = sys.argv[1]
F = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
M = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
T = {
 'dark':  dict(bg='#0d1117', card='#161b22', border='#30363d', fg='#e6edf3', mut='#8b949e', grid='#1f2630', pill='#1f6feb22', pillfg='#79c0ff', a1='#58a6ff', a2='#bc8cff'),
 'light': dict(bg='#ffffff', card='#f6f8fa', border='#d0d7de', fg='#1f2328', mut='#59636e', grid='#eef1f4', pill='#ddf4ff', pillfg='#0969da', a1='#0969da', a2='#8250df'),
}
def w(name, s): open(f"{out}/{name}", 'w').write(s)

for m, c in T.items():
    # ---------- header ----------
    w(f"header-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="260" viewBox="0 0 900 260">
<defs>
 <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c['a1']}"/><stop offset="1" stop-color="{c['a2']}"/></linearGradient>
 <pattern id="p" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{c['grid']}" stroke-width="1"/></pattern>
 <radialGradient id="r" cx="0.85" cy="0.2" r="0.6"><stop offset="0" stop-color="{c['a2']}" stop-opacity=".18"/><stop offset="1" stop-color="{c['a2']}" stop-opacity="0"/></radialGradient>
 <linearGradient id="fade" x1="0" x2="1"><stop offset=".35" stop-color="{c['bg']}" stop-opacity="1"/><stop offset="1" stop-color="{c['bg']}" stop-opacity="0"/></linearGradient>
 <style>
  .in{{opacity:0;animation:f .8s ease-out forwards}} .d1{{animation-delay:.15s}} .d2{{animation-delay:.3s}} .d3{{animation-delay:.45s}}
  @keyframes f{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
  .cur{{animation:b 1.1s steps(1) infinite}} @keyframes b{{50%{{opacity:0}}}}
  @media (prefers-reduced-motion:reduce){{.in{{animation:none;opacity:1}}.cur{{animation:none}}}}
 </style>
</defs>
<rect width="900" height="260" rx="16" fill="{c['bg']}"/>
<rect width="900" height="260" rx="16" fill="url(#p)"/>
<rect width="900" height="260" rx="16" fill="url(#fade)"/>
<rect width="900" height="260" rx="16" fill="url(#r)"/>
<rect x=".5" y=".5" width="899" height="259" rx="15.5" fill="none" stroke="{c['border']}"/>
<g font-family="{F}">
 <text class="in" x="48" y="72" font-family="{M}" font-size="14" fill="{c['a1']}">~/hatrigt $ whoami<tspan class="cur">▍</tspan></text>
 <text class="in d1" x="46" y="128" font-size="46" font-weight="700" fill="{c['fg']}" letter-spacing="-1">Ajeeth Kumar</text>
 <rect class="in d1" x="48" y="146" width="64" height="4" rx="2" fill="url(#g)"/>
 <text class="in d2" x="48" y="186" font-size="19" fill="{c['fg']}">SAP BTP developer building <tspan fill="url(#g)" font-weight="600">AI agent tooling</tspan> &amp; dev tools</text>
 <text class="in d3" x="48" y="218" font-size="14" fill="{c['mut']}">CAP · HANA Cloud · Cloud Foundry · MCP · Node.js · TypeScript</text>
</g>
<g transform="translate(700 70)"><g class="in d2" font-family="{M}" font-size="12">
 <rect width="160" height="120" rx="10" fill="{c['card']}" stroke="{c['border']}"/>
 <circle cx="16" cy="16" r="4" fill="#ff5f57"/><circle cx="30" cy="16" r="4" fill="#febc2e"/><circle cx="44" cy="16" r="4" fill="#28c840"/>
 <text x="14" y="46" fill="{c['mut']}">{{</text>
 <text x="26" y="64" fill="{c['pillfg']}">"focus"<tspan fill="{c['mut']}">:</tspan></text>
 <text x="38" y="82" fill="{c['fg']}">"MCP + SAP"</text>
 <text x="14" y="102" fill="{c['mut']}">}}</text></g>
</g>
</svg>''')

    # ---------- section titles ----------
    for key, label, num in [('about','About','01'),('projects','Featured Projects','02'),('stack','Tech Stack','03'),('stats','Activity','04')]:
        w(f"title-{key}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="48" viewBox="0 0 900 48">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c['a1']}"/><stop offset="1" stop-color="{c['a2']}"/></linearGradient></defs>
<text x="0" y="32" font-family="{M}" font-size="13" fill="{c['a1']}">{num}</text>
<text x="30" y="33" font-family="{F}" font-size="22" font-weight="600" fill="{c['fg']}">{label}</text>
<rect x="0" y="45" width="900" height="1" fill="{c['border']}"/><rect x="0" y="44" width="40" height="3" rx="1.5" fill="url(#g)"/>
</svg>''')

# ---------- project cards ----------
P = [
 ('hana-mcp-server','MCP server for SAP HANA & HANA Cloud.','AI clients explore schemas and run SQL with guardrails.',['MCP','SAP HANA','AI'],'JavaScript','#f1e05a'),
 ('sap-cap-debugger','Debug live CAP apps on BTP in one command.','Attach VS Code or Chrome DevTools over cf ssh. No redeploy.',['SAP CAP','Cloud Foundry','CLI'],'JavaScript','#f1e05a'),
 ('agent-sandbox','Sandbox-as-a-service for coding agents.','Delegate the task, keep the control. Hosted or self-hosted.',['AI Agents','Sandbox','Infra'],'TypeScript','#3178c6'),
 ('ccproxy','Run Cursor & Codex on your Claude plan.','One self-hosted HTTPS endpoint for your agent harnesses.',['Proxy','Claude','Dev Tools'],'Docker','#384d54'),
 ('flix-launcher','A calm, film-first Android TV launcher.','One click from Home to what you are watching. Nothing else.',['Android TV','Kotlin','UX'],'Kotlin','#A97BFF'),
 ('screenxshot','Every screenshot, instantly beautiful.','Privacy-first, client-side beautifier and annotator.',['Web App','Design','Privacy'],'JavaScript','#f1e05a'),
]
for m, c in T.items():
    for name, l1, l2, tags, lang, lc in P:
        pills, x = '', 24
        for t in tags:
            wd = int(len(t)*7.2)+20
            pills += f'<rect x="{x}" y="128" width="{wd}" height="22" rx="11" fill="{c["pill"]}"/><text x="{x+wd/2}" y="143" text-anchor="middle" font-size="11.5" font-weight="500" fill="{c["pillfg"]}">{html.escape(t)}</text>'
            x += wd + 6
        w(f"proj-{name}-{m}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="172" viewBox="0 0 440 172">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c['a1']}"/><stop offset="1" stop-color="{c['a2']}"/></linearGradient></defs>
<rect x=".5" y=".5" width="439" height="171" rx="12" fill="{c['card']}" stroke="{c['border']}"/>
<rect x="24" y="0.5" width="48" height="3" rx="1.5" fill="url(#g)"/>
<g font-family="{F}">
 <svg x="24" y="24" width="16" height="16" viewBox="0 0 16 16"><path fill="{c['mut']}" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>
 <text x="48" y="37" font-size="16" font-weight="600" fill="{c['a1']}">{name}</text>
 <text x="416" y="37" text-anchor="end" font-size="16" fill="{c['mut']}">↗</text>
 <text x="24" y="74" font-size="14.5" font-weight="500" fill="{c['fg']}">{html.escape(l1)}</text>
 <text x="24" y="98" font-size="13" fill="{c['mut']}">{html.escape(l2)}</text>
 {pills}
 <circle cx="{416-len(lang)*6.6-10}" cy="139" r="5" fill="{lc}"/>
 <text x="416" y="143" text-anchor="end" font-size="12" fill="{c['mut']}">{lang}</text>
</g></svg>''')
print("ok")
