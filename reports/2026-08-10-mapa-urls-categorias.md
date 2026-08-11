# Snapshot 2026-08-10 — Mapa de URLs e categorias do site

Fecha parcialmente a lacuna declarada no gate da F1: o export de vendas do
Nuvemshop não trouxe URL nem categoria por SKU (`analysis/10-catalogo.md`).
Este mapa traz a taxonomia como o Google a enxerga.

- **Fonte**: leitura de SERP via WebSearch, restrita a `usezerohora.com.br`
  (operador `site:`), 2026-08-10. Natureza: **qualitativa**, declarada como
  tal pela regra 4 de `<fontes_de_dados>`.
- **Limitação**: o acesso direto ao domínio está bloqueado pelo proxy de rede
  desta sessão e o MCP da Nuvemshop não está conectado a este ambiente. O que
  está abaixo é o que o índice do Google expõe — não é dump do CMS. Confirmar
  a taxonomia completa no admin antes de fechar o gate da F1.

## Taxonomia observada

| Caminho | Subcategorias | Cluster da F2 |
|---|---|---|
| `/feminino/` | `maio/`, `biquini/` (marquinha, asa delta, hot pant, `sunkini/`), lycra surf, poncho, camiseta UV50+, `saida-de-praia/` → `conjunto-atoalhado/` | Maiô, Biquíni, Saída de praia, Lycra |
| `/masculino/` | `lycra-surf/`, `poncho/`, camiseta UV50+, bermuda, moletom, sunga | Lycra, Poncho, Sunga |
| `/infantil/` | sem categoria própria observada — apenas produtos avulsos | — |
| `/roupas-e-acessorios/` | `linha-surf/` → `poncho/`, `lycra/`; `conjunto-atoalhado/` | Poncho, Lycra, Saída de praia |
| `/ioga-fitness/` | calça, macaquinho | Fora de linha |
| Institucional | `/quem-somos/`, `/trocas-e-devolucoes/`, `/search/` | — |

## Três confirmações para a Onda 0

O mapa confirma, por evidência de URL, três dos cinco itens de higiene já
abertos em `pautas/2026-08-10-onda-0-higiene.md`:

1. **H2 — canibalização do poncho é mais ampla do que duas URLs.** Além de
   `/masculino/poncho/` e `/feminino/poncho1/`, o cluster tem uma terceira
   trilha: `/roupas-e-acessorios/linha-surf/poncho/`. São três URLs
   disputando o cluster que gera 54% da receita da loja.
2. **H3 — não existe categoria infantil.** Nenhuma URL `/infantil/` apareceu
   no índice; o poncho infantil é servido por URL de produto. Confirma o
   diagnóstico da F3, e o produto nº 1 da curva ABC (Poncho Premium Infantil,
   17 unidades na semana) não tem categoria para ranquear.
3. **H4 — `/search/?q=` está indexada.** `/search/?q=biquini+maio` aparece no
   índice, como o baseline já apontava.

**Achado novo**: `conjunto-atoalhado` também responde por duas trilhas —
`/feminino/saida-de-praia/conjunto-atoalhado/` e
`/roupas-e-acessorios/conjunto-atoalhado/`. Entra na Onda 0 como H6, mesma
natureza de H2: definir a dona, redirecionar a outra. Custa o mesmo trabalho
e o cluster de saída de praia é o segundo da fila da F3.

## Divergência de volume a verificar

| Keyword | Volume | Fonte | Data |
|---|---:|---|---|
| saída de praia | 14.800 | Semrush `phrase_this`, base BR | 2026-08-10 |
| saída de praia | 60.500 | Semrush bulk, `data/2026-08-09-semrush-bulk-kws-br.csv` | 2026-08-09 |

**RESOLVIDO em 2026-08-11.** Não é divergência: são duas keywords distintas,
ambas presentes em `data/2026-08-10-matriz-kws-classificada.csv`.

| Grafia | Volume | KD | Intenção |
|---|---:|---:|---|
| saida de praia (sem acento) | 60.500 | 26 | informacional + comercial |
| saída de praia (com acento) | 14.800 | 18 | informacional |

A grafia sem acento tem 4× o volume e KD 8 pontos maior. As duas apontam para
a mesma SERP, então a página cobre as duas naturalmente; o `<title>` usa a
forma correta em português e o corpo carrega as duas, sem forçar.

A divergência **não muda a fila da F3**: saída de praia é o cluster nº 2 em
qualquer dos dois números.

## Outros termos coletados nesta sessão

Semrush `phrase_this`, base BR, 2026-08-10:

| Keyword | Volume | CPC (R$) | Competição | Intenção | KD |
|---|---:|---:|---:|---|---:|
| biquini hot pant | 5.400 | 0,16 | 1,00 | comercial | 17 |
| saída de praia feminina | 1.300 | 0,11 | 1,00 | informacional + transacional | 16 |
| biquini de marquinha | 320 | 0,00 | 0,33 | comercial | 15 |
| poncho de surf | 170 | 0,11 | 0,99 | n/d | n/d |
| poncho atoalhado | 170 | 0,10 | 1,00 | n/d | n/d |
| conjunto atoalhado | 90 | 0,38 | 1,00 | comercial | 7 |

## Coleta interrompida

**Unidades de API do Semrush esgotadas.** A conta é uma subconta corporativa
sem unidades suficientes para completar novas requisições. É preciso contatar
o titular da conta e solicitar a alocação de mais unidades de API. Depois que
as unidades estiverem disponíveis, nenhuma ação adicional é necessária.
