# Lista-semente — sub-bunch de vestidos (território T2)

- **Data**: 2026-08-11 (revisado no mesmo dia, após análise da ficha técnica)
- **Para**: coleta manual no Semrush (base **BR**) e no Planejador de
  Palavras-chave. O saldo de API units da sessão zerou em 2026-08-10.
- **Território**: T2 — Saída de praia e resort
- **Total**: 71 keywords em 1 lote

## Por que este seed existe

A matriz de 860 keywords tem apenas **5 termos com "vestido", somando 3.690
buscas/mês**. As variações de uso nunca entraram na coleta.

| Keyword já medida | Volume | KD | Sustentada por produto? |
|---|---:|---:|---|
| vestido de praia | 2.900 | 14 | sim — hub do sub-bunch |
| vestido de praia curto | 320 | 12 | **não** — ver regra de comprimento |
| vestido praia longo | 260 | 19 | sim |
| vestido resort | 140 | 10 | sim |
| vestido longo saída de praia | 70 | 0 | sim |

## O produto, pela ficha técnica

`VESTIDO RESORT ALÇA CRUZADA` — fonte:
`data/2026-08-10-ficha-tecnica-26-skus.csv` (BaseLinker, coleta de 2026-08-10).

| Atributo | Valor |
|---|---|
| Preço | R$ 199,00 (coletado em 10/08/2026) |
| Estoque | 90 |
| **Comprimento** | **Longo** |
| Composição | 96% viscose, 4% elastano |
| Elasticidade | leve |
| Modelagem | confortável e fluida, não marca |
| Alças | largas cruzadas |
| Bolsos | laterais, funcionais |
| Bojo | não possui |
| Transparência | não — gramatura adequada |
| Tamanhos | P, M, G |
| Fabricação | própria |
| Categoria declarada | vestido casual / saída de praia |
| NCM | 6104.42.00 |

Outros dois SKUs da família aparecem no índice do Google e **não têm ficha
técnica** (leitura qualitativa, `reports/2026-08-10-mapa-urls-categorias.md`):
vestido regata de tule transparente para saída de praia, e saia curta de saída
de praia drapeada em tule.

## Regra de comprimento

**O vestido da marca é longo.** O campo de ficha técnica diz isso de forma
explícita, e é o que define o recorte deste sub-bunch.

Consequências, e elas valem para todos os lotes de T2, não só para o primeiro:

1. **"vestido de praia curto" (320, KD 12) sai da fila como alvo de página.**
   A regra da F3 é clara: cluster sem produto tem fator de catálogo zero e sai
   da fila, por mais busca que tenha. Escrever uma página que promete vestido
   curto para entregar vestido longo gera visita que não compra e devolução
   quando compra.
2. **A dúvida "curto ou longo" continua sendo nossa, dentro do hub.** O artigo
   de `vestido de praia` ganha uma seção que responde a comparação e leva para
   o produto longo. Captura a intenção de consideração sem criar uma página que
   frustra a expectativa.
3. **A demanda de comprimento curto tem outro destino no catálogo**: a saia
   curta de saída de praia. Os termos de saia curta vão para a fila de saída de
   praia, não para a de vestido. Confirmar a ficha técnica dessa peça antes de
   subir.
4. **Prioridade dentro do sub-bunch**: termos com "longo" sobem, mesmo com
   volume menor que os neutros, porque casam com o produto e convertem.

## A regra de recorte de escopo

"Vestido" sozinho pertence a moda em geral, não a beachwear. Quem busca isso
quer festa, trabalho ou casamento, e a marca não tem produto nem autoridade
nessa disputa.

**Entra**: keyword com qualificador de contexto de uso — praia, beach, verão,
resort, piscina, mar, saída de praia — ou material típico da categoria.

**Fica fora**: vestido, vestido longo sem contexto de praia, vestido curto,
vestido midi, vestido de festa, vestido de noiva, vestido social, vestido de
formatura, vestido tubinho, vestido plus size sem qualificador de praia.

