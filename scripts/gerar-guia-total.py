#!/usr/bin/env python3
"""Gera producao/painel/guia-copiar-colar-total.html com todos os 70 artigos
produzidos (Onda 1: 20 + Onda 2: 50). Navegação por onda e hub. Reutilizável."""
import re, csv, base64, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE)

def campo(pat, s):
    m = re.search(pat, s, re.S); return m.group(1).strip() if m else ''

def carregar_onda1():
    ORDEM = [
        'maio-de-praia','saida-de-praia-guia','vestido-de-praia','biquini-cortininha',
        'sunga-masculina','short-de-praia-masculino','poncho-de-surf','poncho-toalha-infantil',
        'roupa-de-neoprene','pilates','yoga','natacao-guia','protetor-solar-facial',
        'protetor-solar-infantil','treino-funcional','mindfulness','o-que-e-fps',
        'insolacao-sintomas','skimboard','bola-de-futevolei'
    ]
    grade = {}
    for r in csv.DictReader(open('producao/registro/grade-onda-1.csv', encoding='utf-8')):
        if r['tipo_kw'] == 'primaria':
            grade[r['slug']] = (r['keyword'], r['vol'], r.get('url_cta',''), r.get('hub','Onda 1'), r.get('papel',''))
    arts = []
    for slug in ORDEM:
        try:
            full = open(f'content/{slug}.html', encoding='utf-8').read()
            ed   = open(f'content/{slug}-editor.html', encoding='utf-8').read()
        except FileNotFoundError:
            print(f'  AVISO: {slug} não encontrado, pulando')
            continue
        titulo = re.sub(r'<[^>]+>', '', campo(r'<h1[^>]*>(.*?)</h1>', full)).strip()
        seo    = campo(r'<title>(.*?)</title>', full)
        meta   = campo(r'<meta name="description" content="(.*?)">', full)
        corpo  = ed[ed.find('-->')+3:].strip()
        schema = '\n\n'.join(re.findall(r'<script type="application/ld\+json">.*?</script>', full, re.S))
        kw, vol, cta, hub, fmt = grade.get(slug, ('', '', '', 'Onda 1', ''))
        try: volf = f'{int(float(vol)):,}'.replace(',', '.') + '/mês'
        except: volf = 'vol n-d'
        arts.append(dict(slug=slug, titulo=titulo, seo=seo, meta=meta, corpo=corpo,
                         schema=schema, kw=kw, vol=volf, cta=cta, hub=hub, fmt=fmt, onda='Onda 1'))
    return arts

def carregar_onda2():
    ORDEM = []; grade = {}
    for r in csv.DictReader(open('producao/registro/grade-onda-2.csv', encoding='utf-8')):
        if r['tipo_kw'] == 'primaria':
            ORDEM.append(r['slug'])
            grade[r['slug']] = (r['keyword'], r['vol'], r['url_destino'], r['hub'], r['formato'])
    arts = []
    for slug in ORDEM:
        try:
            full = open(f'content/{slug}.html', encoding='utf-8').read()
            ed   = open(f'content/{slug}-editor.html', encoding='utf-8').read()
        except FileNotFoundError:
            print(f'  AVISO: {slug} não encontrado, pulando')
            continue
        titulo = re.sub(r'<[^>]+>', '', campo(r'<h1[^>]*>(.*?)</h1>', full)).strip()
        seo    = campo(r'<title>(.*?)</title>', full)
        meta   = campo(r'<meta name="description" content="(.*?)">', full)
        corpo  = ed[ed.find('-->')+3:].strip()
        schema = '\n\n'.join(re.findall(r'<script type="application/ld\+json">.*?</script>', full, re.S))
        kw, vol, cta, hub, fmt = grade.get(slug, ('', '', '', '', ''))
        try: volf = f'{int(float(vol)):,}'.replace(',', '.') + '/mês'
        except: volf = 'vol n-d'
        arts.append(dict(slug=slug, titulo=titulo, seo=seo, meta=meta, corpo=corpo,
                         schema=schema, kw=kw, vol=volf, cta=cta, hub=hub, fmt=fmt, onda='Onda 2'))
    return arts

print('Carregando artigos...')
arts_1 = carregar_onda1()
arts_2 = carregar_onda2()
todos  = arts_1 + arts_2
N = len(todos)
print(f'  Onda 1: {len(arts_1)} | Onda 2: {len(arts_2)} | Total: {N}')

def b64(s): return base64.b64encode(s.encode('utf-8')).decode('ascii')
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def fld(rot, val, mono=False, big=False):
    cls = 'val mono' if mono else 'val'; tag = 'pre' if big else 'div'
    return (f'<div class="field"><div class="field-head"><span class="rot">{rot}</span>'
            f'<button class="copy" data-b64="{b64(val)}">Copiar</button></div>'
            f'<{tag} class="{cls}{" box" if big else ""}">{esc(val)}</{tag}></div>')

