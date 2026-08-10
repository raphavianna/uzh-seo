# Ciclo 01 — Seleção

- Data: 2026-08-10

## Escolhido

**Conteúdo: rash guard / camiseta UV** — `pautas/2026-08-10-rash-guard.md`

| Filtro | Resposta |
|---|---|
| Posição na fila da F3 | 1º, prioridade 585 |
| Calendário sazonal autoriza publicar agora? | Sim. Índice entre 0,44 e 1,00 o ano inteiro — único cluster relevante sem vale sazonal |
| URL dona sem canibalização aberta? | Parcial. `/masculino/lycra-surf/` é dona de "lycra surf"; "rash guard" não tem dona. Definir com o time se estende a categoria ou vira URL própria |
| Produto com estoque? | 26 SKUs, o maior sortimento do catálogo — fator de catálogo 1,0 |

**Onda 0, em paralelo** — `pautas/2026-08-10-onda-0-higiene.md`, executada
pelo time de desenvolvimento e operação. Não compete por recurso de redação,
então não disputa lugar na fila: roda junto.

## O número que sustenta a escolha

| Fator | Número | Fonte |
|---|---|---|
| KW primária | rash guard — 18.100/mês, KD 10 | Semrush BR, 2026-08-09 |
| Melhor par volume/dificuldade | da base inteira de 860 keywords | `analysis/11-matriz-kws.md` |
| Sortimento | 26 SKUs, o maior do catálogo | `analysis/10-catalogo.md` |
| Lacuna de vocabulário | os dois textos de lycra publicados nunca usam o termo "rash guard" | `content/*-lycra-surf.html` |
| Sazonalidade | 0,44 a 1,00 o ano todo, contra 0,10 a 0,16 do resto em agosto | `analysis/12-priorizacao.md` |

## Descartados neste ciclo e por quê

- **Saída de praia** (fila nº 2, prioridade 365): publicar até setembro para
  chegar ranqueado no pico de fevereiro. Entra no ciclo 02. Pauta já aberta
  em `pautas/2026-08-10-saida-de-praia.md`.
- **Sunga masculina** (nº 3, prioridade 327): mesma janela, setembro. Pauta
  já aberta.
- **Neoprene** (nº 7): único cluster no pico agora, em agosto. Conteúdo
  orgânico publicado hoje ranqueia em janeiro, quando long john cai para
  0,29. É território de mídia paga agora e de orgânico em março — o que
  valida a linha neoprene como campanha inaugural no repositório `search-mkt`.
- **Maiô** (nº 5): converte a 0,9%. Mandar mais tráfego antes de corrigir a
  conversão amplifica o vazamento. Volta quando a CVR for corrigida.

## Bloqueios que precisam de resposta do time

Herdados da estratégia mestre, seção 7, mais o que este ciclo acrescenta:

1. "sunkini" (1.600 buscas/mês) é termo genérico de categoria ou nome de
   outra marca? Trava H1 da Onda 0.
2. O CMS permite `noindex` na busca interna e canonical em variação de
   produto? Trava H4 e o S1 inteiro.
3. Existe categoria infantil no catálogo? O mapa de URLs não achou nenhuma, e
   "poncho toalha infantil" tem 590 buscas/mês. Trava H3.
4. Qual o slug correto da categoria feminina de poncho, hoje
   `/feminino/poncho1/`? Trava H2 — que agora envolve **três** URLs, não
   duas: a terceira é `/roupas-e-acessorios/linha-surf/poncho/`.
5. **Novo (H6)**: `conjunto-atoalhado` também responde por duas trilhas.
   Mesma natureza de H2.
6. "rash guard" estende `/masculino/lycra-surf/` ou vira URL própria?
   Trava a produção deste ciclo.
7. Quem publica no CMS e em quanto tempo um texto entra no ar? Define se a
   cadência é de duas peças por ciclo ou de uma.

## Pautas do ciclo

- `pautas/2026-08-10-rash-guard.md` — produção
- `pautas/2026-08-10-onda-0-higiene.md` — higiene técnica, em paralelo
