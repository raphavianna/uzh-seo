# Fase — Auditoria SEO/GEO do catálogo (via API Nuvemshop)

- **Data**: 2026-08-12
- **Escopo**: catálogo completo da loja USEZEROHORA (store_id 5540626) — 140 produtos, 902 variantes, 48 categorias, 1.686 imagens. Checks automatizados cobrem 100% do catálogo; leitura qualitativa e inspeção de imagens cobrem a amostra priorizada (top 20 por receita 12m + 5 de estoque parado).
- **Dados**: `reports/2026-08-12-auditoria-catalogo-dados.md` (sync do cache em 2026-08-12, defasagem zero). Regra de receita: `payment_status='paid' AND status<>'cancelled'`, data `COALESCE(paid_at, created_at)`, janela 2025-08-12→2026-08-12. Receita 12m: **R$ 230.977** em 1.205 pedidos.

## Sumário executivo — os 5 problemas de maior impacto em conversão

1. **1.686 de 1.686 imagens sem `alt` (100% do catálogo).** A API devolve `alt: []` em todas as imagens de todos os produtos. Google Imagens é canal gratuito de descoberta para moda praia, e motores de resposta usam alt para entender produto. Receita em risco: todo o catálogo — os 5 maiores produtos (R$ 85,9k/12m somados) inclusive. Correção em massa via API (`PUT` por imagem), esforço baixo, cobertura total.
2. **Imagens geradas por IA em produto físico — 119 imagens em 21 produtos, 16 delas como capa.** Nomes de arquivo `chatgpt-image-*` (104) e `virtual-try-on-*` (15) são evidência direta de origem; a inspeção visual da amostra (75 imagens) reforça: 56 com suspeita de geração por IA, 22 delas em confiança alta — incluindo defeitos anatômicos visíveis (dedos fundidos no MAIO STORM e no Poncho Infantil) e logos que se dissolvem. A FAQ do PONCHO RESORT PREMIUM (R$ 15,7k/12m) afirma on-page "as fotos sao reais, com um toque de IA" — contradição com o banner "FOTOS REAIS" usado nas descrições. Risco: quebra de confiança na compra (conversão) e de elegibilidade em Google Shopping/free listings, que exigem imagem fiel do produto. Produtos afetados incluem MAIO STORM (R$ 11,6k — capa IA) e a linha de maiôs body.
3. **Descrições contradizendo a ficha real do produto (alucinação de ficha técnica) na amostra de maior receita.** MAIO MOANA vendido em verde claro/marrom/verde escuro com descrição "na cor lisa preta"; CAMISETA UV INFANTIL NEON com variantes de tamanho 2–10 anos descrita como "P, M, G" e "três cores lisas" (reais: Rosa e Azul); Poncho Premium (R$ 32,7k, nº 1 em receita) diz "disponível nas cores rosa e azul" com variantes Azul/Rosa/Verde/Preto e "tamanhos únicos" numa página que vende tamanho M; texto de **outra marca ("Surfnelas")** publicado em produto Use Zero Hora. Quem chega pronto para comprar encontra informação errada — é defeito direto de conversão e de confiança de motores de resposta.
4. **29 produtos (20,7%) sem `seo_title` e sem `seo_description`; 48 de 48 categorias sem descrição.** Entre os sem meta tags estão 4 produtos do top 25 por receita (ex.: Poncho Clássico Azul Marinho, R$ 6,4k). Categorias — as páginas com maior potencial de rankear head terms ("poncho de surf", "lycra surf feminina", "maiô manga longa") — não têm uma linha de texto, e os slugs `/poncho1`, `/poncho2`, `/camiseta-uv1` desperdiçam a KW. Sem texto, nem Google nem IA têm o que citar.
5. **92 produtos (65,7%) com descrições quase duplicadas + 11 produtos publicados com estoque zero.** A família de ponchos compartilha um único texto replicado (7+ produtos idênticos na amostra), o que impede qualquer página de ganhar o cluster e cria canibalização. Os 11 publicados sem estoque são soft-404 de intenção de compra. Consolidar/despublicar e diferenciar textos é pré-condição para o restante do trabalho de conteúdo render.

## Scorecard (checks massivos = 100% do catálogo)

