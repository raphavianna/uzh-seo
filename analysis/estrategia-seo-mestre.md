# Estratégia SEO/AEO Use Zero Hora — decomposição sequencial

- **Data**: 2026-08-09
- **Autor**: agente SEO/AEO do repositório `uzh-seo`
- **Dados-base**: `reports/2026-08-09-semrush-baseline-dominio.md` (Semrush BR,
  2026-08-09), `reports/2026-08-08-semrush-kws-lycra-surf.md`,
  `reports/2026-08-08-similarweb-canais-usezerohora.md`,
  `reports/2026-08-08-serp-leitura-territorios.md`,
  `analysis/00-territorios.md`
- **Critério de sucesso**: venda na loja vinda de busca orgânica. Posição e
  citação em IA são meio.

---

## 1. Como ler este documento

A estratégia está decomposta em dez blocos sequenciais, de S0 a S9. Cada
bloco tem pré-requisito, entrada, execução, artefato, gate de saída e KPI. O
gate é um critério objetivo: enquanto ele não fecha, o bloco seguinte não
começa. Essa ordem existe porque cada bloco compra alguma coisa que o próximo
consome. Otimizar conteúdo antes de resolver indexação queima trabalho;
produzir pauta antes de definir dono de keyword cria canibalização; medir
antes de instrumentar produz opinião.

Três blocos rodam em trilha contínua depois de abertos, e o documento marca
quais: S8 (autoridade) e S9 (medição) não fecham, e S3 (colheita) reabre a
cada ciclo de medição.

## 2. Diagnóstico em oito números

Todos de `reports/2026-08-09-semrush-baseline-dominio.md`, Semrush BR,
coleta de 2026-08-09.

| # | Número | O que ele obriga |
|---|---|---|
| 1 | 138 visitas orgânicas/mês | A base é pequena. Ganho absoluto modesto vira ganho percentual grande. |
| 2 | 146 keywords no top 100, 86 delas entre a posição 11 e a 30 | O Google já reconhece o site. Falta cruzar para a página 1. Prioridade é subir, não semear. |
| 3 | 21 keywords no top 10, contra 1.809 da Only Surf | O teto competitivo está longe. Meta de ciclo é Lord Sea e Soulfins, não o líder. |
| 4 | 0,95 visita por keyword, contra 9,2 da Only Surf | O problema é posição média, não cobertura. |
| 5 | 58 das 138 visitas vêm de `/feminino/maio/` | 42% do orgânico depende de uma página. Defender esse ativo é risco, não escolha. |
| 6 | 84 keywords com People Also Ask, 41 com AI Overview, 0 featured snippet | A marca aparece em SERPs onde o Google monta resposta e não é a fonte da resposta. |
| 7 | 63% do tráfego vem de Display e Social Pago (Similarweb, abr-jul/2026) | Cada posição orgânica reduz dependência de mídia paga. |
| 8 | 0 keyword paga no Google Ads | Orgânico e Search pago não competem hoje. O repositório irmão `search-mkt` entra em terreno limpo. |

## 3. Tese estratégica

A Use Zero Hora não precisa de mais conteúdo antes de precisar de mais
posição. O site ranqueia para 146 termos e converte pouco disso em visita
porque 59% das keywords estão na página 2 e 3. O caminho mais curto até venda
orgânica é subir o que já ranqueia, começando pelo cluster de maiô de surf
feminino, que já entrega 42% do tráfego, e pelo cluster de poncho, que está
dividido entre duas categorias mal resolvidas no CMS.

Só depois disso a marca ganha com conteúdo novo, porque aí cada peça publicada
cai num site que indexa direito, tem dono de keyword definido e sabe medir o
que aconteceu.

A camada AEO entra junto do conteúdo, não depois. Com 41 keywords já servindo
AI Overview e nenhum featured snippet capturado, a marca paga o custo de
aparecer sem colher a citação.

## 4. Regra de priorização

Toda pauta e toda otimização entram na fila por este cálculo, registrado no
artefato correspondente:

```
Prioridade = (Volume × Δ CTR esperado × Proximidade da conversão) ÷ Esforço
```

- **Δ CTR esperado**: diferença entre a taxa atual da posição e a taxa da
  posição alvo, usando a curva do próprio site (posição 2–3: 4,3%; 5–8: 2,4%;
  11–16: 0,2%). Nada de curva genérica de mercado.
- **Proximidade da conversão**: transacional 3, comercial 2, informacional 1.
- **Esforço**: 1 para ajuste on-page em página existente, 2 para reescrita de
  categoria, 3 para conteúdo novo, 5 para mudança estrutural no CMS.

Um ajuste on-page numa keyword comercial de 590 buscas parada na posição 12
vence, todas as vezes, um artigo novo de topo de funil.

---

# A cadeia sequencial

## S0 — Baseline e instrumentação

**Pergunta**: de onde estamos partindo e como saberemos que mexemos o ponteiro?

**Pré-requisito**: nenhum. É a entrada da cadeia.

**Entrada**: acesso a Google Search Console, GA4 e ao admin do CMS.

**Execução**
1. Registrar o baseline de posição, keywords e tráfego (feito em
   `reports/2026-08-09-semrush-baseline-dominio.md`).
2. Confirmar propriedade e histórico do Search Console, e exportar as
   consultas dos últimos 16 meses. O GSC mostra impressão e clique reais, que
   vencem estimativa de ferramenta.
3. Confirmar que o GA4 registra a conversão de compra com origem
   `organic search` separada de paga, e que o valor da transação chega.
4. Criar projeto de Position Tracking no Semrush com as keywords do baseline
   mais os clusters de S5, para acompanhar posição semanal.
5. Registrar quem no time publica no CMS e qual o prazo de deploy de um
   texto. Esse número define a cadência realista de S6.

**Artefato**: `reports/00-baseline.md` consolidando Semrush, GSC e GA4.

**Gate**: existe uma linha de base com data, e existe um relatório de GA4 que
mostra receita de busca orgânica isolada. Sem isso, nenhum bloco seguinte
consegue provar resultado.

**KPI de partida**: 138 visitas orgânicas/mês, 21 keywords no top 10, receita
orgânica a medir.

---

## S1 — Saúde técnica e indexabilidade

**Pergunta**: o que impede o Google de ler, indexar e atribuir corretamente as
páginas que já existem?

**Pré-requisito**: gate de S0 fechado.

**Entrada**: baseline, acesso ao CMS, Site Audit do Semrush.

**Execução**
1. Rodar Site Audit no domínio e classificar erros por impacto em página de
   categoria e de produto.
2. Tratar a busca interna. `/search/?q=biquini+maio` ranqueia na posição 11
   para "biquine maiô" (170 buscas/mês). Aplicar `noindex, follow` em todas as
   URLs de resultado de busca interna e redirecionar a demanda para a
   categoria correspondente.
3. Auditar variação de produto. Se cada cor gera URL própria, definir
   canonical para a URL principal do produto, para não dividir sinal entre
   dez variações da mesma peça.
4. Verificar sitemap.xml e robots.txt: categorias vivas presentes, URLs de
   busca e de carrinho fora.
5. Medir Core Web Vitals em mobile nas cinco páginas de maior tráfego, com
   prioridade para LCP das categorias.
6. Conferir se as páginas de categoria têm `<title>`, meta description e H1
   próprios, e não herdados de template.

**Artefato**: `analysis/01-tecnico.md` com a lista de correções, responsável e
prioridade, mais o antes e depois de cada item.

**Gate**: nenhuma URL de busca interna indexada, canonical resolvido nas
variações, e as páginas de `/feminino/maio/`, `/masculino/lycra-surf/`,
`/masculino/poncho/` e `/feminino/poncho1/` retornando 200 e indexáveis.

**KPI**: páginas indexadas válidas no GSC, erros críticos do Site Audit em
zero, LCP mobile abaixo de 2,5s nas cinco principais.

