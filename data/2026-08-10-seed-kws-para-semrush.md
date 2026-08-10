# Lista-semente de keywords para coleta no Semrush

- **Data**: 2026-08-10
- **Para**: coleta manual no Semrush pelo time (o saldo de API units da sessão
  zerou em 2026-08-09 com `ERROR 132`)
- **Base de dados a usar**: **BR**
- **Total**: 550 keywords em 9 lotes de até 100
- **Fase do pipeline**: F2 (consolidação de keywords)

## Como a lista foi montada

1. **Base já mapeada**: as 30 keywords que o domínio ranqueia
   (`reports/2026-08-09-semrush-baseline-dominio.md`) e as 20 do cluster lycra
   (`reports/2026-08-08-semrush-kws-lycra-surf.md`).
2. **Categorias reais do site**, deduzidas das URLs que o Semrush devolveu:
   `/feminino/maio/`, `/feminino/biquini/sunkini/`, `/feminino/poncho1/`,
   `/masculino/poncho/`, `/masculino/lycra-surf/`, além de produtos de saída de
   praia e vestido resort.
3. **Linha neoprene**, dos três produtos registrados no repositório irmão
   `search-mkt`: camiseta Cabo Frio, bermuda Joaquina e sapatilha esportiva.
4. **Expansão por variação real de digitação**: com e sem acento, singular e
   plural, masculino/feminino/infantil, modificador comercial (comprar, preço,
   melhor) e modificador de atributo (manga longa, com bojo, proteção uv).
5. **Camada informacional/GEO**: perguntas na forma em que a pessoa digita, para
   alimentar FAQ e citação em motor de resposta.

**Premissa declarada**: o catálogo real não pôde ser lido (acesso a
usezerohora.com.br bloqueado pela política de egress, e sem conector de
Nuvemshop ou BaseLinker nesta sessão). Quando o CSV do catálogo chegar, os
SKUs que não estiverem cobertos por nenhum lote abaixo geram um lote 10.

## Como rodar

**No Semrush, para volume, KD e intenção** — *Keyword Overview → Bulk
Analysis*. Cole um lote por vez (o limite é 100 keywords por consulta). Base
**BR**. Exporte CSV.

**Colunas a trazer no export** (nesta ordem, para o arquivo entrar direto na
matriz):

```
Keyword | Volume | Keyword Difficulty | CPC | Competitive Density | Intent | SERP Features | Trend | Results
```

**Para descobrir cauda longa que esta lista não tem** — *Keyword Magic Tool*,
uma semente por vez, filtro de volume mínimo 10:

```
poncho surf
lycra surf
maio surf
biquini surf
neoprene surf
saida de praia
moda praia
surfwear
```

**Para o gap contra concorrente** — *Keyword Gap*, colando
`usezerohora.com.br` contra estes cinco domínios (não rode como keyword, rode
como domínio):

```
onlysurf.com.br
wetdreams.com.br
soulfins.com.br
lordsea.com.br
boardlife.com.br
```

Only Surf ranqueia para 1.809 keywords contra 146 nossas. O gap é o backlog.

**No Google Ads Keyword Planner** — use *Descobrir novas palavras-chave →
Começar com um site*, apontando para as URLs de categoria
(`/feminino/maio/`, `/masculino/lycra-surf/`, `/masculino/poncho/`) e para as
três URLs de produto de neoprene. Exporte volume médio mensal e faixa de lance.
O Keyword Planner vence o Semrush para volume e CPC; o Semrush vence para KD,
intenção e SERP feature.

## Onde salvar o retorno

Arquivos exportados em `data/`, com nome datado e origem explícita:

```
data/2026-08-XX-semrush-bulk-lote-1-maio.csv
data/2026-08-XX-keyword-planner-categorias.csv
data/2026-08-XX-semrush-keyword-gap-onlysurf.csv
```

---

# Lote 1 — Maiô e body de surf (75)

