# Pedido ao conector Nuvemshop

- **Data**: 2026-08-12
- **Por quê**: os cinco artigos do lote T1 linkam para 9 URLs do site, e nenhuma
  foi confirmada. Link para URL que não existe é clique perdido, e CTA para
  listagem que não existe é visita que não compra.
- **Fonte das contagens**: `content/*.html` do lote,
  `producao/registro/kw-donos.csv`, e
  `reports/2026-08-09-semrush-baseline-dominio.md` (Semrush BR, 2026-08-09).
- **Como usar**: cole o bloco de "Mensagem para colar" numa sessão com o
  conector Nuvemshop ligado, e traga a resposta de volta.

---

## Bloco A — as 9 URLs que o lote linka

Para cada uma: **existe?** e **é produto ou listagem de categoria?**
A natureza muda o destino do CTA, e é a diferença entre mandar quem quer
comparar para uma peça só ou para a vitrine.

| URL | Citações no lote | KWs reservadas | Ranqueia hoje? |
|---|---:|---:|---|
| `/rash-guard/` | 6 | **8 (24.310 buscas/mês)** | **não aparece no baseline** |
| `/masculino/lycra-surf/` | 11 | 5 | sim, 4 linhas |
| `/feminino/lycra-surf/` | 5 | 0 | não aparece |
| `/feminino/maio/` | 2 | 0 | sim, 11 linhas (42% do orgânico) |
| `/quem-somos/` | 2 | 0 | não aparece |
| `/masculino/` | 1 | 0 | sim, 1 linha |
| `/feminino/` | 1 | 0 | não aparece |
| `/produtos/camiseta-lycra-surf-uv50-manga-longa-verde-liso/` | 1 | 0 | não aparece |
| `/blog/posts/lycra-surf-feminina-bbc79bb33550` | 3 | 2 | post já publicado |

"Não aparece no baseline" significa que a URL não ranqueia para nenhuma das
146 keywords medidas. **Não prova que ela não existe** — prova que, se existe,
não traz tráfego orgânico. Por isso a pergunta precisa ser feita.

`/feminino/lycra-surf/` você já confirmou como página de produto em 2026-08-11.
Está na lista só para o conector confirmar o mesmo para as irmãs.

## Bloco B — as três perguntas que valem dinheiro

**B1. `/rash-guard/` existe?** É a mais cara da lista. Oito keywords de
intenção comercial somando 24.310 buscas/mês estão reservadas a essa URL no
registro, e o lote linka para ela seis vezes. Se ela não existir, esse volume
não tem destino nenhum e os seis links vão para o vazio. Se existir mas for
produto, e não listagem, o CTA precisa mudar.

**B2. Qual categoria recebe "poncho toalha infantil"?** São 590 buscas/mês sem
página de destino registrada. O cluster poncho hoje responde por três URLs
(`/masculino/poncho/`, `/feminino/poncho1/` e um produto), e faz 54% da receita
da loja. Pergunta: existe categoria de poncho infantil, ou o termo cai numa das
existentes?

**B3. `/feminino/poncho1/` é isso mesmo?** O slug tem sufixo numérico e
ranqueia em 2 keywords, disputando o cluster com `/masculino/poncho/`. Sufixo
numérico costuma ser resíduo de categoria duplicada no CMS. Pergunta: existem
duas categorias de poncho feminino, e qual é a canônica?

## Bloco C — o que o conector não resolve

**As URLs dos cinco posts deste lote não existem ainda.** O hash de 12
caracteres nasce no CMS no instante da publicação. Nenhuma API, conector ou
leitura de site devolve o endereço de um post não publicado. Publicar vem
primeiro; colher a URL vem depois, e para isso existe
`scripts/colher-urls-blog.py`.

**A Blog API pode não responder.** O MCP em `integracao-nuvemshop` cobre
products, categories, orders, customers, coupons, checkouts, store e webhooks.
O recurso de blog não está implementado, e o app tem escopo `read_content`
enquanto a Blog API exige permissão de editar conteúdo. Se o conector da outra
sessão for o mesmo, as perguntas de blog voltam vazias e as de categoria e
produto respondem normalmente.

---

## Mensagem para colar

```
Preciso de dados do catálogo da loja usezerohora.com.br (Nuvemshop).

1) Estas URLs existem? Para cada uma, diga se é PÁGINA DE PRODUTO ou
   LISTAGEM DE CATEGORIA, e quantos produtos ativos ela tem:

   /rash-guard/
   /masculino/lycra-surf/
   /feminino/lycra-surf/
   /feminino/maio/
   /quem-somos/
   /masculino/
   /feminino/
   /produtos/camiseta-lycra-surf-uv50-manga-longa-verde-liso/

2) Liste TODAS as categorias da loja com: nome, handle/slug, URL completa,
   categoria pai e número de produtos ativos. Quero a árvore inteira.

3) Existe categoria de poncho infantil? Se sim, qual a URL. Se não, em qual
   categoria os ponchos infantis estão hoje.

4) Existem duas categorias de poncho feminino? A URL /feminino/poncho1/ tem
   sufixo numérico e quero saber se é duplicata. Diga qual é a canônica.

5) Liste os posts do blog já publicados, com título e URL completa
   (incluindo o hash no final).

Se algum item não puder ser respondido pelo conector, diga qual e por quê,
em vez de estimar.
```

O item 5 é o que provavelmente volta vazio, pelo motivo do Bloco C. Os quatro
primeiros são de catálogo e devem responder.

## O que muda no repositório conforme a resposta

| Resposta | Consequência |
|---|---|
| `/rash-guard/` não existe | As 8 KWs comerciais perdem dono. Ou o time cria a categoria, ou o volume é redistribuído entre as URLs que existem. Os 6 links do lote precisam de novo destino antes de publicar. |
| `/rash-guard/` existe mas é produto | Os CTAs de comparação mudam para a listagem que cobrir o cluster. |
| `/masculino/lycra-surf/` é produto | Os 11 links deixam de prometer vitrine. A copy já está agnóstica ao destino desde 2026-08-11, então muda só o `href`. |
| Existe poncho infantil | "poncho toalha infantil" (590/mês) ganha destino e entra na fila de E1. |
| `/feminino/poncho1/` é duplicata | Entra na higiene da Onda 0: canônica definida e redirect da duplicata. |
