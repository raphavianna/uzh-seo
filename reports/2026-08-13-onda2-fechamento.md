# Onda 2 — relatório de fechamento

- **Data**: 2026-08-13
- **Modo**: CRIAÇÃO (F5, produção SEO/GEO), executado em run autônomo.
- **Mandato do usuário**: 50 artigos criativos priorizados por volume (KD não veta),
  formatos variados (Q&A, comparativo, listicle, como-fazer, guia, sazonal), seguidos
  de auditoria anti-IA exaustiva em várias passadas até zero sinal.
- **Entrega**: 50 artigos HTML autocontidos em `content/<slug>.html` + versão CMS
  `content/<slug>-editor.html`, mais o guia de copiar-colar e este relatório.

## 1. Escopo e priorização

Fila ordenada por volume de busca medido, KD como desempate (nunca veto). Fonte de
volume: `data/2026-08-10-matriz-kws-classificada.csv` e
`data/2026-08-12-universo-esporte-MEDIDO.csv` (Semrush BR). Grade travada em
`producao/registro/grade-onda-2.csv`.

- **50 pautas** (primárias): 44 com volume medido, 6 de cauda PAA (volume não isolado,
  declarado como `dado indisponível via Semrush` — regra 3 do CLAUDE.md).
- **Volume medido das primárias**: **149.510 buscas/mês**.
- **27 KWs secundárias** travadas como subtópicos.
- **74 KWs** registradas em `producao/registro/kw-donos.csv` no território `onda2`
  (anticanibalização: nenhuma colide com as 147 da Onda 1/T1; total do registro: 221).

### Volume medido por hub

| Hub | Artigos | Volume medido/mês |
|---|---:|---:|
| Bem-estar (yoga/pilates) | 8 | 27.650 |
| Sol e pele (protetor → camiseta UV) | 7 | 23.820 |
| Canga e mergulho | 2 | 21.400 |
| Natação | 6 | 18.500 |
| Sapatilha (CAP) | 3 | 15.300 |
| Moda praia | 6 | 13.600 |
| Biquíni | 4 | 11.100 |
| Maiô e saída | 4 | 8.570 |
| Sunga e bermuda | 4 | 6.500 |
| Esporte e verão | 6 | 3.070 |

## 2. Caminho até a conversão

Cada artigo declara a intenção de busca e a ponte comercial no comentário de produção.
Padrão dominante: conteúdo informacional de autoridade honesta (a marca não vende creme,
prancha nem equipamento de esporte) → ponte para a categoria/produto real que a loja tem
→ CTA para a categoria de destino. Todo link de produto/categoria sai destacado
(`<strong><u>`), apontando só para URL real de usezerohora.com.br. **Sem preço** em nenhum
artigo (preço muda; o artigo fica meses no ar) — a copy usa o link do produto e o atributo
técnico que não muda.

Onde o catálogo é raso, a pauta foi tratada como CAP (autoridade/ponte), nunca vitrine
prometida, e a limitação é declarada no corpo: sapatilha (1 produto único), canga (0 na
categoria, ponte para saída de praia), crochê (o material real é tule), beach tennis (não
há tênis de quadra; oferece o calçado de neoprene pelo que ele resolve na areia).

## 3. Produção (Bloco 1)

50 artigos escritos por escritores-subagentes aterrados em dado real
(`scripts/ficha-por-categoria.py` sobre `data/2026-08-12-nuvemshop-catalogo.json`), em 5
ondas de 10 (2A–2E), cada onda validada mecanicamente
(`scripts/validar-anti-ia.py`), com editor derivado (`scripts/gerar-editor.py`) e commit
próprio. Estrutura da casa em cada peça: comentário de produção, `<title>` ≤60,
`meta description` ≤155, canonical/OG/Twitter, três blocos JSON-LD (BlogPosting +
BreadcrumbList + FAQPage), `<h1>` único, aberturas autocontidas por seção, FAQ com `<h3>`
espelhando o FAQPage, imagem CDN real. `{HASH}` só em canonical/og:url/@id do schema,
nunca no corpo.

## 4. Auditoria anti-IA (Bloco 2) — duas rodadas

Prioridade máxima do mandato: remover todo sinal de escrita de IA, exaustivamente.