---

## S2 — Arquitetura de informação e mapa keyword para URL

**Pergunta**: qual página é dona de qual cluster, e onde duas páginas nossas
estão brigando pela mesma busca?

**Pré-requisito**: gate de S1 fechado. Sem indexação resolvida, o mapa aponta
para páginas que o Google não lê.

**Entrada**: lista de URLs do baseline, taxonomia real do CMS.

**Execução**
1. Levantar a taxonomia completa: categorias, subcategorias, coleções e
   filtros que geram URL.
2. Resolver o cluster poncho. Hoje `/masculino/poncho/` ranqueia "poncho
   toalha" (320) na posição 15 e `/feminino/poncho1/` ranqueia "poncho surf"
   (480) na posição 12. O sufixo numérico no slug indica categoria duplicada
   no CMS. Decidir entre hub `/poncho/` com filhas masculina, feminina e
   infantil, ou dono único por termo genérico. Registrar a decisão com o
   número que a sustenta.
3. Criar destino para "poncho toalha infantil" (590 buscas/mês, hoje na
   posição 11 por uma URL de produto). O segmento infantil não tem categoria.
4. Definir dono para o cluster maiô. `/feminino/maio/` já é dona de 10
   keywords. Nenhuma página nova pode disputar "maiô surf" com ela.
5. Decidir o caso `sunkini`: 1.600 buscas/mês, posição 24, com
   `/feminino/biquini/sunkini/` já ranqueando "subikini" (210) na posição 8.
   Confirmar com o time se "sunkini" é termo genérico de categoria ou nome de
   outra marca. A resposta muda se a página vira alvo prioritário ou fica
   fora do escopo.
6. Publicar a matriz keyword para URL: uma linha por keyword, uma URL dona,
   status de canibalização.
7. Definir o padrão de link interno: categoria aponta para produtos, produto
   aponta de volta para categoria, conteúdo editorial aponta para a categoria
   comercial do seu cluster.

**Artefato**: `analysis/02-arquitetura.md` com a taxonomia alvo, a matriz
keyword para URL e a lista de canibalizações com plano de resolução.

**Gate**: toda keyword do baseline com uma única URL dona declarada, e as
duplicidades de poncho resolvidas ou com decisão registrada.

**KPI**: número de keywords com mais de uma URL nossa no top 100, alvo zero.

---

## S3 — Colheita de curto prazo (posições 11 a 30)

**Pergunta**: o que sobe de página 2 para página 1 sem escrever nada novo?

**Pré-requisito**: gates de S1 e S2 fechados. Otimizar página que canibaliza
outra é trabalho perdido.

**Entrada**: matriz keyword para URL, as 86 keywords em posição 11 a 30, as
consultas do Search Console.

**Execução**
1. Recoletar a lista completa das 86 keywords quando o saldo do Semrush
   permitir. Enquanto isso, trabalhar as 12 identificadas na amostra de
   2026-08-09, que somam 4.960 buscas/mês e entregam 9 visitas/mês.
2. Para cada URL dona, reescrever `<title>`, meta description e H1 com a
   keyword na forma exata em que ela indexa.
3. Adensar o texto de categoria: primeiro parágrafo respondendo a intenção em
   até três frases, H2 cobrindo as secundárias como subtópico real.
4. Cruzar impressão e CTR do Search Console. Keyword com muita impressão e
   pouco clique é problema de title, não de posição.
5. Reforçar link interno para as páginas alvo a partir das páginas de maior
   autoridade do site.
6. Publicar bloco de FAQ com schema `FAQPage` nas quatro categorias
   prioritárias, usando o fraseado real das perguntas.

**Fila inicial da colheita**, por prioridade da regra da seção 4:

