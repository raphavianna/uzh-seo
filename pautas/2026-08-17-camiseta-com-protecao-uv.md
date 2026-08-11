# Pauta — Camiseta com proteção UV: qual escolher por uso

- **ID na grade**: T1-04 · **Território**: T1 (Lycra, camiseta UV e rash guard)
- **Data**: 2026-08-17 · **Publicação agendada**: 2026-08-24
- **Modo**: CRIAÇÃO
- **Editoria**: E2 — Proteção solar, água e pele (`analysis/21-editorias.md`)
- **Dados**: `data/2026-08-10-matriz-kws-classificada.csv` (Semrush BR, coleta
  de 2026-08-09) · ficha técnica: `data/2026-08-10-ficha-tecnica-26-skus.csv`
  (BaseLinker, coleta de 2026-08-10)
- **URL prevista**: `https://usezerohora.com.br/blog/camiseta-com-protecao-uv/`
  (confirmado pelo usuário em 2026-08-11: a raiz do blog é https://usezerohora.com.br/blog/)

## Nota de ordem na fila

A grade coloca esta linha em T1-04 e `camisa de praia feminina` em T1-03, as
duas com 880 buscas/mês. Pela regra de desempate por KD, esta deveria vir
antes: KD 13 contra 19. Mantive a ordem da grade porque cada ID carrega data
de publicação fixa, e reordenar mexeria no calendário sem ganho.

**Correção para E1**: aplicar o desempate por KD dentro do mesmo volume ao
montar a grade de setembro.

## Oportunidade

`camiseta com proteção uv` traz **880 buscas/mês, KD 13, intenção
Informacional, com People Also Ask e sem featured snippet** (Semrush BR,
2026-08-09).

O conjunto soma **1.970 buscas/mês em 8 keywords, 5 com PAA e nenhuma com
featured snippet**.

Esta é a terceira peça de T1 no lote, e o que a justifica é o eixo que ela
ocupa. T1-01 organiza o cluster pelo mecanismo da proteção, T1-03 pelo público
feminino, e esta pelo **uso**: surf, piscina, praia e dia a dia. Três eixos
distintos sobre o mesmo cluster somam cobertura; três artigos sobre o mesmo
eixo dividiriam sinal.

## Keywords

| Papel | Keyword | Volume | KD | Intenção | PAA |
|---|---|---:|---:|---|:--:|
| **Primária** | camiseta com proteção uv | 880 | 13 | Informacional | sim |
| Secundária | camiseta proteção solar | 480 | 21 | Comercial | sim |
| Secundária | camiseta para piscina | 140 | 23 | Comercial | sim |
| Secundária | camisa de lycra | 110 | 10 | Inform. + Comercial | sim |
| Secundária | camiseta uv 50 masculina | 110 | 10 | Comercial | sim |
| Secundária | camiseta de lycra | 90 | 8 | Inform. + Comercial | sim |
| Secundária | camiseta de praia masculina | 90 | 17 | Comercial | não |
| Cauda | camiseta uv50 | 70 | dado indisponível | dado indisponível | não |

Total: **1.970 buscas/mês**. Fonte:
`data/2026-08-10-matriz-kws-classificada.csv`.

**Deixada de fora de propósito**: `camiseta surf` (720, KD 8, Comercial,
livre) é a keyword de maior volume livre em T1 e caberia aqui. Ela fica de
fora porque é o candidato que a pauta de bloqueio de T1-02
(`pautas/2026-08-13-surf-lycra-BLOQUEIO.md`) propõe para a substituição
daquela linha em E1. Consumi-la agora tiraria a opção do time.

**Também de fora**: `camiseta uv com ziper` (70, livre). Nenhuma camiseta da
ficha técnica tem zíper; o fecho aparece só nos maiôs body. Sem produto que
responda à consulta, a keyword fica na fila até o catálogo cobrir.

**Checagem de dono** (`producao/registro/kw-donos.csv`, 33 linhas, consulta de
2026-08-17):

- Primária livre? **Sim.**
- As oito keywords acima estão livres.
- Secundárias descartadas por já terem dono, que viram âncora de link:

| Keyword | Volume | URL dona |
|---|---:|---|
| camisa uv | 8.100 | `/rash-guard/` |
| camiseta uv | 3.600 | `/rash-guard/` |
| camiseta uv masculina | 2.900 | `/rash-guard/` |
| camiseta uv masculina manga longa | 590 | `/rash-guard/` |
| camiseta surf masculina | 480 | `/masculino/lycra-surf/` |
| lycra surf | 880 | `/masculino/lycra-surf/` |
| camiseta uv infantil | 720 | `/rash-guard/` |

## Anticanibalização

**Pertence a esta página**: a escolha da camiseta por atividade. Qual peça
para surf, qual para piscina, qual para praia e dia a dia, e o que o cloro faz
com o tecido.

**Pertence a T1-01 e aqui só aparece como link**: o mecanismo da proteção. O
que significa UV50+, se a barreira sai na lavagem, se funciona molhada. Esta
página resume em uma frase e manda para o hub.

**Pertence a T1-05 e aqui só aparece como link**: a peça infantil. Esta página
não abre seção de criança.

Corte entre as três peças de T1 do lote:

| | T1-01 | T1-03 | T1-04 (esta) |
|---|---|---|---|
| Eixo | mecanismo | público feminino | **uso e atividade** |
| Intenção | Informacional | Comercial | Informacional |
| Editoria | E2 | E1 | E2 |
| Papel | hub | spoke | spoke |

Nenhum termo com "blusa", "camisa de praia" ou "feminina" entra nesta pauta.

## Intenção e funil

- **Intenção**: informacional com cauda comercial. Quem digita "camiseta com
  proteção uv" quer saber qual modelo serve para o que ela faz.
- **Funil**: meio.
- **Conversão**: o artigo entrega o critério por atividade e joga para
  `/masculino/lycra-surf/` e `/rash-guard/`, onde as peças estão à venda.

## Estrutura

- **H1**: Camiseta com proteção UV: qual escolher para cada uso
- **Primeiro parágrafo**: define a peça e o critério de escolha em três frases
  autocontidas.

**H2 / H3** (abertura autocontida de 2 a 4 frases em cada):

1. O que é uma camiseta com proteção UV → resumo + link para T1-01
2. Camiseta proteção solar para surf → Pipeline
3. Camiseta para piscina: o que o cloro faz → resistência ao cloro
4. Camiseta de praia masculina para o dia a dia → Backdoor
5. Camiseta UV 50 masculina: qual manga para qual uso → `camiseta uv 50 masculina`, `camiseta uv50`
6. Camisa de lycra ou camiseta de lycra: o que muda no nome → `camisa de lycra`, `camiseta de lycra`
7. Como lavar e guardar
8. Como escolher: tabela por atividade
9. FAQ com `FAQPage`

**FAQ**:

- Camiseta com proteção UV pode entrar na piscina?
- Qual camiseta com proteção UV usar para surfar?
- Camiseta UV50 e camiseta UV50+ são a mesma coisa?
- Camisa de lycra e camiseta de lycra são a mesma peça?
- Como lavar camiseta com proteção UV?
- Camiseta com proteção UV serve para pescar?

## Produtos e atributos

Fonte única: `data/2026-08-10-ficha-tecnica-26-skus.csv` (BaseLinker,
2026-08-10). Preços da mesma coleta.

| SKU | Atributos que a ficha sustenta | Preço (2026-08-10) | Pendências |
|---|---|---|---|
| CAMISETA PIPELINE | UV50+ permanente; até 98%; 88% poliamida / 12% elastano; manga longa; costuras anatômicas contra atrito; compressão leve; resistência a cloro e água salgada; indicada para surf, natação, SUP, canoa havaiana, pesca esportiva; 0,24 kg; estoque 192 | R$ 299,99 | gramatura; secagem em minutos; **instruções de lavagem ausentes** |
| CAMISETA BACKDOOR | UV50+ permanente; até 98%; 88% poliamida / 12% elastano; manga curta; elasticidade multidirecional; alta respirabilidade; indicada para surf, natação, SUP, beach tennis, corrida, pesca; 0,22 kg; estoque 134 | R$ 299,00 | conflito de nome BACKDOOR / "Maresias" na base; gramatura; lavagem |
| CAMISETA NEOPRENE CABO FRIO | neoprene Span/Flex 1,5 mm; mangas e gola em poliamida com elastano UV50+; flatlock; resistência a cloro e água salgada; **instruções de lavagem completas na ficha** | R$ 499,99 | — |

**Sobre lavagem**: a ficha técnica traz instruções de cuidado só para a
Camiseta Neoprene Cabo Frio (lavar à mão em água fria, sem alvejante, secar à
sombra, sem secadora, sem passar, não guardar úmida). Para as lycras, as
instruções são **dado indisponível**. O texto atribui as instruções à peça que
as declara e não as estende às outras por analogia.

Citável como contexto:

| SKU | Atributo usado | Preço (2026-08-10) |
|---|---|---|
| MAIO LYCRA JOHN | 300 g/m²; alta resistência a cloro e água salgada; UV50+ | R$ 399,99 |

## Imagens

`midia-produtos` segue vazio (consulta de 2026-08-17).

| Ponto de inserção | SKU | Alt previsto |
|---|---|---|
| Seção de surf | CAMISETA PIPELINE | Camiseta com proteção UV masculina manga longa para surf |
| Seção de dia a dia | CAMISETA BACKDOOR | Camiseta de praia masculina manga curta com proteção UV50+ |

## Links internos

- **Para a categoria**: `/masculino/lycra-surf/` (âncoras: lycra surf, camiseta
  surf masculina), `/rash-guard/` (âncoras: camiseta uv, camisa uv, camiseta uv
  masculina)
- **Para o conteúdo irmão**: `/blog/blusa-com-protecao-uv/` (T1-01), como hub
  do mecanismo de proteção
- **Para o produto**: **pendência.** Slugs não confirmados. CTA para categoria.
- **Das peças irmãs para esta**: T1-01 ganha link na seção de manga quando o
  lote for aprovado em E4.

## Checagens antes de publicar

1. Pedir ao time as instruções de lavagem das três lycras. Sem elas, a seção
   de cuidado fica presa ao neoprene.
2. Resolver o conflito BACKDOOR / Maresias.
3. ~~Confirmar o caminho do blog.~~ **Resolvido em 2026-08-11**: a raiz é
   `https://usezerohora.com.br/blog/`. Falta garantir que o slug criado no CMS
   seja `camiseta-com-protecao-uv`, e confirmar os slugs de produto.
4. Em E4, checar que esta página e T1-01 não repetem a explicação do UV50+
   além do resumo de uma frase.
