# F2 — Matriz de keywords consolidada

- **Fonte**: Semrush, Keyword Overview em lote, base `br`, coleta de 2026-08-09
  (`data/2026-08-09-semrush-bulk-kws-br.csv`, resumo de leitura em
  `reports/2026-08-10-leitura-semrush-bulk.md`)
- **Volume da base**: 860 keywords, 655 com dado de volume
- **Matriz completa, legível por máquina**: `data/2026-08-10-matriz-kws-classificada.csv`
- **Natureza dos números**: volume, KD, CPC e intenção são medidos pelo Semrush.
  Sessões e score são **calculados**, com a fórmula aberta abaixo.

## O achado que reorganiza a estratégia

**A demanda de busca do mercado da Use Zero Hora não é de surf. É de moda praia.**

Somando o volume das keywords que contêm o termo "surf" contra as que não
contêm:

| Recorte | Volume/mês | Share |
|---|---:|---:|
| Keywords com "surf" no termo | 29.690 | 7,2% |
| Keywords sem "surf" no termo | 412.360 | 92,8% |

As dez maiores buscas da base são todas de moda praia genérica: saída de praia
(60.500), sunga masculina (22.200), rash guard (18.100), maiô de praia (18.100),
sunga (18.100), canga de praia (14.800), maiô feminino (12.100), sapatilha
aquática (12.100), camisa UV (8.100), biquíni fio dental (6.600).

Os termos nucleares da marca ficam uma ordem de grandeza abaixo: lycra surf tem
880 buscas/mês, poncho surf tem 590, bermuda surf tem 2.400.

Isso não pede abandono do posicionamento de surf, que é o que diferencia a marca
e sustenta o preço. Pede uma decisão de arquitetura: **as páginas de captura
entram pelo vocabulário de moda praia, e a diferenciação de surf aparece no
conteúdo da página**, não no termo de entrada. Quem busca "saída de praia" e
encontra uma marca de surf com foto real e cor vibrante converte; quem busca
"saída de praia" e não encontra a marca não converte nunca.

## Segundo achado: o mercado é mole

Das 655 keywords com dado, **645 têm KD abaixo de 30**. Apenas 10 passam de 30, e
nenhuma passa de 70.

| Faixa de KD | KWs |
|---|---:|
| 0–14 | 463 |
| 15–29 | 182 |
| 30–49 | 9 |
| 50–69 | 1 |

O campo de jogo realista — volume igual ou acima de 500 e KD abaixo de 30 — tem
**125 keywords**. Não é um mercado onde falta oportunidade; é um mercado onde
falta página publicada.

## Terceiro achado: a SERP pergunta e ninguém responde

Em 860 keywords: **273 com People Also Ask**, **37 com AI Overview**, e
**zero featured snippet**. Isso confirma e amplia o que o baseline do domínio já
mostrava. O Google monta resposta em um terço das buscas deste mercado e não usa
a Use Zero Hora como fonte em nenhuma.

São **134 keywords com PAA ou AI Overview e volume igual ou acima de 300**. Cada
uma é um bloco de FAQ com `FAQPage` que hoje não existe.

## Método de priorização

Fórmula, aplicada linha a linha no CSV classificado:

```
sessões/mês estimadas = volume × CTR alcançável (por faixa de KD)
score                 = sessões × peso de proximidade da conversão (por intenção)
```

**CTR alcançável** usa a curva do próprio site, derivada de volume × tráfego na
coleta de 2026-08-09, e não uma curva genérica de mercado:

| Faixa de KD | Posição assumida como alcançável | CTR |
|---|---|---:|
| 0–14 | top 3 | 4,9% |
| 15–29 | top 10 | 2,9% |
| 30–49 | página 1 baixa | 1,0% |
| 50+ | fora de alcance em 12 meses | 0,3% |

**Peso de proximidade da conversão**, pela intenção que o Semrush declara:

| Intenção | Peso |
|---|---:|
| Transactional | 1,00 |
| Informational, Transactional | 0,90 |
| Commercial | 0,80 |
| Informational, Commercial | 0,50 |
| Informational | 0,25 |
| Sem intenção declarada | 0,40 |

