# F3 — Priorização e backlog

- **Data**: 2026-08-10
- **Entradas**: `analysis/11-matriz-kws.md` (demanda de busca),
  `analysis/10-catalogo.md` (catálogo, conversão e receita),
  `reports/2026-08-09-semrush-baseline-dominio.md` (posição atual)
- **Saída**: fila ordenada abaixo + um arquivo por pauta em `pautas/`

## O cálculo

```
prioridade = score de busca × fator de conversão × fator de catálogo ÷ esforço
```

**Score de busca** vem da F2: volume × CTR alcançável por faixa de KD ×
proximidade da conversão por intenção.

**Fator de conversão** = CVR do cluster ÷ CVR da loja (1,61%, medida na semana de
02 a 09/08/2026). Onde o cluster vendeu menos de 3 unidades na semana, o dado é
insuficiente — a semana é o vale sazonal do ano — e o fator vira **1,00 neutro**,
não zero. Penalizar um cluster por não vender biquíni em agosto seria erro de
leitura, não priorização.

**Fator de catálogo**: sortimento completo (10+ SKUs) = 1,0 · sortimento raso
(2 a 9) = 0,8 · SKU único = 0,4 · sem produto = **0**. Cluster sem produto sai da
fila, por mais busca que tenha.

**Esforço**: higiene on-page em URL existente = 1 · otimizar página existente e
adicionar FAQ = 2 · criar categoria ou página nova com conteúdo completo = 4.

## A fila

| # | Cluster | Score | f.Conv | f.Cat | Esforço | **Prioridade** |
|---|---|---:|---:|---:|---:|---:|
| 1 | Lycra, camiseta UV e rash guard | 1.345 | 0,87 | 1,0 | 2 | **585** |
| 2 | Saída de praia e resort | 1.459 | 1,00 | 1,0 | 4 | **365** |
| 3 | Sunga, bermuda e short | 1.633 | 1,00 | 0,8 | 4 | **327** |
| 4 | Biquíni, top e sunkini | 1.036 | 1,00 | 1,0 | 4 | **259** |
| 5 | Maiô (termos genéricos) | 1.016 | 0,56 | 1,0 | 4 | **142** |
| 6 | Poncho, toalha e roupão | 124 | 2,24 | 1,0 | 2 | **139** |
| 7 | Neoprene | 547 | 1,00 | 0,8 | 4 | **109** |
| 8 | Moda praia e surfwear | 356 | 1,00 | 1,0 | 4 | **89** |
| 9 | Calçado aquático | 846 | 1,00 | 0,4 | 4 | **85** |
| — | Canga e acessórios | 120 | 1,00 | **0,0** | 4 | **0** |

Duas leituras que a fórmula torna explícitas:

**Maiô cai para quinto** apesar de ser 41% da receita, porque converte a 0,9%
contra 1,61% da loja. O fator de 0,56 é a penalidade por mandar mais tráfego para
um funil que vaza. Ele sobe assim que a conversão for corrigida — a fila se
reordena sozinha na F6.

**Poncho sobe para sexto** com o menor score de busca da fila inteira (124),
porque converte a 3,6% e o trabalho é higiene, não produção. É o único item da
lista onde o retorno vem de arrumar o que existe.

## As três ondas

### Onda 0 — Higiene (dias, sem produção de conteúdo)

Não entra na fila de prioridade porque não compete por recurso de redação. Sai na
frente de tudo.

| Item | O quê | Por quê |
|---|---|---|
| H1 | Corrigir title, H1 e primeiro parágrafo de `/feminino/biquini/sunkini/` para "sunkini" | Ranqueia "subikini" (210 buscas) na posição 8 e "sunkini" (1.600, KD 13) na posição 24. Grafia errada priorizada sobre a certa. |
| H2 | Resolver canibalização do poncho: definir dona entre `/masculino/poncho/` e `/feminino/poncho1/`, redirecionar a outra | Duas URLs disputando o cluster que gera 54% da receita. O slug `poncho1` ainda carrega sufixo numérico. |
| H3 | Criar destino para poncho infantil | "poncho toalha infantil" (590, KD 9) e "toalha com capuz infantil" (1.000) sem categoria. O Poncho Premium Infantil é o produto nº 1 do catálogo. |
| H4 | Desindexar `/search/?q=` | Página de busca interna indexada e ranqueando. |
| H5 | Repor estoque das 7 variantes zeradas que venderam | Poncho Premium Infantil azul 6–12 vendeu 13 e zerou. Tráfego para produto esgotado queima verba e sinal. |