Cluster do ativo número um do site. `/feminino/maio/` já entrega 42% do tráfego
orgânico ranqueando da posição 2 à 14 aqui.

```
maio para surf
maiô para surf
maio para surfar
maiô para surfar
maio surf
maiô surf
maio surf feminino
maiô surf feminino
maio de surf
maiô de surf
maio de surf feminino
maiô de surf feminino
maio surfista
maiô surfista
maio surfista feminino
maiô de surfista feminino
maio gola alta
maiô gola alta
maio manga longa
maiô manga longa
maio manga longa surf
maio manga longa proteção uv
maio esportivo
maio esportivo feminino
maio esportivo natação
maio para natação
maio natação feminino
maio fitness
maio cavado
maio frente única
maio com bojo
maio com bojo removível
maio preto surf
maio com ziper
maio com ziper frontal
maio ziper frontal surf
maio de praia
maio feminino
maio feminino esportivo
maio infantil surf
maio de surf infantil
maio com proteção solar
maio com proteção uv
maio uv50
maio proteção uv50
maio para academia
maio para hidroginastica
comprar maio de surf
maio de surf preço
maio de surf barato
melhor maio para surfar
maio ou biquini para surfar
maio que não sai no surf
maio que não marca
maio surf manga curta
maio de surf nacional
maio surf preto
maio surf colorido
maio surf estampado
body de surf feminino
body surf feminino
macaquinho de surf
macaquinho para surfar
maio surf com manga
maio de surfe
roupa de surf feminina maio
maio para stand up paddle
maio para sup
maio para kitesurf
maio de surf com forro
maio surf alta compressão
maio de competição surf
maio para praia esportivo
maio de banho feminino
maio de surf tamanho grande
```

# Lote 2 — Biquíni, sunkini e top (60)

`sunkini` tem 1.600 buscas/mês e o site está na posição 24. Confirmar com o
time se o termo é genérico de categoria ou nome de outra marca antes de
priorizar.

```
sunkini
subikini
sunkini feminino
sunkini biquini
biquini sunkini
biquini para surfar
biquíni para surfar
biquini de surf
biquíni de surf
biquini surf feminino
biquini esportivo
biquíni esportivo
biquini esportivo feminino
biquini que não sai
biquini que não sai no mar
biquini para praia esportivo
biquini de amarrar
biquini hot pants
biquini asa delta
biquini cortininha
biquini com bojo
biquini sem bojo
biquini tomara que caia
biquini frente única
biquini de crochê
biquini estampado
biquini preto
top de surf
top para surfar
top de surf feminino
top esportivo praia
top esportivo para surf
top com manga longa surf
top cropped praia
top de biquini esportivo
sutiã de surf
calcinha de biquini alta
calcinha de biquini asa delta
conjunto de biquini
conjunto praia feminino
conjunto de praia feminino
moda praia feminina
moda praia esportiva
moda praia surf
moda praia brasileira
moda praia 2026
comprar biquini online
biquini para nadar
biquini para vôlei de praia
biquini para stand up paddle
biquini com proteção uv
biquini uv
biquini para surf infantil
biquini infantil
biquini juvenil
biquini fio dental
biquini de lycra
biquini fitness
biquini para esportes aquáticos
top de lycra feminino
```

# Lote 3 — Poncho, toalha e roupão (65)

Cluster dividido hoje entre `/masculino/poncho/` e `/feminino/poncho1/`.
"poncho toalha infantil" tem 590 buscas/mês e nenhuma categoria de destino.