| Eixo | Check | % aprovação | Itens reprovados |
|---|---|--:|--:|
| A | seo_title presente | 79,3% | 29 |
| A | seo_title ≤ 60 caracteres | 71,4% | 40 |
| A | seo_title com KW do produto | 99,3% | 1 |
| A | seo_title único | 95,7% | 6 (3 grupos) |
| A | seo_description presente | 79,3% | 29 |
| A | seo_description ≤ 155 caracteres | 97,9% | 3 |
| A | seo_description única | 100% | 0 |
| A | descrição presente | 100% | 0 |
| A | descrição ≥ 300 caracteres úteis | 100% | 0 |
| A | descrição sem quase-duplicata (Jaccard ≤ 0,8) | **34,3%** | **92** |
| A | descrição com dado concreto (medida/material/UV) | 96,4% | 5 |
| A | handle com KW | 100% | 0 |
| A | imagens com alt | **0%** | **1.686** |
| A | publicado com estoque | 92,1% | 11 |
| A | categoria com descrição | **0%** | **48** |
| A | categoria não-vazia | 95,8% | 2 (Lycra/SURFNELAS, CONJUNTO) |
| C | imagem sem marcador de origem IA no arquivo | 92,9% | 119 (21 produtos; 16 capas) |

Checks qualitativos (amostra de 25 produtos): ver Eixos B e C abaixo.

## Achados — Eixo A (SEO técnico on-catalog)

Ordenados por receita 12m do produto (fonte: cache local, sync 2026-08-12).

| id | produto | check violado | evidência | severidade | receita 12m |
|---|---|---|---|---|---|
| 252094324 | Poncho Premium Adulto (M) | 22 imagens sem alt | `$.images[*].alt` = `[]` | alta | R$ 32.708 |
| 336513465 | PONCHO RESORT PREMIUM | 21 imagens sem alt | idem | alta | R$ 15.719 |
| 331295922 | PONCHO CLASSICO TODAS AS CORES | 67 imagens sem alt | idem | alta | R$ 13.214 |
| 298141305 | Poncho Clássico Adulto (P e M) | seo_title 63c; seo_description 156c; descrição duplicada | `$.seo_title.pt` = "Poncho Clássico Adulto P e M - Conforto e Praticidade Atoalhado" | média | R$ 10.719 |
| 303607414 | Poncho Clássico Azul Marinho | **sem seo_title, sem seo_description**; descrição duplicada | `$.seo_title.pt` = NULL | alta | R$ 6.420 |
| 303607422 | Poncho Clássico Azul Royal | idem | idem | alta | R$ 5.380 |
| 303607431 | Poncho Clássico Vinho | idem | idem | alta | R$ 3.030 |
| 270617865 | Camiseta Lycra Surf UV50 Verde/Preto | **sem seo_title, sem seo_description** | idem | alta | R$ 2.940 |
| 303607440 | Poncho Clássico Grafite | seo_title 68c truncando ("...Confortávei") | `$.seo_title.pt` termina em "Confortávei" | média | R$ 3.470 |
| 315738097 | Camiseta Lycra Feminina Vaca | **sem seo_title, sem seo_description**; estoque parado (105 un.) | idem | alta | R$ 0 |

Padrões de catálogo inteiro:
- **Títulos SEO duplicados (3 grupos, 6 produtos)**: "Sunga Boxer Masculina Lisa com Proteção UV50+..." (2×), "Saída de Praia Vestido Serena Canelado..." (2×), "Poncho Atoalhado Multicolorido: Conforto e Praticidade" (2×, um deles o nº 3 em receita).
- **11 publicados com estoque zero** (soft-404): inclui Conjunto Poseidon Vermelho, Maiô Vermont, Sunga Preta Lisa (lista completa no snapshot). Despublicar ou repor.
- **Slugs de categoria com sufixo numérico**: `/poncho1` (feminino), `/poncho2` (infantil), `/camiseta-uv1`, `/camiseta-uv2`, `/lycra-surf1`, `/maio1`, `/conjunto1`, `/feminino1`, `/masculino1` — a KW do segmento (ex.: "poncho feminino") não está no slug.

## Achados — Eixo B (gaps de conteúdo SEO + GEO)

**KWs com demanda registrada sem página dedicada** (fonte: `reports/2026-08-08-semrush-kws-lycra-surf.md`, Semrush BR, coleta 2026-08-08; e `reports/2026-08-08-serp-leitura-territorios.md`):

