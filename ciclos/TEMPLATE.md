# Template de ciclo

Copie para `ciclos/ciclo-NN-AAAA-MM/` como três arquivos. O ciclo está
descrito em `analysis/20-ciclo-operacional.md`.

---

## 00-sinal.md

```markdown
# Ciclo NN — Sinal

- Data: AAAA-MM-DD

## Venda e estoque (Nuvemshop / BaseLinker)
- Fonte, período e data de recebimento:
- Receita e CVR por cluster:
- Estoque das peças candidatas:
- (Indisponível: "dado indisponível via [ferramenta]" + o que foi pedido ao time.)

## Desempenho do que está no ar (Search Console / Position Tracking)
- Fonte e data:
- Keywords que entraram na faixa 11–30 no período → fila de colheita do S3:
- Posição das KWs alvo dos ciclos anteriores:

## Mercado (Semrush / Keyword Planner)
- Fonte, base e data:
- Números novos ou recoletas:

## Leitura
- O que as três fontes, juntas, dizem sobre onde publicar agora.
```

---

## 01-selecao.md

```markdown
# Ciclo NN — Seleção

- Data: AAAA-MM-DD

## Escolhido
- Cluster e posição na fila da F3 (`analysis/12-priorizacao.md`):
- O calendário sazonal autoriza publicar agora? (índice de tendência, pico)
- URL dona declarada e sem canibalização aberta? (sim/não)
- Produto em catálogo com estoque? (SKUs, fator de catálogo)

## O número que sustenta a escolha
- (prioridade, volume, KD, CVR, receita — fonte e data de cada um)

## Descartados neste ciclo e por quê

## Onda 0 em paralelo
- Itens de higiene em execução e responsável

## Pautas geradas
- `pautas/AAAA-MM-DD-<slug>.md`
```

---

## 02-medicao.md

```markdown
# Ciclo NN — Medição

- D+30: AAAA-MM-DD · D+60: AAAA-MM-DD

| Métrica | Partida | D+30 | D+60 |
|---|---|---|---|
| Receita orgânica do cluster | | | |
| Posição — KW primária | | | |
| Posição — KWs secundárias | | | |
| Sessões orgânicas na URL | | | |
| Featured snippet / citação em IA | | | |

## Realimentação
- CVR medida que substitui o fator neutro de 1,00 na F3:
- Recalibração de KD → posição:
- Keywords novas na faixa 11–30 → colheita do próximo ciclo:
- Pautas podadas (sem movimento em 90 dias):
```
