# Ciclo 01 — Seleção

- Data: 2026-08-10

## Escolhido

**Conteúdo: rash guard / camiseta UV** — `pautas/2026-08-10-rash-guard.md`

| Filtro | Resposta |
|---|---|
| Posição na fila da F3 | 1º, prioridade 585 |
| Calendário sazonal autoriza publicar agora? | Sim. Índice entre 0,44 e 1,00 o ano inteiro — único cluster relevante sem vale sazonal |
| URL dona sem canibalização aberta? | Parcial. `/masculino/lycra-surf/` é dona de "lycra surf"; "rash guard" não tem dona. Definir com o time se estende a categoria ou vira URL própria |
| Produto com estoque? | 26 SKUs, o maior sortimento do catálogo — fator de catálogo 1,0 |

**Onda 0, em paralelo** — `pautas/2026-08-10-onda-0-higiene.md`, executada
pelo time de desenvolvimento e operação. Não compete por recurso de redação,
então não disputa lugar na fila: roda junto.

## O número que sustenta a escolha

| Fator | Número | Fonte |
|---|---|---|
| KW primária | rash guard — 18.100/mês, KD 10 | Semrush BR, 2026-08-09 |
| Melhor par volume/dificuldade | da base inteira de 860 keywords | `analysis/11-matriz-kws.md` |
| Sortimento | 26 SKUs, o maior do catálogo | `analysis/10-catalogo.md` |
| Lacuna de vocabulário | os dois textos de lycra publicados nunca usam o termo "rash guard" | `content/*-lycra-surf.html` |
| Sazonalidade | 0,44 a 1,00 o ano todo, contra 0,10 a 0,16 do resto em agosto | `analysis/12-priorizacao.md` |

## Descartados neste ciclo e por quê

- **Saída de praia** (fila nº 2, prioridade 365): publicar até setembro para
  chegar ranqueado no pico de fevereiro. Entra no ciclo 02. Pauta já aberta
  em `pautas/2026-08-10-saida-de-praia.md`.
- **Sunga masculina** (nº 3, prioridade 327): mesma janela, setembro. Pauta
  já aberta.
- **Neoprene** (nº 7): único cluster no pico agora, em agosto. Conteúdo
  orgânico publicado hoje ranqueia em janeiro, quando long john cai para
  0,29. É território de mídia paga agora e de orgânico em março — o que
  valida a linha neoprene como campanha inaugural no repositório `search-mkt`.
- **Maiô** (nº 5): converte a 0,9%. Mandar mais tráfego antes de corrigir a
  conversão amplifica o vazamento. Volta quando a CVR for corrigida.

## Bloqueios que precisam de resposta do time

Herdados da estratégia mestre, seção 7, mais o que este ciclo acrescenta:

1. "sunkini" (1.600 buscas/mês) é termo genérico de categoria ou nome de
   outra marca? Trava H1 da Onda 0.
2. O CMS permite `noindex` na busca interna e canonical em variação de
   produto? Trava H4 e o S1 inteiro.
3. Existe categoria infantil no catálogo? O mapa de URLs não achou nenhuma, e
   "poncho toalha infantil" tem 590 buscas/mês. Trava H3.
4. Qual o slug correto da categoria feminina de poncho, hoje
   `/feminino/poncho1/`? Trava H2 — que agora envolve **três** URLs, não
   duas: a terceira é `/roupas-e-acessorios/linha-surf/poncho/`.
5. **Novo (H6)**: `conjunto-atoalhado` também responde por duas trilhas.
   Mesma natureza de H2.
6. "rash guard" estende `/masculino/lycra-surf/` ou vira URL própria?
   Trava a produção deste ciclo.
7. Quem publica no CMS e em quanto tempo um texto entra no ar? Define se a
   cadência é de duas peças por ciclo ou de uma.

## Pautas do ciclo

- `pautas/2026-08-10-rash-guard.md` — produção
- `pautas/2026-08-10-onda-0-higiene.md` — higiene técnica, em paralelo

## Produção entregue

- `content/rash-guard.html` — versão completa, com `BreadcrumbList` e
  `FAQPage`
- `content/rash-guard-editor.html` — versão editor-safe, sem `<script>` e sem
  `<h1>`, para colar no editor da Nuvemshop

O bloqueio nº 1 da pauta ("sem ficha técnica, a página vira genérica") **caiu**:
`data/2026-08-10-ficha-tecnica-26-skus.csv` traz descrição completa de quatro
peças do cluster, cobrindo os três recortes de gênero que a pauta pedia.

Atributos usados no texto, todos dessa base:

| Atributo | Valor | SKU |
|---|---|---|
| Composição | 88% poliamida, 12% elastano | Pipeline, Itamambuca, manga curta masculina |
| Proteção | UV50+ permanente, bloqueia até 98% dos raios UV | as quatro peças |
| Manga longa masculina | R$ 299,99, gola anatômica, costuras fora das áreas de atrito | Pipeline |
| Manga curta masculina | R$ 299,00 | SKU "Backdoor" |
| Feminina manga longa | R$ 299,00, punho com abertura para o polegar, recortes ergonômicos | Itamambuca |
| Infantil | R$ 149,00, tamanhos P/M/G, azul claro, azul turquesa e rosa | UV Infantil Neon |
| Maiô UV50+ (link interno) | resiste ao cloro e à água salgada | Storm |

Preços coletados em 2026-08-10 e marcados com a data no texto, pela regra 7 de
`<regras_de_dados>`.

### Decisões tomadas na produção

1. **URL própria `/rash-guard/`, e não extensão de `/masculino/lycra-surf/`.**
   O conteúdo cobre masculino, feminino e infantil com um H3 cada; pendurar um
   hub de gênero neutro dentro da árvore masculina contradiz a própria
   estrutura. **É premissa, não decisão fechada** — depende da resposta do
   time (bloqueio nº 6). Se o time preferir estender a página masculina, mudam
   a canônica, o H1 e o breadcrumb, e os blocos feminino e infantil saem para
   as categorias correspondentes.
2. **Anticanibalização respeitada.** O texto não disputa "lycra surf", "lycra
   surf masculina", "lycra surf feminina" nem "camiseta lycra surf": esses
   termos aparecem só como âncora de link apontando para as páginas donas. A
   página é dona de "rash guard" e da família "uv".
3. **Seção de lavagem e conservação escrita a partir da composição do tecido**
   (poliamida com elastano), porque a base não traz instrução de cuidado.
   **Validar contra a etiqueta antes de publicar.**

### Achado para o time

O SKU **"CAMISETA BACKDOOR"** tem descrição de produto intitulada "Camiseta
Lycra Masculina Manga Curta **Maresias**". Nome de SKU e nome na descrição não
batem. O texto se refere à peça como "manga curta masculina", sem nome de
coleção, até o time resolver. Vale checar se a divergência também está na
página do produto no site.