### Rodada 1 — por arquivo (7 editores adversariais)
Cada editor leu ~7 artigos como editor humano cético e corrigiu in loco o que a varredura
mecânica não pega. **40 dos 50** tiveram correção; 10 já eram naturais. Padrões removidos:
placas de abertura ("Abaixo você vê o passo a passo"), fórmulas de comparativo ("não
existe vencedor absoluto, existe"), moldes definicionais repetidos, ritmo metronômico,
throat-clears ("vale a franqueza"), um vazamento de brief no corpo ("a franqueza que o
brief pede"), uma violação SEM PREÇO recuperada (`loja-de-surf`) e um erro de concordância.

### Rodada 2 — por cluster temático (7 revisores + 7 fixers)
A rodada 1, por ler um arquivo de cada vez, não enxergava o defeito mais denunciador de
produção em lote: **repetição quase-verbatim entre artigos do mesmo tema**. Sete revisores
leram os 50 agrupados por cluster e sete fixers reescreveram cada elemento repetido como
texto único por artigo, ancorado no eixo de cada um, preservando os fatos reais. Exemplos:

- **Sol e pele**: ponte "divide o corpo em duas frentes", o CTA final e o H2 "No corpo, a
  roupa com UV" apareciam verbatim em 3 a 6 dos 7 artigos.
- **Bem-estar**: "constância > intensidade" (3), agenda "segunda/quarta/sexta" (3),
  ressalva de saúde verbatim (2), adorno "para o tecido não segurar o calor" (3).
- **Natação**: parágrafo de descrição do maiô clonado em 3; argumento "biquíni sai no
  movimento" reduzido de 4 para 2 artigos.
- **Biquíni/maiô**: três pontes CTA quase idênticas; linguagem corretiva de corpo
  ("equilibrar o quadril mais largo") trocada por linguagem de destaque.
- **Moda praia/saída**: descrição do tule copy-paste em 4–5; bordão "da areia ao quiosque"
  reservado ao artigo dono; sortimento da saída enunciado uma vez.
- **Masculino/surf**: a frase da lycra era um template com só a última oração trocada em
  6 artigos; a ponte honesta "a marca veste, não vende equipamento" estava clonada em 3.
- **Sapatilha**: o spec-dump do produto único aparecia verbatim nos 3 artigos.

Dois artigos foram confirmados genuinamente limpos e deixados intactos para evitar
sobre-edição (`como-amarrar-canga`, `o-que-levar-para-a-praia`); outros dois já vinham
limpos no cluster masculino (`sunga-slip-ou-preta`, `loja-de-surf`).

### Resultado
`scripts/validar-anti-ia.py` sobre os 50: **0 erro bloqueante, 0 tic**. Editores
regenerados para todos os arquivos alterados.

## 5. Entrega para publicação

- **Guia de copiar-colar**: `producao/painel/guia-copiar-colar-onda2.html` (gerado por
  `scripts/gerar-guia-onda2.py`), 50 cards com Título, Slug, Title SEO, Meta description,
  Corpo (para colar no modo HTML do editor) e Schema opcional, cada campo com botão Copiar.
- **Ordem sugerida de publicação**: a do guia (por hub, começando pelos de maior volume).
- **Nota de publicação**: trocar `{HASH}` pela URL real só no schema, após publicar. O
  corpo colável não contém `{HASH}`.

## 6. Pendências fora do escopo desta onda (Onda 1/T1)

Surgiram na validação global `--todos`, em artigos finalizados em sessão anterior. Não
foram reescritos aqui (fora do mandato dos 50); ficam registrados para decisão:

- Links de post-irmão com `{HASH}` no corpo, no cluster rash-guard/lycra/UV:
  `blusa-com-protecao-uv`, `camisa-de-praia-feminina`, `camiseta-com-protecao-uv`,
  `o-que-e-rash-guard`, `rash-guard-infantil` (link previsto quebra na publicação enquanto
  o hash não for resolvido).
- `feminino-lycra-surf` e `masculino-lycra-surf` sem JSON-LD BlogPosting (usam schema de
  categoria).
- Avisos de bordão "de verdade" em `sunga-masculina` e `vestido-de-praia`.

## 7. Próximo ciclo (sugestão)

- Publicar a Onda 2 pelo guia e registrar as URLs finais (resolver `{HASH}`).
- Rodar o teste de citação AEO (conjunto fixo de perguntas em ChatGPT/Perplexity/Gemini/AI
  Overview) 30 dias após a indexação, com resultado datado em `reports/` (item 6 de
  `<aeo_geo>`).
- Medir posição e tráfego das 74 KWs em 30 dias e reordenar o backlog restante
  (`pautas/backlog-criativo-volume.md`, 33 pautas, ainda não exauridas).
