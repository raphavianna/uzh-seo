#!/usr/bin/env python3
"""
Colhe as URLs reais dos posts do blog e preenche urls-publicadas.csv.

POR QUE ELE EXISTE
  A URL de post é https://usezerohora.com.br/blog/posts/<slug>-<hash>, e o hash
  de 12 caracteres nasce no CMS na publicação. Depois de publicar, alguém
  precisa levar essas URLs de volta para o repositório. Este script faz isso
  lendo o blog público, sem API, sem credencial e sem conector.

  Ele NÃO adivinha URL de post não publicado. Antes da publicação o hash não
  existe em lugar nenhum, e nenhuma ferramenta pode buscá-lo.

COMO USAR
  python3 scripts/colher-urls-blog.py
  python3 scripts/colher-urls-blog.py --dry-run     # só mostra o que achou

  Rode de uma máquina que alcance usezerohora.com.br. Na sessão remota do
  Claude Code a política de egresso do ambiente pode bloquear o domínio; nesse
  caso o script diz isso em vez de fingir que não achou post nenhum.

DEPOIS
  python3 scripts/publicar-fechar-urls.py     # fecha os {HASH} no repositório
  python3 scripts/gerar-painel.py             # atualiza o painel
"""
import csv, os, re, sys, urllib.error, urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = 'https://usezerohora.com.br'
SAIDA = os.path.join(BASE, 'producao/registro/urls-publicadas.csv')
DRY = '--dry-run' in sys.argv

# Sem seletor de CSS: o que identifica um post é o formato da própria URL, e
# esse formato foi confirmado pelo time. Markup do tema pode mudar; o formato
# da URL, não.
PADRAO = re.compile(r'/blog/posts/([a-z0-9][a-z0-9-]*?)-([a-z0-9]{12})(?![a-z0-9-])')

# Várias portas de entrada, porque nenhuma é garantida. O que uma não listar,
# outra costuma listar.
FONTES = [
    '/blog/',
    '/blog/?page=2',
    '/blog/?page=3',
    '/sitemap.xml',
    '/blog/sitemap.xml',
]


def buscar(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'uzh-seo/colher-urls (+https://github.com/raphavianna/uzh-seo)'
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode('utf-8', 'replace')


def main():
    achados, erros, lidas = {}, [], 0
    for caminho in FONTES:
        url = DOMINIO + caminho
        try:
            html = buscar(url)
        except urllib.error.HTTPError as e:
            if e.code != 404:
                erros.append('%s -> HTTP %s' % (caminho, e.code))
            continue
        except Exception as e:
            erros.append('%s -> %s' % (caminho, type(e).__name__ + ': ' + str(e)[:90]))
            continue
        lidas += 1
        for slug, hashe in PADRAO.findall(html):
            achados.setdefault(slug, '%s/blog/posts/%s-%s' % (DOMINIO, slug, hashe))

    if not lidas:
        print('Nenhuma fonte pôde ser lida. O blog não foi alcançado.')
        for e in erros:
            print('  %s' % e)
        print('\nCausa provável: a política de egresso deste ambiente bloqueia')
        print('usezerohora.com.br. Rode o script de uma máquina com acesso, ou')
        print('libere o domínio na configuração de rede do ambiente.')
        print('Nada foi escrito. Isto NÃO significa que o blog está vazio.')
        sys.exit(2)

    print('%d fonte(s) lida(s), %d post(s) encontrado(s).' % (lidas, len(achados)))
    if erros:
        print('Fontes que falharam (o script segue com as demais):')
        for e in erros:
            print('  %s' % e)

    # Cruza com a grade para dizer o que é do lote e o que é post antigo.
    import glob
    grade = sorted(glob.glob(os.path.join(BASE, 'producao/registro/calendario-*.csv')))
    esperados = {}
    if grade:
        for r in csv.DictReader(open(grade[-1], encoding='utf-8')):
            esperados[r['slug']] = r['status']

    print()
    for slug in sorted(achados):
        marca = 'na grade (%s)' % esperados[slug] if slug in esperados else 'fora da grade'
        print('  %-32s %s  [%s]' % (slug, achados[slug].replace(DOMINIO, ''), marca))
    faltando = [s for s, st in esperados.items()
                if st in ('aprovado', 'agendado', 'publicado') and s not in achados]
    if faltando:
        print('\nAprovados ou publicados na grade e ausentes no blog:')
        for s in faltando:
            print('  %s' % s)

    do_lote = {s: u for s, u in achados.items() if s in esperados}
    if not do_lote:
        print('\nNenhum post encontrado bate com um slug da grade. Nada a escrever.')
        return
    if DRY:
        print('\nDry-run: %d linha(s) seriam escritas em %s'
              % (len(do_lote), os.path.relpath(SAIDA, BASE)))
        return

    # Preserva a data já registrada de quem for reencontrado.
    datas = {}
    if os.path.exists(SAIDA):
        for r in csv.DictReader(open(SAIDA, encoding='utf-8')):
            if r.get('data_publicacao'):
                datas[r['slug']] = r['data_publicacao']
    with open(SAIDA, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['slug', 'url_real', 'data_publicacao'])
        for slug in sorted(do_lote):
            w.writerow([slug, do_lote[slug], datas.get(slug, '')])
    print('\nEscrito: %s (%d linha(s)).' % (os.path.relpath(SAIDA, BASE), len(do_lote)))
    print('A coluna data_publicacao fica vazia para post novo: o blog não a')
    print('expõe de forma confiável. Preencha antes de rodar publicar-fechar-urls.py.')


if __name__ == '__main__':
    main()
