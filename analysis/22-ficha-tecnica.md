# Frente de ficha técnica

- **Data**: 2026-08-11
- **Base atual**: `data/2026-08-10-ficha-tecnica-26-skus.csv` (BaseLinker,
  recebida em 2026-08-10). 26 SKUs, os que registraram venda ou visualização
  relevante na semana de 02 a 09/08/2026.
- **Por que esta frente existe**: conteúdo só pode afirmar atributo que existe
  na base ou na página do produto (regra 7 de `<regras_de_dados>`). Motor de
  resposta cita especificidade. Sem ficha técnica, a página vira genérica e
  não é citada — foi o risco nº 1 declarado na pauta de rash guard, e caiu só
  porque quatro peças daquele cluster tinham descrição completa.

## Cobertura hoje

Classificação por nome de produto, feita nesta análise. O catálogo total vem
de `analysis/10-catalogo.md`.

| Cluster | SKUs no catálogo | Com ficha | Cobertura | Prioridade F3 |
|---|---:|---:|---:|---:|
| Neoprene | 3 | 3 | **100%** | 109 |
| Maiô | 24 | 8 | 33% | 142 |
| Sunga, bermuda e short | 6 | 2 | 33% | **327 (3º)** |
| Poncho, toalha e roupão | 15 | 3 | 20% | 139 |
| Lycra, camiseta UV e rash guard | 26 | 4 | 15% | **585 (1º)** |
| Saída de praia e resort | 22 | 2 | **9%** | **365 (2º)** |
| Biquíni e top | 19 | 1 | **5%** | 259 (4º) |
| Fora de linha | 5 | 3 | 60% | — |
| **Total** | **120** | **26** | **22%** | |

**A cobertura está invertida em relação à fila.** Neoprene, o cluster que só
volta ao orgânico em março, tem 100%. Saída de praia, que é o próximo a
produzir e precisa publicar até setembro, tem 9%. Biquíni tem 5%.

## Qualidade do que já existe

| Checagem | Resultado |
|---|---|
| Tabela de medidas (URL) | 26 de 26 |
| Composição do tecido declarada | 12 de 26 |
| Descrição sinalizada como texto de IA | 2 (Poncho Resort Premium Feminino e Infantil) |
| Tamanho médio da descrição | 1.930 caracteres |

Dois problemas concretos:

1. **Composição falta em 14 SKUs.** É o atributo que mais sustenta citação em
   motor de resposta e o que separa uma peça técnica de uma camiseta comum.
   Nas quatro lycras ela existe (88% poliamida, 12% elastano) e virou o
   parágrafo mais específico do texto de rash guard.
2. **As duas descrições de Poncho Resort estão sinalizadas como lixo de IA** e
   têm 3.094 caracteres cada, o dobro da média. São exatamente as peças do
   cluster que faz 54% da receita. Reescrever antes de a editoria E3 entrar
   em produção.

**Divergência de nome**: o SKU `CAMISETA BACKDOOR` tem descrição intitulada
"Camiseta Lycra Masculina Manga Curta **Maresias**". Conferir qual é o nome
correto e se a divergência também está na página do produto.

## Os campos que o conteúdo precisa

Ordenados por quanto cada um rende em citação de motor de resposta e em
resposta a dúvida de compra. Os cinco primeiros são obrigatórios; sem eles a
peça não entra em pauta.

| # | Campo | Para que serve no conteúdo | Já existe? |
|---|---|---|---|
| 1 | Composição do tecido (percentual) | Define a peça, sustenta durabilidade e caimento | 12/26 |
| 2 | Fator de proteção e o que ele bloqueia | Responde "o que significa UV50+", a pergunta com mais PAA da base | nas lycras e maiôs |
| 3 | Se a proteção é da trama ou de acabamento | Responde "a proteção sai na lavagem" | só nas lycras |
| 4 | Tabela de medidas por tamanho | Responde a dúvida que trava a compra | 26/26 |
| 5 | Cores e tamanhos disponíveis | Grade real, evita prometer o que não tem | parcial |
| 6 | Tempo de secagem | Dado concreto, muito citável | declarado como "rápida", sem número |
| 7 | Instrução de lavagem e conservação | Bloco de FAQ inteiro depende disso | **nenhum SKU** |
| 8 | Resistência a cloro e água salgada | Separa uso de piscina de uso de mar | só no Maiô Storm |
| 9 | Origem de fabricação | Sustenta "fabricação própria" e a entidade da marca | só no Maiô Storm |
| 10 | Garantia | Hoje divergente: 7 dias no poncho, 30 no maiô | inconsistente |

**O campo 7 não existe em nenhum SKU.** A seção de conservação do texto de
rash guard foi escrita a partir da composição do tecido e está marcada para
validação contra a etiqueta. Enquanto esse campo não vier, toda peça de E2 e
E3 carrega a mesma pendência.

**O campo 10 está inconsistente entre produtos.** Garantia é promessa
contratual; publicar dois prazos diferentes no mesmo site é problema além do
SEO. Levar para quem responde pelo pós-venda.

## O pedido, na ordem da fila

Cada bloco destrava a produção de um ciclo. A ordem segue a fila da F3
corrigida pelo calendário sazonal, não o tamanho do buraco.

### Bloco 1 — Saída de praia e resort (destrava o ciclo 02, prazo setembro)

20 SKUs sem ficha. É o cluster de maior demanda da base (87.400 buscas/mês,
25 PAA) e o próximo a produzir. Sem ele, a pauta
`pautas/2026-08-10-saida-de-praia.md` entra em produção sem atributo e vira
texto genérico.

Prioridade dentro do bloco: os SKUs com visualização registrada na semana,
porque já recebem tráfego.

### Bloco 2 — Sunga, bermuda e short (destrava o ciclo 02, segunda peça)

4 SKUs sem ficha. Cluster pequeno, 74.720 buscas/mês, prioridade 327. É o
bloco mais barato de fechar da lista inteira.

### Bloco 3 — Lycra, camiseta UV e rash guard (completa o ciclo 01)

22 SKUs sem ficha. As 4 que existem sustentaram o texto de rash guard, mas a
peça de E2 (proteção solar) precisa de mais dado: tempo de secagem em número,
instrução de lavagem, e a confirmação de que toda a linha usa a mesma
composição.

### Bloco 4 — Poncho (destrava E3)

12 SKUs sem ficha, mais a reescrita das duas descrições sinalizadas como
lixo de IA. Cluster de 54% da receita e CVR de 3,6%. Espera a Onda 0 resolver
a canibalização de três URLs antes de virar produção.

### Bloco 5 — Biquíni (ciclo 03, prazo outubro)

18 SKUs sem ficha, a pior cobertura da lista.

## Como esta frente se fecha

O caminho definitivo não é planilha: é o MCP da Nuvemshop, que expõe produto,
variante, preço, estoque e categoria por SKU
(`integracao-nuvemshop`, ferramentas `nuvemshop_query` e
`nuvemshop_get_product`). Ele não está conectado a este ambiente remoto, e é
por isso que a base chega como CSV.

Duas coisas que só o MCP resolve e a planilha não:

1. **URL e categoria por SKU**, que é o que falta para fechar o gate da F1 e
   o que a matriz keyword → URL da F4 consome.
2. **Estoque no momento da publicação.** Publicar conteúdo que manda tráfego
   para produto esgotado queima verba e sinal — sete variantes zeraram na
   semana medida, entre elas o produto nº 1 da curva ABC.

Enquanto o MCP não estiver disponível na sessão, a frente roda por CSV
datado em `data/`, com proveniência registrada, e cada ciclo pede o bloco do
cluster que vai produzir.
