# uzh-seo — Projeto SEO/AEO Use Zero Hora

Operação de crescimento orgânico da **Use Zero Hora** (usezerohora.com.br),
marca D2C brasileira de surf/beachwear. O agente que opera este repositório é
regido pelo prompt em [`CLAUDE.md`](CLAUDE.md).

## Objetivo

Tráfego orgânico qualificado que converte em venda, via indexação em motores
de busca (Google) e citação em motores de resposta de IA (ChatGPT, Perplexity,
Gemini, AI Overviews).

## Por onde começar

A estratégia que rege o projeto está em
[`analysis/estrategia-seo-mestre.md`](analysis/estrategia-seo-mestre.md),
decomposta em dez blocos sequenciais (S0 a S9), cada um com gate objetivo de
saída. O ritmo de execução está em
[`analysis/20-ciclo-operacional.md`](analysis/20-ciclo-operacional.md).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `analysis/` | Estratégia mestre, territórios, catálogo, matriz de KWs, priorização e ciclo |
| `ciclos/` | Um diretório por ciclo: sinal, seleção e medição. Template em `ciclos/TEMPLATE.md` |
| `pautas/` | Uma pauta por arquivo, com KW primária, secundárias e anticanibalização |
| `content/` | HTML final para o CMS, mais a versão editor-safe (sem `<script>` no corpo) |
| `data/` | Bases exportadas pelo time — formato esperado em `data/README.md` |
| `reports/` | Snapshots datados de Semrush/Similarweb, leituras de base e medições |
| `scripts/` | Scripts de leitura e classificação das bases |

## Pipeline

| Fase | Nome | Artefato |
|---|---|---|
| F0 | Baseline e instrumentação | `reports/00-baseline.md` |
| F1 | Base de catálogo | `analysis/10-catalogo.md` |
| F2 | Consolidação de keywords | `analysis/11-matriz-kws.md` |
| F3 | Priorização e backlog | `analysis/12-priorizacao.md` + `pautas/` |
| F4 | Indexação por território | `analysis/13-indexacao.md` |
| F5 | Produção SEO/GEO | `content/<slug>.html` |
| F6 | Medição e realimentação | `reports/YYYY-MM-medicao.md` |

## Ciclo operacional

Mensal, fechando na F6, duas peças por ciclo:

**Semana 1** sinal e seleção (venda, posições, mercado) → **Semana 2** pauta →
**Semana 3** produção → **Semana 4** publicação e amarração de links →
**D+30 e D+60** medição, que reordena a fila.

A fila da F3 é ordenada por prioridade; o calendário sazonal manda na ordem de
publicação. Reconciliar os dois é o trabalho da semana 1.

Nenhuma etapa trava por ferramenta fora do ar — cada fonte tem caminho
degradado declarado. Estimar número de memória continua proibido.
