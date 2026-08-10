# F1 — Base de catálogo

- **Fonte**: Nuvemshop, relatórios *Produtos — Detalhe por produto* e *Produtos —
  Detalhe por variante de produto*
- **Período**: 2026-08-02 a 2026-08-09 (**uma semana**)
- **Recebido**: 2026-08-10, enviado por Raphael Vianna
- **Arquivos**: `data/2026-08-09-nuvemshop-produtos-semana.csv` e
  `data/2026-08-09-nuvemshop-variantes-semana.csv`
- **Mapa SKU → keyword**: `data/2026-08-10-mapa-sku-keyword.csv`
- **Natureza dos números**: medidos, de propriedade própria. Pela regra de
  conflito do `CLAUDE.md`, vencem qualquer estimativa de ferramenta para o que já
  aconteceu na loja.

## Limitação que atravessa todo este documento

**A janela é de sete dias, e são os sete dias de menor demanda do ano.**

Pela coluna Trend do Semrush (índice relativo dos últimos 12 meses), agosto é o
vale anual de praticamente todo o catálogo:

| Keyword | ago | dez | **mar** | jul |
|---|---:|---:|---:|---:|
| saida de praia | 0,16 | 0,30 | **0,66** | 0,30 |
| maio de praia | 0,13 | 0,20 | **0,81** | 0,29 |
| sunga masculina | 0,24 | 0,44 | **0,81** | 0,36 |
| canga de praia | 0,20 | 0,29 | **1,00** | 0,29 |
| poncho de surf | 0,10 | 0,07 | **1,00** | 0,15 |
| biquini fio dental | 0,24 | 0,29 | 0,44 | 0,44 |

Consequências para a leitura:

1. **Venda zero em biquíni, sunga e saída de praia nesta semana é sazonalidade,
   não produto morto.** Nenhuma decisão de descontinuar sortimento se apoia
   nestes sete dias.
2. **A curva ABC abaixo é provisória.** 98 unidades não sustentam classificação
   ABC. Ela vale como direção, não como corte. Precisa de 12 meses.
3. **O que vende no vale tem mérito real.** Poncho vendendo com CVR de 3,6% no
   mês mais fraco do ano é sinal forte, não ruído.

## Perfil da base

| Métrica | Valor |
|---|---:|
| Produtos no catálogo | 120 |
| Produtos com ao menos uma venda | 26 (22%) |
| Produtos com zero venda | 94 (78%) |
| Produtos com zero visualização | 0 |
| Unidades vendidas na semana | 98 |
| Receita na semana | R$ 17.102,23 |
| Visualizações | 6.090 |
| CVR agregada da loja | 1,61% |
| Ticket médio por unidade | R$ 174,51 |

O catálogo não traz URL, categoria, descrição nem atributo de produto — apenas
nome, venda, estoque, visualização e CVR. O gate da F1 pede URL e categoria por
SKU, então **o gate da F1 fecha parcialmente**: curva ABC provisória e atributos
inferidos do nome do produto, sem URL e sem categoria.

## Catálogo por cluster

| Cluster | SKUs | Unid. | Receita | % receita | Views | CVR |
|---|---:|---:|---:|---:|---:|---:|
| Poncho, toalha e roupão | 15 | 62 | R$ 9.314 | **54%** | 1.726 | **3,6%** |
| Maiô | 24 | 30 | R$ 6.963 | 41% | 3.450 | 0,9% |
| Lycra, camiseta UV e rash guard | 26 | 4 | R$ 619 | 4% | 284 | 1,4% |
| Saída de praia e resort | 22 | 1 | R$ 80 | 0% | 165 | 0,6% |
| Biquíni e top | 19 | 0 | R$ 0 | 0% | 194 | 0,0% |
| Neoprene (inclui a sapatilha) | 3 | 0 | R$ 0 | 0% | 97 | 0,0% |
| Sunga, bermuda e short | 6 | 0 | R$ 0 | 0% | 102 | 0,0% |
| Fora de linha (moletom, fitness) | 5 | 1 | R$ 126 | 1% | 72 | 1,4% |

A linha de neoprene tem exatamente os três produtos que o repositório `search-mkt`
registra na campanha inaugural: camiseta Cabo Frio, bermuda Joaquina e sapatilha
esportiva. **A sapatilha é o único produto do catálogo que atende o cluster de
calçado aquático**, que tem 36.160 buscas/mês.

## Curva ABC provisória

Classe A (80% da receita da semana), em ordem:

