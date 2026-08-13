#!/usr/bin/env python3
"""Validador mecânico anti-IA + conformidade estrutural para os HTMLs de content/.
Uso:  python3 scripts/validar-anti-ia.py content/<slug>.html [...]
      python3 scripts/validar-anti-ia.py --todos        (valida todos os content/*.html não-editor)
Reporta por arquivo: ERROS (bloqueiam) e AVISOS (revisar). Saída não-zero se houver ERRO."""
import re, sys, os, glob, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tics de IA (no corpo publicável). Cada um: (regex, rótulo). Case-insensitive.
TICS = [
    (r'\bneste guia\b', 'frase-meta "neste guia"'),
    (r'\beste guia (mostra|conta|explica|traz|apresenta|reúne)', 'frase-meta "este guia ..."'),
    (r'\bvale (ressaltar|lembrar|destacar)\b', 'joiner "vale ressaltar/lembrar"'),
    (r'\bé importante (notar|lembrar|ressaltar|destacar)\b', 'joiner "é importante notar"'),
    (r'\bem resumo\b', 'joiner "em resumo"'),
    (r'\bpor fim\b', 'joiner "por fim"'),
    (r'\bvamos? (explorar|mergulhar|desvendar)\b', 'joiner "vamos explorar/mergulhar"'),
    (r'não é (apenas |só )?[^.,;]{2,40}?,? (e sim|mas sim|mas) ', 'paralelismo negativo "não é X e sim Y"'),
    (r'\bde verdade\b', 'bordão "de verdade"'),
    (r'\bde propósito\b', 'bordão "de propósito"'),
    (r'\bcom folga\b', 'bordão "com folga"'),
    (r'\bverdadeiro aliado\b', 'adjetivo vazio "verdadeiro aliado"'),
    (r'\bgrande (trunfo|aliado)\b', 'adjetivo vazio "grande trunfo/aliado"'),
    (r'\bsolução ideal\b', 'adjetivo vazio "solução ideal"'),
    (r'\ba forma mais eficiente\b', 'adjetivo vazio "a forma mais eficiente"'),
    (r'\bespetáculo de\b', 'adjetivo vazio "espetáculo de"'),
    (r'\bponto de partida\b', 'clichê "ponto de partida"'),
    (r'\bquando o assunto é\b', 'joiner "quando o assunto é"'),
    (r'\bnada mais é (do )?que\b', 'joiner "nada mais é que"'),
    (r'\bseja (bem-vindo|bem vinda)\b', 'clichê "seja bem-vindo"'),
    (r'\bno mundo (do|da|dos|das)\b', 'clichê "no mundo do/da"'),
]

def corpo_publicavel(txt):
    """Remove head, scripts, comentários e tags — devolve só o texto que o leitor vê."""
    # tira comentários de produção
    s = re.sub(r'<!--.*?-->', ' ', txt, flags=re.S)
    # tira head inteiro
    s = re.sub(r'<head\b.*?</head>', ' ', s, flags=re.S|re.I)
    # tira scripts (JSON-LD) e styles
    s = re.sub(r'<script\b.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style\b.*?</style>', ' ', s, flags=re.S|re.I)
    return s

def texto_visivel(corpo):
    s = re.sub(r'<[^>]+>', ' ', corpo)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s)

