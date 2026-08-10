# Pauta — Onda 0: higiene técnica

- **Data**: 2026-08-10
- **Modo**: DADOS / execução técnica. **Não há produção de texto publicável.**
- **Fase**: F4 antecipada, executada antes da F5 por não competir por recurso de
  redação
- **Dados**: `reports/2026-08-09-semrush-baseline-dominio.md`,
  `analysis/10-catalogo.md`, `analysis/11-matriz-kws.md`
- **Executor**: time de desenvolvimento e operação, não redação

Cinco itens que devolvem posição sem escrever uma linha de conteúdo novo. Saem na
frente de toda a fila da F3 porque o gargalo deles é outro time.

---

## H1 — Corrigir a grafia priorizada em `/feminino/biquini/sunkini/`

**Problema medido**: o site ranqueia **"subikini" (210 buscas/mês) na posição 8**
e **"sunkini" (1.600 buscas/mês, KD 13) na posição 24**. Está em top 10 para a
grafia errada e em página 3 para a certa.

**Diagnóstico**: não é autoridade, é on-page. A URL já existe e já tem
autoridade suficiente para top 10 no cluster — ela só está sinalizando o termo
errado.

**O que fazer**: reescrever `<title>`, `<h1>` e o primeiro parágrafo da categoria
priorizando **sunkini**, mantendo "subikini" uma única vez no corpo como variação
reconhecida. Não remover a menção — ela sustenta a posição 8 atual.

**Retorno estimado**: 1.600 buscas saindo da posição 24 para o top 10 rende,
pela curva de CTR do próprio site (2,9% no top 10), cerca de **46 sessões/mês**.
O site inteiro faz 138. Estimado, não medido.

**Cluster sunkini completo**: sunkini (1.600) · sunkini feminino (720) · subikini
(210) · biquini sunkini (90) · sunkini biquini (20). Total 2.640 buscas/mês.

---

## H2 — Resolver a canibalização do poncho

**Problema medido**: `/masculino/poncho/` e `/feminino/poncho1/` disputam o mesmo
cluster. A segunda ainda carrega **sufixo numérico no slug**, sinal de URL criada
por duplicação no CMS.

**Por que importa**: poncho gera **54% da receita da loja** (R$ 9.314 na semana de
02 a 09/08) com CVR de 3,6%, quatro vezes a média. É o cluster que mais converte
e o que tem a arquitetura mais bagunçada.

**O que fazer**:
1. Definir a URL dona do cluster. Recomendação: uma categoria unissex de poncho,
   já que 8 dos 15 SKUs não são segmentados por gênero (Poncho Clássico, Poncho
   Premium Adulto, Poncho Atoalhado Unissex).
2. Redirecionar a perdedora com 301 para a dona.
3. Eliminar o sufixo numérico do slug.
4. Canônica correta em ambas antes do redirecionamento entrar.

**Risco**: mexer em URL que já ranqueia. Fazer com 301 e monitorar posição por 30
dias, conforme o gate da F5.

---

## H3 — Criar destino para poncho infantil

**Problema medido**: **"poncho toalha infantil" (590 buscas/mês, KD 9)** e
**"toalha com capuz infantil" (1.000 buscas/mês, KD 10)** não têm categoria de
destino no site.

**Por que importa**: o **Poncho Premium Infantil é o produto número um do
catálogo** — 17 unidades e R$ 2.211 na semana, CVR de 5,54%. Existem 4 SKUs
infantis de poncho no catálogo (Premium Infantil, Clássico Infantil XPP e PP,
Resort Premium Infantil).

A demanda de busca infantil e a venda infantil coincidem, e não há página que
capture a primeira.

**O que fazer**: criar categoria de poncho infantil sob a URL dona definida em
H2, com as 4 variações de SKU, título e H1 usando "poncho toalha infantil".

**Observação**: KD 9 e KD 10. É a menor dificuldade entre todas as oportunidades
com volume acima de 500 da matriz.

---

## H4 — Desindexar `/search/?q=`

**Problema medido**: a página de busca interna está indexada e ranqueando,
conforme o baseline de 2026-08-09.

**O que fazer**: `noindex` nas URLs de busca interna e bloqueio no `robots.txt`.
Página de resultado de busca interna gera conteúdo duplicado infinito e dilui o
orçamento de rastreamento.

---

## H5 — Repor as 7 variantes zeradas que venderam

**Problema medido**, na semana de 02 a 09/08/2026:

| Produto | Variante | Vendeu | Estoque |
|---|---|---:|---:|
| Poncho Premium Infantil | Azul / 6–12 anos | 13 | **0** |
| MAIO LISO GOLA ALTA MANGA LONGA E ZÍPER | Preto / G | 2 | **0** |
| MAIO STORM | Vermelho / P | 2 | **0** |
| MAIO STORM | Marinho / P | 2 | **0** |
| Poncho Atoalhado Roupão Clássico Adulto | Grafite / M | 1 | **0** |
| Camiseta Lycra Surf UV50 Manga Longa Preto com Verde | M | 1 | **0** |
| PONCHO RESORT PREMIUM INFANTIL | Rosa / 12 | 1 | **0** |

A primeira linha é a variante mais vendida do catálogo inteiro, zerada.

**Por que está numa pauta de SEO**: H3 propõe criar página para capturar 1.590
buscas mensais de poncho infantil. Mandar tráfego orgânico para uma categoria
cujo carro-chefe está esgotado desperdiça a captura e piora o sinal de qualidade
da página. **H5 precisa estar resolvido antes de H3 ir ao ar.**

---

## Ordem de execução

1. **H4** — isolado, sem dependência, menor risco.
2. **H1** — isolado, maior retorno por hora de trabalho da matriz inteira.
3. **H5** — pré-requisito de H3, e depende de produção, então começa cedo.
4. **H2** — precisa de decisão de arquitetura antes de executar.
5. **H3** — depende de H2 (URL dona) e de H5 (estoque).

## Medição

Registrar posição de "sunkini", "subikini", "poncho toalha infantil" e "toalha
com capuz infantil" antes da execução e 30 dias depois, em
`reports/YYYY-MM-medicao.md`. Sem a medição anterior não existe série histórica e
o gate da F5 não fecha.
