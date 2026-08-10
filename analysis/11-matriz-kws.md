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

| # | Cluster | KWs | Volume único | Sessões/mês | Score | PAA | AIO |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Sunga, bermuda e short | 48 | 74.720 | 2.530 | 1.633 | 13 | 1 |
| 2 | Saída de praia e resort | 49 | 87.400 | 3.061 | 1.459 | 26 | 1 |
| 3 | Lycra, camiseta UV e rash guard | 106 | 55.740 | 2.186 | 1.345 | 29 | 4 |
| 4 | *Natação e mergulho (adjacente)* | 129 | 43.280 | 1.670 | 1.088 | 81 | 16 |
| 5 | Biquíni e top | 55 | 41.020 | 1.487 | 1.036 | 12 | 0 |
| 6 | Maiô | 70 | 42.420 | 1.404 | 1.016 | 5 | 0 |
| 7 | Calçado aquático | 61 | 36.160 | 1.227 | 846 | 35 | 1 |
| 8 | Neoprene | 121 | 18.500 | 799 | 547 | 37 | 3 |
| 9 | Moda praia e surfwear | 58 | 21.900 | 512 | 356 | 23 | 9 |
| 10 | Poncho, toalha e roupão | 62 | 4.580 | 227 | 124 | 8 | 0 |
| 11 | Canga e acessórios | 5 | 15.580 | 456 | 120 | 2 | 0 |
| 12 | Informacional / GEO | 59 | 590 | 29 | 12 | 2 | 2 |
| 13 | Marca Use Zero Hora | 34 | 70 | 4 | 1 | 0 | 0 |

**Teto teórico**: 15.596 sessões orgânicas/mês se todos os clusters atingissem a
posição assumida. O site faz 138 hoje. Este número é um teto de mercado, não uma
projeção: ele pressupõe página publicada e ranqueada para as 655 keywords, o que
levaria anos. Serve para dimensionar o mercado, não para prometer resultado.

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

## Decisões abertas

**1. Natação e mergulho entra no escopo?** São 43.280 buscas/mês, 129 keywords,
81 com PAA e 16 com AI Overview — a maior densidade de AEO da base. Entrar
significa alargar a entidade da marca para além de surf e beachwear, o que
conflita com a regra de consistência de entidade do `CLAUDE.md`. A favor: os
produtos de neoprene e lycra servem a natação sem nenhuma adaptação, e o CPC de
$0,08 torna o território barato também no pago. Minha recomendação é entrar
apenas com as keywords que um produto atual atende de fato — "maiô natação
feminino" (5.400), "bermuda natação" (1.000) — e não construir território
editorial de natação. Precisa da sua decisão.

**2. "sunkini" é categoria ou marca de terceiro?** 1.600 buscas/mês, KD 13, e o
site já ranqueia "subikini" na posição 8. Se for marca de terceiro, sai do
escopo. Pergunta pendente desde a lista-semente.

**3. Calçado aquático é linha de produto ou termo adjacente?** 36.160 de volume,
puxado por "sapatilha aquática" (12.100). O `search-mkt` registra uma sapatilha
esportiva de neoprene no catálogo. Se o produto existe e tem estoque, o cluster
vale uma categoria própria; se é SKU único, vira página de produto otimizada.
Depende do catálogo do Nuvemshop.

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
