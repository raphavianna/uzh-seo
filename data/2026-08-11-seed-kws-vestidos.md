# Lista-semente — sub-bunch de vestidos (território T2)

- **Data**: 2026-08-11
- **Para**: coleta manual no Semrush (base **BR**) e no Planejador de
  Palavras-chave. O saldo de API units da sessão zerou em 2026-08-10.
- **Território**: T2 — Saída de praia e resort
- **Total**: 78 keywords em 1 lote

## Por que este seed existe

A matriz de 860 keywords tem apenas **5 termos com "vestido", somando 3.690
buscas/mês**. As variações de uso — praia, verão, resort, piscina — nunca
entraram na coleta. O catálogo tem vestido resort e vestido de tule para saída
de praia, então há produto para sustentar o cluster.

| Keyword já medida | Volume | KD |
|---|---:|---:|
| vestido de praia | 2.900 | 14 |
| vestido de praia curto | 320 | 12 |
| vestido praia longo | 260 | 19 |
| vestido resort | 140 | 10 |
| vestido longo saída de praia | 70 | 0 |

## A regra de recorte

O problema com "vestido" é que a palavra sozinha pertence a moda em geral, não
a beachwear. "Vestido" e "vestido longo" trazem volume alto e intenção errada:
quem busca isso quer festa, trabalho ou casamento, e a Use Zero Hora não tem
produto nem autoridade nessa disputa. Tráfego que não compra beachwear custa
produção e não devolve venda.

**Entra no escopo** a keyword que carrega um qualificador de contexto de uso:
praia, beach, verão, resort, piscina, mar, saída de praia, sunga/biquíni por
proximidade, ou material típico da categoria (tule, crochê, canga, laise).

**Fica fora** a keyword de moda ampla, mesmo com volume alto: vestido, vestido
longo, vestido curto, vestido midi, vestido de festa, vestido de noiva,
vestido social, vestido de formatura, vestido casual, vestido tubinho, vestido
de malha, vestido plus size sem qualificador de praia.

**Zona cinzenta, decidir por leitura de SERP antes de subir**: "vestido de
verão", "vestido leve", "vestido soltinho", "vestido fluido". São termos de
estação, não de praia. Se a SERP brasileira trouxer lojas de moda praia, entra
em T2; se trouxer fast fashion, fica fora e o volume vai para o registro de
descartados. **Não subir nenhum desses sem a leitura feita.**

Regra prática, para valer em todos os lotes e não só no primeiro: se a
keyword faz sentido para alguém que nunca vai à praia, ela não é nossa.

## Arquitetura do sub-bunch

Hub e spoke dentro de T2, para não fragmentar sinal:

- **Hub**: `vestido de praia` (2.900, KD 14) — já está na grade-piloto como
  T2-03. Vira a página que define a categoria e recebe os links dos spokes.
- **Spokes**: comprimento (curto, longo, midi de praia), material (tule,
  crochê, laise, canga), ocasião (resort, piscina, réveillon, casamento na
  praia) e público (plus size, infantil).
- **Anticanibalização**: `saída de praia` (60.500) continua dona da categoria
  mãe. O sub-bunch de vestidos é filho dela, e todo spoke de vestido linka
  para o hub de vestido, que linka para a categoria de saída de praia.

## Lote de coleta

Cole no Semrush em *Keyword Overview → Bulk Analysis*, base BR, e no
Planejador de Palavras-chave para volume e CPC. Salve o retorno em
`data/` e o resumo de leitura em `reports/`.

### Núcleo praia
vestido de praia; vestido para praia; vestido praia; vestidos de praia;
vestido de praia feminino; vestido praia feminino; vestido de praia curto;
vestido praia curto; vestido praia longo; vestido de praia longo; vestido
longo saída de praia; vestido curto saída de praia; vestido saída de praia;
vestido saida de praia; saída de praia vestido; vestido de saída de praia

### Resort e piscina
vestido resort; vestido resort feminino; vestido para resort; vestido de
piscina; vestido para piscina; vestido para usar na piscina; vestido de
verão praia; vestido para o mar

### Material
vestido de tule praia; vestido tule transparente; vestido de crochê praia;
vestido de crochê saída de praia; vestido de laise praia; vestido canga;
vestido de canga; vestido de linho praia; vestido transparente praia; vestido
de renda praia

### Ocasião
vestido para casamento na praia; vestido casamento na praia convidada;
vestido para réveillon praia; vestido para lua de mel praia; vestido para
viagem de praia; vestido para férias praia

### Corte e caimento
vestido soltinho praia; vestido fluido praia; vestido frente única praia;
vestido tomara que caia praia; vestido de alça praia; vestido regata praia;
vestido chemise praia; vestido camisão praia; vestido drapeado praia

### Público
vestido de praia plus size; vestido praia plus size; vestido de praia
infantil; vestido praia mãe e filha; vestido de praia juvenil

### Comercial
comprar vestido de praia; vestido de praia preço; vestido de praia barato;
loja de vestido de praia; vestido de praia online; melhor vestido de praia

### Informacional para FAQ e AEO
o que vestir na praia; qual vestido usar na praia; o que usar por cima do
biquíni; diferença entre saída de praia e vestido de praia; vestido de praia
pode usar molhado; como escolher vestido de praia; que tecido não gruda no
corpo na praia; vestido de praia serve para piscina

### Zona cinzenta — só depois da leitura de SERP
vestido de verão; vestido leve verão; vestido soltinho; vestido fluido;
vestido para o calor

## O que fazer com o retorno

1. Aplicar a regra de recorte acima, linha a linha, e marcar cada keyword como
   `dentro` ou `fora` com o motivo.
2. Checar cada uma contra `producao/registro/kw-donos.csv`.
3. Ordenar por volume decrescente e mesclar na fila de T2, respeitando a
   arquitetura hub e spoke.
4. Registrar as descartadas com o motivo, para não voltarem na coleta seguinte.
