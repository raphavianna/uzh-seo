#!/usr/bin/env python3
"""Grade da Onda 2 (50 pautas criativas, volume-first). Puxa vol/kd/intent das
fontes medidas; trava anticanibalização em kw-donos (idempotente p/ onda2)."""
import csv, os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def carrega(p,k='keyword'):
    idx={}
    for r in csv.DictReader(open(os.path.join(BASE,p),encoding='utf-8')):
        kk=(r.get(k) or '').strip().lower()
        if kk and kk not in idx: idx[kk]=r
    return idx
MAT=carrega('data/2026-08-10-matriz-kws-classificada.csv')
MED=carrega('data/2026-08-12-universo-esporte-MEDIDO.csv','kw')
def busca(kw):
    k=kw.strip().lower()
    if k in MAT: r=MAT[k]; return r.get('volume',''),r.get('kd',''),r.get('intent',''),'matriz'
    if k in MED: r=MED[k]; return r.get('vol',''),r.get('kd',''),r.get('intent',''),'medido'
    return '','','','PAA/n-d'

# (slug, formato, primaria, [secundarias], url_destino, hub)
A=[
# HUB A — Sol e pele
('protetor-solar-com-cor','CMP','protetor solar facial com cor',['protetor solar com cor'],'/feminino/camiseta-uv1/','sol e pele'),
('protetor-solar-spray','Q&A','protetor solar em spray',[],'/feminino/camiseta-uv1/','sol e pele'),
('protetor-solar-pele-oleosa','GUI','protetor solar para pele oleosa',['protetor solar facial pele oleosa','protetor solar facial para pele oleosa'],'/feminino/camiseta-uv1/','sol e pele'),
('melhor-protetor-solar-facial','LST','melhor protetor solar facial',['melhor protetor solar'],'/feminino/camiseta-uv1/','sol e pele'),
('protetor-solar-bastao','Q&A','protetor solar facial bastao',[],'/feminino/camiseta-uv1/','sol e pele'),
('quanto-tempo-dura-protetor-solar','Q&A','quanto tempo dura o protetor solar',[],'/feminino/camiseta-uv1/','sol e pele'),
('como-se-proteger-do-sol','GUI','como se proteger do sol na praia',[],'/feminino/camiseta-uv1/','sol e pele'),
# HUB B — Bem-estar
('hot-yoga','Q&A','hot yoga',[],'/feminino/ioga-fitness/','bem-estar'),
('tapete-de-yoga','GUI','tapete de yoga',[],'/feminino/ioga-fitness/','bem-estar'),
('yoga-ou-pilates','CMP','yoga ou pilates',[],'/feminino/ioga-fitness/','bem-estar'),
('pilates-para-iniciantes','HOW','pilates para iniciantes',[],'/feminino/ioga-fitness/','bem-estar'),
('quantas-vezes-pilates','Q&A','quantas vezes por semana fazer pilates',[],'/feminino/ioga-fitness/','bem-estar'),
('pilates-dor-nas-costas','Q&A','pilates para dor nas costas',[],'/feminino/ioga-fitness/','bem-estar'),
('yoga-para-ansiedade','Q&A','yoga para ansiedade',[],'/feminino/ioga-fitness/','bem-estar'),
('yoga-em-casa','HOW','yoga em casa para iniciantes',[],'/feminino/ioga-fitness/','bem-estar'),
# HUB C — Natação
('maio-natacao-feminino','GUI','maio natação feminino',['maio para natação','maio para hidroginastica'],'/feminino/maio/','natacao'),
('hidroterapia','Q&A','hidroterapia',[],'/feminino/maio/','natacao'),
('polo-aquatico','Q&A','polo aquático',[],'/feminino/maio/','natacao'),
('nado-peito','HOW','nado peito',[],'/feminino/maio/','natacao'),
('roupa-de-natacao','GUI','roupa de natação',[],'/feminino/maio/','natacao'),
('academia-de-natacao','Q&A','academia de natação',[],'/feminino/maio/','natacao'),
# HUB D — Sapatilha (CAP)
('sapatilha-aquatica','GUI','sapatilha aquatica',['sapatilha aquática','sapatilha nautica','sapatilha para praia','sapatilha aquatica feminina','sapatilhas para praia'],'/neoprene/','sapatilha'),
('sapatilha-beach-tennis','Q&A','sapatilha beach tennis',['sapatilha para beach tennis'],'/neoprene/','sapatilha'),
('sapatilha-de-neoprene','Q&A','sapatilha neoprene',['neoprene sapatilha','sapatilha em neoprene'],'/neoprene/','sapatilha'),
# HUB E — Canga & mergulho
('como-amarrar-canga','LST','canga de praia',[],'/feminino/saida-de-praia/','canga e mergulho'),
('roupa-de-mergulho','GUI','roupa de mergulho',['roupas de mergulho feminina'],'/neoprene/','canga e mergulho'),
# HUB F — Biquíni
('biquini-fio-dental','GUI','biquini fio dental',[],'/feminino/biquini/','biquini'),
('biquini-asa-delta','GUI','biquini asa delta',[],'/feminino/biquini/asa-delta/','biquini'),
('sunkini','Q&A','sunkini',['sunkini feminino'],'/feminino/biquini/sunkini/','biquini'),
('como-escolher-biquini','GUI','como escolher biquini para o corpo',[],'/feminino/biquini/','biquini'),
# HUB G — Maiô & saída
('maio-manga-longa','GUI','maio manga longa',['maiô manga longa'],'/feminino/maio/manga-longa/','maio e saida'),
('maio-ou-biquini','CMP','maio ou biquini',[],'/feminino/maio/','maio e saida'),
('como-usar-saida-de-praia','HOW','como usar saída de praia',[],'/feminino/saida-de-praia/','maio e saida'),
('saida-de-praia-croche','GUI','saída de praia de crochê',[],'/feminino/saida-de-praia/','maio e saida'),
# HUB H — Moda praia
('roupa-de-praia-feminina','GUI','roupa de praia feminina',[],'/feminino/','moda praia'),
('roupa-de-praia-masculina','GUI','roupa de praia masculina',[],'/masculino/','moda praia'),
('moda-praia-feminina','SAZ','moda praia feminina',['moda praia 2026'],'/feminino/','moda praia'),
('moda-praia-masculina','GUI','moda praia masculina',[],'/masculino/','moda praia'),
('roupa-de-surf','GUI','roupa de surf',['roupa de surf masculina','roupa de surfista'],'/masculino/lycra-surf/','moda praia'),
('loja-de-surf','Q&A','loja de surf',['surf shop','surf shop brasil'],'/','moda praia'),
# HUB I — Sunga/bermuda
('short-de-praia-feminino','GUI','short de praia feminino',[],'/feminino/','sunga e bermuda'),
('sunga-slip-ou-preta','Q&A','sunga slip',['sunga preta'],'/masculino/sunga/','sunga e bermuda'),
('bermuda-de-praia-masculina','GUI','bermuda de praia masculina',['boardshort masculino'],'/masculino/bermuda/','sunga e bermuda'),
('bermuda-natacao','GUI','bermuda natação',['bermuda natação masculina'],'/masculino/bermuda/','sunga e bermuda'),
# HUB J — Esporte novo & sazonal
('prancha-de-wakeboard','Q&A','prancha de wakeboard',[],'/masculino/lycra-surf/','esporte e verao'),
('look-de-praia','SAZ','look de praia',[],'/feminino/saida-de-praia/','esporte e verao'),
('surf-para-iniciantes','HOW','surf para iniciantes',['como comecar a surfar'],'/masculino/lycra-surf/','esporte e verao'),
('stand-up-paddle-iniciante','HOW','stand up paddle para iniciantes',[],'/masculino/lycra-surf/','esporte e verao'),
('o-que-levar-para-a-praia','LST','o que levar para a praia',[],'/feminino/saida-de-praia/','esporte e verao'),
('kitesurf-como-comecar','HOW','kitesurf como começar',['kitesurf o que é'],'/masculino/lycra-surf/','esporte e verao'),
]
assert len(A)==50, len(A)
grade=os.path.join(BASE,'producao/registro/grade-onda-2.csv')
with open(grade,'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['slug','formato','hub','tipo_kw','keyword','vol','kd','intent','fonte','url_destino'])
    for slug,fmt,prim,secs,url,hub in A:
        v,k,i,fo=busca(prim); w.writerow([slug,fmt,hub,'primaria',prim,v,k,i,fo,url])
        for s in secs:
            v,k,i,fo=busca(s); w.writerow([slug,fmt,hub,'secundaria',s,v,k,i,fo,url])
# trava kw-donos (idempotente onda2)
dp=os.path.join(BASE,'producao/registro/kw-donos.csv')
ex=[r for r in csv.DictReader(open(dp,encoding='utf-8')) if r.get('territorio')!='onda2']
ja=set(r['keyword'].strip().lower() for r in ex); novos=[]
for slug,fmt,prim,secs,url,hub in A:
    for kw in [prim]+secs:
        if kw.strip().lower() in ja: continue
        ja.add(kw.strip().lower()); v,k,i,fo=busca(kw)
        novos.append({'keyword':kw,'volume':v,'kd':k,'url_dona':f'/blog/posts/{slug}-{{HASH}}','artigo':f'content/{slug}.html','territorio':'onda2','status':'grade'})
with open(dp,'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['keyword','volume','kd','url_dona','artigo','territorio','status']); w.writeheader()
    for r in ex: w.writerow(r)
    for r in novos: w.writerow(r)
tv=sum(int(float(busca(p)[0] or 0)) for _,_,p,_,_,_ in A)
print(f'grade-onda-2.csv: 50 pautas | +{len(novos)} KWs travadas | volume primárias medido: {tv:,}/mês'.replace(',','.'))
