#!/usr/bin/env python3
"""
Monta a grade da Onda 1 (20 artigos) puxando volume/kd/intent das fontes
medidas (matriz 2026-08-10 e universo esporte MEDIDO 2026-08-12), e trava a
anticanibalizacao anexando cada KW (primaria + secundarias) ao kw-donos.csv.

Nenhum numero e digitado a mao: cada termo e resolvido por busca nas fontes.
Termo nao encontrado sai com vol/kd vazios e marcado (ausente na fonte).
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carrega(p, kcol='keyword'):
    idx = {}
    for r in csv.DictReader(open(os.path.join(BASE, p), encoding='utf-8')):
        k = (r.get(kcol) or '').strip().lower()
        if k and k not in idx:
            idx[k] = r
    return idx

MATRIZ = carrega('data/2026-08-10-matriz-kws-classificada.csv')
MEDIDO = carrega('data/2026-08-12-universo-esporte-MEDIDO.csv', 'kw')

def busca(kw):
    k = kw.strip().lower()
    if k in MATRIZ:
        r = MATRIZ[k]; return r.get('volume', ''), r.get('kd', ''), r.get('intent', ''), 'matriz'
    if k in MEDIDO:
        r = MEDIDO[k]; return r.get('vol', ''), r.get('kd', ''), r.get('intent', ''), 'medido'
    return '', '', '', 'ausente'

# (slug, primaria, [secundarias], url_categoria_cta, territorio, hub, papel)
ARTIGOS = [
 ('maio-de-praia','maio de praia',['maio feminino','maio cavado','maio com bojo','maio para surfar'],'/feminino/maio/','maio','Comercial','comercial'),
 ('saida-de-praia-guia','saida de praia',['saída de praia longa','saída de praia feminina','saída de praia curta','saída de praia plus size','saída de praia branca'],'/feminino/saida-de-praia/','saida','Comercial','comercial'),
 ('vestido-de-praia','vestido de praia',['saia de praia','saia de praia longa','conjunto de praia feminino'],'/feminino/saida-de-praia/vestido-manga-longa/','saida','Comercial','comercial'),
 ('biquini-cortininha','biquini cortininha',['biquini preto','biquini tomara que caia','biquini com bojo','biquini hot pants'],'/feminino/biquini/','biquini','Comercial','comercial'),
 ('sunga-masculina','sunga masculina',['sunga','sunga boxer','sunga de praia'],'/masculino/sunga/','sunga','Comercial','comercial'),
 ('short-de-praia-masculino','short de praia masculino',['short de praia','bermuda surf','boardshort','short de banho masculino'],'/masculino/bermuda/','sunga','Comercial','comercial'),
 ('poncho-de-surf','poncho surf',['poncho de surf','poncho surf masculino','roupao de surf','poncho atoalhado'],'/masculino/poncho/','poncho','Comercial','comercial'),
 ('poncho-toalha-infantil','poncho toalha infantil',['toalha com capuz infantil','poncho atoalhado infantil','roupão de praia infantil'],'/infantil1/poncho2/','poncho','Comercial','comercial'),
 ('biquini-infantil','biquini infantil',['biquini juvenil'],'/feminino/biquini/','biquini','Comercial','comercial'),
 ('pilates','pilates',['benefícios do pilates','pilates emagrece','pilates solo','roupa de pilates'],'/feminino/ioga-fitness/','pilates','Bem-estar','autoridade-comercial'),
 ('yoga','yoga',['tipos de yoga','yoga para iniciantes','posições de yoga','hatha yoga','vinyasa yoga','ashtanga yoga','saudação ao sol'],'/feminino/ioga-fitness/','yoga','Bem-estar','autoridade-comercial'),
 ('natacao-guia','natação',['nado crawl','tipos de nado','como aprender a nadar','natação emagrece','maiô para natação'],'/feminino/maio/','natacao','Natacao','autoridade-comercial'),
 ('protetor-solar-facial','protetor solar facial',['protetor solar com cor','protetor solar corporal','protetor solar para pele oleosa','protetor solar fps 50','melhor protetor solar'],'/feminino/camiseta-uv1/','protetor solar','Sol e pele','autoridade-ponte'),
 ('protetor-solar-infantil','protetor solar infantil',[],'/infantil1/camiseta-uv2/','protecao infantil','Sol e pele','autoridade-ponte'),
 ('treino-funcional','treino funcional em casa',['circuito funcional','calistenia para iniciantes'],'/feminino/ioga-fitness/','treino funcional','Bem-estar','autoridade-comercial'),
 ('mindfulness','mindfulness',[],'/feminino/ioga-fitness/','yoga','Bem-estar','autoridade-ponte'),
 ('o-que-e-fps','o que é fps',[],'/feminino/camiseta-uv1/','protecao solar','Sol e pele','autoridade-ponte'),
 ('insolacao-sintomas','insolação sintomas',['sintomas de insolação','sintomas insolação leve','alergia ao sol'],'/feminino/camiseta-uv1/','pele e saude','Sol e pele','autoridade-ponte'),
 ('skimboard','skimboard',['longboard surf','aula de surf','escola de surf','surf trip'],'/masculino/lycra-surf/','surf','Surf','comercial'),
 ('bola-de-futevolei','bola de futevôlei',['quadra de futevôlei','aula de futevôlei','bola de vôlei de praia'],'/masculino/sunga/','futevolei','Praia esportiva','comercial'),
]

grade = os.path.join(BASE, 'producao/registro/grade-onda-1.csv')
with open(grade, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['slug','papel','hub','tipo_kw','keyword','vol','kd','intent','fonte','url_cta','territorio'])
    for slug, prim, secs, url, terr, hub, papel in ARTIGOS:
        v,k,i,fo = busca(prim)
        w.writerow([slug,papel,hub,'primaria',prim,v,k,i,fo,url,terr])
        for s in secs:
            v,k,i,fo = busca(s)
            w.writerow([slug,papel,hub,'secundaria',s,v,k,i,fo,url,terr])

# trava anticanibalizacao no kw-donos
donos_p = os.path.join(BASE, 'producao/registro/kw-donos.csv')
existentes = list(csv.DictReader(open(donos_p, encoding='utf-8')))
ja = set((r['keyword'].strip().lower()) for r in existentes)
novos = []
for slug, prim, secs, url, terr, hub, papel in ARTIGOS:
    for kw in [prim]+secs:
        if kw.strip().lower() in ja:
            continue
        ja.add(kw.strip().lower())
        v,k,i,fo = busca(kw)
        novos.append({'keyword':kw,'volume':v,'kd':k,
            'url_dona':f'/blog/posts/{slug}-{{HASH}}','artigo':f'content/{slug}.html',
            'territorio':'onda1','status':'grade'})
with open(donos_p, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['keyword','volume','kd','url_dona','artigo','territorio','status'])
    w.writeheader()
    for r in existentes: w.writerow(r)
    for r in novos: w.writerow(r)

print(f'grade-onda-1.csv: {len(ARTIGOS)} artigos')
print(f'kw-donos.csv: +{len(novos)} keywords travadas (agora {len(existentes)+len(novos)} total)')
# resumo
print('\nResumo por artigo:')
for slug, prim, secs, url, terr, hub, papel in ARTIGOS:
    v,k,i,fo = busca(prim)
    print(f'  {v:>7}  {prim:32s} -> {url}  ({papel})')
