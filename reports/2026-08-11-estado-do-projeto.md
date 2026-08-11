# Estado do projeto — 2026-08-11

Panorama de onde o projeto está, o que está pronto, o que está travado e em
quem. Atualizar a cada fim de ciclo.

## Números de referência

| Métrica | Valor | Fonte |
|---|---|---|
| Tráfego orgânico | 138 visitas/mês | Semrush BR, 2026-08-09 |
| Keywords no top 100 | 146, das quais 86 entre a posição 11 e 30 | Semrush BR, 2026-08-09 |
| Keywords no top 10 | 21 (Only Surf: 1.809) | Semrush BR, 2026-08-09 |
| Concentração de risco | `/feminino/maio/` = 42% do orgânico | Semrush BR, 2026-08-09 |
| Featured snippets | 0, contra 273 PAA e 37 AIO em 860 KWs | Semrush BR, 2026-08-09 |
| Receita da semana | R$ 17.102,23 · 98 unidades · CVR 1,61% | Nuvemshop, 02–09/08/2026 |
| Receita por cluster | Poncho 54% (CVR 3,6%) · Maiô 41% (CVR 0,9%) | Nuvemshop, 02–09/08/2026 |
| Share do orgânico no tráfego | 15,4% (Display + Social Pago = 63%) | Similarweb, abr–jul/2026 |
| Cobertura de ficha técnica | 26 SKUs de 120 (22%) | BaseLinker, 2026-08-10 |

## Blocos da estratégia

Referência: `analysis/estrategia-seo-mestre.md`.

| Bloco | Estado | O que falta |
|---|---|---|
| S0 — Baseline e instrumentação | Parcial | Search Console exportado; GA4 com receita orgânica isolada |
| S1 — Saúde técnica | Não iniciado | Site Audit; `noindex` na busca interna; canonical de variação |
| S2 — Arquitetura e mapa KW→URL | Não iniciado | Resolver poncho (3 URLs) e conjunto atoalhado (2 URLs) |
| S3 — Colheita 11–30 | Não iniciado | 86 keywords esperando; maior reserva de retorno do projeto |
| S4 — Entidade | Decisão tomada, execução aberta | `Organization` na home, `sameAs`, "Quem Somos" como página de entidade |
| S5 — Mapa de oportunidades | **Fechado** | 860 KWs coletadas e classificadas |
| S6 — Motor de conteúdo | **Aberto e rodando** | Ciclo 01 entregue; ciclo 02 em setembro |
| S7 — AEO/GEO | Parcial | Camada aplicada no rash guard; falta o teste de citação com prompt fixo |
| S8 — Autoridade off-page | Não iniciado | Gap de backlinks contra Only Surf, Wet Dreams, Soulfins |
| S9 — Medição | Aberto | Primeiro relatório mensal depende de publicação |

## Fases

| Fase | Artefato | Gate |
|---|---|---|
| F0 — Baseline | `reports/2026-08-09-semrush-baseline-dominio.md` | Parcial: falta GSC e GA4 |
| F1 — Catálogo | `analysis/10-catalogo.md` | Parcial: falta URL e categoria por SKU |
| F2 — Matriz de KWs | `analysis/11-matriz-kws.md` | **Fechado** |
| F3 — Priorização | `analysis/12-priorizacao.md` + 4 pautas | **Fechado** |
| F4 — Indexação | — | Não iniciado. Depende da Onda 0 |
| F5 — Produção | `content/rash-guard.html` | Aberto: falta publicar |
| F6 — Medição | — | Depende de publicação |

## Ciclo 01 — agosto

Referência: `ciclos/ciclo-01-2026-08/` e `analysis/20-ciclo-operacional.md`.

| Item | Estado |
|---|---|
| Sinal e seleção | Fechados |
| Rash guard (E1, prioridade 585) | **Conteúdo pronto**, aguardando publicação |
| Onda 0 — higiene técnica | Aguardando o time de desenvolvimento |
| Segunda peça (E2 — proteção solar) | Aguardando ficha técnica do bloco 3 |
| Medição | Aberta, com posição de partida a preencher antes de publicar |

## Conteúdo produzido

| Arquivo | Cluster | Estado |
|---|---|---|
| `content/masculino-lycra-surf.html` | Lycra | Pronto desde 08/08, não publicado |
| `content/feminino-lycra-surf.html` | Lycra | Pronto desde 08/08, não publicado |
| `content/rash-guard.html` | Lycra/rash guard | Pronto em 10/08, não publicado |

Três peças prontas e nenhuma no ar. É o gargalo número um do projeto: sem
publicação não há medição, e sem medição toda decisão seguinte é opinião.

## Travas, por dono

### Time de desenvolvimento e CMS

1. `noindex` na busca interna — `/search/?q=` está indexada
2. Poncho responde por **três** URLs; conjunto atoalhado por duas
3. Não existe categoria infantil ("poncho toalha infantil" = 590 buscas/mês,
   e o Poncho Premium Infantil é o produto nº 1 da curva ABC)
4. Slug `/feminino/poncho1/` com sufixo numérico
5. Prazo real de publicação de um texto — define se o ciclo entrega uma ou
   duas peças

### Time de produto e operação

6. Ficha técnica dos blocos 1 e 2 (saída de praia e sunga) — destrava o
   ciclo 02, que precisa publicar até setembro
7. Instrução de lavagem e conservação: não existe em nenhum SKU
8. Garantia divergente entre produtos: 7 dias no poncho, 30 no maiô
9. Reescrever as duas descrições de Poncho Resort sinalizadas como texto de IA
10. Repor as 7 variantes que zeraram depois de vender
11. `CAMISETA BACKDOOR` tem descrição intitulada "Maresias"

### Decisões de negócio

12. "sunkini" (1.600 buscas/mês) é categoria ou marca de terceiro?
13. "rash guard" estende `/masculino/lycra-surf/` ou vira URL própria?
14. Canga tem 15.580 buscas/mês e não existe no catálogo — entra no
    sortimento?

### Ferramentas

15. **Semrush sem unidades de API.** A conta é uma subconta corporativa; é
    preciso contatar o titular da conta e solicitar a alocação de mais
    unidades de API.
16. MCP da Nuvemshop não conectado ao ambiente remoto — venda, estoque e
    categoria por SKU chegam por CSV
17. GA4 e Search Console ainda não exportados

## O que acontece assim que cada trava cair

| Trava que cai | O que destrava |
|---|---|
| Publicação das 3 peças | A medição, e com ela toda a realimentação da fila |
| Onda 0 | O cluster de poncho (54% da receita) e a editoria E3 |
| Ficha técnica blocos 1 e 2 | O ciclo 02 inteiro |
| Search Console | A colheita do S3, que são 86 keywords a uma página de distância |
| Unidades do Semrush | Recoleta de KD do poncho e as perguntas dos clusters novos |