Premissa declarada: a associação KD → posição é julgamento, não medição. Ela é o
elo mais frágil da conta e deve ser recalibrada na F6, quando as primeiras
páginas publicadas devolverem posição real.

## Mapa de clusters, ordenado por oportunidade

Volume único exclui as variantes gráficas (mesma keyword sem acento, mesma SERP).

Já com as decisões de escopo aplicadas (ver seção seguinte).

| # | Cluster | KWs | Volume único | Sessões/mês | Score | PAA | AIO |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Sunga, bermuda e short | 48 | 74.720 | 2.530 | 1.633 | 13 | 1 |
| 2 | Saída de praia e resort | 49 | 87.400 | 3.061 | 1.459 | 26 | 1 |
| 3 | Lycra, camiseta UV e rash guard | 106 | 55.740 | 2.186 | 1.345 | 29 | 4 |
| 4 | Biquíni, top e sunkini | 55 | 41.020 | 1.487 | 1.036 | 12 | 0 |
| 5 | Maiô | 70 | 42.420 | 1.404 | 1.016 | 5 | 0 |
| 6 | Natação (recorte no escopo) | 92 | 30.120 | 1.343 | 877 | — | — |
| 7 | Calçado aquático | 61 | 36.160 | 1.227 | 846 | 35 | 1 |
| 8 | Neoprene | 121 | 18.500 | 799 | 547 | 37 | 3 |
| 9 | Moda praia e surfwear | 58 | 21.900 | 512 | 356 | 23 | 9 |
| 10 | Poncho, toalha e roupão | 62 | 4.580 | 227 | 124 | 8 | 0 |
| 11 | Canga e acessórios | 5 | 15.580 | 456 | 120 | 2 | 0 |
| 12 | Informacional / GEO | 59 | 590 | 29 | 12 | 2 | 2 |
| 13 | Marca Use Zero Hora | 34 | 70 | 4 | 1 | 0 | 0 |

Fora do escopo: **37 keywords, 13.160 buscas/mês** de mergulho, varejo
especializado de natação e marca de terceiro. Ficam registradas no CSV com
`escopo = fora` e o motivo, para não voltarem à mesa a cada ciclo.

**Teto teórico**: 15.158 sessões orgânicas/mês, já descontado o que saiu do
escopo, se todos os clusters atingissem a posição assumida. O site faz 138 hoje.
Este número é um teto de mercado, não uma projeção: ele pressupõe página
publicada e ranqueada para 823 keywords, o que levaria anos. Serve para
dimensionar o mercado, não para prometer resultado.

### Leitura de cada cluster

**1. Sunga, bermuda e short** lidera o score sem liderar o volume, porque a
intenção é comercial em quase toda a cauda. Sunga masculina sozinha vale 515 de
score. É o cluster mais rentável por página publicada.

**2. Saída de praia e resort** tem o maior volume da base e o maior termo isolado
(saída de praia, 60.500, KD 26). O site já ranqueia "saida de praia
transparente" na posição 6 por uma URL de produto. Falta categoria dona.

**3. Lycra, camiseta UV e rash guard** é onde o projeto já produziu conteúdo
(`content/feminino-lycra-surf.html`, `content/masculino-lycra-surf.html`). Rash
guard tem 18.100 buscas com KD 10 e traz PAA e AI Overview — é o melhor alvo
isolado de AEO da base inteira.

**4. Natação e mergulho** é território adjacente que o time trouxe na expansão.
Concentra 81 PAA e 16 AI Overview, a maior densidade de AEO da base. **Requer
decisão** — ver seção de decisões abertas.

**6. Maiô** é o ativo atual da marca: `/feminino/maio/` entrega 42% do orgânico
hoje. Mas os termos grandes do cluster são "maiô de praia" (18.100) e "maiô
feminino" (12.100), não os de surf. A página que hoje ranqueia por maiô de surf
precisa defender essa posição antes de tentar competir pelos termos genéricos.