| KW | Volume (fonte/data) | Situação no catálogo |
|---|---|---|
| lycra surf | 880/mês (Semrush BR, 2026-08-08) | categorias `/lycra-surf` e `/lycra-surf1` existem, **sem descrição** e sem conteúdo citável |
| camiseta surf | 720/mês (idem) | sem página informacional; categorias sem texto |
| camiseta surf masculina | 480/mês (idem) | `/masculino/camiseta-uv` sem descrição |
| lycra surf masculina | 260/mês (idem) | pauta em produção (`content/` tem texto pendente de publicação) |
| lycra surf feminina | 170/mês (idem) | pauta registrada em `pautas/2026-08-08-lycra-surf-feminina.md`; categoria sem texto |
| poncho de surf (head do território de produto) | dado indisponível via snapshots de `reports/` — volume não coletado; SERP lida em 2026-08-08 mostra espaço informacional "quase vazio" | **não existe página única de poncho**: o cluster está fatiado em `/poncho` (masc), `/poncho1` (fem), `/poncho2` (inf), todas sem descrição |

- **Cluster informacional sem cobertura**: "o que é poncho de surf", "como escolher", "como lavar lycra surf" (perguntas reais do snapshot Semrush com fraseado de PAA) não têm nenhuma página no domínio. É o espaço que motores de resposta citam primeiro.
- **Blocos AEO ausentes**: nenhuma descrição de produto abre com resposta direta; as FAQs existem como texto solto dentro de 8 descrições da amostra (boa matéria-prima), mas sem marcação `FAQPage` verificável e com conteúdo operacional (frete/prazo), não informacional de produto.
- **Consistência de entidade (grave)**: grafias concorrentes "Use Zero Hora", "UseZeroHora", "USEZEROHORA", "UseZerohora" nos textos; produto 315738097 descreve e estampa a marca **"Surfnelas"** (outra marca); existe categoria raiz **"SURFNELAS"** (`/surfnelas`) publicada. Para desambiguar do jornal Zero Hora/GZH, a entidade precisa ser uma só: "Use Zero Hora" + surf/beachwear.
- **Validação on-page (title/JSON-LD/canonical/FAQPage renderizados)**: **dado indisponível via WebFetch e curl nesta sessão** — o proxy de rede bloqueia `usezerohora.com.br` (EGRESS_BLOCKED). Julgamento qualitativo, declarado como tal: o template Nuvemshop padrão emite `Product`+`Offer` e canonical, mas o `alt` renderizado vem do campo da API — vazio em 100% das imagens —, e nada indica marcação `FAQPage`. Validar numa sessão com acesso ao domínio ou via Rich Results Test.

## Achados — Eixo C (sinais de conteúdo de IA)

### Textos (amostra de 25 produtos, critério stop-slop + confronto com variantes)

| id | produto | classificação | sinais e evidência | confiança | receita 12m |
|---|---|---|---|---|---|
| 252094324 | Poncho Premium Adulto (M) | **forte suspeita** | "perfeito para quem busca praticidade, conforto e estilo" (regra de três); descrição afirma "cores rosa e azul" e "tamanhos únicos" — variantes reais: Azul/Rosa/Verde/Preto, tamanho M (contradição de ficha) | alta | R$ 32.708 |
| 336513465 | PONCHO RESORT PREMIUM | **forte suspeita** | mesmo template do 252094324 com composição divergente (84% algodão vs. 84% viscose no gêmeo); FAQ on-page admite "toque de IA" nas fotos sob o selo "FOTOS REAIS" | alta | R$ 15.719 |
| 349127985 | MAIO STORM | suspeito | ficha com campo vazio ("Composição do Forro:"); lista de 13 usos genéricos; cor Vermelho das variantes ausente do texto | média | R$ 11.639 |
| 298141305 + 5 irmãos | família Poncho Clássico | **forte suspeita** | um único texto replicado em ≥7 produtos, com regra de três e fecho idêntico; densidade de "poncho atoalhado" artificial | alta | R$ 33,3k somados |
| 355991421 | MAIO MOANA | **forte suspeita** | descrição: "na cor lisa preta" — variantes reais: Verde Claro, Marrom, Verde Escuro (alucinação de ficha) | alta | R$ 3.120 |
| 349128003 | MAIO RINCON | suspeito | campos de ficha vazios ("Tecnologias:", "Tecido Principal:", "Forro Interno:"); template idêntico ao STORM | média | R$ 3.700 |
| 331018836 | CAMISETA UV INFANTIL NEON | **forte suspeita** | "Tamanhos: P, M, G" vs. variantes 2–10 anos; "três cores lisas: Azul Claro, Azul Turquesa, Rosa" vs. variantes Rosa/Azul; "Indicações de uso: Motociclismo" em camiseta infantil (template alheio) | alta | R$ 0 (estoque parado) |
| 315738097 | Camiseta Lycra Feminina Vaca | **forte suspeita** | texto descreve "logo Surfnelas" e "Camiseta Surfnelas" — marca alheia; "P, M, G e GG" vs. variantes P/M/G; claim sem lastro ("material sustentável com baixo impacto ambiental") | alta | R$ 0 (105 un. paradas) |
| 357775732 | BIQUINI FLORIPA | suspeito | descrição copiada do Biquini Empina Bumbum (nome do modelo errado no texto); "2 opções de cores" coerente, mas texto-mãe fala em 6 | média | R$ 0 (200 un. paradas) |
| demais 16 da amostra | — | limpo a suspeito leve | vocabulário de slop recorrente ("Compre já!", "escolha ideal", "alta performance") sem contradição de ficha | baixa–média | — |

