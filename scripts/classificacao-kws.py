import csv, re, unicodedata, collections, json

SRC = 'data/2026-08-09-semrush-bulk-kws-br.csv'
rows = list(csv.DictReader(open(SRC, encoding='utf-8')))

def num(r, c):
    try: return float((r.get(c) or '').strip())
    except: return None

def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower())
                   if unicodedata.category(c) != 'Mn')

# primeira regra que casa vence; ordem = prioridade de territorio
REGRAS = [
    ('Marca Use Zero Hora',        r'zero hora|usezerohora'),
    ('Informacional / GEO',        r'^(o que|para que|como|qual|quais|quando|onde|quanto|diferenca|melhores|temperatura|tabela)\b|vale a pena|dura quanto|funciona$'),
    ('Natacao e mergulho (adj.)',  r'natacao|nadador|nadar|mergulho|traje |hidroginastica'),
    ('Calcado aquatico',           r'sapatilha|sapato|tenis|meia aquatica|bota aquatica|botinha|bota de neoprene'),
    ('Maio',                       r'\bmaio\b|\bmaios\b|\bmaio |body de surf|body surf'),
    ('Biquini e top',              r'biquini|sunkini|subikini|\btop\b|calcinha|sutia'),
    ('Poncho, toalha e roupao',    r'poncho|toalha|roupao|capa de banho'),
    ('Neoprene',                   r'neoprene|wetsuit|long john|roupa de borracha|roupa termica|colete|luva de|capuz de'),
    ('Lycra, camiseta UV e rash',  r'lycra|rash guard|camiseta|camisa|blusa|protecao solar|protecao uv|uv50|uv 50|anti uv|segunda pele'),
    ('Sunga, bermuda e short',     r'sunga|bermuda|boardshort|board short|\bshort\b|calcao'),
    ('Saida de praia e resort',    r'saida de praia|saia|vestido|kaftan|tunica|robe|resort|macacao|macaquinho|cropped|\bbody\b|conjunto'),
    ('Canga e acessorios',         r'canga|pareo|acessorio|artigos|equipamento|material'),
    ('Moda praia e surfwear',      r'moda praia|surfwear|surf shop|loja de|roupa |roupas |beachwear|marca de surf|marcas de|look de praia|surf|praia'),
]

def cluster(kw):
    k = sem_acento(kw)
    for nome, pat in REGRAS:
        if re.search(pat, k): return nome
    return 'Nao classificado'

# CTR alcancavel por faixa de KD, usando a curva propria do site (2026-08-09)
def ctr(kd):
    if kd is None: return None
    if kd < 15: return 0.049   # top 3 alcancavel
    if kd < 30: return 0.029   # top 10 alcancavel
    if kd < 50: return 0.010   # pagina 1 baixa
    return 0.003               # fora de alcance na janela de 12 meses

# proximidade da conversao, por intencao declarada pelo Semrush
PESO = {'Transactional': 1.0, 'Informational, Transactional': 0.9, 'Commercial': 0.8,
        'Informational, Commercial': 0.5, 'Informational': 0.25, '': 0.4}
def peso(i): return PESO.get((i or '').strip(), 0.4)

out = []
for r in rows:
    kw = r['Keyword'].strip()
    v, kd = num(r, 'Volume'), num(r, 'Keyword Difficulty')
    c = ctr(kd)
    sessoes = round(v * c, 1) if (v is not None and c is not None) else None
    score = round(sessoes * peso(r.get('Intent')), 1) if sessoes is not None else None
    feats = [f.strip() for f in (r.get('SERP Features') or '').split(',') if f.strip()]
    out.append({'keyword': kw, 'norm': sem_acento(kw), 'cluster': cluster(kw),
                'volume': v, 'kd': kd, 'cpc': num(r, 'CPC (USD)'),
                'intent': (r.get('Intent') or '').strip(),
                'paa': 'People Also Ask' in feats, 'aio': 'AI Overview' in feats,
                'fs': 'Featured Snippet' in feats, 'sessoes': sessoes, 'score': score})

# variante grafica (mesma KW sem acento) compartilha SERP: maior volume manda
grp = collections.defaultdict(list)
for o in out: grp[o['norm']].append(o)
for g in grp.values():
    if len(g) > 1:
        mx = max(g, key=lambda x: (x['volume'] or -1))
        for o in g:
            if o is not mx: o['variante_de'] = mx['keyword']

with open('data/2026-08-10-matriz-kws-classificada.csv', 'w', newline='', encoding='utf-8') as f:
    campos = ['keyword','cluster','volume','kd','cpc','intent','paa','aio','fs','sessoes','score','variante_de','norm']
    w = csv.DictWriter(f, fieldnames=campos); w.writeheader()
    for o in sorted(out, key=lambda x: (x['cluster'], -(x['score'] or -1))):
        w.writerow({k: o.get(k, '') for k in campos})

print(f"{'CLUSTER':<30}{'KWs':>5}{'Vol unico':>11}{'Sessoes':>9}{'Score':>8}{'PAA':>5}{'AIO':>5}")
tot = collections.defaultdict(lambda: {'n':0,'v':0,'s':0.0,'sc':0.0,'paa':0,'aio':0})
for o in out:
    t = tot[o['cluster']]; t['n'] += 1
    if not o.get('variante_de') and o['volume']: t['v'] += int(o['volume'])
    t['s'] += o['sessoes'] or 0; t['sc'] += o['score'] or 0
    t['paa'] += o['paa']; t['aio'] += o['aio']
for c, t in sorted(tot.items(), key=lambda x: -x[1]['sc']):
    print(f"{c:<30}{t['n']:>5}{t['v']:>11,}{t['s']:>9.0f}{t['sc']:>8.0f}{t['paa']:>5}{t['aio']:>5}")
print(f"\nTOTAL sessoes/mes estimadas: {sum(t['s'] for t in tot.values()):.0f}")
print(f"TOTAL score: {sum(t['sc'] for t in tot.values()):.0f}")
print(f"Nao classificado: {tot['Nao classificado']['n']}")

json.dump(out, open('/tmp/claude-0/-home-user/bab88b5f-03cd-5e81-b1b8-5ba8c1b28f53/scratchpad/out.json','w'), ensure_ascii=False)
