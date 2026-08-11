# E4 — Revisão do lote T1 de agosto

- **Data**: 2026-08-11
- **Etapa**: E4, revisão e aprovação (`producao/prompts/01-etapas.md`)
- **Lote**: T1-01, T1-03, T1-04 e T1-05. T1-02 bloqueado em E2.
- **Painel de aprovação**: https://claude.ai/code/artifact/8acece86-8ca3-40d6-9818-ff1db3840bb7
- **Estado na grade**: os quatro passaram de `rascunho` para `em_revisao`.
  A decisão de aprovar é do usuário, conforme a tabela "quem aprova" em
  `producao/00-workflow.md`.

## Item 1 — Checklist por artigo

`producao/qa/checklist.md` rodado nos quatro. Nenhuma falha.

| Artigo | Itens OK | Title | Meta | FAQ | Links |
|---|---:|---|---|---:|---|
| T1-01 `blusa-com-protecao-uv` | 42/42 | 52/60 | 140/155 | 6 | 1 post, 4 produto |
| T1-03 `camisa-de-praia-feminina` | 43/43 | 55/60 | 130/155 | 6 | 2 post, 3 produto |
| T1-04 `camiseta-com-protecao-uv` | 42/42 | 55/60 | 131/155 | 6 | 1 post, 3 produto |
| T1-05 `rash-guard-infantil` | 42/42 | 50/60 | 132/155 | 6 | 1 post, 2 produto |

Verificado em cada um: `<h1>` único com a primária, hierarquia de headings sem
salto, primeiro parágrafo autocontido em até três frases, JSON-LD de
`BlogPosting`, `BreadcrumbList` e `FAQPage` válido, toda secundária presente no
corpo, versão editor-safe sem `<script>`, sem `<h1>` e sem breadcrumb, sem
travessão, sem contraste "não é X, é Y" e sem advérbio de muleta.

## Item 2 — Passada de canibalização do lote

É a única etapa que olha as quatro peças como conjunto.

| Checagem | Resultado |
|---|---|
| Keyword com dois donos no registro | Nenhuma. 50 linhas, sem duplicata. |
| Primária de um artigo no `h1` ou `title` de outro | Nenhuma. |
| Duas peças disputando a mesma intenção | Nenhum dos 6 pares. |
| Termo com dono anterior usado como alvo | 3 marcações, todas artefato de substring |

**Matriz de pares**, por eixo e intenção:

| | T1-01 mecanismo | T1-03 feminino | T1-04 uso | T1-05 infantil |
|---|---|---|---|---|
| T1-01 | — | distintos | distintos | distintos |
| T1-03 | — | — | distintos | distintos |
| T1-04 | — | — | — | distintos |

**As 3 marcações do último item, verificadas uma a uma:**

| Artigo | Termo curto | Onde | Keyword própria que o contém | Veredito |
|---|---|---|---|---|
| T1-04 | `camiseta uv` (3.600, de `/rash-guard/`) | h2 | `camiseta uv 50 masculina` | artefato |
| T1-05 | `rash guard` (18.100, de `/rash-guard/`) | h1 | `rash guard infantil` | artefato |
| T1-05 | `camiseta uv` (3.600, de `/rash-guard/`) | h2 | `camiseta uv para criança` | artefato |

Nos três, o termo curto aparece só dentro de uma keyword mais longa que o
próprio artigo possui. Não dá para escrever "rash guard infantil" sem escrever
"rash guard". O modificador específico diferencia a intenção, e nenhum dos três
h2 tem o termo curto como alvo isolado. **Canibalização real: zero.**

## Cobertura do lote

| Artigo | KWs | Volume/mês | Com PAA | Com FS |
|---|---:|---:|---:|---:|
| T1-01 | 8 | 2.480 | 6 | 0 |
| T1-03 | 9 | 2.160 | 5 | 0 |
| T1-04 | 8 | 1.970 | 6 | 0 |
| T1-05 | 9 | 1.420 | 2 | 0 |
| **Total** | **34** | **8.030** | **19** | **0** |

Fonte: `data/2026-08-10-matriz-kws-classificada.csv` (Semrush BR, coleta de
2026-08-09), cruzada com `producao/registro/kw-donos.csv`.

## Dependência de ordem, criada pelo formato de URL

O blog monta a URL como `/blog/posts/<slug>-<hash>` e o hash nasce na
publicação. T1-03, T1-04 e T1-05 linkam para T1-01, então **T1-01 sobe
primeiro**, obrigatoriamente. São 28 marcadores `{HASH}` nos quatro arquivos, e
canonical publicado com o marcador sem substituir quebra a indexação.

## Pendências antes de E5

| Pendência | Trava publicação |
|---|---|
| Substituir os 28 `{HASH}` pelas URLs reais | **Sim** |
| Slug do CMS igual ao nome do arquivo em `content/` | **Sim** |
| Fator de proteção do MAIO CEPILHO INFANTIL (R$ 299,00) | Não, mas é lacuna de catálogo |
| Fichas idênticas de MAIO BELLS e MAIO MOANA | Não |
| Conflito CAMISETA BACKDOOR / "Maresias" | Não |
| Natureza de `/masculino/lycra-surf/`, `/rash-guard/` e `/feminino/maio/` | Não, mas muda o destino dos CTAs |
| 9 imagens (`midia-produtos` vazio) | Não |
| `classificacao-kws.py` sem detecção de permutação | Não, afeta a grade de setembro |

## Gate de E4

O gate pede decisão registrada por artigo. **Ainda aberto**: os quatro estão em
`em_revisao` aguardando aprovação do usuário. Lote com artigo pendente não
avança para E5.