```
poncho de surf
poncho surf
poncho toalha
toalha poncho
toalha poncho surf
poncho toalha surf
poncho atoalhado
roupão de surf
roupao de surf
roupão toalha surf
poncho de praia
poncho praia
poncho toalha praia
poncho para trocar de roupa
poncho de trocar roupa
poncho surf masculino
poncho surf feminino
poncho surf infantil
poncho toalha infantil
poncho atoalhado infantil
poncho infantil praia
poncho toalha adulto
poncho natação
poncho para natação
poncho de natação infantil
toalha de surf
toalha para surf
toalha de praia com capuz
toalha com capuz adulto
toalha com capuz infantil
poncho microfibra
poncho microfibra praia
poncho de algodão praia
poncho felpudo praia
poncho atoalhado masculino
poncho atoalhado feminino
poncho de surf preço
comprar poncho de surf
poncho de surf barato
melhor poncho de surf
poncho de surf tamanho
poncho de surf como usar
roupão de praia
roupão de praia infantil
roupão toalha praia
roupão com capuz praia
capa de banho praia
toalha poncho para bebê
poncho de banho infantil
poncho para trocar roupa na praia
poncho surf nacional
poncho de surf feminino
poncho de surf masculino
poncho de surf infantil
poncho para mergulho
poncho para kitesurf
poncho para stand up paddle
poncho toalha esportivo
toalha poncho academia
toalha poncho piscina
poncho para piscina
poncho toalha com bolso
poncho toalha secagem rápida
poncho de surf grande
poncho de surf estampado
```

# Lote 4 — Lycra, camiseta UV e rash guard (90)

Cluster com números já coletados em
`reports/2026-08-08-semrush-kws-lycra-surf.md`. Rodar de novo só para pegar as
variações novas e atualizar KD.

```
lycra surf
lycra de surf
lycra para surf
lycra surf masculina
lycra surf feminina
lycra surf infantil
surf lycra
surf lycras
camiseta lycra surf
camisetas lycra surf
camiseta lycra surf manga longa
camiseta lycra masculina
camiseta lycra feminina
camiseta de lycra
camisa de lycra surf
camisa de lycra
camiseta surf
camiseta surf masculina
camiseta surf feminina
camiseta para surf
camiseta para surf feminina
camisetas femininas surf
camiseta surfista
camisa de surfista masculina
camiseta manga longa surf
camisa manga longa praia
camiseta manga longa praia
camisa manga longa proteção solar
camiseta uv
camiseta uv masculina
camiseta uv feminina
camiseta uv infantil
camisa uv
camisa uv surf
camiseta uv surf
camiseta uv50
camisa uv50
camiseta uv 50 masculina
camiseta com proteção uv
camisa com proteção solar
camiseta proteção solar
blusa uv
blusa uv feminina
blusa com proteção uv
blusa de proteção solar feminina
rash guard
rash guard feminino
rash guard masculino
rash guard infantil
lycra uv infantil
lycra infantil praia
lycra manga longa infantil
camiseta uv para criança
roupa com proteção solar
roupa com proteção uv
roupa uv50
camiseta de praia masculina
camiseta de praia feminina
camiseta para nadar
camiseta para piscina
camiseta para natação
camiseta para stand up paddle
camiseta para kitesurf
lycra para natação
lycra de praia
lycra manga curta surf
lycra manga longa surf
camiseta lycra surf proteção solar
comprar lycra de surf
lycra de surf preço
melhor lycra para surf
lycra surf tamanho
camiseta térmica surf
camiseta segunda pele surf
camiseta uv com ziper
camiseta uv gola alta
camiseta uv slim
camiseta uv folgada
camisa uv pesca
camiseta surf com capuz
camiseta surfwear
camiseta de surf estampada
camiseta de surf colorida
camiseta uv feminina manga longa
camiseta uv masculina manga longa
camisa de proteção solar masculina
camisa de proteção solar feminina
camiseta anti uv
roupa anti uv praia
proteção uv roupa surf
```

# Lote 5 — Neoprene (55)

Linha da campanha inaugural do repositório `search-mkt`. Rodar este lote
alinha orgânico e pago no mesmo cluster.