| Keyword | Vol. | Pos. | URL dona | Alvo |
|---|---:|---:|---|---|
| lycra surf | 880 | 15 | /masculino/lycra-surf/ | top 5 |
| poncho toalha infantil | 590 | 11 | categoria infantil a criar | top 5 |
| maio surf feminino | 590 | 12 | /feminino/maio/ | top 5 |
| surf lycras | 590 | 16 | /masculino/lycra-surf/ | top 10 |
| maiô surf | 480 | 12 | /feminino/maio/ | top 5 |
| poncho surf | 480 | 12 | dono a definir em S2 | top 5 |
| maio surfista feminino | 320 | 11 | /feminino/maio/ | top 5 |
| poncho toalha | 320 | 15 | dono a definir em S2 | top 10 |
| vestido praia longo | 260 | 29 | produto | top 20 |
| saida de praia bege | 170 | 23 | produto | top 20 |
| camisa manga longa praia | 140 | 13 | produto | top 10 |
| maiô de surfista feminino | 140 | 14 | /feminino/maio/ | top 10 |

**Artefato**: `analysis/03-colheita.md` com uma linha por keyword: posição
inicial, ação executada, data, posição em 30 e em 60 dias.

**Gate**: todas as keywords da fila com ação executada e data registrada, e
uma medição de 30 dias feita.

**KPI**: essas 12 keywords saindo de 9 visitas/mês. Na taxa de 2,4% da faixa
5 a 8, o alvo é 119 visitas/mês. Na taxa de 4,3% do top 3, 213 visitas/mês.
O tráfego orgânico do site inteiro hoje é 138 visitas/mês.

**Trilha contínua**: S3 reabre a cada ciclo de S9, com a nova lista de
keywords que entraram na faixa 11 a 30.

---

## S4 — Identidade de entidade "Use Zero Hora"

**Pergunta**: o Google e os motores de resposta sabem que Use Zero Hora é uma
marca de surf e beachwear, e não o jornal do Grupo RBS?

**Pré-requisito**: gate de S3 fechado. Entidade rende mais depois que as
páginas comerciais estão firmes, porque a marca ganha volume de busca
navegacional quando o produto começa a ser encontrado.

**Entrada**: `analysis/00-territorios.md`, perfis sociais da marca, página
institucional.

**Execução**
1. Publicar JSON-LD `Organization` na home, com `name` "Use Zero Hora",
   `alternateName`, `logo`, `sameAs` apontando para Instagram, Facebook e
   demais perfis oficiais, `foundingDate` 2023 e `areaServed` Brasil.
2. Padronizar a descrição da marca em todos os perfis externos com a mesma
   frase de entidade: Use Zero Hora, marca brasileira de surf e beachwear.
   Consistência literal, não paráfrase.
3. Reescrever "Quem Somos" como página de entidade: quem fundou, quando,
   onde, o que fabrica, como produz, o que a diferencia. Motores de resposta
   citam fato verificável, não adjetivo.
4. Ocupar o território narrativo "surf zero hora", a sessão de surf de
   madrugada identificada na Fase 0. É a ponte semântica entre o nome da
   marca e a cultura de surf, e nenhum concorrente pode reivindicá-la.
5. Publicar `BreadcrumbList` em todas as categorias e produtos.
6. Não disputar a marca seca "zero hora". Monitorar apenas, conforme a
   decisão da Fase 0.

**Artefato**: `analysis/04-entidade.md` com o texto padrão de entidade, o
JSON-LD publicado e o inventário de perfis alinhados.

**Gate**: `Organization` validado no Rich Results Test, `sameAs` completo, e a
mesma frase de entidade em todos os perfis oficiais.

**KPI**: aparecimento de painel de conhecimento para "use zero hora";
proporção de respostas de ChatGPT, Perplexity e Gemini que associam a marca a
surf e beachwear quando perguntadas diretamente, medida com prompt fixo e
registrada com data.

---

## S5 — Mapa de oportunidades completo

**Pergunta**: quanta demanda existe em cada território, e onde os concorrentes
ranqueiam e nós não?

**Pré-requisito**: gate de S4 fechado e saldo de Semrush disponível. Este
bloco é o único da cadeia que depende de crédito externo.

