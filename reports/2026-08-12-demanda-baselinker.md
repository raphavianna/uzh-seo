# Demanda medida por venda — fator de catálogo (7 meses)

- **Coletado em**: 2026-08-12
- **Fonte**: `zerohora-painel/public/data/vendas.json` (BaseLinker via getOrders, BaseMestre v6)
- **Período**: 2026-01-01 a 2026-08-10 (manifest versao_dados 3)
- **Natureza**: medido. Venda líquida (aprovada, sem cancelamento/devolução), todos os canais
- **Escopo**: 7829 linhas válidas de 8174, R$ 1,034,901.14

Substitui o export de 1 semana da Nuvemshop como sinal de demanda. Sete
meses e todos os canais (Mercado, Shopee, Shein, TikTok, Site) em vez de
uma semana de uma loja só.

## Receita por canal

| Canal | Receita | Share |
|---|---:|---:|
| Mercado | R$ 667,584.04 | 64.5% |
| Site | R$ 245,348.79 | 23.7% |
| Shopee | R$ 84,388.25 | 8.2% |
| Shein | R$ 34,581.31 | 3.3% |
| TikTok | R$ 2,998.75 | 0.3% |

## Demanda por cluster SEO (fator de catálogo)

O fator de catálogo do projeto pondera a fila de pautas pela venda real
do cluster. Cluster que vende sustenta conteúdo que converte; cluster sem
venda vira visita que não compra.

| Cluster | Unidades | Receita | Share receita | Fator (0-1) |
|---|---:|---:|---:|---:|
| Poncho, toalha e roupão | 4,097 | R$ 523,913.62 | 50.6% | 1.00 |
| Maiô | 1,651 | R$ 308,031.26 | 29.8% | 0.59 |
| Saída de praia, resort e vestidos | 1,151 | R$ 88,009.41 | 8.5% | 0.17 |
| Lycra, camiseta UV e rash guard | 544 | R$ 63,251.61 | 6.1% | 0.12 |
| Biquíni e top | 297 | R$ 29,868.31 | 2.9% | 0.06 |
| Outros | 95 | R$ 10,354.12 | 1.0% | 0.02 |
| Ioga e fitness | 51 | R$ 6,624.44 | 0.6% | 0.01 |
| Sunga, bermuda e short | 43 | R$ 3,019.80 | 0.3% | 0.01 |
| Moletom e casaco | 18 | R$ 1,828.57 | 0.2% | 0.00 |

## O que isto muda na priorização

- **Poncho lidera a receita com folga** (R$ 523 mil, 46% do total). A editoria
  E3, que existe por conversão e não por volume de busca, ganha o número que
  a sustenta. Poncho infantil, com categoria confirmada no catálogo, herda esse peso.
- **Maiô é o segundo** (R$ 308 mil). Casa com `/feminino/maio/` ser 42% do orgânico:
  o ativo número um vende e ranqueia.
- **O cluster do lote T1** (camiseta lycra) fez R$ 63 mil em categoria e R$ 89 mil
  no recorte por produto. É demanda real, não hipótese — sustenta a ordenação
  do T1-06 por venda e o destino comercial de rash guard em `/masculino/lycra-surf/`.
- **Ioga/fitness vendeu R$ 6,6 mil** com 51 unidades. Pequeno, mas existe: tira
  a frente de yoga do 'sem lastro' do parking-lot.

## Ressalva

Base pseudonimizada: `id_cliente` opaco, sem PII. Uso agregado por categoria e
SKU apenas. A correspondência id→identidade pertence ao CRM e não entra aqui.