#!/usr/bin/env python3
"""Gera producao/painel/guia-copiar-colar-onda2.html a partir dos content/* da Onda 2.
Ordem = ordem da grade-onda-2.csv (agrupada por hub A–J). Reutilizável: rode quando
os artigos mudarem. Espelha scripts/gerar-guia.py (Onda 1), adaptado às colunas da grade 2."""
import re, csv, base64, os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE)
# ORDEM e dados primários vêm da grade-onda-2.csv (colunas: slug,formato,hub,tipo_kw,keyword,vol,kd,intent,fonte,url_destino)
ORDEM=[]; grade={}
for r in csv.DictReader(open('producao/registro/grade-onda-2.csv',encoding='utf-8')):
    if r['tipo_kw']=='primaria':
        ORDEM.append(r['slug'])
        grade[r['slug']]=(r['keyword'],r['vol'],r['url_destino'],r['hub'],r['formato'])
N=len(ORDEM)
def campo(pat,s):
    m=re.search(pat,s,re.S); return m.group(1).strip() if m else ''
arts=[]
for i,slug in enumerate(ORDEM,1):
    full=open(f'content/{slug}.html',encoding='utf-8').read()
    ed=open(f'content/{slug}-editor.html',encoding='utf-8').read()
    titulo=re.sub(r'<[^>]+>','',campo(r'<h1[^>]*>(.*?)</h1>',full)).strip()
    seo=campo(r'<title>(.*?)</title>',full); meta=campo(r'<meta name="description" content="(.*?)">',full)
    corpo=ed[ed.find('-->')+3:].strip()
    schema='\n\n'.join(re.findall(r'<script type="application/ld\+json">.*?</script>',full,re.S))
    kw,vol,cta,hub,fmt=grade.get(slug,('','','','',''))
    try: volf=f'{int(float(vol)):,}'.replace(',','.')+'/mês'
    except: volf='vol n-d'
    arts.append(dict(n=i,slug=slug,titulo=titulo,seo=seo,meta=meta,corpo=corpo,schema=schema,kw=kw,vol=volf,cta=cta,hub=hub,fmt=fmt))
def b64(s): return base64.b64encode(s.encode('utf-8')).decode('ascii')
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
navs=[];cards=[]
for a in arts:
    navs.append(f'<a href="#a{a["n"]}"><span class="idx-n">{a["n"]:02d}</span>{esc(a["titulo"])}</a>')
    def fld(rot,val,mono=False,big=False):
        cls='val mono' if mono else 'val'; tag='pre' if big else 'div'
        return (f'<div class="field"><div class="field-head"><span class="rot">{rot}</span>'
                f'<button class="copy" data-b64="{b64(val)}">Copiar</button></div>'
                f'<{tag} class="{cls}{" box" if big else ""}">{esc(val)}</{tag}></div>')
    cards.append('\n'.join([
      f'<section class="card" id="a{a["n"]}">',
      f'<header class="card-h"><div class="badge">{a["n"]:02d}/{N}</div>',
      f'<h2>{esc(a["titulo"])}</h2>',
      f'<div class="tags"><span class="tag">KW: {esc(a["kw"])}</span>'
      f'<span class="tag">{a["vol"]}</span>'
      f'<span class="tag">{esc(a["fmt"])} · {esc(a["hub"])}</span>'
      f'<span class="tag mono">slug: {esc(a["slug"])}</span>'
      f'<span class="tag">CTA → {esc(a["cta"])}</span></div></header>',
      '<div class="grid2">',
      fld('Título do post',a['titulo']), fld('Slug (URL)',a['slug'],mono=True),
      fld('Title SEO',a['seo']), fld('Meta description',a['meta']),
      '</div>',
      fld('Corpo do post — cole no modo HTML/código (&lt;&gt;) do editor',a['corpo'],mono=True,big=True),
      '<details class="det"><summary>Dados estruturados (schema) — opcional, cole no campo de SEO avançado</summary>'
      '<p class="hint">Troque <code>{HASH}</code> pela URL real do post depois de publicar. Sem o hash, deixe como está — não quebra o texto do artigo.</p>'
      + fld('Schema JSON-LD',a['schema'],mono=True,big=True) + '</details>',
      '</section>']))
TPL=open('scripts/_guia_template.html',encoding='utf-8').read()
TPL=TPL.replace('Onda 1','Onda 2').replace('20 artigos',f'{N} artigos').replace('/20','/'+str(N))
html=TPL.replace('<!--NAV-->','\n'.join(navs)).replace('<!--CARDS-->','\n'.join(cards))
open('producao/painel/guia-copiar-colar-onda2.html','w',encoding='utf-8').write(html)
print(f'guia onda2 gerado: {len(html)} bytes, {N} artigos')
