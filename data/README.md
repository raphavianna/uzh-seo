# `data/` — bases exportadas pelo time

Arquivos que o agente não consegue coletar sozinho e que o time exporta e sobe
aqui. Cada arquivo entra com **nome datado** e a proveniência registrada em um
resumo de leitura em `reports/`.

Convenção de nome: `AAAA-MM-DD-<origem>-<assunto>.<ext>`
Exemplo: `2026-08-15-nuvemshop-catalogo.csv`

## Por que estas bases não são coletadas automaticamente

Verificado em 2026-08-10 nesta sessão:

- Não existe conector de **BaseLinker** nem de **Nuvemshop** disponível.
- Não existe conector de **Google Ads Keyword Planner**.
- O acesso a **usezerohora.com.br** está bloqueado pela política de egress, o
  que impede ler o catálogo pelo próprio site.

## O que exportar

### 1. Catálogo — Nuvemshop

Uma linha por SKU. Colunas mínimas:

```
sku | nome_do_produto | url | categoria | subcategoria | preco | preco_promocional
descricao | atributos (material, gramatura, protecao_uv, tamanhos, cores)
estoque | status (ativo/inativo) | data_de_criacao
```

Serve para: mapear cada SKU a um cluster de keyword, extrair os atributos reais
que o conteúdo pode afirmar, e descobrir produtos sem página otimizada.

### 2. Vendas por SKU — BaseLinker

Uma linha por SKU por período. Colunas mínimas:

```
sku | canal | periodo (mes/ano) | unidades_vendidas | receita | ticket_medio
devolucoes | margem (se disponivel)
```

Serve para: montar a curva ABC. Keyword que aponta para SKU classe A vale mais
que keyword de volume maior apontando para SKU classe C, porque o objetivo do
projeto é venda, não visita.

### 3. Ideias de keyword — Google Ads Keyword Planner

Export do *Descobrir novas palavras-chave*, semeado pelas URLs de categoria e
pelas URLs de produto. Colunas mínimas:

```
palavra_chave | media_de_pesquisas_mensais | concorrencia
lance_topo_pagina_min | lance_topo_pagina_max | sazonalidade_mensal
```

Serve para: volume e CPC. Na regra de conflito do `CLAUDE.md`, o Keyword
Planner vence o Semrush nestas duas colunas.

### 4. Consultas — Google Search Console

Export de *Desempenho → Consultas*, últimos 16 meses, e de *Desempenho →
Páginas*. Colunas mínimas:

```
consulta | pagina | cliques | impressoes | ctr | posicao_media
```

Serve para: é a única fonte de clique e impressão reais. Vence estimativa de
ferramenta para tudo que o site já ranqueia, e revela as keywords com muita
impressão e pouco clique, que são problema de title e não de posição.

### 5. Semrush em lote

Os CSVs de *Keyword Overview → Bulk Analysis*, base **BR**, rodados sobre os
lotes de `2026-08-10-seed-kws-para-semrush.md`, mais o export de *Keyword Gap*
contra os cinco concorrentes do benchmark.

## Ordem de prioridade

Se der para subir só duas bases agora, suba o **catálogo do Nuvemshop** e as
**consultas do Search Console**. As duas juntas destravam a matriz de keywords
sem depender de crédito de ferramenta.
