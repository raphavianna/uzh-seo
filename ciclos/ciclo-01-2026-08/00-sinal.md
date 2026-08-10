# Ciclo 01 — Sinal

- Data: 2026-08-10

## Nuvemshop (venda e estoque)

**Dado indisponível via Nuvemshop nesta sessão.** O MCP da loja não está
conectado a este ambiente remoto — a integração existe e está commitada no
repositório `integracao-nuvemshop`, mas roda como servidor local.

Pendência para o time, a responder antes da etapa de seleção do ciclo 02:
1. Receita por categoria nos últimos 90 dias (`nuvemshop_query` sobre
   `orders` + `order_items`, regra `payment_status='paid' AND
   status<>'cancelled'`).
2. Estoque atual das peças candidatas: lycra surf masculina e feminina,
   poncho atoalhado (adulto e infantil), conjunto atoalhado, saída de praia.
3. Quais categorias a marca pretende sustentar nos próximos 6 meses — não
   escrever para categoria que vai sair do ar.

## Desempenho do que está no ar

Similarweb, coleta de 2026-08-08 (`reports/2026-08-08-similarweb-canais-usezerohora.md`),
período abr–jul/2026, BR: 3.139 visitas no quadrimestre; busca orgânica
15,4%; Display + Social Pago ~63%.

Nenhum dos dois textos de lycra estava publicado até esta data — não há
desempenho de conteúdo próprio a medir. É exatamente o que o ciclo 01
resolve.

## Mercado (Semrush)

Fonte: Semrush MCP, `phrase_this`, base BR, coleta de 2026-08-10. Registrado
em `reports/2026-08-10-catalogo-e-kws-semrush.md`.

- saída de praia — 14.800 — KD 18 — informacional
- biquini hot pant — 5.400 — KD 17 — comercial
- saída de praia feminina — 1.300 — KD 16 — informacional + transacional
- biquini de marquinha — 320 — KD 15 — comercial
- poncho de surf — 170 — KD n/d
- poncho atoalhado — 170 — KD n/d
- conjunto atoalhado — 90 — KD 7 — comercial

Coleta interrompida: unidades de API do Semrush esgotadas. A conta é uma
subconta corporativa; é preciso contatar o titular da conta e solicitar a
alocação de mais unidades de API.

Catálogo mapeado por leitura indireta (busca com `site:`), no mesmo snapshot
— o acesso direto ao domínio está bloqueado pelo proxy de rede desta sessão.

## Leitura

Três coisas, em ordem de consequência:

1. **Há conteúdo pronto e não publicado.** Dois textos de categoria de lycra
   estão em `content/` desde 2026-08-08. Enquanto não forem ao ar, o ciclo
   não tem linha de base e nenhuma decisão posterior é verificável. É o
   trabalho do ciclo 01.
2. **O mapa de produto da Fase 0 estava estreito.** "Saída de praia" com
   14.800 buscas/mês e a categoria existindo na loja é a maior oportunidade
   medida até agora, e não estava no radar. Entra como cluster C1 e abre o
   motor de volume em `analysis/01-oportunidades.md`.
3. **Faltam os dois lados do dado que decidem prioridade**: venda real
   (Nuvemshop) e volume dos clusters ainda não medidos (Semrush). Sem eles, a
   priorização atual é boa para dois ciclos e precisa ser reavaliada no
   terceiro.
