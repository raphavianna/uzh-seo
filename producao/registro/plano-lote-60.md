# Plano — lote de 60 artigos (antecipação de escrita)

- **Data**: 2026-08-12
- **Objetivo**: escrever e revisar 60 artigos cobrindo várias categorias,
  antecipando a produção enquanto o upload por API não está liberado.
- **Fontes de dado** (todas medidas, no repositório):
  - `data/2026-08-10-matriz-kws-classificada.csv` — 860 KWs, volume/KD/intenção/PAA/AIO
  - `data/2026-08-12-nuvemshop-catalogo.json` — 140 produtos reais, com descrição,
    variantes, preço, imagem e URL canônica (coleta ao vivo de hoje)
  - `producao/registro/kw-donos.csv` — 58 keywords já com dono (excluídas)
  - `reports/2026-08-12-demanda-baselinker.md` — venda de 7 meses (fator de catálogo)

## A tensão que decide o lote

Demanda e catálogo não andam juntos. Cruzando os dois:

| Área | Busca/mês | Produtos no catálogo | KWs livres (≥300) |
|---|---:|---:|---:|
| Sunga, bermuda, short | 74.720 | **5** | 22 |
| Calçado aquático | 34.320 | **1** | 25 |
| Natação | 22.750 | fold (7 fitness) | 25 |
| Canga | 15.390 | **0** | 2 |
| Maiô | 42.420 | 27 | 10 |
| Biquíni e top | 41.020 | 18 | 10 |
| Saída de praia / resort / vestido | 87.400 | 22 | 12 |
| Poncho / toalha / roupão | 4.580 (54% da receita) | 38 | 5 |
| Lycra / camiseta UV / rash guard | 55.740 | 35 | 1 (resto já tem dono) |
| Neoprene | 18.500 | 3 | 15 |
| Moletom / casaco | — | 16 | — |
| Ioga / fitness | — | 7 | — |

A regra do projeto: **cluster com muita busca e pouco produto vira visita que
não compra** (fator de catálogo zero). Sunga tem 74 mil buscas e 5 produtos;
calçado 34 mil e 1 produto; canga 15 mil e 0 produto.

Os clusters com catálogo fundo (maiô, biquíni, saída, poncho) têm **poucas KWs
livres ≥300**, porque já cobrimos ou o volume da cauda cai. Somados dão ~37.
Para chegar a 60 com qualidade, há dois caminhos, e é isso que preciso que
você decida.

## Alocação recomendada (60)

Mistura peça comercial de catálogo fundo + peça informacional de alta demanda
(AEO), com moldura honesta onde o catálogo é raso.

| Área | Artigos | Tipo | Catálogo | Por quê |
|---|---:|---|---:|---|
| Saída de praia / resort / vestido | 11 | comercial | 22 | demanda + produto |
| Maiô | 10 | comercial | 27 | demanda + produto |
| Biquíni e top | 9 | comercial | 18 | demanda + produto |
| Poncho / toalha / roupão | 5 | comercial | 38 | 54% da receita |
| Natação | 6 | informacional/AEO | atributo | 55 PAA, o maior índice de pergunta da base |
| Sunga / bermuda / short | 5 | informacional | 5 | CAP: demanda alta, catálogo raso |
| Neoprene / long john | 4 | comercial/sazonal | 3 | inverno |
| Ioga / fitness | 4 | comercial | 7 | território novo com produto |
| Moletom / casaco | 3 | comercial | 16 | inverno |
| Moda praia / institucional | 2 | marca | — | autoridade de entidade |
| Lycra / camiseta UV | 1 | comercial | 35 | única KW livre ≥300 |
| **Total** | **60** | | | |

**Capados de propósito** (com o número): calçado aquático (1 produto) → 0;
canga (0 produto) → 0. Ambos entram no parking-lot até o catálogo abrir.

## As 6 auditorias que todo artigo passa

Cada um dos 60 passa por seis gates antes de virar rascunho aprovável:

1. **Anticanibalização** — KW primária livre no registro; nenhum par do lote
   com mesmo eixo e mesma intenção; termo de outro dono só como âncora de link.
2. **Dados** — todo número e atributo vem de `data/2026-08-12-nuvemshop-catalogo.json`
   ou da ficha; ausente vira "dado indisponível", nunca estimativa.
3. **Padrão HTML** — title ≤60, meta ≤155, canonical com `{HASH}`, Open Graph,
   JSON-LD (Article/BlogPosting + FAQPage + BreadcrumbList), um só `<h1>`.
4. **AEO/GEO** — resposta direta e autocontida na abertura de cada seção; FAQ
   com perguntas de PAA; dado concreto; definição do termo; entidade
   "Use Zero Hora, marca de surf e beachwear".
5. **stop-slop** — vícios de escrita de IA removidos.
6. **Links e imagens** — URL de categoria/produto ativa (do catálogo); imagem
   real do produto (CDN); link de irmão como `{HASH}` para fechar depois.

## Como roda