**Entrada**: matriz keyword para URL de S2, clusters da Fase 0.

**Execução**
1. Coletar volume, KD, CPC e intenção dos clusters ainda sem número: poncho e
   roupão, maiô e biquíni de surf, neoprene, moda praia esportiva, infantil.
   O cluster lycra já está em `reports/2026-08-08-semrush-kws-lycra-surf.md`.
2. Rodar gap de keywords contra Only Surf, Wet Dreams e Soulfins. Only Surf
   ranqueia para 1.809 termos com 146 nossos. O gap é o backlog.
3. Extrair `phrase_questions` de cada cluster para alimentar a camada AEO de
   S7.
4. Marcar cada keyword com território, intenção, URL dona e prioridade pela
   regra da seção 4.
5. Separar o que é território de SEO e o que é território de mídia paga,
   entregando essa fatia ao repositório `search-mkt`.

**Artefato**: `analysis/01-oportunidades.md` com os clusters priorizados, mais
snapshot datado em `reports/`.

**Gate**: todo cluster do catálogo com volume coletado ou marcado como dado
indisponível, e uma fila priorizada de no mínimo 20 oportunidades.

**KPI**: cobertura de keywords do catálogo mapeadas, e volume total endereçado
pela fila.

---

## S6 — Motor de conteúdo hub e spoke

**Pergunta**: que conteúdo novo captura demanda que as categorias não capturam?

**Pré-requisito**: gate de S5 fechado.

**Entrada**: fila priorizada de oportunidades, padrão de conteúdo do
`CLAUDE.md`.

**Execução**
1. Montar cada cluster como hub e spoke: a categoria comercial é o hub, os
   conteúdos informacionais são os spokes, todos apontando para o hub com
   anchor descritivo.
2. Abrir o primeiro cluster pelo poncho, que tem intenção transacional e
   espaço informacional vazio na SERP brasileira: o que é poncho de surf, como
   escolher tamanho, poncho contra toalha comum, poncho infantil.
3. Segundo cluster: maiô e biquíni para surfar, protegendo o ativo de 42% do
   tráfego e ampliando para as dúvidas de quem ainda escolhe a peça.
4. Terceiro cluster: neoprene, sincronizado com a campanha de Search do
   repositório `search-mkt`, para que orgânico e pago cheguem juntos.
5. Uma pauta por arquivo em `pautas/`, com keyword primária, secundárias,
   intenção, funil, formato e caminho até a conversão. HTML final em
   `content/`, no padrão do `CLAUDE.md`.
6. Cadência definida pelo prazo real de publicação levantado em S0. Ritmo
   sustentável vence lote grande parado na fila do CMS.

**Artefato**: arquivos em `pautas/` e `content/`, mais o backlog priorizado.

**Gate**: primeiro cluster completo, publicado e indexado, com posição
registrada 30 dias depois.

**KPI**: keywords novas entrando no top 100, tráfego por cluster, e transações
com origem orgânica atribuídas às páginas do cluster.

---

## S7 — Camada AEO e GEO

**Pergunta**: por que a marca aparece em 41 SERPs com AI Overview e não é
citada como fonte em nenhuma?

**Pré-requisito**: gate de S6 aberto no primeiro cluster. A camada AEO se
aplica sobre conteúdo existente, não no vazio.

**Entrada**: conteúdo publicado, perguntas reais dos clusters coletadas em S5.

**Execução**
1. Reformatar a abertura de cada seção como resposta autocontida de duas a
   quatro frases. Motor de resposta extrai bloco curto e completo, não
   parágrafo que depende do anterior.
2. Publicar FAQ com schema `FAQPage` em toda categoria e todo conteúdo, com a
   pergunta escrita como o usuário digita.
3. Encher o conteúdo de dado concreto: gramatura do tecido, medida da peça,
   fator de proteção, tempo de secagem, faixa de preço, prazo de envio.
   Especificidade é o que motor de IA cita.
