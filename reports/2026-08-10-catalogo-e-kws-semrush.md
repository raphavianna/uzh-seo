# Snapshot 2026-08-10 — Catálogo mapeado + KWs de cabeça de categoria

Coleta feita na retomada do projeto, para sustentar a Fase 1 (seleção de
produtos, editorias e keywords).

## 1. Catálogo — árvore de categorias

- **Fonte**: leitura indireta por busca no Google restrita a
  `usezerohora.com.br` (operador `site:`), em 2026-08-10.
- **Limitação declarada**: o acesso direto a `usezerohora.com.br` está
  bloqueado pelo proxy de rede desta sessão, e o MCP da Nuvemshop não está
  conectado aqui. A árvore abaixo é o que o índice do Google expõe, não um
  dump do CMS. **Confirmar com o time ou com o MCP da Nuvemshop antes de
  tratar como catálogo completo** — em especial a contagem de SKUs por
  categoria e as categorias que não apareceram no índice.

| Caminho | Subcategorias observadas | Evidência |
|---|---|---|
| `/feminino/` | `maio/`, `biquini/` (marquinha, asa delta, hot pant, sunkini), lycra surf, poncho, camiseta UV50+, `saida-de-praia/` → `conjunto-atoalhado/` | páginas de categoria indexadas |
| `/masculino/` | `lycra-surf/`, poncho, camiseta UV50+, bermuda, moletom, sunga | `/masculino/lycra-surf/` indexada |
| `/infantil/` | poncho atoalhado infantil, moda praia infantil | produto `poncho-atoalhado-...-infantil1` |
| `/roupas-e-acessorios/` | `linha-surf/` → `poncho/`, `lycra/`; `conjunto-atoalhado/` | páginas de categoria indexadas |
| `/ioga-fitness/` | calça, macaquinho | descrição de navegação no índice |
| Institucional | `/quem-somos/`, `/trocas-e-devolucoes/`, `/search/` | páginas indexadas |

**Achado técnico — duplicação de caminho.** O mesmo produto aparece sob mais
de uma árvore: poncho vive em `/roupas-e-acessorios/linha-surf/poncho/` e
também nas trilhas de gênero; conjunto atoalhado aparece em
`/feminino/saida-de-praia/conjunto-atoalhado/` **e** em
`/roupas-e-acessorios/conjunto-atoalhado/`. Duas URLs de categoria com o
mesmo conjunto de produtos competem entre si no índice e dividem sinal.
Entra na Fase 1 como item técnico: escolher a URL canônica de cada categoria
antes de escrever texto para ela — texto novo em URL que será despriorizada
é trabalho jogado fora.

Produtos identificados no índice (amostra, não exaustiva): camiseta lycra
surf UV50 manga longa (preto, verde, azul), camiseta lycra surf feminina
UV50 segunda pele, poncho atoalhado adulto (P, M/G) e infantil, bermuda
Ergonomic Premium masculina, conjunto atoalhado (cropped + short),
saia/vestido de tule saída de praia, biquíni hot pant cós alto com top fixo,
biquíni sunkini hot pant top faixa.

## 2. Keywords — cabeças de categoria

- **Fonte**: Semrush MCP, relatório `phrase_this`
- **Base de dados**: BR
- **Data da coleta**: 2026-08-10

| Keyword | Volume | CPC (R$) | Competição | Intenção | KD |
|---|---:|---:|---:|---|---:|
| saída de praia | 14.800 | 0,12 | 1,00 | informacional | 18 |
| biquini hot pant | 5.400 | 0,16 | 1,00 | comercial | 17 |
| saída de praia feminina | 1.300 | 0,11 | 1,00 | informacional + transacional | 16 |
| biquini de marquinha | 320 | 0,00 | 0,33 | comercial | 15 |
| poncho de surf | 170 | 0,11 | 0,99 | n/d | n/d |
| poncho atoalhado | 170 | 0,10 | 1,00 | n/d | n/d |
| conjunto atoalhado | 90 | 0,38 | 1,00 | comercial | 7 |

KD = Keyword Difficulty. As duas linhas de poncho foram coletadas antes de as
colunas de intenção e KD entrarem na consulta; recoletar no próximo ciclo.

Somado ao snapshot de 2026-08-08 (`2026-08-08-semrush-kws-lycra-surf.md`),
o cluster de lycra já medido: lycra surf 880 (KD 9), camiseta surf 720
(KD 8), camiseta surf masculina 480 (KD 13), lycra surf masculina 260 (KD 7),
camiseta para surf feminina 210 (KD 9), camisetas femininas surf 210 (KD 9),
lycra surf feminina 170 (KD 7).

## 3. O que ficou pendente nesta coleta

**Unidades de API do Semrush esgotadas.** A conta é uma subconta corporativa
sem unidades suficientes para completar novas requisições. É preciso
contatar o titular da conta e solicitar a alocação de mais unidades de API.
Depois que as unidades estiverem disponíveis, nenhuma ação adicional é
necessária.

Ficaram sem número, por isso: maiô feminino, sunga masculina, camisa UV
masculina, bermuda de praia masculina, biquíni asa delta, sunkini, moda
praia feminina, camiseta UV infantil, roupa de ioga/fitness, e toda a
expansão de cauda (`phrase_related`, `phrase_fullsearch`) e de perguntas
(`phrase_questions`) dos clusters novos. A Fase 1 registra esses termos como
**dado indisponível via Semrush** e a priorização deles fica condicionada à
recoleta.

Também indisponíveis nesta sessão, por não estarem conectados a este
ambiente: MCP da Nuvemshop (catálogo, vendas, estoque) e Google Ads /
Planejador de Palavras-chave. Ver `analysis/03-ciclo-editorial.md` para como
cada fonte entra no ciclo quando estiver acessível.