Fechos idênticos "Compre já!"/"Adquira já o seu!"/"Compre agora!" aparecem em 18 dos 21 `seo_description` presentes na amostra — padrão de geração em série.

### Imagens (amostra priorizada: capa + 2 por produto = 75 imagens, inspeção visual em 2026-08-12)

Resultado consolidado da inspeção visual (25 produtos):

| Classificação | Imagens | % |
|---|--:|--:|
| Suspeita de geração por IA | **56** | 74,7% |
| — confiança alta | 22 | 29,3% |
| — confiança média | 32 | 42,7% |
| — confiança baixa | 2 | 2,7% |
| Edição pesada (arte gráfica sobre foto) | 14 | 18,7% |
| Fotografia real | 5 | 6,7% |

- **10 dos 25 produtos têm pelo menos uma imagem com suspeita de IA em confiança ALTA**: 252378126, 276833135, 276833145, 298141305, 298141312, 315738164, 316378400, 336513465, 349127985, 355991468. Somente 2 produtos (MAIO RINCON, BIQUINI FLORIPA) saíram sem nenhuma suspeita.
- Achados de maior severidade (formato completo, um por linha):
  - **349127985 MAIO STORM (R$ 11,6k, capa)** — SUSPEITA DE IA, confiança alta. Sinais: arquivo `chatgpt-image-10-de-ago-de-2026-21_18_41`; na img 2, dedos da mão esquerda fundidos/deformados e mão que se mistura à coxa; dentes do zíper irregulares; logo "OH" ambíguo.
  - **298141312 Poncho Clássico Infantil (R$ 4,7k)** — SUSPEITA DE IA, confiança alta. Sinais: dedos do pé deformados em bloco (img 2); wordmark com glifos ilegíveis tipo "ΛGΘZΛ" (img 3), tell clássico de difusão em texto. Contra-evidência: anatomia da criança correta.
  - **252378126 Poncho Premium P (R$ 12,7k)** — SUSPEITA DE IA, confiança alta. Sinais: halo de difusão no cabelo; dedos do pé esquerdo fundidos; logo dissolvido em blocos triangulares com pontos dourados aleatórios.
  - **298141305 Poncho Clássico Adulto (R$ 10,7k, img 2)** — SUSPEITA DE IA, confiança alta. Sinais: arquivo `virtual-try-on-*`; tecido que se dissolve (bolso destoando do corpo da peça); pés sob a água sem refração; dimensão 832×1248 típica de gerador. A capa (img 1) é fotografia real, confiança alta.
  - **336513465 PONCHO RESORT (R$ 15,7k, img 3)** — SUSPEITA DE IA, confiança alta. Sinal decisivo: a modelo tem cabelo e traços **diferentes** entre as imagens do mesmo set (inconsistência de identidade). Coerente com a FAQ on-page que admite "toque de IA".
  - **303607414/303607422 Ponchos Azul Marinho e Azul Royal (R$ 11,8k somados)** — SUSPEITA, confiança média: mesma base recolorizada (pose e dobras pixel-idênticas entre produtos), wordmark ilegível, polegar anômalo.
  - **252094324 Poncho Premium M (R$ 32,7k, nº 1 em receita)** — SUSPEITA, confiança média nas 3 imagens: pele/tecido pintados, marcas fantasma sobre o logo, tapete com padrão procedural. Contra-evidência: tatuagem consistente entre poses. Verificação humana prioritária.