4. Definir termos do nicho de forma explícita, para capturar consulta
   informacional em IA: o que é poncho de surf, o que é lycra UV50, diferença
   entre maiô de surf e maiô comum.
5. Marcar produto com `Product` e `Offer`, incluindo preço, disponibilidade e
   avaliação quando existir.
6. Criar o teste de citação: um conjunto fixo de dez perguntas rodado em
   ChatGPT, Perplexity, Gemini e AI Overview, com data e resultado registrados
   em `reports/`. Sem prompt fixo não existe série histórica.

**Artefato**: `analysis/05-aeo.md` com o protocolo de teste e a série de
citações, mais o schema aplicado por página.

**Gate**: `FAQPage` validado em todas as categorias prioritárias, e a primeira
rodada do teste de citação registrada.

**KPI**: featured snippets capturados, hoje zero; citações da marca por motor
de resposta; tráfego de referência vindo de ChatGPT e Perplexity no GA4.

---

## S8 — Autoridade off-page e prova

**Pergunta**: por que o Google confiaria mais na Use Zero Hora que na Only
Surf?

**Pré-requisito**: gate de S6 aberto. Link para página fraca desperdiça link.

**Entrada**: perfil de backlinks do domínio e dos concorrentes.

**Execução**
1. Levantar o perfil de backlinks próprio e o das cinco concorrentes do
   benchmark, e listar os domínios que linkam para elas e não para nós.
2. Trabalhar as fontes naturais do nicho: escolas de surf, campeonatos,
   atletas patrocinados, blogs e veículos de surf brasileiros, marketplaces
   com página de marca.
3. Transformar prova em conteúdo linkável: fabricação própria, teste de
   produto na água, guia de tamanho real.
4. Manter consistência de nome, endereço e perfis, reforçando S4.
5. Registrar avaliação de cliente com marcação estruturada, que serve a
   ranking e a citação em IA.

**Artefato**: `analysis/06-autoridade.md` com o gap de domínios referentes e a
fila de ações.

**Gate**: bloco sem gate de fechamento. Roda em trilha contínua com meta
trimestral de domínios referentes novos.

**KPI**: domínios referentes novos por trimestre, Authority Score, e posição
média nas keywords de maior KD.

---

## S9 — Medição, cadência e realimentação

**Pergunta**: o que mudou, quanto vendeu, e o que entra na fila do próximo
ciclo?

**Pré-requisito**: gate de S0 fechado. Roda em paralelo a partir de S3.

**Entrada**: Search Console, GA4, Position Tracking, artefatos dos blocos.

**Execução**
1. Ciclo mensal fechado em relatório datado em `reports/`: posição das
   keywords alvo, tráfego por cluster, transações e receita de origem
   orgânica.
2. Comparar o previsto de cada bloco com o realizado. Onde a previsão errou,
   corrigir a curva de CTR do site com o dado novo, não manter a estimativa.
3. Reabrir S3 com as keywords que entraram na faixa 11 a 30 no período.
4. Rever a divisão de território da Fase 0 quando o dado contradisser a
   decisão, conforme o critério já registrado em `analysis/00-territorios.md`.
5. Podar o backlog: pauta que não moveu posição em 90 dias sai ou é reescrita
   com ângulo diferente.

**Artefato**: `reports/YYYY-MM-medicao.md`, um por mês.

**Gate**: bloco sem gate de fechamento. É o loop.

**KPI de topo do projeto**: receita de busca orgânica por mês, e participação
do orgânico no total de sessões, hoje em 15,4% conforme Similarweb.

---

## 5. Metas por horizonte

Partindo de 138 visitas orgânicas/mês e 21 keywords no top 10, com as taxas de
clique derivadas do próprio site.