```
roupa de neoprene
roupa de neoprene surf
roupa de neoprene feminina
roupa de neoprene masculina
roupa de neoprene infantil
camiseta de neoprene
camiseta neoprene surf
camisa de neoprene
bermuda de neoprene
bermuda neoprene surf
short de neoprene
calça de neoprene
sapatilha de neoprene
sapatilha neoprene surf
bota de neoprene
botinha de neoprene surf
luva de neoprene surf
capuz de neoprene surf
long john neoprene
long john surf
macaquinho de neoprene
roupa de borracha surf
roupa térmica surf
wetsuit
wetsuit feminino
wetsuit masculino
wetsuit infantil
neoprene 3mm
neoprene 2mm
neoprene surf 3 2
roupa de neoprene 3mm
comprar roupa de neoprene
roupa de neoprene preço
melhor roupa de neoprene
como escolher roupa de neoprene
roupa de neoprene para água fria
roupa de neoprene para mergulho
roupa de neoprene natação
neoprene para stand up paddle
neoprene para kitesurf
neoprene para pesca
espessura de neoprene surf
tamanho de roupa de neoprene
como lavar roupa de neoprene
como vestir roupa de neoprene
neoprene nacional
roupa de neoprene brasileira
sapatilha para surf
sapatilha para pedra surf
sapatilha esportiva neoprene
sapatilha antiderrapante praia
sapatilha para esportes aquáticos
neoprene inverno surf
top de neoprene feminino
colete de neoprene
```

# Lote 6 — Saída de praia e resort (55)

O site já ranqueia "saida de praia transparente" na posição 6 e "vestido praia
longo" na 29, ambos por URL de produto. Falta categoria dona.

```
saída de praia
saida de praia
saída de praia feminina
saida de praia transparente
saída de praia longa
saída de praia curta
saida de praia bege
saída de praia preta
saída de praia branca
saída de praia de crochê
saída de praia de tule
saia transparente tule
mini saia transparente
saia de praia
saia de praia curta
saia de praia longa
saia drapeada praia
vestido de praia
vestido praia longo
vestido longo saída de praia
vestido de praia curto
vestido resort
moda resort feminina
kaftan de praia
canga de praia
canga estampada
canga de praia grande
pareô de praia
short de praia feminino
short saia praia
macaquinho praia
macacão de praia
body de praia
cropped de praia
camisa de praia feminina
conjunto saída de praia
saída de praia com manga
saída de praia com proteção uv
saída de praia esportiva
saída de praia para surf
comprar saída de praia
saída de praia preço
saída de praia 2026
saída de praia plus size
saída de praia infantil
robe de praia
túnica de praia
saída de praia de linho
saída de praia com franja
saída de praia de renda
look de praia feminino
roupa de praia feminina
roupa para praia
o que vestir na praia
saída de praia para gestante
```

# Lote 7 — Masculino: sunga, bermuda e boardshort (50)

```
sunga
sunga masculina
sunga de praia
sunga boxer
sunga slip
sunga estampada
sunga preta
bermuda de surf
bermuda de surf masculina
bermuda para surfar
boardshort
boardshort masculino
board short surf
short de praia masculino
short de praia
bermuda de praia masculina
bermuda tactel praia
bermuda de banho masculina
bermuda elastano surf
bermuda com bolso surf
bermuda com cordão
short de surf
short surf masculino
short de banho masculino
bermuda para natação
bermuda para stand up paddle
bermuda de surf infantil
short de praia infantil
sunga infantil
bermuda de surf preço
comprar bermuda de surf
melhor bermuda para surfar
bermuda de surf tamanho
bermuda de surf secagem rápida
bermuda de surf sem costura
roupa de praia masculina
roupa de surf masculina
roupas de surf masculina
roupas de surf feminina
roupa de surf
roupa para surfar
moda praia masculina
surfwear masculino
surfwear
surf shop
loja de surf
loja de surf online
loja de surfwear
marca de surf brasileira
marcas de surfwear
```

# Lote 8 — Marca e navegacional (30)

Território de defesa, 20% do esforço conforme `analysis/00-territorios.md`.
Serve para medir se a marca composta cresce e se a entidade está desambiguada
do jornal.

