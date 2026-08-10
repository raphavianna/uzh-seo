# Ciclo editorial — o sistema de produção de conteúdo

- **Data**: 2026-08-10
- **Base**: `analysis/01-oportunidades.md`, `analysis/02-editorias.md`.

O projeto deixa de ser uma sequência de fases que termina e passa a ser um
ciclo que roda. As fases 0 a 2 (territórios, oportunidades, editorias)
continuam existindo como fundação e são revisadas por dado, não repetidas do
zero. O que roda toda quinzena é o ciclo abaixo.

**Objetivo do ciclo, sem eufemismo**: cada peça publicada precisa capturar
uma intenção de busca declarada e levar a uma página que vende. Conteúdo que
não tem destino de conversão não entra no ciclo.

## Cadência

Ciclo de **duas semanas**, duas peças por ciclo (uma de fundo, uma de
autoridade — regra de mistura em `02-editorias.md`). Um ciclo por vez; não se
abre o seguinte com o anterior sem publicar.

## As cinco etapas

### 1. Sinal (dia 1)

Ler os dados antes de decidir o que escrever. Três fontes, nesta ordem de
autoridade:

| Fonte | O que responde | Vence quando |
|---|---|---|
| Nuvemshop (MCP / `data/exports`) | O que a loja de fato vende, com que margem, o que tem estoque | Sempre, para o que já aconteceu na loja |
| Search Console + posições | O que já traz visita e onde estamos ranqueando | Sempre, para desempenho do que está no ar |
| Semrush / Planejador de KW | Tamanho do mercado, dificuldade, cauda, perguntas | Sempre, para mercado e concorrência |

Regra dura: **não escrever para um produto sem estoque nem para uma
categoria que a loja não pretende sustentar.** É a checagem que a Nuvemshop
existe para responder, e é o que separa esse ciclo de um calendário
editorial genérico.

### 2. Seleção (dia 2)

Escolher a categoria ou o produto do ciclo, cruzando: cluster priorizado em
`01-oportunidades.md` × venda e estoque reais × existência da página de
destino. A escolha é registrada com o número que a sustenta — nunca "porque
faz sentido".

Se a página de destino não existir, o entregável do ciclo passa a ser o
pedido de criação da página, e a produção de texto vai para o ciclo seguinte.

### 3. Keyword e pauta (dia 3)

Pesquisa do cluster escolhido: KW primária, secundárias, cauda, perguntas
reais para o bloco de FAQ. Anticanibalização declarada — quais termos
pertencem a esta página e quais já pertencem a outra página publicada.

Saída: um arquivo em `pautas/`, no padrão já usado em
`pautas/2026-08-08-lycra-surf-feminina.md`. A pauta é o contrato: se algo não
está nela, não entra no texto.

**Portão**: pauta sem KW primária com volume medido não passa. Vale a regra 3
de `<ferramentas_de_dados>` — se o dado não existe, escreve-se "dado
indisponível via [ferramenta]" e a pauta só avança com julgamento
qualitativo declarado como tal e aprovado pelo time.

### 4. Produção (dias 4 a 7)

MODO CRIAÇÃO, ou MODO REVISÃO quando o time mandar esqueleto. Padrão de
`<padrao_de_conteudo_html>` e camada AEO de `<aeo_geo>` obrigatórios. Skill
**stop-slop** aplicada antes de entregar, nos dois modos.

Saída: HTML em `content/`, mais a versão editor-safe quando o editor da
Nuvemshop não aceitar `<script>` no corpo — a experiência do ciclo anterior
mostrou que essa versão é necessária, não opcional.

### 5. Publicação e amarração (dia 8)

Publicar no editor da Nuvemshop e fechar os links: da peça nova para a
categoria e o produto, e das peças irmãs já publicadas para a nova. Conteúdo
publicado sem link interno de entrada não recebe autoridade e demora o dobro
para indexar.

Checagem final antes de publicar: URL canônica correta (ver item técnico em
`01-oportunidades.md`), title e meta description dentro do limite, schema
válido, imagens com `alt`.

### 6. Medição (D+30 e D+60, fora do ciclo corrente)

Indexação, posição das KWs primária e secundárias, sessões orgânicas na URL,
e — o número que decide — pedidos atribuídos ao caminho orgânico daquela
categoria, pela Nuvemshop.

Saída: arquivo em `reports/`, e o efeito prático: reordenar
`pautas/00-backlog.md`. Cluster que sobe vira expansão de cauda; cluster
parado após três ciclos cai de prioridade conforme o critério de revisão da
Fase 1.

## Artefatos por ciclo

Um diretório por ciclo em `ciclos/`, nomeado `ciclo-NN-AAAA-MM`:

```
ciclos/ciclo-01-2026-08/
  00-sinal.md        # o que os dados disseram (fontes e datas)
  01-selecao.md      # produto/categoria escolhidos + o número que sustenta
  02-medicao.md      # preenchido em D+30 e D+60
```

Pautas continuam em `pautas/`, conteúdo em `content/`, snapshots de dados em
`reports/`. O diretório do ciclo guarda a decisão e o rastro, não o material.

## Papéis das fontes quando alguma está fora do ar

Nenhuma etapa trava por indisponibilidade de ferramenta; cada uma tem um
caminho degradado declarado.

| Fonte fora | Efeito | Caminho degradado |
|---|---|---|
| Semrush sem unidades | Sem volume/KD novos | Trabalhar sobre clusters já medidos em `reports/`; ou usar export do Planejador de Palavras-chave arquivado em `data/` |
| MCP Nuvemshop desconectado | Sem venda/estoque | Pedir ao time a lista de categorias sustentadas e o estoque das peças candidatas, e registrar a resposta no `00-sinal.md` do ciclo |
| Acesso ao site bloqueado | Sem leitura direta de página | Leitura indireta por busca com `site:`, declarada como tal |

O que **não** é caminho degradado: estimar número de memória. Isso continua
proibido pela regra 1 de `<ferramentas_de_dados>`.

## Primeiro ciclo

Está definido em `pautas/00-backlog.md` e começa por publicar o que já está
pronto — os dois textos de lycra parados em `content/` desde 2026-08-08. Sem
isso não há o que medir, e um ciclo sem medição é um calendário, não um
sistema.
