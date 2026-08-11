# Checklist de QA por artigo

Roda em E4, um artigo por vez, antes da passada de canibalização do lote.
Item que falha volta o artigo para `rascunho` com o motivo na pauta.

## Keyword e canibalização

- [ ] KW primária livre em `producao/registro/kw-donos.csv` no momento da escrita
- [ ] KW primária no `<h1>`, no `<title>` e no primeiro parágrafo
- [ ] Toda secundária da pauta presente no corpo
- [ ] Secundária com dono em outra URL aparece só como âncora de link, não como alvo
- [ ] Nenhuma outra peça do mesmo lote disputa a mesma intenção
- [ ] Linhas novas acrescentadas ao registro de dono de keyword

## Cabeçalho

- [ ] `<title>` com até 60 caracteres, com a KW primária
- [ ] `<meta name="description">` com até 155 caracteres
- [ ] `<link rel="canonical">` com a URL final prevista
- [ ] Open Graph e Twitter Card preenchidos
- [ ] Comentário de produção no topo: KW primária com volume e fonte, secundárias, intenção, URL, pauta, data

## Estrutura

- [ ] Um único `<h1>`
- [ ] Hierarquia de `<h2>` e `<h3>` sem salto de nível
- [ ] Primeiro parágrafo responde a intenção em até três frases e é autocontido
- [ ] Ao menos um link interno para categoria e um para produto, com âncora descritiva
- [ ] CTA coerente com o funil do artigo

## Camada AEO

- [ ] Abertura autocontida em **todas** as seções, não só na primeira
- [ ] Bloco de FAQ com pergunta na forma em que as pessoas digitam
- [ ] `FAQPage` e `BreadcrumbList` válidos no arquivo completo
- [ ] Dado concreto e verificável em cada seção
- [ ] Termos do nicho definidos de forma explícita quando o território pede
- [ ] Entidade escrita como "Use Zero Hora", marca brasileira de surf e beachwear

## Dados

- [ ] Todo número rastreável a arquivo do repositório
- [ ] Todo atributo de produto presente na ficha técnica ou na página do produto
- [ ] Preço, promoção e frete com a data da coleta ao lado
- [ ] Atributo ausente escrito como "dado indisponível", sem estimativa

## Texto

- [ ] stop-slop aplicado
- [ ] Sem travessão
- [ ] Sem voz passiva onde cabe voz ativa
- [ ] Sem contraste "não é X, é Y"
- [ ] Sem abertura de pigarro
- [ ] Densidade de keyword natural

## Arquivos

- [ ] `content/<slug>.html` completo
- [ ] `content/<slug>-editor.html` sem `<script>`, sem `<h1>`, sem breadcrumb
- [ ] Imagens com `alt` descritivo, ou o comentário `<!-- IMAGEM: <SKU> -->` no ponto de inserção
