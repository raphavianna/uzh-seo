# Snapshot — Auditoria SEO/GEO do catálogo (dados)

- **Fonte**: cache SQL da integração Nuvemshop (`data/nuvemshop.db`), loja USEZEROHORA (store_id 5540626)
- **Sync**: completo em 2026-08-12T15:04Z (mesmo dia da auditoria — defasagem zero)
- **Regra de receita**: `payment_status='paid' AND status<>'cancelled'`, data `COALESCE(paid_at, created_at)`, janela 2025-08-12 → 2026-08-12
- **Cobertura**: checks automatizados = 100% do catálogo (140 produtos, 902 variantes, 48 categorias, 1.686 imagens)

## Fase 1 — Inventário

| Métrica | Valor |
|---|---:|
| Produtos | 140 (todos publicados) |
| Variantes | 902 |
| Categorias | 48 |
| Imagens de produto | 1.686 (média 12/produto; nenhum produto sem imagem) |
| Pedidos no cache | 1.447 |
| Receita 12m (regra acima) | R$ 230.977,13 em 1205 pedidos |

Consulta-base do inventário: contagens diretas nas tabelas `products`, `variants`, `categories`, `orders` + `json_extract(payload,'$.images')`.

## Fase 2 — Ranking de receita (12 meses)

```sql
SELECT i.product_id, SUM(i.quantity), SUM(i.line_total) FROM order_items i
JOIN orders o ON o.id=i.order_id
WHERE o.payment_status='paid' AND o.status<>'cancelled'
  AND COALESCE(o.paid_at,o.created_at) >= '2025-08-12'
GROUP BY i.product_id ORDER BY 3 DESC;
```

| # | product_id | Produto (nome do item vendido) | Unid. | Receita 12m |
|--:|---|---|--:|--:|
| 1 | 252094324 | Poncho Atoalhado Roupao Toalha Surf Natacao Adulto M/G (Azul, Único) | 215 | R$ 32.707,85 |
| 2 | 336513465 | PONCHO RESORT PREMIUM (Azul Marinho, Unico) | 85 | R$ 15.719,15 |
| 3 | 331295922 | PONCHO CLASSICO TODAS AS CORES (BEGE, M) | 100 | R$ 13.214 |
| 4 | 252378126 | Poncho Atoalhado Roupao Toalha Surf Natacao Adulto P (Preto, 34 - 40) | 83 | R$ 12.659,17 |
| 5 | 349127985 | MAIO STORM (Marinho, G) | 51 | R$ 11.639,49 |
| 6 | 335090358 | MAIO LISO GOLA ALTA MANGA LONGA E ZIPER (Preto, G) | 55 | R$ 11.599,45 |
| 7 | 298141305 | Poncho Clássico Adulto (P e M) (Bege, M) | 81 | R$ 10.719,19 |
| 8 | 276833145 | Maiô Body Surf Manga Longa Proteção Solar UV50 Liso Preto (G, Preto) | 48 | R$ 8.592,9 |
| 9 | 252382225 | Poncho Infantil Atoalhado Roupao Toalha Surf Natacao (Verde, 6 anos - 12 anos) | 64 | R$ 8.299,37 |
| 10 | 340798026 | MAIO MACAQUINHO PARATY (Off White, GG) | 31 | R$ 6.939,69 |
| 11 | 303607414 | Poncho Atoalhado Roupao Toalha Surf Natacao Classico Adulto (Azul Marinho, M) | 48 | R$ 6.419,52 |
| 12 | 303607422 | Poncho Atoalhado Roupao Toalha Surf Natacao Classico Adulto (Azul Royal, M) | 41 | R$ 5.379,59 |
| 13 | 298141312 | Poncho Clássico Infantil (XPP e PP) (Bege, PP) | 42 | R$ 4.667,58 |
| 14 | 276833135 | Maio Feminino Manga Longa Body Surf Natacao Estampado Coral (Azul - Coral, G) | 23 | R$ 4.124,23 |
| 15 | 349128003 | MAIO RINCON (BRANCO, G) | 17 | R$ 3.699,83 |
| 16 | 303607440 | Poncho Atoalhado Roupao Toalha Surf Natacao Classico Adulto (Grafite, M) | 26 | R$ 3.469,74 |
| 17 | 355991421 | MAIO MOANA (Marrom, G) | 12 | R$ 3.119,88 |
| 18 | 303607431 | Poncho Atoalhado Roupao Toalha Surf Natacao Classico Adulto (Vinho, M) | 23 | R$ 3.029,77 |
| 19 | 270617865 | Camiseta Lycra Surf UV50 Manga Longa Verde com Preto (G) | 21 | R$ 2.939,79 |
| 20 | 316378400 | Maiô Manga Longa Bicolor Zíper UV50 Blackout Premium (Rosa, G) | 14 | R$ 2.799,86 |