def valida(path):
    erros, avisos = [], []
    txt = open(path, encoding='utf-8').read()

    # title
    m = re.search(r'<title>(.*?)</title>', txt, re.S|re.I)
    if not m: erros.append('sem <title>')
    elif len(m.group(1).strip()) > 60: erros.append(f'<title> {len(m.group(1).strip())} chars (>60)')
    # meta description
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', txt, re.S|re.I)
    if not m: erros.append('sem meta description')
    elif len(m.group(1).strip()) > 155: erros.append(f'meta description {len(m.group(1).strip())} chars (>155)')
    # JSON-LD
    for tipo in ('BlogPosting', 'BreadcrumbList', 'FAQPage'):
        if f'"{tipo}"' not in txt and f"'{tipo}'" not in txt:
            erros.append(f'sem JSON-LD {tipo}')
    # h1 único
    n_h1 = len(re.findall(r'<h1\b', txt, re.I))
    if n_h1 != 1: erros.append(f'{n_h1} <h1> (deve ser 1)')

    corpo = corpo_publicavel(txt)
    vis = texto_visivel(corpo)  # só o texto que o leitor vê (sem tags, sem atributos)

    # travessão no texto visível (atributos como og:description/@id ficam dentro de <...> e não contam)
    if '—' in vis: erros.append(f'travessão (—) no texto visível ({vis.count("—")}x)')
    # {HASH} no texto visível (canonical/og:url/@id ficam em atributos e não contam)
    if '{HASH}' in vis: erros.append('{HASH} no texto visível (só em canonical/og:url/@id)')
    # preço
    for pat, rot in [(r'R\$', 'R$'), (r'\breais\b', '"reais"'), (r'\bpreço\b', '"preço"')]:
        if re.search(pat, vis, re.I):
            avisos.append(f'possível preço/{rot} no corpo — conferir')
            break
    # tics de IA
    for rgx, rot in TICS:
        if re.search(rgx, vis, re.I):
            avisos.append(f'tic IA: {rot}')

    # links de produto/categoria destacados: todo <a href="...usezerohora ou /...> deve ter <strong><u>
    for a in re.finditer(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', corpo, re.S|re.I):
        href, inner = a.group(1), a.group(2)
        if href.startswith('#') or 'mailto:' in href: continue
        eh_interno = ('usezerohora.com.br' in href) or href.startswith('/')
        # ignora link para post-irmão (blog/posts) — não deve existir, mas se existir é outro erro
        if '/blog/posts/' in href:
            erros.append(f'link para post-irmão no corpo: {href[:50]}')
            continue
        if eh_interno:
            if not (re.search(r'<strong>', inner, re.I) and re.search(r'<u>', inner, re.I)):
                avisos.append(f'link interno sem <strong><u>: {href[:45]}')

    # FAQ: h3 do corpo x name do FAQPage
    faq_names = re.findall(r'"@type"\s*:\s*"Question"\s*,\s*"name"\s*:\s*"([^"]+)"', txt)
    h3s = [texto_visivel(x).strip() for x in re.findall(r'<h3\b[^>]*>(.*?)</h3>', corpo, re.S|re.I)]
    if faq_names:
        faq_norm = set(html.unescape(x).strip().lower() for x in faq_names)
        h3_norm = set(x.lower() for x in h3s)
        faltando = faq_norm - h3_norm
        if faltando:
            avisos.append(f'{len(faltando)} pergunta(s) do FAQPage sem <h3> idêntico')

    # aberturas repetidas de parágrafo (3+ <p> seguidos abrindo com A/O/É/Os/As)
    ps = re.findall(r'<p\b[^>]*>\s*([A-ZÁÉÍÓ])', corpo)
    run = 1
    for i in range(1, len(ps)):
        if ps[i] == ps[i-1] and ps[i] in 'AOÉ':
            run += 1
            if run >= 3: avisos.append(f'3+ parágrafos abrindo com "{ps[i]}"'); break
        else: run = 1

    return erros, avisos

def main():
    args = sys.argv[1:]
    if not args: print('uso: validar-anti-ia.py <arquivo|--todos>'); sys.exit(2)
    if args == ['--todos']:
        args = sorted(f for f in glob.glob(os.path.join(BASE,'content','*.html')) if '-editor' not in f)
    tot_e = 0
    for path in args:
        if not os.path.isabs(path): path = os.path.join(BASE, path)
        slug = os.path.basename(path).replace('.html','')
        e, a = valida(path)
        tot_e += len(e)
        if not e and not a:
            print(f'✓ {slug}: limpo')
        else:
            print(f'{"✗" if e else "△"} {slug}:')
            for x in e: print(f'    ERRO  {x}')
            for x in a: print(f'    aviso {x}')
    print(f'\n== {len(args)} arquivo(s), {tot_e} erro(s) bloqueante(s) ==')
    sys.exit(1 if tot_e else 0)

if __name__ == '__main__':
    main()
