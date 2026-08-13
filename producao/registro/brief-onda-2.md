# Briefing de produção — Onda 2 (kit para o escritor)

Você escreve UM artigo HTML autocontido para o blog da Use Zero Hora, marca
brasileira de surf e beachwear. Entregue SÓ o arquivo `content/<slug>.html`
completo — nada de comentário fora do arquivo. Português do Brasil impecável.

## Aterramento (dado real, zero invenção)

- Rode `python3 scripts/ficha-por-categoria.py <URL_DESTINO>` para pegar nome,
  atributos, imagem CDN e trecho de descrição dos produtos REAIS da categoria de
  destino. Use SÓ esses fatos para falar de produto. Precisa de outra categoria?
  Rode o helper nela.
- Atributo que não está na ficha/descrição vira **"dado indisponível"** — nunca
  invente composição, medida, gramatura ou preço.
- **SEM PREÇO em lugar nenhum** (preço muda, o artigo fica meses no ar). Onde
  citaria preço, use link do produto e o atributo técnico que não muda.
- Conteúdo informacional (esporte, saúde, método) é conhecimento geral — pode
  usar, declarando quando for orientação de saúde ("não substitui avaliação
  profissional").
- Marca sempre nesta forma exata: **Use Zero Hora, marca brasileira de surf e
  beachwear**. Não repita a aposição em toda seção; uma vez por artigo basta.

## Estrutura do arquivo (siga à risca)

1. Comentário de produção no topo `<!-- ... -->`: KW primária (vol/KD/fonte),
   secundárias, formato, intenção, destino, ponte até a conversão, data 2026-08-13.
2. `<title>` com a KW primária, **≤60 caracteres**, formulado para clique.
3. `<meta name="description">` **≤155 caracteres**, com KW primária e valor.
4. `<link rel="canonical" href="https://usezerohora.com.br/blog/posts/<slug>-{HASH}">`
   (o {HASH} é o único placeholder permitido — só em canonical, og:url e nos @id
   do schema).
5. Open Graph (og:title/description/type=article/url/image) + Twitter Card. A
   `og:image` é uma imagem CDN real de produto (do helper).
6. Três blocos `<script type="application/ld+json">`: **BlogPosting**,
   **BreadcrumbList**, **FAQPage**. inLanguage pt-BR, datePublished/Modified
   2026-08-13. O texto das perguntas do FAQPage = o mesmo do bloco `<h3>` no corpo.
7. Um único `<h1>` com a KW primária.
8. Corpo: 1º parágrafo responde à intenção em até 3 frases; `<h2>`/`<h3>` cobrindo
   as secundárias como subtópicos reais; **abertura autocontida em cada seção**
   (2–4 frases que respondem antes de aprofundar, para o motor de resposta
   extrair o bloco); uma `<figure>` com `<img>` CDN real (alt descritivo).
9. Bloco de FAQ ao fim: 5 perguntas na forma que o usuário digita, respostas de
   2 a 4 frases, marcadas em `<h3>` e espelhadas no FAQPage.
10. CTA coerente com o funil, levando ao destino.

## Links (regra de destaque)

- Todo link interno aponta para URL REAL de categoria/produto de usezerohora.com.br
  (confira a categoria com o helper; produto pela `canonical_url` da ficha).
- **NUNCA** linke para post-irmão com `{HASH}` no corpo. Só categoria/produto real.
- Todo link de produto/categoria sai **destacado**: 
  `<a href="URL"><strong><u>texto do link</u></strong></a>`.

## FORMATO da pauta (escreva no formato pedido, não sempre "guia de tipos")

- **Q&A**: uma pergunta central respondida a fundo, com sub-perguntas em `<h2>`.
- **CMP** (comparativo X ou Y): critério a critério, com veredito honesto por uso.
- **LST** (listicle/tipos/N formas): itens reais, cada um com 2–4 frases.
- **HOW** (passo a passo): passos numerados de verdade, do iniciante ao próximo nível.
- **GUI** (guia de escolha): o que olhar + como decidir + o que a loja tem.
- **SAZ** (sazonal/tendência): ancore a tendência no que a loja realmente vende.

## ANTI-IA — a peça JÁ NASCE limpa (prioridade máxima)

Proibido (não use nada disto):
- Frase-meta / joiner: "Neste guia", "Este guia mostra", "Vale ressaltar",
  "É importante notar", "Em resumo", "Por fim", "Além disso" como muleta.
- Paralelismo negativo: "não é X, e sim Y" / "não X, mas Y" como fórmula.
- Tricolon abstrato: "conforto, segurança e estilo"; "força, controle e postura".
  Prefira DOIS elementos concretos a três decorativos.
- Adjetivo promocional vazio: "grande trunfo", "solução ideal", "a forma mais
  eficiente", "espetáculo de", "verdadeiro aliado".
- Verbo-muleta repetido no mesmo texto: "resolve", "conta", "oferece", "garante".
- Abertura de seção repetindo a definição já dada; restatement do H2.
- Reticências retóricas, "de verdade" / "de propósito" / "com folga" como bordão.
- **TRAVESSÃO (—) é proibido.** Use vírgula, ponto ou dois-pontos.
- Voz passiva evitável e sujeito inanimado com verbo humano ("a peça resolve",
  "a decisão emerge"). Toda frase com sujeito humano fazendo algo.

Exija de si:
- Frases de tamanhos variados (nada metronômico). Aberturas de parágrafo variadas
  (não abrir 3 seguidas com "A"/"O"/"É").
- Português quente de quem vive praia e surf, direto, sem corporativês nem gíria
  forçada. Escreva para a pessoa, não para o robô de busca.
- Dado concreto onde couber (fator UV, tempo, técnica), sempre real.

Antes de fechar, releia e corte tudo que "cheira" a IA. A peça vai passar por
auditoria adversarial depois; entregue já sem sinais.