### Estoque parado (publicado, com estoque, zero venda em 12m) — top 5

| product_id | Produto | Estoque |
|---|---|--:|
| 357775732 | BIQUINI FLORIPA | 200 |
| 355991468 | CAMISETA LYCRA FEMININA ITAMAMBUCA | 139 |
| 315738164 | Biquini Empina Bumbum Cortininha Preto | 108 |
| 315738097 | Camiseta Lycra Surf Feminina UV50 Segunda Pele Vaca | 105 |
| 331018836 | CAMISETA UV INFANTIL NEON | 100 |

**Amostra qualitativa das Fases 4–5** = top 20 por receita + estes 5 (25 produtos).

## Fase 3 — Tabela de cobertura por check (Eixo A, catálogo completo)

| Check | Itens reprovados | % aprovação |
|---|--:|--:|
| seo_title_ausente | 29 | 79.3% |
| seo_title_60 | 40 | 71.4% |
| seo_title_sem_kw | 1 | 99.3% |
| seo_title_dup | 6 | 95.7% |
| seo_desc_ausente | 29 | 79.3% |
| seo_desc_155 | 3 | 97.9% |
| seo_desc_dup | 0 | 100% |
| desc_ausente | 0 | 100% |
| desc_thin | 0 | 100% |
| desc_near_dup | 92 | 34.3% |
| desc_sem_dado_concreto | 5 | 96.4% |
| handle_sem_kw | 0 | 100% |
| handle_stopwords | 0 | 100% |
| publicado_sem_estoque | 11 | 92.1% |
| imgs_sem_alt_total | 1686 | — |

Notas de método:
- `desc_near_dup`: similaridade Jaccard > 0,8 entre conjuntos de tokens dos primeiros 600 caracteres (texto sem HTML).
- `seo_title_sem_kw`: nenhum dos 4 primeiros tokens significativos do nome do produto aparece no seo_title.
- `desc_sem_dado_concreto`: ausência de regex de medidas/material/composição/UV.
- alt de imagem: a API devolve `alt: []` (array vazio) — **as 1.686 imagens do catálogo estão sem alt** (0% de cobertura).

### Títulos SEO duplicados (grupos)

- "Biquíni Esportivo Feminino Hot Pant com Top Transpassado" → produtos 274536023,274613181 (2×)
- "Camiseta Lycra Surf UV50 Manga Longa - Proteção e Conforto" → produtos 306381140,315738151 (2×)
- "Maiô Body Feminino Manga Longa com Zíper e Proteção UV50+" → produtos 355991421,355997321 (2×)

### Produtos publicados com estoque zero (soft-404 de intenção de compra)

| product_id | Produto | Estoque |
|---|---|--:|
| 315738111 | Biquini Empina Bumbum Cortininha Onça | 0 |
| 315738108 | Biquini Empina Bumbum Cortininha Vaca | 0 |
| 274613181 | Biquini Sunkini Hot Pant Top Faixa Futevôlei Piscina Surf | 0 |
| 274536023 | Biquini Sunkini Hot Pant Top Faixa Surf Futevôlei Piscina | 0 |
| 274613187 | Biquini Sunkini Hot Pant Top Faixa Surf Piscina Futevôlei | 0 |
| 273297759 | Blusa Casaco Moletom Frio Canguru Capuz Surf Unissex | 0 |
| 273343037 | Camisa Masculina Lycra UV50 Manga Longa Protecao Solar Praia | 0 |
| 270617797 | Camiseta Lycra Surf UV50 Manga Longa Azul Liso | 0 |
| 270617788 | Camiseta Lycra Surf UV50 Manga Longa Verde Liso | 0 |
| 298118384 | Maiô Body Surf Manga Longa Proteção Solar UV50 Liso Branco | 0 |
| 352307547 | PONCHO ZIPER | 0 |

### Categorias

- **48/48 categorias sem descrição** (campo `description` vazio em todas).
- Categorias vazias (sem produto): "Lycra" (id 34709877), "CONJUNTO" (id 34709981).