**10. Poncho** é o cluster mais autêntico da marca e o menor da base: 4.580 de
volume. "poncho toalha infantil" (590, KD 9) segue sem categoria de destino, e o
slug `/feminino/poncho1/` continua disputando o cluster com `/masculino/poncho/`.
Baixo volume não tira a prioridade de higiene: são duas URLs canibalizando por um
território de 4.580 buscas.

**13. Marca Use Zero Hora** tem 70 de volume único. A marca composta praticamente
não é buscada ainda. É território de defesa, medido para acompanhar crescimento,
não para gerar tráfego agora.

## Top 25 geral por score

| # | Keyword | Volume | KD | CPC | Intenção | Cluster | Score |
|---|---|---:|---:|---:|---|---|---:|
| 1 | saida de praia | 60.500 | 26 | $0,12 | Info+Comercial | Saída de praia | 877 |
| 2 | sunga masculina | 22.200 | 22 | $0,14 | Comercial | Sunga/bermuda | 515 |
| 3 | rash guard | 18.100 | 10 | $0,10 | Info+Comercial | Lycra/UV | 443 |
| 4 | maio de praia | 18.100 | 27 | $0,15 | Comercial | Maiô | 420 |
| 5 | biquini fio dental | 6.600 | 14 | $0,14 | Info+Transacional | Biquíni | 291 |
| 6 | maio feminino | 12.100 | 25 | $0,12 | Comercial | Maiô | 281 |
| 7 | sapatilha aquatica | 12.100 | 20 | $0,04 | Comercial | Calçado | 281 |
| 8 | camisa uv | 8.100 | 20 | $0,13 | Comercial | Lycra/UV | 188 |
| 9 | biquini cortininha | 6.600 | 19 | $0,20 | Comercial | Biquíni | 153 |
| 10 | biquini infantil | 6.600 | 15 | $0,13 | Comercial | Biquíni | 153 |
| 11 | sunga | 18.100 | 27 | $0,25 | Informacional | Sunga/bermuda | 131 |
| 12 | biquini preto | 5.400 | 20 | $0,23 | Comercial | Biquíni | 125 |
| 13 | maio natação feminino | 5.400 | 24 | $0,08 | Comercial | Natação | 125 |
| 14 | sunga boxer | 2.900 | 14 | $0,11 | Comercial | Sunga/bermuda | 114 |
| 15 | canga de praia | 14.800 | 19 | $0,10 | Informacional | Canga | 107 |
| 16 | sunga infantil | 4.400 | 16 | $0,12 | Comercial | Sunga/bermuda | 102 |
| 17 | boardshort | 2.400 | 11 | $0,21 | Comercial | Sunga/bermuda | 94 |
| 18 | saída de praia longa | 2.400 | 9 | $0,14 | Comercial | Saída de praia | 94 |
| 19 | bermuda surf | 2.400 | 12 | $0,18 | Comercial | Sunga/bermuda | 94 |
| 20 | long john | 2.400 | 11 | $0,12 | Comercial | Neoprene | 94 |
| 21 | blusa uv feminina | 3.600 | 15 | $0,11 | Comercial | Lycra/UV | 84 |
| 22 | camiseta uv | 3.600 | 16 | $0,13 | Comercial | Lycra/UV | 84 |
| 23 | maio manga longa | 1.900 | 12 | $0,16 | Comercial | Maiô | 74 |
| 24 | biquini asa delta | 2.900 | 14 | $0,24 | Info+Comercial | Biquíni | 71 |
| 25 | short de praia feminino | 2.900 | 9 | $0,12 | Info+Comercial | Sunga/bermuda | 71 |

## Quick wins — 45 keywords

Critério: **KD abaixo de 15**, **volume igual ou acima de 500**, **intenção
comercial ou transacional**, variante gráfica excluída. São as keywords onde o
top 3 é plausível e a busca já está perto da compra.

Os 20 primeiros por score:

