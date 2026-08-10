# Fase 1 — Oportunidades: seleção de produtos e clusters de keyword

- **Data**: 2026-08-10
- **Dados-base**: `reports/2026-08-10-catalogo-e-kws-semrush.md` (Semrush BR
  + catálogo mapeado) e `reports/2026-08-08-semrush-kws-lycra-surf.md`
  (Semrush BR).
- **Status**: parcial. Cobre os clusters com número real coletado. Os
  clusters marcados como pendentes esperam recoleta no Semrush — ver a
  seção "O que falta medir".

## O que mudou desde a Fase 0

A Fase 0 decidiu 75% do esforço em produto e olhou produto pela lente de
surf: poncho e lycra. A coleta desta fase mostra que a lente estava estreita.

**"Saída de praia" tem 14.800 buscas/mês com KD 18.** É 17 vezes o volume de
"lycra surf" (880) e 87 vezes o de "poncho de surf" (170) — e a loja tem a
categoria pronta, com produtos indexados. "Biquini hot pant" tem 5.400 com
KD 17, e a loja tem a subcategoria. Nenhum desses termos estava no mapa da
Fase 0.

Isso **não contradiz** a decisão de território (produto acima de marca; não
disputar "zero hora" seco). Refina a decisão por dentro: o esforço de produto
precisa se dividir entre duas naturezas de cluster que resolvem problemas
diferentes.

## Decisão: dois motores dentro do território de produto

| Motor | Clusters | Papel | Peso dentro do esforço de produto |
|---|---|---|---|
| **Volume — beachwear feminino** | saída de praia, biquíni (hot pant, marquinha, asa delta, sunkini), maiô, conjunto atoalhado | Onde a busca existe em escala. Entrega crescimento absoluto de tráfego qualificado. KD 15–18: alto para um domínio de 3.139 visitas no quadrimestre, mas atacável pela cauda e pelo informacional. | ~55% |
| **Autoridade — linha surf** | lycra surf (masc/fem), poncho/roupão, camiseta UV50+, proteção solar | Volume menor, concorrência editorial quase nula, KD 7–9. Onde a marca consegue ser a primeira resposta, inclusive em motores de IA, e onde a entidade "Use Zero Hora = surf/beachwear" se firma contra o jornal. | ~45% |

O motor de volume traz gente; o motor de autoridade define quem a marca é
para o Google e para os motores de resposta, e converte melhor por visita
porque a intenção é mais específica. Cortar qualquer um dos dois quebra o
outro: sem autoridade, o beachwear feminino não sai do lugar num KD 18; sem
volume, a autoridade rende centenas de visitas, não milhares.

**A divisão macro da Fase 0 permanece**: ~75% produto (agora repartido
acima), ~20% marca composta e navegacional, ~5% monitoramento de "zero hora"
seco.

## Clusters priorizados

Critério de ordenação: volume × (baixa dificuldade) × proximidade da compra ×
existência de página de destino no catálogo. Um cluster sem página de destino
real não entra na produção — vira pedido de página para o time antes de virar
pauta.

### C1 — Saída de praia (motor de volume)

| Keyword | Volume | KD | Intenção |
|---|---:|---:|---|
| saída de praia | 14.800 | 18 | informacional |
| saída de praia feminina | 1.300 | 16 | informacional + transacional |
| conjunto atoalhado | 90 | 7 | comercial |

Destino: `/feminino/saida-de-praia/` (confirmar canônica — ver item técnico
abaixo). A head term é **informacional**: quem digita "saída de praia" quer
ver modelos e entender o que serve para quê antes de comprar. Isso favorece
um texto de categoria que ensina, não uma vitrine muda — e é justamente o
formato que a marca sabe produzir. "Conjunto atoalhado" com KD 7 e intenção
comercial é a porta de entrada barata do cluster: ganha rápido e alimenta
links internos para a categoria mãe.

### C2 — Lycra surf e proteção UV (motor de autoridade)

