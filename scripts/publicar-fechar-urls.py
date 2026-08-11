#!/usr/bin/env python3
"""
E5 — fecha as URLs reais depois da publicação.

Substitui todo {HASH} pelos hashes que o CMS gerou, corrige a data de
publicação no schema, e atualiza o registro e a grade. Roda quantas vezes for
preciso: cada rodada fecha os artigos cuja URL já estiver preenchida.

COMO USAR
  1. Publique o artigo no blog da Nuvemshop.
  2. Cole a URL final em producao/registro/urls-publicadas.csv.
  3. Rode:  python3 scripts/publicar-fechar-urls.py
     Para conferir antes sem gravar nada:
            python3 scripts/publicar-fechar-urls.py --dry-run

O QUE ELE TOCA
  content/<slug>.html          canonical, og:url, @id, BreadcrumbList, links
  content/<slug>-editor.html   cabeçalho e links do corpo
  producao/registro/kw-donos.csv        coluna url_dona
  producao/registro/calendario-*.csv    url_final e status

O QUE ELE RECUSA A FAZER
  - Gravar se a URL não contiver o slug do artigo (protege contra colar a URL
    errada, que é o erro mais caro desta etapa).
  - Dizer que terminou se sobrou algum {HASH}.
"""
import csv, re, sys, glob, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPA = os.path.join(BASE, 'producao/registro/urls-publicadas.csv')
DRY = '--dry-run' in sys.argv
DOMINIO = 'https://usezerohora.com.br'

def ler_mapa():
    if not os.path.exists(MAPA):
        sys.exit(f'Falta {MAPA}. Crie com as colunas: slug,url_real,data_publicacao')
    linhas = [r for r in csv.DictReader(open(MAPA)) if r['url_real'].strip()]
    urls = {}
    for r in linhas:
        slug, url = r['slug'].strip(), r['url_real'].strip().rstrip('/')
        esperado = f'{DOMINIO}/blog/posts/{slug}-'
        if not url.startswith(esperado):
            sys.exit(f'RECUSADO: a URL de "{slug}" não bate com o slug.\n'
                     f'  esperado começar com: {esperado}<hash>\n'
                     f'  recebido:             {url}\n'
                     f'  Confira se o slug criado no CMS é mesmo "{slug}".')
        urls[slug] = {'url': url, 'hash': url[len(esperado):], 'data': r['data_publicacao'].strip()}
    return urls

def aplicar(texto, urls):
    """Troca a URL absoluta e também a relativa. A relativa aparece nos
    comentários de anticanibalização e no registro."""
    n = 0
    for slug, d in urls.items():
        rel = f'/blog/posts/{slug}-{{HASH}}'
        for alvo, novo in ((f'{DOMINIO}{rel}', d['url']),
                           (rel, d['url'].replace(DOMINIO, ''))):
            n += texto.count(alvo)
            texto = texto.replace(alvo, novo)
    return texto, n

def main():
    urls = ler_mapa()
    if not urls:
        sys.exit('Nenhuma URL preenchida ainda em urls-publicadas.csv.')
    print(f'{"[DRY-RUN] " if DRY else ""}Fechando {len(urls)} artigo(s): {", ".join(urls)}\n')
    total = 0
    depois = {}   # texto resultante, para o dry-run reportar o restante de verdade

    # 1. arquivos de conteúdo
    for f in sorted(glob.glob(os.path.join(BASE, 'content/*.html'))):
        s = o = open(f).read()
        s, n = aplicar(s, urls)
        # data de publicação no schema, só do próprio artigo
        slug = os.path.basename(f).replace('-editor.html', '').replace('.html', '')
        if slug in urls and urls[slug]['data']:
            d = urls[slug]['data']
            s2 = re.sub(r'"datePublished": "[0-9-]+"', f'"datePublished": "{d}"', s)
            s2 = re.sub(r'"dateModified": "[0-9-]+"', f'"dateModified": "{d}"', s2)
            if s2 != s: n += 2; s = s2
        depois[f] = s
        if s != o:
            total += n
            print(f'  {n:>3} troca(s)  {os.path.relpath(f, BASE)}')
            if not DRY: open(f, 'w').write(s)

    # 2. registro de dono de keyword
    p = os.path.join(BASE, 'producao/registro/kw-donos.csv')
    rows = list(csv.DictReader(open(p))); fn = list(rows[0].keys()); n = 0
    for r in rows:
        for slug, d in urls.items():
            alvo = f'/blog/posts/{slug}-{{HASH}}'
            if r['url_dona'] == alvo:
                r['url_dona'] = d['url'].replace(DOMINIO, ''); r['status'] = 'publicado'; n += 1
    depois[p] = '\n'.join(r['url_dona'] for r in rows)
    if n:
        total += n; print(f'  {n:>3} troca(s)  producao/registro/kw-donos.csv')
        if not DRY:
            w = csv.DictWriter(open(p, 'w', newline=''), fieldnames=fn); w.writeheader(); w.writerows(rows)

    # 3. grade do mês
    for p in sorted(glob.glob(os.path.join(BASE, 'producao/registro/calendario-*.csv'))):
        rows = list(csv.DictReader(open(p))); fn = list(rows[0].keys()); n = 0
        for r in rows:
            if r['slug'] in urls:
                d = urls[r['slug']]
                r['url_final'] = d['url']; r['status'] = 'publicado'
                if d['data']: r['data_publicacao'] = d['data']
                n += 1
        if n:
            total += n; print(f'  {n:>3} linha(s)  {os.path.relpath(p, BASE)}')
            if not DRY:
                w = csv.DictWriter(open(p, 'w', newline=''), fieldnames=fn); w.writeheader(); w.writerows(rows)

    # 4. o que ainda falta
    print()
    # conta só {HASH} dentro de URL. O marcador também aparece como prosa no
    # comentário de produção, e ali ele é explicação, não pendência.
    resta = {}
    for f, texto in depois.items():
        c = len(re.findall(r'/blog/posts/[a-z0-9-]+-\{HASH\}', texto))
        if c: resta[os.path.relpath(f, BASE)] = c
    print(f'{"Trocas que seriam feitas" if DRY else "Trocas feitas"}: {total}')
    if resta:
        print(f'\nAinda com {{HASH}} ({sum(resta.values())} marcador(es)) — falta publicar os irmãos:')
        for k, v in sorted(resta.items()): print(f'  {v:>3}  {k}')
        print('\nNÃO publique nenhum artigo que ainda tenha {HASH}: canonical com o')
        print('marcador quebra a indexação da página.')
    else:
        print('\nNenhum {HASH} restante. O lote está fechado.')

if __name__ == '__main__':
    main()