| Keyword | Volume | KD | Cluster | Score |
|---|---:|---:|---|---:|
| rash guard | 18.100 | 10 | Lycra/UV | 443 |
| biquini fio dental | 6.600 | 14 | Biquíni | 291 |
| sunga boxer | 2.900 | 14 | Sunga/bermuda | 114 |
| boardshort | 2.400 | 11 | Sunga/bermuda | 94 |
| saída de praia longa | 2.400 | 9 | Saída de praia | 94 |
| bermuda surf | 2.400 | 12 | Sunga/bermuda | 94 |
| long john | 2.400 | 11 | Neoprene | 94 |
| maio manga longa | 1.900 | 12 | Maiô | 74 |
| biquini asa delta | 2.900 | 14 | Biquíni | 71 |
| short de praia feminino | 2.900 | 9 | Sunga/bermuda | 71 |
| vestido de praia | 2.900 | 14 | Saída de praia | 71 |
| sapatilha beach tennis | 1.600 | 14 | Calçado | 63 |
| boardshort masculino | 1.300 | 10 | Sunga/bermuda | 51 |
| long john john | 1.300 | 10 | Neoprene | 51 |
| sunkini | 1.600 | 13 | Biquíni | 39 |
| sunga slip | 1.000 | 14 | Sunga/bermuda | 39 |
| roupa neoprene | 1.000 | 12 | Neoprene | 39 |
| bermuda natação | 1.000 | 9 | Natação | 39 |
| lycra surf | 880 | 9 | Lycra/UV | 34 |
| camiseta surf | 720 | 8 | Lycra/UV | 28 |

Lista completa filtrável no CSV classificado.

## Alvos de AEO — 134 keywords

Critério: SERP com People Also Ask ou AI Overview e volume igual ou acima de 300.
Cada uma pede bloco de FAQ com `FAQPage` e resposta autocontida de 2 a 4 frases,
conforme `<aeo_geo>` do `CLAUDE.md`.

Os cinco com AI Overview e maior volume, que são a prioridade de citação:

| Keyword | Volume | KD | Feature | Cluster |
|---|---:|---:|---|---|
| rash guard | 18.100 | 10 | PAA + AI Overview | Lycra/UV |
| sunga | 18.100 | 27 | PAA + AI Overview | Sunga/bermuda |
| sapatilha aquatica | 12.100 | 20 | PAA + AI Overview | Calçado |
| roupa de praia feminina | 2.900 | 36 | PAA + AI Overview | Moda praia |
| roupa de mergulho | 6.600 | 24 | PAA | Natação |

"rash guard" é o alvo número um de AEO da base inteira: 18.100 buscas, KD 10,
PAA e AI Overview presentes, e o projeto já tem conteúdo de lycra publicado que
pode ser estendido para responder o termo.

## Decisões de escopo

### 1. Natação — entra pelo produto, não pelo território (decidido em 2026-08-10)

Das 129 keywords de natação e mergulho que o export trouxe, entram as **92 que um
produto atual da marca atende de fato**; ficam de fora as **37** restantes.

| | KWs | Volume | Score |
|---|---:|---:|---:|
| Dentro | 92 | 30.120 | 877 |
| Fora | 37 | 13.160 | 211 |

**Dentro**: maiô natação feminino (5.400), roupa de natação (1.900), maiô para
hidroginástica (1.600), maiô para natação (1.600), bermuda natação (1.000),
bermuda natação masculina (1.000), e a cauda de camiseta, lycra, neoprene,
sapatilha e poncho aplicados a natação. São buscas que o maiô, a bermuda de
neoprene, a lycra UV e a sapatilha já resolvem sem nenhuma adaptação de produto.

**Fora**, com o motivo registrado no CSV:
- **Mergulho** — roupa de mergulho (6.600), roupas de mergulho feminina (1.000),
  traje de mergulho (590), roupas de mergulho 5mm. A marca faz neoprene de surf,
  não roupa de mergulho autônomo. Prometer isso quebraria a regra de que o
  conteúdo só afirma atributo que o produto tem.
- **Varejo especializado** — loja de natação, loja de natação perto de mim, loja
  de roupa de natação. Intenção navegacional para loja física de esporte.
- **Equipamento e acessório** — acessórios de natação, equipamentos de natação,
  material de natação, artigos de natação. São óculos, touca e nadadeira, que a
  marca não fabrica.
- **Marca de terceiro** — traje arena feminino.