**Zona cinzenta, decidir por leitura de SERP antes de subir**: "vestido de
verão", "vestido leve", "vestido soltinho", "vestido fluido". São termos de
estação, não de praia. Se a SERP brasileira trouxer lojas de moda praia, entra;
se trouxer fast fashion, fica fora com o motivo registrado. **Nenhum desses
sobe sem a leitura feita.**

Regra prática: se a keyword faz sentido para alguém que nunca vai à praia, ela
não é nossa. Se ela promete um comprimento que a marca não fabrica, ela também
não é.

## Arquitetura do sub-bunch

- **Hub**: `vestido de praia` (2.900, KD 14) — já está na grade-piloto como
  T2-03. Define a categoria, responde "curto ou longo", recebe os spokes.
- **Spokes**: comprimento longo, material, ocasião, atributo (com bolso, não
  transparente, não marca) e público.
- **Anticanibalização**: `saída de praia` (60.500) é a categoria mãe. Todo
  spoke de vestido linka para o hub de vestido, e o hub linka para a categoria
  de saída de praia.

## Lote de coleta

Cole no Semrush em *Keyword Overview → Bulk Analysis*, base BR, e no
Planejador de Palavras-chave para volume e CPC. Salve o retorno em `data/` e o
resumo de leitura em `reports/`.

### Núcleo praia
vestido de praia; vestido para praia; vestido praia; vestidos de praia;
vestido de praia feminino; vestido praia feminino; vestido saída de praia;
vestido saida de praia; saída de praia vestido; vestido de saída de praia;
vestido para usar na praia

### Comprimento longo — prioridade, casa com o produto
vestido praia longo; vestido de praia longo; vestido longo saída de praia;
vestido longo de praia feminino; saída de praia longa vestido; vestido longo
para praia; vestido longo verão praia; vestido longo resort; vestido longo
fluido praia; vestido longo de viscose praia

### Resort, piscina e férias
vestido resort; vestido resort feminino; vestido para resort; vestido de
piscina; vestido para piscina; vestido para férias praia; vestido para viagem
de praia; vestido para lua de mel praia

### Material e atributo real
vestido de viscose praia; vestido viscose com elastano; vestido de praia que
não marca; vestido de praia com bolso; vestido com bolso longo; vestido de
praia sem transparência; vestido de praia fluido; vestido de tule praia;
vestido de crochê praia; vestido de canga; vestido de linho praia

### Corte e caimento do produto
vestido alça larga praia; vestido alça cruzada; vestido frente única praia;
vestido soltinho praia; vestido chemise praia; vestido regata praia; vestido
drapeado praia

### Ocasião
vestido para casamento na praia; vestido casamento na praia convidada; vestido
para réveillon praia; vestido para almoço na praia

### Público
vestido de praia plus size; vestido praia plus size; vestido de praia
infantil; vestido praia mãe e filha

### Comercial
comprar vestido de praia; vestido de praia preço; loja de vestido de praia;
vestido de praia online; vestido de praia fabricante; melhor vestido de praia

### Informacional para FAQ e AEO
o que vestir na praia; qual vestido usar na praia; o que usar por cima do
biquíni; diferença entre saída de praia e vestido de praia; vestido de praia
curto ou longo; vestido de praia pode molhar; como escolher vestido de praia;
que tecido não gruda no corpo na praia; viscose é fresca; vestido de praia
serve para piscina

### Zona cinzenta — só depois da leitura de SERP
vestido de verão; vestido leve verão; vestido soltinho; vestido fluido;
vestido para o calor

### Fora do lote, registradas como descartadas
vestido de praia curto; vestido praia curto; vestido curto saída de praia —
**sem produto que sustente**. Recoletar apenas se o sortimento passar a ter
vestido curto.

## O que fazer com o retorno

1. Aplicar a regra de escopo e a regra de comprimento, linha a linha, marcando
   cada keyword como `dentro` ou `fora` com o motivo.
2. Checar cada uma contra `producao/registro/kw-donos.csv`.
3. Ordenar por volume decrescente, com os termos de comprimento longo subindo
   no desempate.
4. Registrar as descartadas com o motivo, para não voltarem na coleta seguinte.