| Keyword | Volume | KD |
|---|---:|---:|
| lycra surf | 880 | 9 |
| camiseta surf | 720 | 8 |
| camiseta surf masculina | 480 | 13 |
| lycra surf masculina | 260 | 7 |
| lycra surf feminina | 170 | 7 |

Destino: `/masculino/lycra-surf/` e a categoria feminina equivalente — **os
dois textos já estão escritos e commitados** em `content/`. Este cluster está
na frente de todos os outros em maturidade: falta publicar, medir e expandir
para o informacional de proteção solar, que hoje não tem página nenhuma.

### C3 — Poncho / roupão de surf (motor de autoridade)

| Keyword | Volume | KD |
|---|---:|---:|
| poncho de surf | 170 | n/d |
| poncho atoalhado | 170 | n/d |

Destino: `/roupas-e-acessorios/linha-surf/poncho/`. Volume pequeno, mas a
Fase 0 já constatou que o espaço informacional ("o que é poncho de surf",
"como escolher") está vazio na SERP brasileira, e o produto tem um
diferencial concreto e citável: abertura lateral para trocar de roupa. É o
cluster com maior chance de virar resposta padrão em IA por custo baixo.
Cobre também infantil e natação, que ampliam o cluster sem canibalizar.

### C4 — Biquíni por modelagem (motor de volume)

| Keyword | Volume | KD | Intenção |
|---|---:|---:|---|
| biquini hot pant | 5.400 | 17 | comercial |
| biquini de marquinha | 320 | 15 | comercial |

Destino: subcategorias de `/feminino/biquini/`. Intenção comercial pura e
volume alto, mas é o cluster mais disputado do catálogo e o mais distante do
diferencial da marca. Entra depois de C1 e C2 terem tração — subir aqui sem
autoridade acumulada é gastar produção contra players maiores.

### C5 — Território de marca (defesa)

"use zero hora", "usezerohora" e variações. Já ocupado pela marca (Fase 0).
Trabalho: dados estruturados `Organization`, consistência de entidade em todo
conteúdo, e o ângulo narrativo "surf de zero hora" (sessão de madrugada) como
ponte semântica que nenhum concorrente pode copiar. Custo baixo, feito uma
vez, protege o que já converte.

## Itens técnicos que precedem a produção

1. **Canônicas duplicadas.** Conjunto atoalhado responde por duas URLs de
   categoria; poncho por pelo menos duas trilhas. Definir a URL canônica de
   cada categoria antes de escrever para ela. Sem isso, o texto novo divide
   sinal com uma URL concorrente da própria loja.
2. **Confirmar o slug da categoria feminina de lycra.** A pauta
   `2026-08-08-lycra-surf-feminina.md` assumiu `/feminino/lycra-surf/` por
   simetria com a masculina. Confirmar no CMS.
3. **Publicar o que já está pronto.** Os dois textos de lycra estão em
   `content/` desde 2026-08-08. Enquanto não forem ao ar, não há o que medir
   e o ciclo não fecha.

## O que falta medir

Sem número por esgotamento das unidades de API do Semrush (ver o snapshot de
2026-08-10): maiô feminino, sunga masculina, camisa UV masculina, bermuda de
praia masculina, biquíni asa delta, sunkini, moda praia feminina, camiseta UV
infantil, ioga/fitness. Também falta a expansão de cauda e as perguntas reais
(`phrase_related`, `phrase_fullsearch`, `phrase_questions`) dos clusters C1,
C3 e C4 — que são o insumo dos blocos de FAQ e da camada AEO.

Enquanto isso não vem, a produção trabalha sobre C1, C2 e C3, que têm número.

## Critério de revisão desta priorização

Rever se: (a) a recoleta mostrar cluster não medido com volume acima de C1 e
KD abaixo de 15; (b) os dados de venda da Nuvemshop mostrarem que a receita
se concentra em categoria fora dos dois motores; ou (c) três ciclos de
medição mostrarem C1 sem ganho de posição — nesse caso o KD 18 é alto demais
para o perfil de autoridade atual e o esforço migra para a cauda longa do
mesmo cluster.