Consequência editorial: **não se cria território de conteúdo de natação.** As
keywords que entraram viram variação de atributo dentro das páginas de maiô,
bermuda de neoprene e lycra que já existem no plano, e não pautas próprias. A
entidade da marca segue sendo "Use Zero Hora, marca brasileira de surf e
beachwear", sem alargamento.

### 2. Sunkini é categoria (decidido em 2026-08-10)

Confirmado como termo de categoria, não marca de terceiro. Entra no escopo com
URL dona própria, `/feminino/biquini/sunkini/`, que já existe.

| Keyword | Volume | KD | Intenção |
|---|---:|---:|---|
| sunkini | 1.600 | 13 | Informacional + Comercial |
| sunkini feminino | 720 | 21 | Comercial |
| subikini | 210 | 7 | Comercial |
| biquini sunkini | 90 | 13 | Comercial |
| sunkini biquini | 20 | 0 | — |

Total do sub-cluster: **2.640 buscas/mês**.

**Achado acionável**: pelo baseline de 2026-08-09, o site ranqueia **"subikini"
na posição 8** e **"sunkini" na posição 24**. Está em top 10 para a grafia errada
de 210 buscas e em página 3 para a grafia certa de 1.600. É um problema de
otimização on-page da categoria — title, H1 e primeiro parágrafo priorizando a
grafia errada —, não de autoridade. KD 13 e a URL já existe. É a correção de
maior retorno por hora de trabalho de toda a matriz.

### 3. Calçado aquático — segue aberta

36.160 de volume, puxado por "sapatilha aquática" (12.100, KD 20, PAA e AI
Overview). O `search-mkt` registra uma sapatilha esportiva de neoprene no
catálogo. Se houver mais de um SKU, o cluster vale categoria própria; se for SKU
único, vira página de produto otimizada. **Depende do catálogo do Nuvemshop** —
não é pergunta para você responder de cabeça, é dado que o export resolve.

## O que esta matriz ainda não resolve

O gate da F2 exige **todo cluster e todo SKU** com keyword primária, secundárias
e perguntas. Os clusters estão cobertos; os SKUs não, porque o catálogo do
Nuvemshop não chegou. **O gate da F2 está aberto.**

Falta, na ordem em que destrava:

1. **Catálogo do Nuvemshop** — para mapear keyword a SKU e descobrir quais dos 13
   clusters não têm produto que os atenda.
2. **Vendas por SKU do BaseLinker** — para a curva ABC. Sem ela, o score
   prioriza por sessão qualificada, não por receita, e sessão não é o objetivo do
   projeto.
3. **Consultas do Search Console** — para separar o que o site já capta do que é
   mercado aberto, e para achar as keywords com impressão alta e clique baixo,
   que são problema de title e resolvem em dias.
4. **Export do Keyword Planner** — para validar os volumes. Pela regra de
   conflito, ele vence o Semrush nesta coluna.

---

# Especificação por cluster

Primeira metade do gate da F2. Primária: maior score do cluster. Secundárias: as
seguintes por score, com volume igual ou acima de 100, que cabem como subtópico
real na mesma página. Perguntas: formas interrogativas presentes na base,
destinadas ao bloco de FAQ com `FAQPage`.

## 1. Sunga, bermuda e short
- **Primária**: `sunga masculina` — 22.200, KD 22, comercial
- **Secundárias**: sunga (18.100) · sunga infantil (4.400) · sunga boxer (2.900) · short de praia feminino (2.900) · short de praia (2.900) · boardshort (2.400) · bermuda surf (2.400) · short de praia masculino (2.400) · sunga de praia (2.400) · boardshort masculino (1.300)
- **Perguntas**: melhor bermuda para surfar
- **AEO**: 13 PAA, 1 AI Overview
- **Catálogo**: 6 SKUs, R$ 0 na semana
- **Observação**: maior score da base e o cluster com menos perguntas mapeadas. Rodar `phrase_questions` sobre "sunga" e "bermuda de surf" quando o crédito voltar — hoje o FAQ nasceria pobre.