```
use zero hora
usezerohora
use zero hora surf
use zero hora loja
use zero hora biquini
use zero hora maio
use zero hora poncho
use zero hora lycra
usezerohora.com.br
zero hora surf
surf zero hora
zero hora beachwear
zero hora moda praia
zero hora surfwear
loja use zero hora
use zero hora avaliações
use zero hora é confiável
use zero hora frete
use zero hora troca
use zero hora tamanhos
use zero hora cupom
use zero hora instagram
comprar use zero hora
marca use zero hora
zero hora roupa de praia
zero hora lycra surf
zero hora poncho surf
zero hora maio de surf
zero hora neoprene
zero hora sunkini
```

# Lote 9 — Informacional e GEO (70)

Volume baixo é esperado aqui. O valor deste lote é o fraseado: são as perguntas
que viram FAQ com schema `FAQPage` e que motores de resposta citam. Rode
também `phrase_questions` sobre as sementes do Keyword Magic Tool para pegar as
perguntas que esta lista não previu.

```
o que é poncho de surf
para que serve poncho de surf
como usar poncho de surf
qual o tamanho do poncho de surf
poncho de surf vale a pena
poncho de surf ou toalha
o que é lycra de surf
para que serve a lycra de surf
como escolher lycra de surf
como vestir a lycra de surf
como lavar lycra de surf
como tirar parafina da lycra de surf
qual sabão lavar roupa de lycra surf
lycra de surf pode usar na piscina
o que vestir para surfar
o que usar embaixo da lycra de surf
o que usar embaixo do maio de surf
como escolher maio de surf
maio ou biquini para surfar
qual biquini não sai surfando
como evitar assadura no surf
como se proteger do sol no surf
qual protetor solar para surf
protetor solar para surf
roupa para surfar iniciante
equipamento de surf iniciante
o que levar para o surf
como começar a surfar
surf feminino iniciante
surf feminino
o que é uv50
o que significa uv50
o que significa fps na roupa
roupa com fps 50 funciona
proteção uv da roupa dura quanto tempo
o que é rash guard
rash guard para que serve
diferença entre rash guard e lycra
qual a diferença entre maio de surf e maio comum
diferença entre neoprene e lycra
quando usar neoprene no surf
qual espessura de neoprene usar
temperatura da água para usar neoprene
como escolher tamanho de roupa de surf
tabela de medidas roupa de surf
como medir tamanho de biquini
como lavar roupa de praia
como conservar roupa de praia
como secar roupa de surf
quanto tempo dura uma lycra de surf
melhor tecido para roupa de praia
o que é tecido com proteção uv
roupa de praia sustentável
como se trocar na praia
como trocar de roupa na praia sem constrangimento
quanto custa uma roupa de surf
onde comprar roupa de surf
onde comprar lycra de surf
onde comprar poncho de surf
melhores marcas de surfwear do brasil
marcas brasileiras de moda praia
qual a melhor marca de biquini
surf de madrugada
surf ao amanhecer
sessão de surf de manhã
melhores praias para surfar no brasil
surf para iniciantes praia
o que é beachwear
diferença entre beachwear e surfwear
roupa de praia que não desbota
roupa de praia que não marca
```

---

## O que eu faço quando os CSVs voltarem

1. Perfilo cada arquivo e registro a proveniência em `reports/`.
2. Cruzo Keyword Planner (volume e CPC) com Semrush (KD, intenção, SERP
   feature), aplicando a regra de conflito da seção `<regras_de_dados>` do
   `CLAUDE.md`.
3. Monto `analysis/11-matriz-kws.md`: uma linha por keyword, com cluster, URL
   dona, papel (primária, secundária, cauda longa), volume, KD, intenção e
   status de canibalização.
4. Aplico o cálculo de prioridade de `analysis/estrategia-seo-mestre.md`
   (volume × Δ CTR esperado × proximidade da conversão ÷ esforço) e entrego
   `analysis/12-priorizacao.md` com a fila ordenada.
5. Só então abro as pautas dos artigos SEO/GEO.
