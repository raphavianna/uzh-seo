# Instruções por etapa

Cada etapa declara o que ancora, o que produz e o gate que precisa fechar. Use
junto do system prompt em `00-system.md`.

---

## E1 — Pesquisa e grade

**Ancora**: `data/<data>-matriz-kws-classificada.csv`, `producao/registro/kw-donos.csv`,
`analysis/12-priorizacao.md` (calendário sazonal).

**Produz**: `producao/registro/calendario-AAAA-MM.csv`.

**Instrução**

Monte a grade do mês seguinte, uma linha por artigo, três por dia útil, uma
para cada território.

1. Recolha volume, KD, CPC e intenção dos três clusters no Semrush e no
   Planejador de Palavras-chave. Salve o snapshot datado em `reports/`.
2. Em cada território, ordene por volume decrescente e remova toda keyword já
   presente em `kw-donos.csv` e toda variante gráfica de uma keyword já na
   grade.
3. Confira o calendário sazonal: keyword cujo pico está a menos de três meses
   sobe na fila, porque conteúdo publicado hoje ranqueia entre três e seis
   meses depois.
4. Preencha a grade com `status = rascunho` e `url_final` vazio.

**Refresh diário**: varra termos emergentes nos três clusters. Termo novo com
volume acima do menor da grade corrente entra **por substituição**, e a linha
substituída volta para a fila do mês seguinte. A grade não cresce no meio do
mês.

**Gate**: toda linha com keyword primária de volume medido, sem dono no
registro, e com data de produção e de publicação preenchidas.

---

## E2 — Pauta

**Ancora**: uma linha da grade aprovada, `data/2026-08-10-ficha-tecnica-26-skus.csv`,
`analysis/21-editorias.md`.

**Produz**: `pautas/AAAA-MM-DD-<slug>.md`.

**Instrução**

1. Confirme no registro que a KW primária está livre. Ocupada, devolva
   `<bloqueio>` e pare.
2. Levante secundárias e cauda do mesmo cluster, checando cada uma contra o
   registro. Secundária com dono vira âncora de link interno para a URL dona.
3. Declare a anticanibalização por escrito: quais termos pertencem a esta
   página e quais já pertencem a outra.
4. Escolha a editoria (`analysis/21-editorias.md`) e declare a intenção, o
   funil e a página de destino do CTA.
5. Liste os SKUs citáveis e, para cada um, os atributos que a ficha técnica
   sustenta. Atributo ausente entra como pendência explícita, não como
   suposição.

**Gate**: anticanibalização declarada, KW primária livre, e ao menos um
atributo real de produto por seção planejada.

---

## E3 — Redação

**Ancora**: pauta aprovada, ficha técnica, imagens do repo `midia-produtos`.

**Produz**: `content/<slug>.html` e `content/<slug>-editor.html`.

**Instrução**

Escreva conforme `<padrao_de_conteudo>` e `<camada_aeo>` do system prompt.
Aplique a skill stop-slop antes de entregar.

Sobre imagem: use o arquivo que o mapeamento indicar para o SKU citado, com
`alt` descritivo contendo a keyword quando o texto do alt ficar natural.
Imagem ausente, deixe o comentário `<!-- IMAGEM: <SKU> -->` no ponto de
inserção e siga. Artigo não espera imagem para ir para aprovação.

**Gate**: title até 60 caracteres, meta até 155, todas as secundárias
presentes no corpo, schema válido, e todo número rastreável a arquivo do
repositório.

---

## E4 — Revisão e aprovação

**Ancora**: o lote de artigos escritos, a grade do mês.

**Produz**: painel de aprovação (artifact) e a coluna `status` atualizada.

**Instrução**

1. Rode a checagem de `producao/qa/checklist.md` em cada artigo do lote.
2. Rode a passada de canibalização sobre o lote inteiro de uma vez: duas peças
   do lote não podem disputar a mesma intenção. É a única etapa em que o lote
   é olhado como conjunto, e é o motivo de produzir em lote em vez de diário.
3. Publique o painel com a fila, a prévia e o status de cada artigo.
4. Registre a decisão por artigo na grade: `aprovado` com data em
   `aprovado_em`, ou de volta para `rascunho` com o motivo anotado na pauta.

**Gate**: todo artigo do lote com decisão registrada. Lote com artigo
pendente não avança para E5.

---

## E5 — Publicação

**Ancora**: artigos aprovados, data de publicação da grade.

**Produz**: post no ar, `url_final` preenchida, `status = publicado`.

