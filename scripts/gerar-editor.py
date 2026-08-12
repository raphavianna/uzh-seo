#!/usr/bin/env python3
"""Deriva content/<slug>-editor.html a partir de content/<slug>.html.

O -editor.html e a versao que o time cola no editor de blog do CMS: sem head,
sem schema, sem h1 (o CMS tem campo proprio de titulo). Mantem o corpo com as
imagens reais do CDN e os links. Extrai os campos do CMS do arquivo completo:
  Titulo do post  = texto do <h1>
  Title SEO       = conteudo do <title>
  Meta description= conteudo da <meta name=description>
  URL prevista    = href do <link rel=canonical> (com {HASH})

USO: python3 scripts/gerar-editor.py <slug> [<slug> ...]   (ou --todos)
"""
import re, sys, os, glob
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAB = """<!--
  VERSAO EDITOR DE BLOG: sem head, sem schema, sem breadcrumb, sem h1.
  Titulo do post (campo do CMS): {titulo}
  Title SEO: {seo}
  Meta description: {meta}

  ================== ATENCAO: {{HASH}} PRECISA SER SUBSTITUIDO ==================
  O blog da Nuvemshop monta a URL como
    https://usezerohora.com.br/blog/posts/<slug>-<hash>
  e gera o <hash> so na publicacao. URL prevista: {url}
  Em E5: publique, copie a URL final com o hash, e troque {{HASH}} no arquivo
  {slug}.html (canonical, og:url, BlogPosting @id, BreadcrumbList) e na coluna
  url_dona de producao/registro/kw-donos.csv. Canonical com o marcador quebra a
  indexacao — nao publique com o placeholder.

  Schema BlogPosting/BreadcrumbList/FAQPage: colar via campo de dados
  estruturados do CMS, com o JSON de {slug}.html, ja com o hash.
  Imagens: URLs do CDN da propria loja (acdn-us.mitiendanube.com), ja no corpo.
  ARQUIVO GERADO por scripts/gerar-editor.py — nao editar a mao; edite {slug}.html.
-->
"""

def campo(pat, s, flags=re.S):
    m = re.search(pat, s, flags)
    return m.group(1).strip() if m else ''

def gera(slug):
    full_p = os.path.join(BASE, f'content/{slug}.html')
    if not os.path.exists(full_p):
        print(f'  ! {slug}: content/{slug}.html nao existe'); return
    s = open(full_p, encoding='utf-8').read()
    seo = campo(r'<title>(.*?)</title>', s)
    meta = campo(r'<meta name="description" content="(.*?)">', s)
    url = campo(r'<link rel="canonical" href="(.*?)">', s)
    h1 = campo(r'<h1[^>]*>(.*?)</h1>', s)
    titulo = re.sub(r'<[^>]+>', '', h1).strip()
    # corpo = do fim do </h1> ao fim do arquivo
    m = re.search(r'</h1>', s)
    corpo = s[m.end():].strip() if m else s
    out = CAB.format(titulo=titulo, seo=seo, meta=meta, url=url, slug=slug) + '\n' + corpo + '\n'
    open(os.path.join(BASE, f'content/{slug}-editor.html'), 'w', encoding='utf-8').write(out)
    print(f'  ok {slug}-editor.html  (titulo: {titulo[:50]})')

alvos = sys.argv[1:]
if alvos == ['--todos']:
    alvos = [os.path.basename(f)[:-5] for f in glob.glob(os.path.join(BASE, 'content/*.html'))
             if not f.endswith('-editor.html')]
if not alvos:
    sys.exit('USO: gerar-editor.py <slug> [...] | --todos')
for slug in alvos:
    gera(slug)