| # | Produto | Unid. | Receita | Views | CVR |
|---|---|---:|---:|---:|---:|
| 1 | Poncho Premium Infantil | 17 | R$ 2.211 | 307 | 5,54% |
| 2 | MAIO STORM | 8 | R$ 1.879 | 540 | 1,48% |
| 3 | MAIO MOANA | 7 | R$ 1.734 | 145 | 4,83% |
| 4 | PONCHO RESORT PREMIUM FEMININO | 8 | R$ 1.676 | 201 | 3,98% |
| 5 | MAIO RINCON | 7 | R$ 1.482 | 1.168 | **0,60%** |
| 6 | PONCHO CLASSICO TODAS AS CORES | 10 | R$ 1.229 | 166 | 6,02% |
| 7 | Poncho Premium Adulto M/G | 7 | R$ 1.163 | 127 | 5,51% |
| 8 | Poncho Atoalhado Roupão Toalha Surf Natação Clássico Adulto | 5 | R$ 703 | 160 | 3,12% |
| 9 | Poncho Clássico Infantil (XPP e PP) | 5 | R$ 616 | 145 | 3,45% |

Sete dos nove produtos de classe A são poncho.

## Três achados operacionais

### 1. O maiô recebe o tráfego, o poncho faz a receita

Maiô concentra **3.450 das 6.090 visualizações da loja (57%)** e converte a
**0,9%**. Poncho recebe 1.726 visualizações (28%) e converte a **3,6%** — quatro
vezes mais.

O caso extremo é **MAIO RINCON: 1.168 visualizações, 19% de todo o tráfego de
produto da loja, e CVR de 0,60%**. É o produto mais visto do catálogo e o de
pior conversão entre os que vendem.

Isso conversa diretamente com o baseline de SEO: `/feminino/maio/` entrega 42%
do tráfego orgânico do site. **O ativo orgânico número um da marca desemboca no
cluster que pior converte.** Antes de mandar mais tráfego para maiô, vale
descobrir por que 1.168 pessoas olharam o RINCON e 1.161 saíram — preço, foto,
tabela de medidas, frete ou disponibilidade de tamanho.

### 2. Ruptura de estoque em produto que estava vendendo

Sete variantes venderam na semana e terminaram com **estoque zero**:

| Produto | Variante | Vendeu |
|---|---|---:|
| Poncho Premium Infantil | Azul / 6–12 anos | 13 |
| MAIO LISO GOLA ALTA MANGA LONGA E ZÍPER | Preto / G | 2 |
| MAIO STORM | Vermelho / P | 2 |
| MAIO STORM | Marinho / P | 2 |
| Poncho Atoalhado Roupão Clássico Adulto | Grafite / M | 1 |
| Camiseta Lycra Surf UV50 Manga Longa Preto com Verde | M | 1 |
| PONCHO RESORT PREMIUM INFANTIL | Rosa / 12 | 1 |

A primeira linha é o produto mais vendido do catálogo, na cor mais vendida,
zerado. Não é assunto de SEO, mas nenhuma keyword resolve estoque zero — e
mandar tráfego para produto esgotado queima verba e sinal de qualidade.

### 3. Dois clusters de demanda alta sem produto que os atenda

| Cluster | Buscas/mês | SKUs |
|---|---:|---:|
| Canga e acessórios | 15.580 | **0** |
| Calçado aquático | 36.160 | **1** (a sapatilha de neoprene) |

Canga de praia tem 14.800 buscas em uma única keyword, KD 19, e pico de 1,00 em
março. Não existe canga no catálogo. **É decisão de sortimento, não de SEO** —
nenhum conteúdo converte demanda para produto que não existe.

Calçado aquático tem 36.160 buscas e um SKU com 21 visualizações e zero venda na
semana. Isso responde a decisão que estava aberta: **com um SKU, o cluster vira
página de produto otimizada, não categoria.** Vale registrar que "sapatilha
aquática" é contra-sazonal — índice entre 0,44 e 1,00 o ano inteiro, e 0,81 em
julho, quando o resto do catálogo está em 0,29. Junto com rash guard, é um dos
dois territórios que suavizariam a curva de receita fora do verão. Se o
sortimento crescer, o cluster vira categoria.

## O que ainda falta para fechar a F1 por completo

1. **URL e categoria por SKU** — o gate exige. Nenhum dos dois relatórios traz.
   Um export do catálogo (não do relatório de vendas) resolve.
2. **Atributos** — material, gramatura, proteção UV, medidas. Hoje só há o que o
   nome do produto revela. Conteúdo não pode afirmar atributo que não está na
   base.
3. **Doze meses de venda** — para a curva ABC valer como corte. O BaseLinker
   resolve.