**Instrução, modo manual (hoje)**

A URL de post do blog é `https://usezerohora.com.br/blog/posts/<slug>-<hash>`,
e o `<hash>` de 12 caracteres só existe depois da publicação. Por isso os
arquivos de `content/` trazem o marcador `{HASH}`.

**Não substitua o `{HASH}` à mão.** No lote de agosto são 103 trocas em 11
arquivos, e canonical publicado com o marcador sem substituir quebra a
indexação da página. Há dois caminhos, e os dois chegam ao mesmo resultado:

| Caminho | Quando usar |
|---|---|
| **Painel** (`producao/painel/`) | O normal. Mova o card para Online, cole a URL, e ele fecha o marcador em todo o lote, acerta a data do schema e atualiza o cabeçalho da versão editor. Depois exporte o patch e rode `scripts/aplicar-patch-painel.py`. |
| **Terminal** (`scripts/publicar-fechar-urls.py`) | Quando preferir não passar pelo navegador. Cole as URLs em `producao/registro/urls-publicadas.csv` e rode o script. |

Os dois recusam gravar se a URL colada não bater com o slug do artigo.

### O lote sobe em rodadas, não artigo por artigo

Artigo que linka para um irmão precisa do hash daquele irmão. Isso agrupa a
publicação por camada de dependência, e a conta costuma dar menos rodadas do
que artigos. No lote de agosto, cinco artigos cabem em **três rodadas**:

| Rodada | Sobe | Por quê |
|---|---|---|
| 1 | o artigo que não linka para nenhum irmão | é a raiz de todas as dependências |
| 2 | todos os que dependem só da rodada 1 | podem ir juntos |
| 3 | o hub, que linka para todos | precisa do hash de todos |

O cabeçalho de cada `-editor.html` lista de quem aquele artigo depende.

### Passo a passo de cada rodada

1. Cole a versão editor-safe no editor do blog e confirme que **o slug ficou
   igual ao nome do arquivo** em `content/`. Slug diferente deixa o canonical
   apontando para URL que não existe.
2. Preencha title e meta description nos campos de SEO do CMS.
3. Copie a URL final que o CMS gerou, com o hash, para
   `producao/registro/urls-publicadas.csv`, junto da data real de publicação.
4. Rode `python3 scripts/publicar-fechar-urls.py --dry-run` para conferir, e
   depois sem a flag para gravar.
5. Adicione o JSON-LD pelo campo de dados estruturados, com o conteúdo do
   arquivo completo **já fechado pelo script**.
6. Repita para a próxima rodada. O script diz quantos `{HASH}` ainda faltam.

### Depois da última rodada

7. Feche os links de entrada: das páginas de produto e categoria para os novos
   posts, e das peças irmãs já publicadas. Conteúdo sem link de entrada demora
   o dobro para indexar.
8. Submeta as URLs no Search Console. É o caminho mais curto entre publicar e
   indexar, e sem isso o lote depende do rastreamento espontâneo.
9. Confirme que `url_final` e `status` estão preenchidos na grade. O script já
   faz isso; a conferência é para pegar artigo que ficou de fora do CSV.

**Instrução, modo automatizado (quando as travas caírem)**

A Blog API da Nuvemshop cobre criar, ler, atualizar e apagar post, upload de
imagem de conteúdo e de capa, e o endpoint que devolve o blog ID. Base:
`https://api.nuvemshop.com.br/2025-03/{store_id}`.

Duas travas, ambas no repositório `integracao-nuvemshop`:

1. **Escopo**: o app tem `read_content`; a Blog API exige permissão de editar
   conteúdo. A Nuvemshop não recebe escopo na URL de autorização — marcar a
   permissão no Painel de Parceiros e reautorizar o app na loja.
2. **Recurso não implementado**: `src/resources/index.ts` cobre products,
   categories, orders, customers, coupons, checkouts, store e webhooks. Falta
   o recurso de blog e as ferramentas MCP.

A escrita continua com as duas travas do próprio repositório:
`NUVEMSHOP_ENABLE_WRITES=true` no ambiente e `confirmacao="CONFIRMO"` por
operação.

**Gate**: post no ar, indexável, com link interno de entrada, e `url_final`
registrada na grade.

---

## E6 — Medição

Fora do lote. D+30 e D+60 por artigo, consolidados no relatório mensal da F6,
conforme `analysis/20-ciclo-operacional.md`. O que a medição realimenta: a
ordem da fila de E1, a associação KD → posição, e a poda de artigos sem
movimento em 90 dias.
