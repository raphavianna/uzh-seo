#!/usr/bin/env python3
"""
Publica um artigo do lote no blog da Nuvemshop via API.

Só toca o blog da loja. Cria o post a partir do arquivo de content/, montando
o corpo limpo: tira o comentário de produção, transforma link de irmão ainda
não publicado em texto, e mantém as imagens do CDN e os links de produto.

USO
  python3 scripts/publicar-blog-api.py --slug blusa-com-protecao-uv            # rascunho
  python3 scripts/publicar-blog-api.py --slug blusa-com-protecao-uv --publicar  # no ar
  python3 scripts/publicar-blog-api.py --slug blusa-com-protecao-uv --dry-run   # não envia
  python3 scripts/publicar-blog-api.py --lote                                   # os 5, na ordem

SEGURANÇA
  - Sem --publicar, o post nasce como RASCUNHO (published_at null): aparece no
    painel do blog para revisão e não fica público.
  - Recusa criar se o arquivo tiver {HASH} pendente (link de irmão quebrado).
  - Credenciais lidas de integracao-nuvemshop/.env, nunca gravadas aqui.
  - Grava a URL criada em producao/registro/urls-publicadas.csv.
"""
import argparse, csv, json, os, re, sys, urllib.request, urllib.error, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = '/workspace/integracao-nuvemshop/.env'
DOMINIO = 'https://usezerohora.com.br'
BLOG_ID = '019f2858-20bc-7cca-9606-b08b2df67dcd'
UA = 'integracao-nuvemshop (raphael.ferreira@nsx.bet)'
# ordem de publicação: raiz -> dependentes -> hub
LOTE = ['blusa-com-protecao-uv', 'camisa-de-praia-feminina',
        'camiseta-com-protecao-uv', 'rash-guard-infantil', 'o-que-e-rash-guard']


def cred():
    if not os.path.exists(ENV):
        sys.exit(f'Falta {ENV} com NUVEMSHOP_STORE_ID e NUVEMSHOP_ACCESS_TOKEN.')
    e = dict(re.findall(r'^(NUVEMSHOP_\w+)=(.*)$', open(ENV).read(), re.M))
    sid, tok = e.get('NUVEMSHOP_STORE_ID'), e.get('NUVEMSHOP_ACCESS_TOKEN')
    if not sid or not tok:
        sys.exit('Credenciais incompletas no .env.')
    return sid, tok


def monta(slug):
    f = os.path.join(BASE, f'content/{slug}-editor.html')
    if not os.path.exists(f):
        sys.exit(f'Não existe {f}.')
    s = open(f, encoding='utf-8').read()
    topo = s[:s.find('-->')]

    def campo(rot):
        m = re.search(rot + r':\s*(.+)', topo)
        return m.group(1).strip() if m else ''
    title = campo(r'Titulo do post \(campo do CMS\)')
    seo_title = campo('Title SEO')
    meta = campo('Meta description')
    corpo = s[s.find('-->') + 3:]
    corpo = re.sub(r'<a\s+href="[^"]*\{HASH\}[^"]*">(.*?)</a>', r'\1', corpo, flags=re.S)
    corpo = re.sub(r'<!--.*?-->', '', corpo, flags=re.S).strip()
    if '{HASH}' in corpo:
        sys.exit(f'{slug}: sobrou {{HASH}} no corpo. Não publico link quebrado.')
    if not (title and meta and corpo):
        sys.exit(f'{slug}: faltou title, meta ou corpo.')
    return title, seo_title or title, meta, corpo


def registra_url(slug, url, data):
    p = os.path.join(BASE, 'producao/registro/urls-publicadas.csv')
    linhas = {}
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            linhas[r['slug']] = r
    linhas[slug] = {'slug': slug, 'url_real': url, 'data_publicacao': data or ''}
    with open(p, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['slug', 'url_real', 'data_publicacao'])
        for s in sorted(linhas):
            r = linhas[s]
            w.writerow([r['slug'], r['url_real'], r.get('data_publicacao', '')])


def publica(slug, sid, tok, ao_ar, dry):
    title, seo_title, meta, corpo = monta(slug)
    hoje = datetime.date.today().isoformat()
    body = {
        'metadata': {'language': 'pt'},
        'published_at': f'{hoje}T12:00:00.000Z' if ao_ar else None,
        'data': [{
            'language': 'pt', 'title': title, 'summary': meta,
            'seo_title': seo_title[:70], 'seo_description': meta, 'content': corpo,
        }],
    }
    estado = 'NO AR' if ao_ar else 'rascunho'
    print(f'[{slug}] {estado} — title {len(title)}, meta {len(meta)}, corpo {len(corpo)}b, {corpo.count("<img")} img')
    if dry:
        print('  [dry-run] não enviado.')
        return
    url = f'https://api.nuvemshop.com.br/2025-03/{sid}/blogs/{BLOG_ID}/posts'
    req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), method='POST',
        headers={'Authentication': f'bearer {tok}', 'User-Agent': UA, 'Content-Type': 'application/json'})
    try:
        r = urllib.request.urlopen(req, timeout=45)
        out = json.load(r)
    except urllib.error.HTTPError as e:
        print(f'  FALHOU HTTP {e.code}: {e.read().decode()[:300]}')
        return
    p = out.get('post') or out
    handle = (p.get('data') or [{}])[0].get('handle')
    post_url = f'{DOMINIO}/blog/posts/{handle}'
    registra_url(slug, post_url, hoje if ao_ar else '')
    print(f'  criado: post_id {p.get("post_id")}')
    print(f'  URL:    {post_url}')
    print(f'  publicado_em: {p.get("published_at")}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug')
    ap.add_argument('--lote', action='store_true')
    ap.add_argument('--publicar', action='store_true', help='põe no ar; sem isso, rascunho')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    if not a.slug and not a.lote:
        sys.exit('Passe --slug <slug> ou --lote.')
    sid, tok = cred()
    alvos = LOTE if a.lote else [a.slug]
    for slug in alvos:
        publica(slug, sid, tok, a.publicar, a.dry_run)


if __name__ == '__main__':
    main()