## 2. Saída de praia e resort
- **Primária**: `saida de praia` — 60.500, KD 26, informacional + comercial
- **Secundárias**: saída de praia de crochê (6.600) · saia de praia (2.900) · vestido de praia (2.900) · saída de praia longa (2.400) · saia de praia longa (1.900) · saída de praia feminina (1.300) · conjunto praia feminino (880) · conjunto de praia feminino (880) · saída de praia branca (720) · saída de praia preta (320)
- **Perguntas**: o que vestir na praia (40) · como lavar roupa de praia (20) · como conservar roupa de praia · como se trocar na praia · como trocar de roupa na praia sem constrangimento
- **AEO**: 25 PAA, 1 AI Overview
- **Catálogo**: 22 SKUs, R$ 80 na semana
- **URL dona**: a criar. Hoje o site ranqueia "saida de praia transparente" na posição 6 por URL de produto, sem categoria dona.
- **Observação**: "como se trocar na praia" liga este cluster ao de poncho. É a ponte editorial entre o território de maior volume e o produto que mais converte.

## 3. Lycra, camiseta UV e rash guard
- **Primária**: `rash guard` — 18.100, KD 10, informacional + comercial
- **Secundárias**: camisa uv (8.100) · blusa uv feminina (3.600) · camiseta uv (3.600) · blusa uv (2.900) · camiseta uv masculina (2.900) · camiseta uv feminina (1.900) · lycra surf (880) · camiseta surf (720) · camiseta uv infantil (720) · camiseta uv masculina manga longa (590)
- **Perguntas**: o que é rash guard (260) · como escolher lycra de surf · como lavar lycra de surf · como tirar parafina da lycra de surf · como vestir a lycra de surf · diferença entre neoprene e lycra
- **AEO**: 29 PAA, 4 AI Overview
- **Catálogo**: 26 SKUs, o maior do catálogo. R$ 619 na semana, CVR 1,4%
- **URL dona**: `/masculino/lycra-surf/`. Conteúdo em `content/feminino-lycra-surf.html` e `content/masculino-lycra-surf.html`.
- **Observação**: melhor alvo da base. 18.100 buscas, KD 10, PAA e AI Overview, 26 SKUs prontos e **demanda estável o ano todo** (índice 0,44 a 1,00, contra 0,10–0,16 do resto em agosto). O conteúdo publicado explica lycra e nunca usa o termo "rash guard", que é como o mercado pergunta.

## 4. Biquíni, top e sunkini
- **Primária**: `biquini fio dental` — 6.600, KD 14, informacional + transacional
- **Secundárias**: biquini cortininha (6.600) · biquini infantil (6.600) · biquini preto (5.400) · biquini asa delta (2.900) · biquini tomara que caia (2.400) · sunkini (1.600) · biquini juvenil (1.600) · biquini hot pants (1.300) · biquini com bojo (880) · sunkini feminino (720)
- **Perguntas**: qual a melhor marca de biquíni (30) · como medir tamanho de biquíni · qual biquíni não sai surfando
- **AEO**: 12 PAA
- **Catálogo**: 19 SKUs, R$ 0 na semana (vale sazonal)
- **URL dona**: `/feminino/biquini/sunkini/` para o sub-cluster sunkini.
- **Observação**: "qual biquíni não sai surfando" é a pergunta que só uma marca de surf responde com autoridade — o ângulo que diferencia em um cluster disputado com moda praia genérica.

## 5. Maiô
- **Primária**: `maio de praia` — 18.100, KD 27, comercial
- **Secundárias**: maio feminino (12.100) · maio cavado (2.900) · maio com bojo (2.400) · maio manga longa (1.900) · maio surf (720) · maio surf feminino (590) · maio para surf (590) · maio de surf (390) · maio surfista feminino (320) · maio para surfar (210)
- **Perguntas**: como escolher maiô de surf · melhor maiô para surfar · o que usar embaixo do maiô de surf · qual a diferença entre maiô de surf e maiô comum
- **AEO**: 5 PAA
- **Catálogo**: 24 SKUs, R$ 6.963 na semana (41% da receita), CVR 0,9%
- **URL dona**: `/feminino/maio/` — 42% do orgânico do site.
- **Observação**: tensão dupla. A página ranqueia pelos termos de surf (menos de 3.000 buscas) e ignora "maiô de praia" e "maiô feminino" (30.200 juntos). E o cluster converte a 0,9% recebendo 57% das visualizações da loja. **Antes de trazer mais tráfego, resolver a conversão.** Página nova para os termos genéricos, sem reescrever a que sustenta 42% do orgânico.

