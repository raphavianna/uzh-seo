# Workflow de produção em escala

- **Data**: 2026-08-11
- **Escopo**: criação, aprovação e publicação de posts no blog da Nuvemshop
- **Cadência**: 1 artigo por território por dia · 3 territórios · lote mensal
  produzido de uma vez, publicação agendada dia a dia
- **Estado**: manual nas etapas E1 a E4; E5 automatizável assim que as duas
  travas da Blog API caírem (ver E5)

## Os três territórios

Cada território produz um artigo por dia e tem um cluster fechado. Rodam em
paralelo, não em sequência.

| ID | Território | Cluster da F2 | KWs livres | Ciclo de origem |
|---|---|---|---:|---|
| **T1** | Lycra, camiseta UV e rash guard | Lycra/UV/rash | 57 | 01 (ago) |
| **T2** | Saída de praia, resort e **vestidos** | Saída de praia | 42 + a coletar | 02 (set) |
| **T3** | Biquíni e top | Biquíni e top | 35 | 03 (out) |

"KWs livres" = no escopo, sem variante gráfica, sem dono declarado em
`registro/kw-donos.csv`. São 134 alvos distintos nos três territórios.

### T2 tem dois sub-bunches

**Saída de praia** é a categoria mãe, com `saída de praia` (60.500) como hub.

**Vestidos** entra como sub-bunch filho, decidido em 2026-08-11. A matriz atual
só tem 5 termos com "vestido", somando 3.690 buscas/mês, porque as variações de
uso nunca entraram na coleta. O seed do lote está em
`data/2026-08-11-seed-kws-vestidos.md`, com 78 keywords a coletar.

**Recorte obrigatório**: o sub-bunch cobre vestido **qualificado por contexto de
uso** — praia, verão, resort, piscina, mar, saída de praia — ou por material
típico da categoria. Fica fora vestido de moda ampla, mesmo com volume alto:
vestido, vestido longo, vestido de festa, vestido social, vestido de noiva.
Quem busca esses termos quer festa ou trabalho, e a marca não tem produto nem
autoridade nessa disputa. Esta regra vale para todos os lotes de T2, não só
para o primeiro.

Zona cinzenta — "vestido de verão", "vestido leve", "vestido soltinho",
"vestido fluido" — só sobe depois de leitura de SERP: se a SERP brasileira
trouxer lojas de moda praia, entra; se trouxer fast fashion, fica fora com o
motivo registrado.

**Regra de comprimento**: o vestido da marca é longo. O
`VESTIDO RESORT ALÇA CRUZADA` declara "Comprimento: Longo" na ficha técnica,
com 96% viscose e 4% elastano, bolsos laterais, sem transparência, R$ 199,00 em
10/08/2026. Por isso `vestido de praia curto` (320, KD 12) **sai da fila como
alvo de página**: cluster sem produto tem fator de catálogo zero, e prometer
curto para entregar longo gera visita que não compra e devolução quando compra.
A comparação "curto ou longo" vira seção dentro do hub, e a demanda de
comprimento curto tem outro destino no catálogo — a saia curta de saída de
praia. Termos com "longo" sobem no desempate mesmo com volume menor, porque
casam com o produto.

Arquitetura: `vestido de praia` (2.900, KD 14) é o hub do sub-bunch e já está
na grade-piloto como T2-03. Os spokes de comprimento, material, ocasião e
público linkam para ele, e ele linka para a categoria de saída de praia. Sem
essa hierarquia, o sub-bunch canibaliza a própria categoria mãe.

## A regra que sustenta a escala

**Volume manda na ordem. KD é tolerado.** Decisão do usuário em 2026-08-11: a
fila de cada território é ordenada por volume decrescente, e a dificuldade só
desempata. O que a escala compra é cobertura; o que ela arrisca é
canibalização.

Por isso existe um gate duro: **`registro/kw-donos.csv` é a autoridade sobre
quem é dono de qual keyword.** Nenhum artigo entra em produção com uma KW
primária já registrada. Sem esse registro, 90 artigos por mês se anulam entre
si, e o site já sofre disso — o poncho hoje briga em três URLs.

O inventário justifica o rigor:

| Corte de volume | KWs disponíveis |
|---|---:|
| ≥ 1.000 | 75 |
| ≥ 500 | 128 |
| ≥ 300 | 174 |
| ≥ 100 | 321 |
| ≥ 50 | 392 |

A 90 artigos/mês, os alvos com volume ≥300 duram menos de dois meses. A partir
daí a produção entra na cauda longa como spoke apontando para o hub do
território, e não como página nova disputando a mesma intenção.

## As cinco etapas

Cada etapa consome um artefato aprovado da anterior e produz o insumo da
seguinte. Etapa sem artefato âncora não roda.

