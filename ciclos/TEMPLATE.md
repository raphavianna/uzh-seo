# Template de ciclo

Copie este arquivo para `ciclos/ciclo-NN-AAAA-MM/` como três arquivos
(`00-sinal.md`, `01-selecao.md`, `02-medicao.md`). O ciclo completo está
descrito em `analysis/03-ciclo-editorial.md`.

---

## 00-sinal.md

```markdown
# Ciclo NN — Sinal

- Data: AAAA-MM-DD

## Nuvemshop (venda e estoque)
- Fonte: MCP `nuvemshop_query` / `data/exports` — data do sync:
- Categorias com mais receita no período:
- Estoque das peças candidatas:
- (Se indisponível: "dado indisponível via Nuvemshop" + resposta do time.)

## Desempenho do que está no ar
- Fonte / data:
- URLs com sessões orgânicas:
- Posições das KWs já trabalhadas:

## Mercado (Semrush / Planejador de KW)
- Fonte, base e data:
- Números novos:

## Leitura
- O que os três blocos, juntos, dizem sobre onde escrever agora.
```

---

## 01-selecao.md

```markdown
# Ciclo NN — Seleção

- Data: AAAA-MM-DD

## Escolhido
- Categoria/produto:
- Cluster (de `analysis/01-oportunidades.md`):
- Editoria (de `analysis/02-editorias.md`):
- Página de destino (URL canônica confirmada? sim/não):

## O número que sustenta a escolha
- (volume, KD, venda, estoque — com fonte e data de cada um)

## Descartados neste ciclo e por quê

## Pautas geradas
- `pautas/AAAA-MM-DD-<slug>.md`
```

---

## 02-medicao.md

```markdown
# Ciclo NN — Medição

- D+30: AAAA-MM-DD
- D+60: AAAA-MM-DD

| Métrica | D+30 | D+60 |
|---|---|---|
| Indexada (sim/não) | | |
| Posição — KW primária | | |
| Posição — KWs secundárias | | |
| Sessões orgânicas na URL | | |
| Pedidos atribuídos (Nuvemshop) | | |

## Decisão
- Expandir cauda / manter / despriorizar cluster — e o que muda em
  `pautas/00-backlog.md`.
```
