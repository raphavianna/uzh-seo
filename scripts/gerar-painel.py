#!/usr/bin/env python3
"""
Gera o painel gerencial de conteúdos a partir do estado real do repositório.

O painel é uma página estática: ele não lê o repositório em tempo de execução,
então os dados vão embutidos no HTML. Toda vez que a grade, um texto ou o
registro de donos mudar, rode este script de novo.

  python3 scripts/gerar-painel.py

Entradas
  producao/registro/calendario-AAAA-MM.csv   a grade (a mais recente pelo nome)
  producao/registro/kw-donos.csv             registro de dono de keyword
  content/<slug>.html e <slug>-editor.html   os textos
  pautas/AAAA-MM-DD-<slug>.md                a pauta de cada artigo

Saída
  producao/painel/painel-conteudos.html
"""
import csv, glob, json, os, re, sys, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(BASE, 'producao/painel/painel-conteudos.html')
MODELO = os.path.join(BASE, 'producao/painel/template.html')

TERRITORIOS = {
    'T1': 'T1 — Lycra, camiseta UV e rash guard',
    'T2': 'T2 — Saída de praia, resort e vestidos',
    'T3': 'T3 — Biquíni e top',
}
MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

faltando = []


def ler(caminho):
    """Devolve o texto, ou None se o arquivo não existir. Ausência é dado."""
    p = os.path.join(BASE, caminho)
    if not os.path.exists(p):
        faltando.append(caminho)
        return None
    return open(p, encoding='utf-8').read()


def achar_pauta(slug):
    achados = sorted(glob.glob(os.path.join(BASE, 'pautas', '*-%s*.md' % slug)))
    return os.path.relpath(achados[0], BASE) if achados else None


def motivo_do_bloqueio(slug):
    """Lê o motivo na pauta de bloqueio: o primeiro parágrafo de prosa da
    primeira seção `##`. Sem pauta, devolve None, e o painel mostra 'motivo
    não registrado' em vez de inventar um."""
    for p in sorted(glob.glob(os.path.join(BASE, 'pautas', '*%s*BLOQUEIO*.md' % slug))):
        txt = open(p, encoding='utf-8').read()
        corpo = re.split(r'^##\s+', txt, maxsplit=1, flags=re.M)
        alvo = corpo[1] if len(corpo) > 1 else txt
        alvo = alvo.split('\n', 1)[1] if len(corpo) > 1 else alvo
        for bloco in alvo.split('\n\n'):
            bloco = bloco.strip()
            if not bloco or bloco.startswith(('#', '-', '|', '*', '>')):
                continue
            limpo = re.sub(r'\s+', ' ', bloco).replace('`', '')
            return limpo[:400]
    return None


def main():
    grades = sorted(glob.glob(os.path.join(BASE, 'producao/registro/calendario-*.csv')))
    if not grades:
        sys.exit('Nenhuma grade em producao/registro/calendario-*.csv')
    grade = grades[-1]
    nome_grade = os.path.basename(grade)
    ano, mes = re.search(r'calendario-(\d{4})-(\d{2})', nome_grade).groups()

    with open(grade, encoding='utf-8') as f:
        colunas = next(csv.reader(f))
    linhas = list(csv.DictReader(open(grade, encoding='utf-8')))

    donos = [d for d in csv.DictReader(open(os.path.join(BASE, 'producao/registro/kw-donos.csv'), encoding='utf-8'))]

    artigos = []
    usados = set()
    for r in linhas:
        slug = r['slug']
        completo = ler('content/%s.html' % slug)
        editor = ler('content/%s-editor.html' % slug)
        if completo is not None:
            usados.add('content/%s.html' % slug)
        if editor is not None:
            usados.add('content/%s-editor.html' % slug)
        a = {
            'id': r['id'], 'territorio': r['territorio'],
            'data_producao': r['data_producao'], 'data_publicacao': r['data_publicacao'],
            'kw_primaria': r['kw_primaria'], 'volume': r['volume'], 'kd': r['kd'],
            'intencao': r['intencao'], 'slug': slug,
            'url_final': r['url_final'], 'status': r['status'], 'aprovado_em': r['aprovado_em'],
            'arquivos': {'completo': completo, 'editor': editor},
            'pauta': achar_pauta(slug),
            'bruto': [r[c] for c in colunas],
        }
        if r['status'] == 'bloqueado':
            a['motivo_bloqueio'] = motivo_do_bloqueio(slug)
        artigos.append(a)

    # Conteúdo que existe em content/ sem linha na grade. Não vira card: não há
    # linha para gravar status. Aparece na faixa de leitura, declarado.
    orfaos = []
    for p in sorted(glob.glob(os.path.join(BASE, 'content/*.html'))):
        rel = os.path.relpath(p, BASE)
        if rel in usados:
            continue
        base = os.path.basename(p).replace('-editor.html', '.html')
        if 'content/' + base in [o['arquivo'] for o in orfaos]:
            continue
        kws = [d for d in donos if d['artigo'] == 'content/' + base]
        pub = [d for d in kws if d['url_dona'].startswith('/blog/posts/') and '{HASH}' not in d['url_dona']]
        if pub:
            nota = 'Publicado em %s. %d keyword(s) no registro. Sem linha na grade de %s/%s: o painel não tem onde gravar status.' % (
                pub[0]['url_dona'], len(kws), mes, ano)
        elif kws:
            nota = '%d keyword(s) no registro, com URL dona %s. Sem linha na grade de %s/%s.' % (
                len(kws), kws[0]['url_dona'], mes, ano)
        else:
            nota = 'Arquivo em content/ sem linha na grade e sem keyword no registro.'
        orfaos.append({'slug': base[:-5], 'arquivo': 'content/' + base, 'nota': nota})

    dados = {
        'hoje': datetime.date.today().isoformat(),
        'mes': '%s de %s' % (MESES[int(mes) - 1], ano),
        'nome_grade': nome_grade,
        'colunas': colunas,
        'territorios': TERRITORIOS,
        'artigos': artigos,
        'donos': donos,
        'orfaos': orfaos,
    }

    modelo = open(MODELO, encoding='utf-8').read()
    if '/*__DADOS__*/' not in modelo:
        sys.exit('O template perdeu o marcador /*__DADOS__*/.')
    blob = json.dumps(dados, ensure_ascii=False).replace('</script', '<\\/script')
    html = modelo.replace('/*__DADOS__*/', blob)
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8').write(html)

    n_arq = sum(1 for a in artigos for v in a['arquivos'].values() if v is not None)
    print('%s  (%.0f KB)' % (os.path.relpath(SAIDA, BASE), len(html) / 1024))
    print('  %d artigos na grade, %d arquivos de conteúdo, %d keywords no registro' % (
        len(artigos), n_arq, len(donos)))
    print('  %d conteúdo(s) fora da grade: %s' % (
        len(orfaos), ', '.join(o['slug'] for o in orfaos) or '—'))
    if faltando:
        print('  %d arquivo(s) esperado(s) e não encontrado(s):' % len(faltando))
        for f in faltando:
            print('    %s' % f)


if __name__ == '__main__':
    main()
