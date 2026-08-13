#!/usr/bin/env python3
"""
Aplica no repositório o patch exportado pelo painel gerencial.

O painel roda no navegador e não escreve em disco. O botão Exportar baixa um
`patch-painel.json` com a grade atualizada e os textos que foram editados;
este script escreve os dois de volta.

  python3 scripts/aplicar-patch-painel.py ~/Downloads/patch-painel.json
  python3 scripts/aplicar-patch-painel.py patch-painel.json --dry-run

O QUE ELE ESCREVE
  producao/registro/calendario-AAAA-MM.csv   status, datas, url_final, motivo
  content/<slug>.html e <slug>-editor.html   só os que o painel marcou
  producao/registro/kw-donos.csv             url_dona dos artigos publicados
  producao/registro/urls-publicadas.csv      registro das URLs reais

O QUE ELE RECUSA A FAZER
  - Escrever arquivo de conteúdo que não exista no repositório. Caminho novo
    é sinal de patch de outro repo ou de slug renomeado à mão.
  - Escrever URL de post que não bata com o slug do arquivo.
  - Escrever texto que ainda contenha o marcador {HASH} num artigo marcado
    como publicado: canonical com marcador deindexa a página.

Depois de aplicar, regere o painel:
  python3 scripts/gerar-painel.py
"""
import csv, io, json, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = 'https://usezerohora.com.br'
DRY = '--dry-run' in sys.argv


def caminho(rel):
    return os.path.join(BASE, rel)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit('Uso: python3 scripts/aplicar-patch-painel.py <patch-painel.json> [--dry-run]')
    origem = args[0]
    if not os.path.exists(origem):
        sys.exit('Não achei %s' % origem)

    try:
        p = json.load(open(origem, encoding='utf-8'))
    except json.JSONDecodeError as e:
        sys.exit('O arquivo não é JSON válido: %s' % e)
    for chave in ('grade', 'arquivos'):
        if chave not in p:
            sys.exit('O patch não tem a chave "%s". Confira se exportou pelo botão Exportar.' % chave)

    print('%sPatch gerado em %s' % ('[DRY-RUN] ' if DRY else '', p.get('gerado_em', 'data não registrada')))

    recusas = []
    escritas = []

    # ------------------------------------------------------------------ 1. grade
    grade_rel = p['grade']['caminho']
    if not os.path.exists(caminho(grade_rel)):
        sys.exit('RECUSADO: a grade %s não existe neste repositório.' % grade_rel)
    linhas_novas = list(csv.DictReader(io.StringIO(p['grade']['csv'])))
    atual = list(csv.DictReader(open(caminho(grade_rel), encoding='utf-8')))
    por_id = {r['id']: r for r in atual}
    mudou_grade, novas_colunas = 0, set()
    for nova in linhas_novas:
        r = por_id.get(nova['id'])
        if r is None:
            recusas.append('linha %s do patch não existe na grade' % nova['id'])
            continue
        for col, val in nova.items():
            if col not in r:
                novas_colunas.add(col)
                r[col] = val
                mudou_grade += 1
            elif r[col] != val:
                r[col] = val
                mudou_grade += 1
    if mudou_grade:
        escritas.append((grade_rel, '%d campo(s)%s' % (
            mudou_grade, ', coluna nova: ' + ', '.join(sorted(novas_colunas)) if novas_colunas else '')))

    publicados = {r['slug']: r for r in atual if r.get('status') == 'publicado' and r.get('url_final')}

    # -------------------------------------------------------- 2. textos editados
    for rel, texto in sorted(p['arquivos'].items()):
        if not os.path.exists(caminho(rel)):
            recusas.append('%s não existe no repositório' % rel)
            continue
        slug = os.path.basename(rel).replace('-editor.html', '').replace('.html', '')
        if slug in publicados and re.search(r'/blog/posts/[a-z0-9-]+-\{HASH\}', texto):
            recusas.append('%s está marcado como publicado e o texto ainda tem {HASH}' % rel)
            continue
        if open(caminho(rel), encoding='utf-8').read() != texto:
            escritas.append((rel, '%d bytes' % len(texto.encode('utf-8'))))

    # ------------------------------------------------- 3. URLs reais e kw-donos
    urls = {}
    for u in p.get('urls_publicadas', []):
        esperado = '%s/blog/posts/%s-' % (DOMINIO, u['slug'])
        if not u['url'].startswith(esperado):
            recusas.append('a URL de %s não bate com o slug (esperado começar com %s)' % (u['slug'], esperado))
            continue
        urls[u['slug']] = u

    donos_rel = 'producao/registro/kw-donos.csv'
    donos = list(csv.DictReader(open(caminho(donos_rel), encoding='utf-8')))
    mudou_donos = 0
    for d in donos:
        slug = os.path.basename(d['artigo']).replace('.html', '')
        u = urls.get(slug)
        if u and d['url_dona'] == '/blog/posts/%s-{HASH}' % slug:
            d['url_dona'] = u['url'].replace(DOMINIO, '')
            d['status'] = 'publicado'
            mudou_donos += 1
    if mudou_donos:
        escritas.append((donos_rel, '%d url_dona' % mudou_donos))

    pub_rel = 'producao/registro/urls-publicadas.csv'
    if urls:
        escritas.append((pub_rel, '%d URL(s)' % len(urls)))

    # ------------------------------------------------------------------ relatório
    print()
    if not escritas:
        print('Nada a escrever: o repositório já bate com o patch.')
    for rel, nota in escritas:
        print('  %s  %s  (%s)' % ('escreveria' if DRY else 'escrito   ', rel, nota))
    if recusas:
        print('\n%d recusa(s) — esses itens não foram aplicados:' % len(recusas))
        for r in recusas:
            print('  - %s' % r)

    if DRY or not escritas:
        if DRY:
            print('\nDry-run: nada foi gravado. Rode sem --dry-run para aplicar.')
        return

    # ------------------------------------------------------------------ gravação
    alvos = {rel for rel, _ in escritas}
    if grade_rel in alvos:
        cols = list(linhas_novas[0].keys()) if linhas_novas else list(atual[0].keys())
        with open(caminho(grade_rel), 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(atual)
    for rel, texto in p['arquivos'].items():
        if rel in alvos:
            open(caminho(rel), 'w', encoding='utf-8').write(texto)
    if donos_rel in alvos:
        with open(caminho(donos_rel), 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(donos[0].keys()))
            w.writeheader()
            w.writerows(donos)
    if pub_rel in alvos:
        with open(caminho(pub_rel), 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['slug', 'url_real', 'data_publicacao'])
            for slug in sorted(urls):
                w.writerow([slug, urls[slug]['url'], urls[slug].get('data_publicacao', '')])

    print('\nAplicado. Regere o painel:  python3 scripts/gerar-painel.py')


if __name__ == '__main__':
    main()