| Etapa | Entrada (âncora) | Saída | Gate |
|---|---|---|---|
| **E1 — Pesquisa e grade** | matriz de KWs + refresh do mês | `registro/calendario-AAAA-MM.csv` | Toda linha com KW primária de volume medido e sem dono |
| **E2 — Pauta** | linha da grade + ficha técnica do SKU | `pautas/AAAA-MM-DD-<slug>.md` | Anticanibalização declarada; KWs secundárias sem dono conflitante |
| **E3 — Redação** | pauta aprovada + imagens do `midia-produtos` | `content/<slug>.html` e `<slug>-editor.html` | Padrão de `<padrao_de_conteudo_html>` + camada AEO + stop-slop |
| **E4 — Revisão e aprovação** | lote de artigos escritos | painel de aprovação + status na grade | Aprovação registrada por artigo, com data |
| **E5 — Publicação** | artigo aprovado + data agendada | post no blog + `url_final` na grade | Publicado, indexável, com link interno de entrada |

### E1 — Pesquisa e grade

Roda uma vez por mês, para o mês seguinte, mais dois refreshes:

- **Refresh mensal**: recoleta completa dos três clusters no Semrush e no
  Planejador de Palavras-chave. Gera a grade do mês seguinte.
- **Refresh diário**: varredura curta por termo emergente — variação nova,
  sazonalidade antecipada, pico de busca. Termo novo com volume acima do menor
  da grade corrente entra por substituição, não por acréscimo, e a linha
  substituída volta para a fila.

Ordenação: volume decrescente dentro de cada território. A grade nasce com
`status = rascunho` e sem `url_final`.

### E2 — Pauta

Uma pauta por linha da grade. O que ela fixa: KW primária, secundárias, cauda,
anticanibalização, intenção, ângulo, SKUs citáveis e imagens. A pauta é o
contrato — o que não está nela não entra no texto.

**Depende de ficha técnica.** Artigo sobre peça sem atributo real vira texto
genérico e não é citado por motor de resposta. A cobertura hoje é de 26 SKUs
em 120; ver `analysis/22-ficha-tecnica.md` para o que falta por cluster.

### E3 — Redação

Duas saídas por artigo, como já se faz: o HTML completo com `BreadcrumbList` e
`FAQPage`, e a versão editor-safe sem `<script>`.

Imagens vêm de `https://github.com/raphavianna/midia-produtos`. Enquanto o
mapeamento imagem → SKU não estiver definido, a redação marca o ponto de
inserção com um comentário e o artigo segue para aprovação sem a imagem.

### E4 — Revisão e aprovação

Painel de aprovação publicado como artifact, com a fila do lote, prévia de
cada artigo e status. A aprovação é registrada na coluna `status` da grade,
com data em `aprovado_em`.

Estados: `rascunho` → `em_revisao` → `aprovado` → `agendado` → `publicado`.
Um artigo reprovado volta para `rascunho` com o motivo registrado na pauta.

### E5 — Publicação

**A Blog API da Nuvemshop existe** e cobre criar, ler, atualizar e apagar
post, mais upload de imagem de conteúdo e de capa, e o endpoint que devolve o
blog ID. Base: `https://api.nuvemshop.com.br/2025-03/{store_id}`.

Duas travas antes de automatizar, ambas no repositório `integracao-nuvemshop`:

1. **Escopo.** O app hoje tem `read_content`. A Blog API exige permissão de
   editar conteúdo (`write_content`). A Nuvemshop não recebe escopo na URL de
   autorização: é preciso marcar a permissão no Painel de Parceiros e o
   lojista reautorizar o app.
2. **Recursos não implementados.** `src/resources/index.ts` cobre products,
   categories, orders, customers, coupons, checkouts, store e webhooks. Falta
   o recurso de blog e as ferramentas MCP correspondentes.

Enquanto as duas não caírem, E5 roda manual: o time cola a versão editor-safe
no admin e registra a `url_final` na grade.

## Piloto de agosto

15 artigos, 3 territórios × 5 dias de produção, publicação escalonada.

- Produção: 12, 13, 14, 17 e 18 de agosto
- Publicação: 19, 20, 21, 24 e 25 de agosto
- Volume endereçado: **107.820 buscas/mês**
- Grade: `registro/calendario-2026-08.csv`

O piloto existe para medir onde o fluxo quebra antes de escalar para 90. O
gargalo conhecido não é produção: é publicação e ficha técnica.

## O que cada etapa ancora

| Artefato | Onde vive | Quem aprova |
|---|---|---|
| Grade do mês | `producao/registro/calendario-AAAA-MM.csv` | usuário, antes de E2 |
| Registro de dono de KW | `producao/registro/kw-donos.csv` | atualizado por E2, consultado por E1 |
| Pauta | `pautas/` | usuário, antes de E3 |
| Artigo | `content/` | usuário, em E4 |
| Publicação | `url_final` na grade | confirmada em E5 |