# Navegar por onda
nav_blocos = []
cards_html = []
onda_atual = None
for i, a in enumerate(todos, 1):
    a['n'] = i
    if a['onda'] != onda_atual:
        onda_atual = a['onda']
        nav_blocos.append(f'<div class="nav-onda">{onda_atual}</div>')
    nav_blocos.append(
        f'<a href="#a{i}"><span class="idx-n">{i:02d}</span>{esc(a["titulo"])}</a>'
    )
    onda_badge_cls = 'badge-onda1' if a['onda'] == 'Onda 1' else 'badge-onda2'
    cards_html.append('\n'.join([
        f'<section class="card" id="a{i}">',
        f'<header class="card-h">',
        f'<div style="display:flex;gap:8px;align-items:center;margin-bottom:4px">',
        f'<div class="badge">{i:02d}/{N}</div>',
        f'<span class="badge-onda {onda_badge_cls}">{esc(a["onda"])}</span>',
        f'</div>',
        f'<h2>{esc(a["titulo"])}</h2>',
        f'<div class="tags">',
        f'<span class="tag">KW: {esc(a["kw"])}</span>',
        f'<span class="tag">{a["vol"]}</span>',
        (f'<span class="tag">{esc(a["fmt"])} · {esc(a["hub"])}</span>' if a["fmt"] else f'<span class="tag">{esc(a["hub"])}</span>'),
        f'<span class="tag mono">slug: {esc(a["slug"])}</span>',
        (f'<span class="tag">CTA → {esc(a["cta"])}</span>' if a["cta"] else ''),
        f'</div></header>',
        '<div class="grid2">',
        fld('Título do post', a['titulo']),
        fld('Slug (URL)', a['slug'], mono=True),
        fld('Title SEO', a['seo']),
        fld('Meta description', a['meta']),
        '</div>',
        fld('Corpo do post — cole no modo HTML/código (&lt;&gt;) do editor', a['corpo'], mono=True, big=True),
        '<details class="det"><summary>Dados estruturados (schema) — opcional</summary>'
        '<p class="hint">Troque <code>{HASH}</code> pela URL real do post depois de publicar.</p>'
        + fld('Schema JSON-LD', a['schema'], mono=True, big=True) + '</details>',
        '</section>'
    ]))

# Montar HTML final a partir do template com ajustes para total
TPL = open('scripts/_guia_template.html', encoding='utf-8').read()

# Injetar CSS extra para badges de onda
extra_css = """
.nav-onda{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);font-weight:700;padding:10px 9px 4px;margin-top:4px}
.badge-onda{font-size:.65rem;font-weight:700;letter-spacing:.06em;padding:2px 7px;border-radius:10px}
.badge-onda1{background:#e8f4f1;color:#0e7c6b}
.badge-onda2{background:#e8eef9;color:#2554a8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  .badge-onda1{background:#0e2e28;color:#3bb39c}
  .badge-onda2{background:#0e1f3a;color:#7baaf7}
}}
:root[data-theme="dark"] .badge-onda1{background:#0e2e28;color:#3bb39c}
:root[data-theme="dark"] .badge-onda2{background:#0e1f3a;color:#7baaf7}
"""
TPL = TPL.replace('</style>', extra_css + '\n</style>')

# Substituições de texto — manter semântica correta
TPL = TPL.replace('Publicador Onda 1', 'Publicador Total')
TPL = TPL.replace(
    '<div class="kick">Use Zero Hora · Onda 1 · 20 artigos</div>',
    f'<div class="kick">Use Zero Hora · Onda 1 + Onda 2 · {N} artigos</div>'
)
TPL = TPL.replace(
    '<h1>Publicador da Onda 1</h1>',
    '<h1>Todos os artigos produzidos</h1>'
)
TPL = TPL.replace(
    'Cada artigo com os campos prontos para colar no editor de blog da Nuvemshop. Um botão por campo: clique, cole no lugar certo, salve como rascunho.',
    f'70 artigos prontos para publicação — 20 da Onda 1 e 50 da Onda 2. Cada card tem os campos para colar diretamente no editor de blog da Nuvemshop.'
)
TPL = TPL.replace('20 artigos', f'{N} artigos')
TPL = TPL.replace('/20', f'/{N}')

html = TPL.replace('<!--NAV-->', '\n'.join(nav_blocos)).replace('<!--CARDS-->', '\n'.join(cards_html))
out  = 'producao/painel/guia-copiar-colar-total.html'
open(out, 'w', encoding='utf-8').write(html)
print(f'Guia total gerado: {out} ({len(html):,} bytes, {N} artigos)')
