# Ciclo operacional de conteúdo

- **Data**: 2026-08-10
- **Entradas**: `analysis/estrategia-seo-mestre.md` (blocos S0–S9),
  `analysis/12-priorizacao.md` (fila, ondas e calendário sazonal)
- **O que este documento acrescenta**: o ritmo. A estratégia diz *o que* fazer
  e em que ordem; a F6 diz que há realimentação mensal. Faltava definir o
  ciclo que executa isso toda vez, sem depender de alguém lembrar.

## O princípio

A fila da F3 é ordenada por prioridade; o **calendário sazonal manda na ordem
de publicação**. As duas coisas divergem de propósito, e é isso que o ciclo
precisa reconciliar todo mês. Publicar poncho em agosto, quando o índice de
tendência está em 0,10, entrega ranqueamento em novembro, antes do pico de
março — certo. Publicar neoprene agora, no pico, entrega ranqueamento em
janeiro, quando a demanda já caiu — errado, e por isso neoprene é território
de mídia paga agora e de orgânico em março.

Um ciclo que só olha a fila publica na hora errada. Um ciclo que só olha o
calendário publica o item de menor retorno. O ciclo abaixo olha os dois.

## Cadência

**Ciclo mensal**, fechando na F6. Dentro dele, quatro semanas com função
distinta. A cadência de produção é de **duas peças por ciclo**, número
derivado do que a fila comporta sem estourar a redação — a F3 já registra que
as pautas de biquíni, maiô, poncho e neoprene só abrem quando as quatro
primeiras estiverem em produção.

Se o prazo real de publicação no CMS (pendência do S0) for maior que duas
semanas, a cadência cai para uma peça por ciclo. Backlog grande com CMS lento
produz artefato parado no repositório, não posição.

## As quatro semanas

### Semana 1 — Sinal e seleção

Ler antes de decidir. Três fontes, na ordem de precedência já fixada nas
regras de dados:

| Fonte | O que responde |
|---|---|
| Nuvemshop / BaseLinker | O que vendeu, com que CVR, o que tem estoque |
| Search Console + Position Tracking | O que já traz impressão e clique, e o que entrou na faixa 11–30 |
| Semrush / Keyword Planner | Tamanho do mercado, KD, intenção, perguntas reais |

Saída: `ciclos/ciclo-NN-AAAA-MM/00-sinal.md` e `01-selecao.md`. A seleção
cruza três filtros, e **os três precisam passar**:

1. Está na fila da F3 e o calendário diz que é hora de publicar.
2. Tem produto no catálogo com estoque — fator de catálogo maior que zero.
   Cluster sem produto sai da fila por mais busca que tenha; foi assim que
   canga (15.580 buscas/mês) ficou de fora.
3. Tem URL dona declarada e sem canibalização aberta. Se a canibalização
   existe, o item vira Onda 0 e a produção espera.

### Semana 2 — Pauta

Pesquisa do cluster e escrita da pauta em `pautas/`, no padrão dos arquivos
de 2026-08-10: KW primária, secundárias, cauda, anticanibalização declarada,
intenção, funil, formato, caminho até a conversão.

**Portão**: pauta sem KW primária com volume medido não passa. Se a coleta
não está disponível, vale a regra 3 — "dado indisponível via [ferramenta]",
motivo, e julgamento qualitativo declarado, aprovado pelo time antes de virar
produção.

### Semana 3 — Produção

MODO CRIAÇÃO, ou MODO REVISÃO quando o time mandar esqueleto. Padrão de
`<padrao_de_conteudo_html>` e camada AEO obrigatória — não é etapa posterior,
entra junto: resposta autocontida na abertura de cada seção, FAQ com
`FAQPage`, dado concreto e verificável, definição explícita dos termos do
nicho.

Saída: HTML em `content/`, mais a **versão editor-safe** sem `<script>` no
corpo. Não é opcional: o editor da Nuvemshop rejeitou o schema inline no
ciclo anterior, e é por isso que `content/` já tem os pares
`*-editor.html`.

### Semana 4 — Publicação, amarração e abertura da medição

Publicar, e então fechar os links: da peça nova para a categoria comercial do
cluster (o hub), das peças irmãs já publicadas para a nova, e da categoria de
volta para os produtos. Conteúdo publicado sem link interno de entrada demora
o dobro para indexar e não recebe autoridade.

Registrar a data de publicação e a posição de partida das KWs alvo. Sem esse
registro, a medição de D+30 não tem contra o que comparar.

## Medição — fora do ciclo corrente

D+30 e D+60 sobre cada peça publicada, consolidados no relatório mensal da
F6 (`reports/YYYY-MM-medicao.md`). Quatro números, nesta ordem:

1. Receita orgânica atribuída às páginas do cluster — abre o relatório,
   sempre. Ranking sem transação é sinal de intenção mal escolhida.
2. Posição das KWs primária e secundárias.
3. Sessões orgânicas na URL.
4. Featured snippet ou citação em motor de resposta capturada.

**O que a medição realimenta**, mecanicamente:

- Substitui os fatores de conversão neutros de 1,00 da F3 pela CVR medida. Os
  clusters de verão só têm CVR real depois de dezembro; até lá a fila carrega
  essa imprecisão declarada.
- Recalibra a associação KD → posição, que hoje é julgamento e é o elo mais
  frágil do cálculo de prioridade.
- Reabre o S3: as keywords que entraram na faixa 11–30 no período viram a
  fila de colheita do ciclo seguinte, que rende mais que conteúdo novo por
  custar esforço 1 ou 2 em vez de 4.
- Poda: pauta que não moveu posição em 90 dias sai da fila ou é reescrita com
  outro ângulo.

## Artefatos por ciclo

```
ciclos/ciclo-NN-AAAA-MM/
  00-sinal.md      # o que as três fontes disseram, com data
  01-selecao.md    # o que foi escolhido e o número que sustenta
  02-medicao.md    # D+30 e D+60, e o que muda na fila
```

Pautas em `pautas/`, conteúdo em `content/`, snapshots em `reports/`, bases
recebidas em `data/`. O diretório do ciclo guarda a decisão e o rastro, não o
material.

## Quando uma fonte está fora do ar

Nenhuma semana trava por indisponibilidade de ferramenta. O caminho degradado
é declarado, e nunca inclui estimar número de memória.

| Fonte fora | Caminho degradado |
|---|---|
| Semrush sem unidades | Trabalhar sobre a matriz já coletada em `data/2026-08-10-matriz-kws-classificada.csv` e sobre o Search Console, que é medição própria e vence estimativa |
| MCP Nuvemshop desconectado | Pedir ao time o export da semana e arquivar em `data/`, com proveniência, como já foi feito em 2026-08-09 |
| Acesso ao site bloqueado | Leitura indireta por busca com `site:`, declarada como qualitativa |
| CMS lento | Cadência cai para uma peça por ciclo; a fila não cresce |

## Estado de partida

O ciclo 01 está em `ciclos/ciclo-01-2026-08/`. Ele não abre pela produção:
abre pela Onda 0, porque cinco itens de higiene devolvem posição sem escrever
uma linha e o gargalo deles é outro time — rodam em paralelo à primeira
pauta, não na frente dela na fila de redação.