- Padrão transversal: fotos de "estúdio" com pele sem poros, tecido sem costura/trama e logos que se dissolvem em zoom; as artes gráficas (tabelas de medida, infográficos) são de design humano sobre essas bases. Nas peças com texto/logo visível, o zoom no wordmark foi o sinal mais discriminante.
- Conforme regra de evidência nº 4: tudo acima é reportado como **suspeita com nível de confiança**, não como fato; itens de confiança média/baixa exigem verificação humana (fotos originais da sessão, RAW/EXIF) antes de qualquer remoção.

**Check massivo (100% do catálogo, por nome de arquivo)**: 104 imagens `chatgpt-image-*`, 15 `virtual-try-on-*` → 119 imagens com evidência externa de origem IA, em 21 produtos, 16 como imagem de capa. Maiores concentrações: Maiô Body Gola Alta Saquarema (14), PONCHO SUPREME Algodão (12), Hot Pant Top Nadador (10), Maiô Bicolor Blackout (10), CAMISETA ITAMAMBUCA (10).

## Backlog de correção priorizado (impacto × esforço × conversão)

| # | Ação | Impacto | Esforço | Artefato |
|--:|---|---|---|---|
| 1 | **Alt em massa nas 1.686 imagens** — gerar alt descritivo com KW (produto + cor + ângulo) e gravar via API (`PUT /products/{id}/images/{id}`), começando pelo top 20 de receita | alto (catálogo inteiro) | baixo (script + revisão) | script na integração + snapshot de verificação |
| 2 | **Corrigir fichas alucinadas** (MOANA, UV INFANTIL NEON, Poncho Premium, Surfnelas/Vaca, FLORIPA) — reescrever em MODO CRIAÇÃO confrontando `variants` | alto (conversão direta) | baixo (5 produtos) | textos em `content/`, atualização via API |
| 3 | **Meta tags dos 29 produtos sem seo_title/seo_description** — priorizar os 4 do top 25 de receita; títulos ≤ 60c com KW, descriptions ≤ 155c com proposta de valor | alto | baixo | correção em massa via API |
| 4 | **Substituir imagens IA dos 16 produtos com capa `chatgpt-image`/`virtual-try-on`** por foto real do produto (a loja declara "FOTOS REAIS"); remover ou rotular as demais 103 após verificação humana | alto (confiança + Shopping) | médio (produção de foto) | lista de URLs no snapshot; verificação humana |
| 5 | **Descrições das 48 categorias** + renomear slugs numéricos (`/poncho1`→`/poncho-feminino` etc., com redirect) — começar por PONCHO (3), LYCRA SURF (2), MAIÔ | alto (head terms) | médio | pautas em `pautas/`, uma por categoria-chave |
| 6 | **Desduplicar a família de ponchos** (92 near-dup no catálogo): consolidar variantes de cor num produto pai quando fizer sentido comercial; senão, diferenciar cada texto por cor/uso | médio-alto | médio | análise de consolidação + textos |
| 7 | **Despublicar ou repor os 11 produtos com estoque zero**; avaliar os 5 de estoque parado (433 un. sem giro) para pauta de conteúdo ou promoção | médio | baixo | decisão comercial + API |
| 8 | **Unificar entidade**: grafia única "Use Zero Hora" em todos os textos; eliminar categoria e menções "SURFNELAS"; associar sempre a surf/beachwear | médio (GEO/AEO) | baixo | correção em massa + guideline |
| 9 | **Cluster informacional do poncho** ("o que é poncho de surf", "como escolher", tabela de medidas) com FAQ marcada — captura o espaço vazio identificado na SERP de 2026-08-08 | médio-alto (AEO) | médio | pautas + conteúdo em `content/` |

## Limitações e cobertura

- Checks massivos (Eixo A, filename de imagens): 100% do catálogo, cache sincronizado em 2026-08-12 (defasagem zero).
- Leitura qualitativa de textos e inspeção visual de imagens: 25 produtos da amostra priorizada (top 20 receita + 5 estoque parado); os demais 115 produtos não foram lidos integralmente.
- Validação on-page (JSON-LD, canonical, FAQPage, og:tags renderizados): **dado indisponível via WebFetch/curl** — egress da sessão bloqueia usezerohora.com.br. Recomendada validação externa (Rich Results Test) antes de fechar o Eixo B on-page.
- Volumes de busca: apenas os já coletados em `reports/` (Semrush BR, 2026-08-08). Nenhuma chamada nova a Semrush/Similarweb nesta sessão (preservação de créditos). KWs de poncho/maiô/biquíni sem volume registrado ficam como pendência da próxima coleta.
- Detecção de IA reportada como suspeita com nível de confiança, nunca como fato; imagens com confiança baixa exigem verificação humana antes de ação.