Antecipação determinística (eu, antes de disparar): seleciono as 60 KWs
primárias, e para cada uma fixo categoria de destino, produtos de apoio,
secundárias sem colisão, editoria e intenção. Isso trava a anticanibalização
das 60 de uma vez.

Depois, **ondas por cluster** (não um bloco só), cada onda produzindo ~10
artigos por pauta→redação→revisão. Reporto ao fim de cada onda para você
conferir por amostragem. Ao todo, ~4 horas.

## O que você recebe

- 60 × `content/<slug>.html` e `<slug>-editor.html` (rascunhos)
- `producao/registro/grade-lote-60.csv` — a grade do lote
- `kw-donos.csv` atualizado (+~300 keywords, sem colisão)
- Um guia de revisão por cluster, como o guia do T1, para você conferir
- Tudo commitado no branch, onda a onda

Nada é publicado. O upload continua sendo etapa à parte.

---

# Expansão (2026-08-12) — lycra a 10 + módulo esporte e bem-estar

Pedido do usuário: subir lycra para 10 sem tirar nada, e abrir a frente ampla
de esporte e bem-estar, sempre ancorada a produto da marca, com KW de escala
(volume) como primeiro critério e KD como segundo.

## Semrush sem unidades

A pesquisa medida dos termos novos (surf, SUP, yoga, futevôlei…) não roda: a
conta corporativa está sem unidades de API. Para volume/KD medido, ou o dono
da conta aloca unidades, ou o time exporta o Google Ads Keyword Planner
desses termos (que, pela regra de dados 5, vence para volume e CPC). Esses
termos não estão na matriz atual, então sem uma dessas fontes o ranqueamento
por escala fica pendente.

## Módulo 2 — Lycra a 10 (dado medido, da matriz)

As 10 KWs livres de maior volume do cluster: camiseta surf (720), camisa uv
pesca (260), lycra de surf (140), camisa de surfista masculina (140), camiseta
manga longa surf (110), camiseta surfista (90), camiseta uv com zíper (70),
camisa manga longa proteção solar (50), camisa uv50 (50), camiseta lycra surf
manga longa (50). Destino comercial: /masculino/lycra-surf/ e /*/camiseta-uv*/.

## Módulo 3 — Esporte e bem-estar (novo, ~21), ancorado a produto

Cada tema amarra a uma categoria real do catálogo. Contagem por tema é
proposta; a ordem final segue o volume quando a fonte de dado voltar.

| Bloco | Temas | Âncora de produto | Artigos |
|---|---|---|---:|
| Água e prancha | surf, stand up paddle, kitesurf, wakeboard | /masculino/lycra-surf/, camiseta UV, neoprene | 6 |
| Natação e remo | natação piscina, natação mar, canoagem, canoa havaiana | maiô, camiseta UV, neoprene | 6 |
| Bem-estar | yoga, pilates, treino funcional | IOGA / FITNESS (7 produtos) | 4 |
| Praia esportiva | vôlei de praia, futevôlei | biquíni/top, sunga, lycra | 3 |
| Hub do módulo | roupa com proteção UV para esporte ao ar livre | guarda-chuva do módulo | 2 |

Ancoragem honesta: surf, SUP, kitesurf, natação estão na lista de esportes da
ficha técnica; yoga/pilates ganham lastro pela categoria IOGA/FITNESS; canoa
havaiana e futevôlei entram pelo fio condutor da proteção UV (o produto
protege em qualquer esporte de sol e água), sem prometer produto dedicado.

## Total expandido

| Módulo | Artigos | Dado |
|---|---:|---|
| 1. Comercial de catálogo | 49 | medido (matriz) |
| 2. Lycra / UV / rash | 10 | medido (matriz) |
| 3. Esporte e bem-estar | ~21 | estrutura pronta, volume pendente |
| **Total** | **~80** | |

## Ordem de execução proposta

Começo pelos módulos 1 e 2 (59 artigos, todos com volume medido), em ondas por
cluster. O módulo 3 entra assim que houver volume (Keyword Planner ou unidades
Semrush) para ranquear por escala, ou já com moldura qualitativa declarada se
o usuário aceitar.

---

# Regra de conteúdo (2026-08-12) — SEM PREÇO no corpo dos artigos

Decisão do usuário: **não citar preço nos artigos**. O artigo fica no ar por
meses; o preço muda rápido e vira informação errada, o que envelhece o conteúdo
e quebra a confiança. Vale para **todas as ondas e todos os artigos**.

- Onde havia preço, o artigo usa **link do produto** (canônica real do catálogo)
  ou da categoria, e o atributo técnico que não muda (composição, UV50+, tecido,
  modelagem, garantia). Ex.: em vez de "Maiô Storm por R$ 299,00", usar
  "[Maiô Storm](url) com gola alta anatômica e zíper YKK®".
- Atributo técnico e composição continuam entrando com a data da ficha
  (regra de dados 7), porque mudam devagar; preço, promoção e frete saem.
- Auditoria 2 (Dados) do lote fica: número e atributo da ficha, **sem preço**.
- Aplicado retroativamente aos artigos 01–04 da Onda 1 em 2026-08-12.
