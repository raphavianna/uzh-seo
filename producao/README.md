# producao/ — máquina de conteúdo em escala

Produção de posts para o blog da Nuvemshop: **1 artigo por território por
dia**, três territórios, lote mensal produzido de uma vez e publicação
agendada dia a dia.

O desenho completo, com gates e artefatos âncora de cada etapa, está em
[`00-workflow.md`](00-workflow.md).

## Territórios

| ID | Território | KWs livres |
|---|---|---:|
| T1 | Lycra, camiseta UV e rash guard | 57 |
| T2 | Saída de praia e resort | 42 |
| T3 | Biquíni e top | 35 |

## Etapas

**E1** pesquisa e grade → **E2** pauta → **E3** redação → **E4** revisão e
aprovação → **E5** publicação → **E6** medição.

E1 a E4 rodam manuais hoje. E5 vira automática quando as duas travas da Blog
API caírem (escopo de editar conteúdo e o recurso de blog no
`integracao-nuvemshop`).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `prompts/` | `00-system.md`, o system prompt do agente, e `01-etapas.md`, as instruções de cada etapa |
| `templates/` | `pauta.md` e os esqueletos de artigo |
| `registro/` | `kw-donos.csv`, a autoridade sobre dono de keyword, e a grade de cada mês |
| `qa/` | `checklist.md`, rodado por artigo em E4 |

## As duas regras que sustentam a escala

**Volume manda, KD é tolerado.** A fila de cada território é ordenada por
volume decrescente; a dificuldade só desempata.

**Nenhum artigo entra em produção com KW primária já registrada.**
`registro/kw-donos.csv` é a autoridade. A 90 artigos por mês, os alvos com
volume ≥300 duram menos de dois meses — sem o registro, o lote passa a
competir consigo mesmo, que é o problema técnico que o site já tem.

## Piloto de agosto

15 artigos, 3 territórios × 5 dias, **107.820 buscas/mês endereçadas**.
Produção de 12 a 18/08, publicação de 19 a 25/08. Grade em
[`registro/calendario-2026-08.csv`](registro/calendario-2026-08.csv).

O piloto existe para achar onde o fluxo quebra antes de escalar para 90. O
gargalo conhecido não é a produção: é a publicação e a ficha técnica, que hoje
cobre 26 SKUs em 120.
