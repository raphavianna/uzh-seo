# Editorias

- **Data**: 2026-08-11
- **Entradas**: `analysis/11-matriz-kws.md` e
  `data/2026-08-10-matriz-kws-classificada.csv` (Semrush BR, 2026-08-09),
  `analysis/12-priorizacao.md` (fila, ondas e calendário),
  `analysis/10-catalogo.md` (venda e CVR por cluster)
- **Natureza dos números**: volume, KD, intenção e SERP feature são medidos
  pelo Semrush. Sessões e score são calculados pela fórmula da F2.

Editoria não é tema: é um compromisso de cobertura. Cada uma captura um tipo
de intenção, tem cluster de origem, página de destino e caminho até a venda.
Pauta que não cabe em nenhuma editoria não entra no backlog — ou a editoria
muda, com o número que justifica, ou a pauta cai.

## O que os dados obrigam

**A SERP deste mercado pergunta e ninguém responde.** Em 860 keywords: 273
com People Also Ask, 37 com AI Overview e **zero featured snippet**. São
**138 keywords com PAA ou AI Overview e volume igual ou acima de 300** — cada
uma é um bloco de FAQ que hoje não existe em lugar nenhum do site.

Isso define a arquitetura das editorias: **toda editoria carrega bloco de
FAQ com `FAQPage`**, e a camada AEO entra junto do conteúdo, não depois.

**O vocabulário de entrada é moda praia, a diferenciação é surf.** 92,8% do
volume do mercado está em termos sem a palavra "surf". Quem busca "saída de
praia" e encontra uma marca de surf com foto real converte; quem busca e não
encontra a marca não converte nunca. As editorias entram pelo termo que as
pessoas digitam e entregam o diferencial dentro da página.

## Demanda por cluster

Volume único, escopo dentro, variantes gráficas excluídas.

| Cluster | KWs | Volume/mês | PAA | AIO | Prioridade F3 |
|---|---:|---:|---:|---:|---:|
| Saída de praia e resort | 48 | 87.400 | 25 | 1 | 365 (2º) |
| Sunga, bermuda e short | 48 | 74.720 | 13 | 1 | 327 (3º) |
| Lycra, camiseta UV e rash guard | 105 | 55.740 | 29 | 4 | 585 (1º) |
| Maiô | 61 | 42.420 | 5 | 0 | 142 (5º) |
| Biquíni e top | 52 | 41.020 | 12 | 0 | 259 (4º) |
| Calçado aquático | 58 | 36.160 | 33 | 1 | 85 (bloqueado: SKU único) |
| Natação e mergulho | 83 | 30.120 | 55 | 7 | atributo, sem território próprio |
| Moda praia e surfwear | 58 | 21.900 | 23 | 9 | 89 |
| Neoprene | 118 | 18.500 | 36 | 3 | 109 (orgânico só em março) |
| Canga e acessórios | 5 | 15.580 | 2 | 0 | 0 (sem produto) |
| Poncho, toalha e roupão | 61 | 4.580 | 7 | 0 | 139 (6º) |

Duas leituras que a tabela força:

**Natação tem 55 PAA e 7 AIO, o maior índice de pergunta da base inteira**, e
por decisão de 2026-08-10 não ganha território próprio. Ela entra como
atributo dentro de maiô, bermuda de neoprene e lycra. A editoria E2 é onde
esse volume de pergunta vira conteúdo sem criar categoria nova.

**Poncho tem 4.580 buscas e faz 54% da receita da loja, com CVR de 3,6%.** É
o inverso de tudo o mais na tabela. A editoria E3 existe por causa disso: o
cluster não se justifica por volume de busca, se justifica por conversão.

## As cinco editorias

### E1 — Escolha e caimento

**Captura**: intenção comercial e transacional. Quem já quer comprar e trava
em qual modelo, qual tamanho, como veste.

**Clusters**: saída de praia, sunga/bermuda, lycra/rash guard, biquíni, maiô.

**Formato**: texto de categoria e guia de escolha, com FAQ e `FAQPage`.

**Destino**: a página de categoria do cluster, com CTA para produto.

**Conversão**: a busca já é de compra. O conteúdo remove a insegurança de
escolher errado, que é a única coisa entre a pessoa e o carrinho. É a
editoria de conversão mais curta, e por isso abre todo ciclo.

**Exemplo do cluster**: o guia informacional de rash guard é o T1-06 do lote
de agosto (`content/o-que-e-rash-guard.html`), E2 sobre o cluster de maior
prioridade. O rascunho antigo `content/rash-guard.html` foi arquivado em
2026-08-12: era a página de produto da URL `/rash-guard/`, que a coleta do
catálogo (`reports/2026-08-12-catalogo-nuvemshop.md`) confirmou não existir.