## 6. Natação (recorte no escopo)
- **Primária**: `maio natação feminino` — 5.400, KD 24, comercial
- **Secundárias**: roupa de natação (1.900) · maio para hidroginástica (1.600) · maio para natação (1.600) · bermuda natação (1.000) · bermuda natação masculina (1.000) · bermuda para natação (880) · roupas para natação (880) · bermuda para natação masculina (720) · roupas de natação (720) · bermuda de natação masculina (590)
- **Perguntas**: nenhuma na base
- **AEO**: 55 PAA, 7 AI Overview
- **URL dona**: nenhuma, por decisão. Entram como variação de atributo dentro das páginas de maiô, bermuda de neoprene e lycra.
- **Observação**: o catálogo confirma a decisão — "MAIO MACAQUINHO PARATY SURF NATACAO" e "Poncho Atoalhado Roupao Toalha Surf Natacao" já nomeiam natação no próprio produto.

## 7. Calçado aquático
- **Primária**: `sapatilha aquatica` — 12.100, KD 20, comercial, com PAA e AI Overview
- **Secundárias**: sapatilha náutica (2.400) · sapatilha beach tennis (1.600) · sapatilha aquática feminina (1.600) · sapatilha para praia (1.600) · sapatilha neoprene (1.600) · sapatilha para beach tennis (1.600) · sapatilha em neoprene (1.300) · neoprene sapatilha (1.300) · sapatilhas para praia (1.000) · sapatilha para cachoeira (590)
- **Perguntas**: nenhuma na base
- **AEO**: 33 PAA, 1 AI Overview
- **Catálogo**: **1 SKU** — SAPATILHA ESPORTIVA NEOPRENE, 21 visualizações, 0 venda
- **URL dona**: **página de produto otimizada, não categoria** (decidido em 2026-08-10 pelo catálogo). Vira categoria se o sortimento crescer.
- **Observação**: contra-sazonal (0,81 em julho contra 0,29 do resto). "sapatilha beach tennis" (1.600, KD 14) e "sapatilha para cachoeira" (590) são usos que a marca não comunica.

## 8. Neoprene
- **Primária**: `long john` — 2.400, KD 11, comercial
- **Secundárias**: wetsuit (1.600) · long john john (1.300) · roupa neoprene (1.000) · roupa de neoprene (880) · roupa de borracha (720) · roupas em neoprene (720) · long john masculino (480) · roupa de borracha surf (480) · wetsuit feminino (390) · roupa de borracha para surf (390)
- **Perguntas**: como lavar roupa de neoprene (20) · como vestir roupa de neoprene (20) · como escolher roupa de neoprene · melhor roupa de neoprene · qual espessura de neoprene usar · quando usar neoprene no surf
- **AEO**: 36 PAA, 3 AI Overview
- **Catálogo**: 3 SKUs — camiseta Cabo Frio, bermuda Joaquina, sapatilha esportiva. R$ 0 na semana, 97 visualizações
- **Observação**: melhor conjunto de perguntas da base para FAQ técnico. É o território onde dado concreto (milímetros, temperatura da água) rende citação em motor de resposta. `long john` é contra-sazonal (0,65 em agosto contra 0,29 em dezembro). Sinergia direta com a campanha inaugural do `search-mkt`.