H3 e H5 são a mesma oportunidade vista de dois ângulos: a demanda de busca
infantil e a venda infantil coincidem, e hoje nem a página existe nem o produto
está disponível.

### Onda 1 — Produção de conteúdo, na ordem da fila

Itens 1 a 7 da tabela. Ver calendário abaixo para a ordem de publicação, que
**não é a mesma da prioridade** — a sazonalidade reordena.

### Onda 2 — Bloqueada por decisão fora do SEO

| Item | Bloqueio |
|---|---|
| Canga e acessórios (15.580 buscas) | Não existe canga no catálogo. Decisão de sortimento. |
| Calçado aquático (36.160 buscas) | SKU único. Vira categoria só se o sortimento crescer. |
| Natação (30.120 buscas) | Por decisão de 2026-08-10, não ganha território próprio. Entra como atributo dentro de maiô, bermuda de neoprene e lycra. |

## O calendário manda na ordem de publicação

SEO leva de três a seis meses para ranquear. Hoje é 10 de agosto de 2026. O que
for publicado agora chega ranqueado entre dezembro e janeiro — exatamente a
tempo do pico de fevereiro a abril, quando quase todo o catálogo multiplica a
demanda por três ou quatro.

| Cluster | Pico | Índice no pico | Índice em ago | Publicar até |
|---|---|---:|---:|---|
| Rash guard / camiseta UV | estável o ano todo | 1,00 (dez–abr) | 0,44 | **agora** |
| Saída de praia | fevereiro | 0,81 | 0,16 | setembro |
| Sunga masculina | março | 0,81 | 0,24 | setembro |
| Canga de praia | março | 1,00 | 0,20 | setembro |
| Poncho | março | 1,00 | 0,10 | setembro |
| Maiô de praia | março–abril | 0,81 | 0,13 | outubro |
| Biquíni | março–julho | 0,44 | 0,24 | outubro |
| Long john / neoprene | **agosto–setembro** | 0,65 | 0,65 | **março de 2027** |

**Rash guard sai primeiro por dois motivos que coincidem**: é o item de maior
prioridade da fila (585) e é o único cluster relevante sem vale sazonal — índice
entre 0,44 e 1,00 o ano inteiro, contra 0,10 a 0,16 do resto em agosto. Ele
começa a devolver tráfego assim que ranqueia, sem esperar a temporada.

**Neoprene é o caso invertido e merece atenção**: é o único cluster que está no
pico agora, em agosto. Publicar conteúdo orgânico hoje entrega ranqueamento em
janeiro, quando long john cai para 0,29. Então **neoprene é território de mídia
paga agora e de orgânico em março** — o que valida a escolha da linha neoprene
como campanha inaugural no repositório `search-mkt`, onde o resultado é imediato.

## Backlog de pautas

Pautas abertas nesta fase, uma por arquivo:

| Arquivo | Cluster | Prioridade |
|---|---|---:|
| `pautas/2026-08-10-onda-0-higiene.md` | — | Onda 0 |
| `pautas/2026-08-10-rash-guard.md` | Lycra, camiseta UV e rash guard | 585 |
| `pautas/2026-08-10-saida-de-praia.md` | Saída de praia e resort | 365 |
| `pautas/2026-08-10-sunga-masculina.md` | Sunga, bermuda e short | 327 |
| `pautas/2026-08-08-lycra-surf-feminina.md` | Lycra (pauta anterior, já executada) | — |

Pautas de biquíni, maiô genérico, poncho e neoprene abrem quando as quatro
acima estiverem em produção, para não estourar a fila de redação.

## Como esta fila se reordena

Na F6, mensalmente, três coisas mexem na ordem:

1. **Conversão medida** substitui os fatores neutros de 1,00. Os clusters de
   verão só têm CVR real depois de dezembro.
2. **Posição alcançada** recalibra a associação KD → posição, que hoje é
   julgamento e é o elo mais frágil do cálculo.
3. **Receita por cluster com 12 meses** do BaseLinker troca a proxy de conversão
   por margem real, que é o objetivo do projeto.
