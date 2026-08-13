#!/usr/bin/env python3
"""Dump da ficha real dos produtos de uma categoria, do catalogo salvo.
USO: python3 scripts/ficha-por-categoria.py /feminino/maio/ [n_max]
Imprime nome, preco (min das variantes), 1a imagem CDN, atributos e trecho
da descricao — tudo do data/2026-08-12-nuvemshop-catalogo.json (coleta viva).
"""
import json, sys, re, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(BASE, 'data/2026-08-12-nuvemshop-catalogo.json')))
cats = d['categorias']; byid = {c['id']: c for c in cats}
def nm(c):
    n = c.get('handle') or c.get('name'); return n.get('pt') if isinstance(n, dict) else n
def path(c):
    parts = []; cur = c
    while cur: parts.append(nm(cur)); cur = byid.get(cur.get('parent'))
    return '/' + '/'.join(reversed(parts)) + '/'
pathid = {path(c): c['id'] for c in cats}
def L(x): return (x.get('pt') if isinstance(x, dict) else x) or ''
def preco(p):
    ps = [float(v['price']) for v in (p.get('variants') or []) if v.get('price')]
    return f'R$ {min(ps):.2f}'.replace('.', ',') if ps else '?'
def limpa(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()

alvo = sys.argv[1] if len(sys.argv) > 1 else '/feminino/maio/'
nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 8
cid = pathid.get(alvo)
if not cid:
    print('categoria nao encontrada. disponiveis com produto:')
    for p in sorted(set(path(byid[c['id']]) for c in cats)): print(' ', p)
    sys.exit()
n = 0
for p in d['produtos']:
    if not any(c['id'] == cid for c in (p.get('categories') or [])): continue
    n += 1
    if n > nmax: break
    img = (p.get('images') or [{}])[0].get('src', '')
    attrs = p.get('attributes') or []
    print('#', L(p.get('name')), '—', preco(p))
    print('  url:', p.get('canonical_url'))
    print('  img:', img)
    if attrs: print('  attrs:', attrs)
    desc = limpa(L(p.get('description')))
    if desc: print('  desc:', desc[:400])
    print()
total = sum(1 for p in d['produtos'] if any(c['id'] == cid for c in (p.get('categories') or [])))
print(f'({min(n, nmax)} de {total} produtos em {alvo})')