### E2 — Proteção solar, água e pele

**Captura**: informacional com cauda comercial. O que significa UV50+, se a
proteção resiste à lavagem, se funciona molhada, o que serve para natação,
hidroginástica e mergulho.

**Clusters**: lycra/rash guard (29 PAA, 4 AIO) e natação (55 PAA, 7 AIO, o
maior índice de pergunta da base).

**Formato**: editorial com dado verificável — fator de proteção, composição
do tecido, se a barreira é da trama ou de acabamento químico. Motor de
resposta cita especificidade; texto sem número não é citado.

**Destino**: categoria de lycra e camiseta UV; dentro de maiô quando o
recorte for natação.

**Conversão**: captura quem ainda não decidiu comprar peça e entrega o
argumento que transforma protetor solar em roupa. Funil médio, conversão no
segundo contato.

**É a maior aposta de AEO do projeto**, porque concentra o maior volume de
pergunta da base num cluster onde a marca tem 26 SKUs e ficha técnica.

### E3 — Rotina de água

**Captura**: informacional de nicho. Trocar de roupa na praia, o que levar na
sessão, como lavar e secar, tirar parafina, o que fazer com a peça molhada.

**Clusters**: poncho (54% da receita, CVR 3,6%) e o transbordo de cuidado das
outras peças.

**Formato**: editorial curto e prático, muito citável, com FAQ.

**Destino**: a categoria de poncho, depois que a Onda 0 resolver qual das
três URLs é a dona.

**Conversão**: vende o poncho sem falar de poncho. O produto aparece como
solução de um problema real, e a abertura lateral para troca de roupa é o
diferencial concreto que nenhum concorrente descreve na SERP brasileira.

**Depende da Onda 0.** Escrever para um cluster que canibaliza em três URLs
divide sinal em vez de somar.

### E4 — Corpo e movimento

**Captura**: comercial de uso específico. Peça que não sai do lugar em surf,
beach tennis, futevôlei, natação, corrida.

**Clusters**: biquíni e top (52 KWs, 41.020 buscas), sunga/bermuda, e o
cruzamento com calçado aquático quando o sortimento crescer.

**Formato**: comparativo e guia por atividade.

**Destino**: biquíni esportivo, sunga, maiô.

**Conversão**: separa a marca da moda praia genérica ao disputar quem
pratica, não quem posa. É onde o posicionamento de surf paga o preço mais
alto sem precisar da palavra "surf" no termo de entrada.

### E5 — Entidade e território de marca

**Captura**: navegacional e de entidade. 34 keywords, 70 buscas/mês — volume
irrelevante, função crítica.

**Formato**: institucional, `Organization` na home, e o ângulo narrativo
"surf de zero hora", a sessão de madrugada.

**Destino**: home e institucionais.

**Conversão**: defende o tráfego que já converte e desambigua "Use Zero Hora"
do jornal do Grupo RBS para Google e para motores de resposta. Manutenção,
não crescimento. Uma pauta por trimestre, fora da conta do ciclo.

## Mistura por ciclo

Cada ciclo entrega **duas peças**: uma de E1 (fundo, conversão curta) e uma
de E2, E3 ou E4 (meio, autoridade e AEO). E5 entra uma vez por trimestre,
fora da conta.

A regra existe para impedir os dois modos de falha conhecidos: só fundo de
funil, e o site nunca vira fonte de resposta apesar de 138 keywords com PAA
ou AIO esperando; só topo, e o conteúdo não paga a própria produção em venda.

## Ordem de execução

O calendário sazonal manda, não a prioridade da fila
(`analysis/12-priorizacao.md`). Hoje é agosto, e o que for publicado agora
chega ranqueado entre dezembro e janeiro, a tempo do pico de fevereiro a
abril.

| Ciclo | E1 | Segunda peça | Publicar até |
|---|---|---|---|
| 01 (ago) | Rash guard ✅ entregue | E2 — proteção solar, do mesmo cluster | agora |
| 02 (set) | Saída de praia | E4 — sunga e short por atividade | setembro |
| 03 (out) | Biquíni por modelagem | E3 — rotina de água (depende da Onda 0) | outubro |

Neoprene fica fora até março: é o único cluster no pico agora, e conteúdo
orgânico publicado em agosto ranqueia em janeiro, quando long john cai para
0,29. Até lá é território de mídia paga, no repositório `search-mkt`.

## Bloqueio comum a E1, E2 e E4

Ficha técnica. As três editorias dependem de atributo real de produto, e a
cobertura hoje é de 26 SKUs em 120. Ver `analysis/22-ficha-tecnica.md` para
o que falta por cluster e em que ordem pedir.
