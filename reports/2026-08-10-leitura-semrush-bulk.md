# Resumo de leitura — export Semrush em lote (860 keywords)

## Proveniência

| Campo | Valor |
|---|---|
| Arquivo original | `UZHSEO_list_20260809.csv` |
| Arquivado como | `data/2026-08-09-semrush-bulk-kws-br.csv` |
| Quem enviou | Raphael Vianna, na sessão de 2026-08-10 |
| Ferramenta | Semrush, Keyword Overview em lote |
| Base de dados | `br` (coluna `Database`, uniforme em todas as linhas) |
| Data de referência | 2026-08-09, conforme sufixo do nome do arquivo |
| Colunas | 18, incluindo Volume, Keyword Difficulty, CPC (USD), Competitive Density, Number of Results, Intent, SERP Features, Trend, Click potential |
| Natureza dos números | Medidos pelo Semrush (estimativa da ferramenta para volume) |

Semente de origem: `data/2026-08-10-seed-kws-lista-corrida.txt`, as 550 keywords
que este projeto gerou em 2026-08-10.

## Perfil da base

- **860 linhas**, nenhuma duplicata.
- **655 com volume**; **205 sem nenhum dado** — o Semrush não tem registro
  dessas keywords na base BR. Dado indisponível via Semrush; não são zero, são
  ausência de medição.
- **63 keywords com volume zero** medido.
- Das 550 da semente, **as 550 voltaram**. O time expandiu com **310 keywords
  adicionais**, majoritariamente de natação, mergulho e calçado aquático.
- Volume somado: **466.450 buscas/mês**. Este número está inflado — ver
  limitação 1.

### Distribuição de Keyword Difficulty (655 com dado)

| Faixa | KWs |
|---|---|
| 0–14 (muito fácil) | 463 |
| 15–29 (fácil) | 182 |
| 30–49 (médio) | 9 |
| 50–69 (difícil) | 1 |
| 70+ | 0 |

### SERP features (860 keywords)

| Feature | Ocorrências |
|---|---|
| Site Links | 388 |
| Video | 388 |
| Related Searches | 377 |
| Popular Products | 347 |
| Image Pack | 332 |
| **People Also Ask** | **273** |
| Video Carousel | 126 |
| Short Videos | 79 |
| **AI Overview** | **37** |
| Local Pack | 26 |
| Reviews | 23 |
| **Featured Snippet** | **0** |

## Limitações registradas

1. **Variantes gráficas inflam o volume somado.** O Semrush trata "saida de
   praia" (60.500) e "saída de praia" (14.800) como keywords distintas, mas o
   Google entrega a mesma SERP. O mesmo vale para "sapatilha aquatica" (12.100)
   e "sapatilha aquática" (3.600), e outros pares. Na matriz classificada, a
   variante de menor volume é marcada na coluna `variante_de` e não é somada nos
   totais por cluster.
2. **Click potential veio quase constante.** 393 das 860 têm o campo
   preenchido, e 388 delas trazem o mesmo valor 20. A coluna não discrimina e
   não foi usada na priorização.
3. **Volume é estimativa do Semrush.** Pela regra de conflito do `CLAUDE.md`, o
   Google Ads Keyword Planner vence nesta coluna. Enquanto o export do Planner
   não chegar, os volumes aqui são o melhor dado disponível e estão declarados
   como estimativa.
4. **Sem dado de posição atual.** Este export é de mercado, não do domínio. O
   cruzamento com o que a Use Zero Hora já ranqueia usa o baseline de
   `reports/2026-08-09-semrush-baseline-dominio.md`, que cobre 146 keywords.
5. **CPC em dólar.** A coluna é `CPC (USD)`. Para uso no `search-mkt`, converter
   com a taxa da data de coleta.

## Decisões que esta base sustenta

- Ordenação dos clusters por oportunidade, em `analysis/11-matriz-kws.md`.
- Identificação dos 45 quick wins (KD abaixo de 15, volume igual ou acima de
  500, intenção comercial ou transacional).
- Lista de 134 alvos de AEO com People Also Ask ou AI Overview e volume igual ou
  acima de 300.

## Decisões que esta base NÃO sustenta

- Curva ABC de produto: depende do export de vendas do BaseLinker.
- Mapeamento keyword → SKU: depende do catálogo do Nuvemshop.
- Priorização por receita: depende das duas acima.
- Diagnóstico de canibalização: depende do export de páginas do Search Console.