| Horizonte | Blocos | Meta de tráfego orgânico | Meta de posição |
|---|---|---:|---|
| 0 a 60 dias | S0, S1, S2 | manter 138 | zero canibalização, zero URL de busca indexada |
| 60 a 120 dias | S3 | 250 a 300/mês | 12 keywords da fila da colheita no top 10 |
| 120 a 210 dias | S4, S5, S6 | 400 a 600/mês | superar Lord Sea (323/mês) |
| 210 a 365 dias | S6, S7, S8 | 1.000 a 1.200/mês | alcançar Soulfins (1.166/mês), primeiros featured snippets |

A meta de 12 meses coloca a marca no patamar da Soulfins e a menos da metade
da Wet Dreams. Only Surf, com 16.591 visitas/mês, é referência de teto e não
meta de ciclo.

## 6. Riscos e como este plano falha

1. **O CMS não permite as correções de S1 e S2.** É o risco maior, porque S3
   depende delas. Se a plataforma não deixa aplicar `noindex` na busca interna
   ou corrigir slug de categoria, o plano perde o bloco de maior retorno.
   Levantar isso no início de S1, não no meio.
2. **A dependência de `/feminino/maio/`.** Uma página responde por 42% do
   orgânico. Perda de posição nela apaga o ganho de vários ciclos. Por isso
   ela entra na colheita como defesa, antes de qualquer expansão.
3. **Saldo de Semrush.** S5 é o único bloco que depende de crédito externo.
   Enquanto ele não abre, S3 roda com dado do Search Console, que é medição
   própria e vence estimativa.
4. **Cadência de publicação.** Backlog grande com CMS lento produz artefato
   parado no repositório. S0 levanta o prazo real de publicação e S6 se
   ajusta a ele.
5. **Confundir posição com venda.** Todo relatório de S9 abre pela receita
   orgânica. Ranking sem transação é sinal de intenção mal escolhida, e o
   backlog muda.

## 7. Decisões que dependem do time

Estas travam blocos específicos e precisam de resposta antes deles.

| # | Decisão | Trava | Prazo |
|---|---|---|---|
| 1 | "sunkini" (1.600 buscas/mês) é termo de categoria ou nome de outra marca? | S2 e S3 | antes de S2 |
| 2 | O CMS permite `noindex` em busca interna e canonical em variação de produto? | S1 | antes de S1 |
| 3 | Existe categoria infantil no catálogo, ou só produtos avulsos? "poncho toalha infantil" tem 590 buscas/mês sem página de destino. | S2 | antes de S2 |
| 4 | Qual o slug correto da categoria feminina de poncho, hoje `/feminino/poncho1/`? | S2 | antes de S2 |
| 5 | Quem publica no CMS e em quanto tempo um texto entra no ar? | S0 e S6 | antes de S0 fechar |
| 6 | O GA4 separa receita de orgânico e de paga hoje? | S0 | antes de S0 fechar |

## 8. Estado de execução

| Bloco | Estado | Artefato |
|---|---|---|
| S0 | Parcial. Baseline coletado, GSC e GA4 pendentes. | `reports/2026-08-09-semrush-baseline-dominio.md` |
| S1 | Não iniciado | |
| S2 | Não iniciado | |
| S3 | Não iniciado. Fila inicial definida neste documento. | |
| S4 | Decisão de território tomada na Fase 0. | `analysis/00-territorios.md` |
| S5 | Parcial. Cluster lycra coletado. | `reports/2026-08-08-semrush-kws-lycra-surf.md` |
| S6 | Duas categorias produzidas fora de ordem, antes desta estratégia. Revisitar contra a matriz de S2. | `content/masculino-lycra-surf.html`, `content/feminino-lycra-surf.html`, `pautas/2026-08-08-lycra-surf-feminina.md` |
| S7 | Não iniciado | |
| S8 | Não iniciado | |
| S9 | Não iniciado | |

Os dois textos de lycra já publicados no repositório nasceram antes da matriz
keyword para URL. Quando S2 fechar, eles voltam para revisão de canibalização
contra `/masculino/lycra-surf/` e `/feminino/lycra-surf/`, que hoje ranqueiam
"surf lycra" na posição 5 e "lycra surf" na 15 pela mesma URL masculina.