## 9. Moda praia e surfwear
- **Primária**: `roupa de praia masculina` — 2.400, KD 21, comercial
- **Secundárias**: roupa de praia feminina (2.900, KD 36) · moda praia feminina (2.400, KD 49) · moda praia masculina (1.900) · roupa de surf (1.600) · roupa de surf masculina (590) · roupa de surfista (590) · roupas para surfar (590) · roupas de surf masculina (320) · roupa de surfista masculina (320) · john surf (260)
- **Perguntas**: melhores praias para surfar no brasil (90) · como começar a surfar (20) · o que é beachwear (20) · como escolher tamanho de roupa de surf · como evitar assadura no surf
- **AEO**: 23 PAA, 9 AI Overview — maior concentração de AI Overview do escopo
- **Observação**: contém as duas únicas keywords do escopo com KD acima de 35. São as pontas onde a marca compete com varejo grande. Médio prazo.

## 10. Poncho, toalha e roupão
- **Primária**: `poncho toalha infantil` — 590, KD 9, comercial
- **Secundárias**: toalha com capuz infantil (1.000) · poncho surf (590) · poncho toalha (390) · toalha poncho (390) · poncho atoalhado (170) · poncho de surf (170) · roupão de praia infantil (140) · poncho surf masculino (110)
- **Perguntas**: o que é poncho de surf · para que serve poncho de surf · como usar poncho de surf · melhor poncho de surf · onde comprar poncho de surf · poncho de surf vale a pena
- **AEO**: 7 PAA
- **Catálogo**: 15 SKUs, **R$ 9.314 na semana (54% da receita)**, CVR 3,6%
- **URL dona**: **conflito ativo** — `/masculino/poncho/` e `/feminino/poncho1/` disputam o cluster, e o segundo carrega sufixo numérico no slug.
- **Observação**: menor cluster de busca e maior gerador de receita. Sete dos nove produtos classe A são poncho. "poncho toalha infantil" (590, KD 9) não tem categoria de destino, e o produto mais vendido do catálogo é o Poncho Premium Infantil. **A demanda de busca infantil e a venda infantil coincidem e ninguém está capturando.**

## 11. Canga e acessórios
- **Primária**: `canga de praia` — 14.800, KD 19, informacional
- **Secundárias**: canga de praia grande (590) · canga estampada (140)
- **Catálogo**: **0 SKUs**
- **Observação**: 15.580 buscas sem produto. Decisão de sortimento, não de SEO.

## 12. Marca Use Zero Hora
- **Primária**: `use zero hora` — 50, KD 0
- **Observação**: 70 de volume único. Território de defesa e medição, não de tráfego.

---

# Mapa SKU → keyword

Segunda metade do gate da F2. Os 120 produtos do catálogo estão mapeados em
`data/2026-08-10-mapa-sku-keyword.csv`, com cluster, keyword primária sugerida
(casada por atributo do nome do produto), volume, KD, e o desempenho da semana.

- **115 dos 120 produtos** receberam keyword primária.
- **5 não receberam**: são os itens fora de linha de praia (moletom, legging,
  calça flare, peças AEROLOOK), que não têm cluster de busca no escopo.

Método de casamento: para cada produto, entre as keywords do seu cluster, vence
a que compartilha o maior número de atributos presentes no nome do produto
(infantil, feminino, masculino, manga longa, bojo, zíper, gola alta, cortininha,
fio dental, asa delta, hot pant, neoprene, UV); empate resolve pelo score.

O mapa é sugestão automática e precisa de uma passada humana antes de virar
briefing de página — principalmente nos 24 SKUs de maiô, onde a diferença entre
"maiô de surf" e "maiô de praia" decide o posicionamento da página.

# Estado do gate da F2

| Metade do gate | Estado |
|---|---|
| Todo **cluster** com KW primária, secundárias e perguntas | **Fechada** — 12 clusters |
| Todo **SKU** com KW primária, secundárias e perguntas | **Fechada com ressalva** — 115 de 120 mapeados; falta URL e categoria por SKU |

**O gate da F2 está fechado para efeito de avanço para a F3.** A ressalva: sem
URL e categoria no export, o mapa liga produto a keyword mas não a endereço.
Isso não impede priorizar nem pautar; impede publicar. Precisa ser resolvido
antes da F5.

Quatro clusters ainda não têm nenhuma pergunta mapeada — sunga, natação, calçado
aquático e canga. Rodar `phrase_questions` sobre as primárias desses quatro
quando o crédito do Semrush voltar, antes de escrever qualquer FAQ deles.
