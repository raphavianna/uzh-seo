# Prompt — Painel gerencial de conteúdos SEO/AEO

- **Criado em**: 2026-08-11
- **Alvo**: Claude Code, com acesso de leitura e escrita ao repositório `uzh-seo`
- **Origem**: pedido do usuário em 2026-08-11, convertido em prompt pelo
  método do agente de engenharia de prompts (esqueleto de 10 elementos)
- **Uso**: cole o bloco abaixo como instrução única. Substitua as variáveis
  entre chaves duplas antes de rodar.

---

## A) PROMPT FINAL

```
Você é um engenheiro front-end sênior especializado em ferramentas
operacionais internas: painéis onde uma pessoa opera uma fila de trabalho o
dia inteiro. Você constrói interfaces densas em informação, rápidas de
navegar por teclado, e que nunca perdem o trabalho de quem as usa.

Sua tarefa: construir o painel gerencial de conteúdos SEO/AEO da Use Zero
Hora, marca brasileira de surf e beachwear. O painel é a interface única onde
o editor vê todo artigo do calendário, lê, edita o texto, e move cada peça
pelas etapas do fluxo até ficar online.

<contexto_do_projeto>
O projeto produz artigos de blog para indexar em busca e em motores de
resposta de IA. A produção roda em cinco etapas (E1 pesquisa, E2 pauta, E3
redação, E4 revisão, E5 publicação). O painel cobre a vida do artigo depois
que ele existe: da grade até o post no ar.

A fonte de verdade do que existe é o repositório em {{CAMINHO_REPO}}:

- `{{ARQUIVO_GRADE}}` — a grade do mês. Uma linha por artigo. Colunas:
  id, territorio, data_producao, data_publicacao, kw_primaria, volume, kd,
  intencao, slug, url_final, status, aprovado_em.
- `{{PASTA_CONTENT}}` — dois arquivos por artigo escrito:
  `<slug>.html` (versão completa, com JSON-LD) e `<slug>-editor.html`
  (versão que vai colada no CMS, sem `<script>` e sem `<h1>`).
- `producao/registro/kw-donos.csv` — registro de qual URL é dona de qual
  keyword. Serve de aviso de canibalização dentro do painel.
- `pautas/AAAA-MM-DD-<slug>.md` — a pauta que originou cada artigo.

Data de hoje para o painel: {{DATA_HOJE}}.
</contexto_do_projeto>

<maquina_de_estados>
O painel tem cinco raias. Elas mapeiam os estados que já existem na coluna
`status` da grade. Use exatamente estes nomes de raia e estes valores de
status; a correspondência abaixo é obrigatória, porque a grade é lida e
escrita por scripts que dependem dos valores literais.

| Raia no painel | Valor em `status` | O que significa |
|---|---|---|
| 1. Criados | `rascunho` | Linha existe na grade. Pode ainda não ter arquivo em content/. |
| 2. Revisão | `em_revisao` | Artigo escrito, aguardando decisão do editor. |
| 3. Prorrogado | `prorrogado` | Adiado. Sai da fila do dia sem ser reprovado. |
| 4. Aprovados | `aprovado` e `agendado` | Decisão registrada. `agendado` é o subestado de quem já tem data firme. |
| 5. Online | `publicado` | Post no ar, com `url_final` preenchida. |

Três regras de transição, e elas valem para todas as raias, não só para a
primeira:

1. **`prorrogado` é estado novo.** A grade hoje só conhece `rascunho`,
   `em_revisao`, `aprovado`, `agendado` e `publicado`. Ao mover um card para
   Prorrogado, o painel exige dois campos: o motivo (texto livre, obrigatório)
   e a nova `data_publicacao` (obrigatória). Sem os dois, o card não move.
   Guarde o motivo em uma coluna nova `motivo_prorrogacao` na grade exportada.
2. **`aprovado` grava data.** Mover para Aprovados preenche `aprovado_em` com
   a data do dia. Mover para fora limpa o campo.
3. **`publicado` exige URL.** Mover para Online exige `url_final` no formato
   `https://usezerohora.com.br/blog/posts/<slug>-<hash>`, onde `<slug>` é
   idêntico ao da linha e `<hash>` tem 12 caracteres. URL que não bate com o
   slug é recusada com mensagem explícita, porque canonical apontando para URL
   inexistente é o erro mais caro desta etapa. O painel também recusa a
   transição se o texto do artigo ainda contiver o marcador `{HASH}`.

Um artigo reprovado volta para Criados, e o painel pede o motivo, que vira
uma anotação visível no card.
</maquina_de_estados>

<agrupamento>
Dentro de cada raia, os cards aparecem agrupados **por dia e, dentro do dia,
por categoria**.

- **Dia**: a data de publicação (`data_publicacao`). É a data que o negócio
  compromete e a que a prorrogação empurra. Ofereça um seletor no topo para
  trocar o agrupamento para `data_producao`, com `data_publicacao` como
  padrão.
- **Categoria**: o território da coluna `territorio`. Renderize com o nome
  legível, não com o código:
  - T1 — Lycra, camiseta UV e rash guard
  - T2 — Saída de praia, resort e vestidos
  - T3 — Biquíni e top
  Território que aparecer na grade e não estiver nesta lista renderiza com o
  código puro e um aviso discreto de território não mapeado.

Cabeçalho de dia mostra a data por extenso em pt-BR e a contagem de cards.
Cabeçalho de categoria mostra o nome e a contagem. Dia sem card na raia não
renderiza cabeçalho vazio.
</agrupamento>

<funcionalidades>
Aplique esta lista inteira. Cada item é requisito, não sugestão.

**Navegação**
- Cinco raias visíveis ao mesmo tempo em tela larga, com rolagem
  independente por raia. Em tela estreita, um seletor de raia por vez.
- Busca por texto que filtra por keyword primária, slug e id, em tempo real.
- Filtros combináveis: território, intenção de busca, e faixa de KD.
- Contadores no topo: total por raia e total geral.
- Atalhos de teclado: `/` foca a busca, `Esc` fecha o editor, `←` e `→`
  movem o card selecionado de raia.

**Card**
Cada card mostra, sem precisar abrir: id, keyword primária, volume, KD,
intenção, slug, e um indicador de qual arquivo de conteúdo existe (completo,
editor, nenhum). Card cujo artigo linka para um artigo irmão ainda não
publicado mostra selo de dependência com o nome do irmão. Card com `{HASH}`
pendente mostra selo de alerta.

**Edição de texto**
- Abrir o card abre um painel lateral ou modal com duas abas: a versão
  completa e a versão editor.
- A edição acontece em duas visões alternáveis: **código** (textarea com o
  HTML cru, fonte monoespaçada) e **prévia** (o HTML renderizado dentro de um
  contêiner isolado, com estilo próprio que não vaza para o painel).
- Contadores ao vivo enquanto edita: caracteres do `<title>` sobre o limite
  de 60, caracteres da `<meta name="description">` sobre o limite de 155, e
  contagem de palavras do corpo. Passar do limite pinta o contador de
  vermelho e não bloqueia a digitação.
- Botão de desfazer para a última gravação e indicador de "editado, não
  exportado".
- A edição nunca apaga o comentário de produção no topo do arquivo.

**Contexto ao lado do texto**
No painel de edição, mostre também: as keywords que a grade associa ao
artigo, e um aviso quando a keyword primária do card já aparecer em
`kw-donos.csv` com outra URL dona. Esse aviso é a trava anticanibalização, e
o painel a mostra sem impedir a edição.

**Persistência e saída**
O painel roda como página estática e não escreve no repositório. Portanto:
- Todo estado (posição das raias, textos editados, motivos, datas novas) vive
  em `localStorage`, com chave versionada, e sobrevive a recarregar a página.
- Um botão **Exportar** baixa um pacote com: a grade em CSV já com os status
  e datas atualizados, e um arquivo por conteúdo editado, nomeado com o slug
  original. Formato do CSV idêntico ao de entrada, mesma ordem de colunas,
  mais `motivo_prorrogacao`.
- Um botão **Copiar resumo** coloca na área de transferência um resumo em
  texto do que mudou desde a última exportação: quais cards mudaram de raia,
  quais textos foram editados. Serve para colar de volta na sessão e o
  repositório ser atualizado.
- Um botão **Importar** aceita colar o CSV da grade para recarregar o estado
  a partir do repositório, sobrescrevendo o `localStorage` mediante
  confirmação.
- Aviso permanente e visível: o painel não publica nada e não grava no
  repositório. Publicação é etapa separada.
</funcionalidades>

<regras_de_dados>
Estas regras valem para todos os cards e todos os campos, não só para o
primeiro.

1. Todo número e todo texto que aparece no painel vem de arquivo do
   repositório. Volume, KD, intenção, datas e status saem da grade; o texto
   sai de `content/`; o aviso de dono sai de `kw-donos.csv`.
2. Nenhum dado de exemplo, nenhum artigo inventado, nenhuma métrica
   estimada. Se um artigo da grade não tiver arquivo em `content/`, o card
   existe e mostra "sem arquivo de conteúdo" — não invente o texto.
3. Campo vazio na origem aparece vazio no painel, com um traço, e nunca com
   um valor plausível preenchido no lugar.
4. Se um arquivo esperado não existir ou não puder ser lido, registre isso na
   sua resposta final e siga com o restante. Não interrompa a construção por
   causa de um arquivo faltante.
</regras_de_dados>

<exemplos_de_registro>
Três linhas reais da grade e como o card correspondente se comporta. Cobrem
os casos que quebram implementação ingênua.

<exemplo>
Linha: T1-01,T1,2026-08-12,2026-08-19,blusa com proteção uv,1300,18,Informacional,blusa-com-protecao-uv,,em_revisao,
Card: raia 2 (Revisão), no dia 19/08, categoria T1. Tem os dois arquivos em
content/. Selo de {HASH} pendente. Sem selo de dependência: não linka para
irmão nenhum.
</exemplo>

<exemplo>
Linha: T1-02,T1,2026-08-13,2026-08-20,surf lycra,880,8,"Informacional, Comercial",surf-lycra,,bloqueado,
Card: status fora das cinco raias. Renderize numa faixa separada de
"Bloqueados", acima das raias, somente leitura, com o motivo lido da pauta
`pautas/2026-08-13-surf-lycra-BLOQUEIO.md`. Não pode ser arrastado para
raia nenhuma. Note que a coluna intencao contém vírgula dentro de aspas: o
parser de CSV precisa respeitar aspas.
</exemplo>

<exemplo>
Linha: T2-01,T2,2026-08-12,2026-08-19,saida de praia,60500,26,"Informacional, Comercial",saida-de-praia,,rascunho,
Card: raia 1 (Criados), dia 19/08, categoria T2. Não existe
`content/saida-de-praia.html`. O card mostra "sem arquivo de conteúdo", e
abrir o editor mostra estado vazio com explicação, não um textarea em branco
que dá a impressão de que o texto sumiu.
</exemplo>
</exemplos_de_registro>

<construcao>
Antes de escrever o painel:

1. Leia a grade, a pasta de conteúdo, o registro de donos e as pautas. Monte
   o modelo de dados a partir do que existe de verdade.
2. Carregue a skill `artifact-design` para calibrar o desenho da página. Ela é
   obrigatória antes de escrever qualquer artifact.
3. Escreva o arquivo em `{{ARQUIVO_SAIDA}}` e publique com a ferramenta
   Artifact.

Restrições técnicas do artifact, todas obrigatórias:
- Página autocontida. Todo CSS e todo JavaScript inline; nada de CDN, fonte
  remota ou imagem externa. Requisições a host externo são bloqueadas.
- Escreva o conteúdo da página direto, sem `<!doctype>`, `<html>`, `<head>`
  ou `<body>` próprios.
- `<title>` no topo do arquivo.
- Tema claro e escuro: defina a paleta completa em `:root`, redefina os
  tokens sob `@media (prefers-color-scheme: dark)` com a guarda
  `:root:not([data-theme="light"])`, e de novo sob `:root[data-theme="dark"]`.
  Dê ao `body` um fundo explícito por token.
- Responsivo. Conteúdo largo rola dentro do próprio contêiner; o corpo da
  página nunca rola na horizontal.
- Os dados dos artigos vão embutidos no próprio HTML como um objeto
  JavaScript, gerado a partir dos arquivos do repositório.
</construcao>

<tarefa_imediata>
Construa o painel conforme descrito acima, com os dados reais de
{{CAMINHO_REPO}}. Cinco raias, agrupamento por dia e por categoria, edição de
texto com prévia, e exportação que devolve a grade e os textos alterados.
</tarefa_imediata>

Antes de escrever qualquer código, raciocine em <planejamento> sobre: o
modelo de dados que sai dos arquivos lidos, como cada estado da grade cai
numa das cinco raias, e o que acontece com os registros que não caem em
nenhuma. Depois construa.

Ao terminar, responda com:
- <painel>o caminho do arquivo e a URL do artifact publicado</painel>
- <cobertura>quantos artigos entraram, quantos por raia, e quais arquivos
  esperados não foram encontrados</cobertura>
- <decisoes>toda escolha de implementação que o pedido não determinava, em
  uma linha cada</decisoes>
```

---

## B) Racional técnico

| Escolha | Motivo |
|---|---|
| Esqueleto completo de 10 elementos (Cap. 9) | Pedido complexo, com regras de estado, layout e dados. Elemento 10 (prefill) omitido: descontinuado nos modelos 4.6+; o formato é forçado pelo elemento 9. |
| Role prompting (Cap. 3) | "Engenheiro de ferramentas internas" puxa densidade de informação e navegação por teclado, que é o que um painel de fila precisa. Um role genérico de front-end entregaria landing page. |
| Dados de entrada em tags XML próprias (Cap. 4) | Separa a descrição do projeto das regras executáveis. Os arquivos são referenciados por caminho em vez de colados: a grade muda toda semana e o prompt precisa continuar válido. |
| Few-shot com 3 exemplos diversos (Cap. 7) | Cada exemplo cobre um caso que quebra implementação ingênua: card normal, card com status fora das raias, e card sem arquivo de conteúdo. Vírgula dentro de aspas no CSV entra no exemplo porque é o bug mais provável. |
| Precognition em `<planejamento>` (Cap. 6) | O modelo de dados precisa ser decidido antes do HTML. Sem isso o executor escreve a interface e descobre o parsing depois. |
| Saída ("out") anti-alucinação (Cap. 8) | Regra 2 e 4 de `<regras_de_dados>`: artigo sem arquivo aparece como vazio declarado, arquivo faltante vira nota na resposta. É a mesma regra do CLAUDE.md do projeto, e é o que impede o painel de nascer com conteúdo inventado. |
| Escopo declarado explicitamente | Três marcações de "vale para todas as raias / todos os cards, não só a primeira", conforme a regra de literalidade do Playbook §2. |
| Formato de saída em tags (`<painel>`, `<cobertura>`, `<decisoes>`) | Torna a entrega conferível sem ler o código. `<cobertura>` é o critério de sucesso embutido. |

**Reconciliação aplicada**: nenhum prefill na fala final; nenhuma
recomendação de `temperature` ou `budget_tokens`; instruções de ferramenta em
linguagem normal, sem "CRITICAL: You MUST".

**Bloco D (parâmetros de API) omitido**: o alvo é Claude Code / Claude.ai.

---

## C) Variáveis

| Variável | O que recebe | Valor sugerido hoje |
|---|---|---|
| `{{CAMINHO_REPO}}` | Raiz do repositório | `/home/user/uzh-seo` |
| `{{ARQUIVO_GRADE}}` | Grade do mês em uso | `producao/registro/calendario-2026-08.csv` |
| `{{PASTA_CONTENT}}` | Pasta dos HTML | `content/` |
| `{{DATA_HOJE}}` | Data de referência do painel | `2026-08-11` |
| `{{ARQUIVO_SAIDA}}` | Onde gravar o HTML do painel | `producao/painel/painel-conteudos.html` |

---

## D) Premissas declaradas

Quatro pontos do pedido original não tinham resposta única. Foram resolvidos
pelo que o repositório já sustenta, e cada um é um interruptor: mudar a
premissa muda o prompt em um lugar só.

1. **"Prorrogado" não existe na grade.** A máquina de estados registrada em
   `producao/00-workflow.md` é `rascunho → em_revisao → aprovado → agendado →
   publicado`. O prompt cria o estado `prorrogado` e o obriga a carregar
   motivo e nova data, senão vira um limbo onde artigo entra e não sai.
   `agendado` não foi descartado: virou subestado dentro da raia Aprovados.
2. **"Categoria" = território.** O projeto tem três eixos que poderiam ser
   categoria — território (T1/T2/T3), editoria (E1–E5) e cluster de produto.
   Só o território é coluna da grade, então é o único que o painel consegue
   ler sem inventar. Editoria vive nas pautas e entra depois, se pedido.
3. **"Por dia" = `data_publicacao`.** É a data que o negócio compromete e a
   que a prorrogação empurra. `data_producao` fica como alternativa no
   seletor.
4. **Persistência.** Um artifact HTML não escreve no repositório. O estado
   vive em `localStorage` e sai por exportação de arquivos mais um resumo
   copiável. Se o time quiser estado compartilhado entre pessoas e
   dispositivos, o caminho é declarar capabilities de runtime no artifact, e
   isso é uma decisão à parte.

**Sobre as skills citadas no pedido**: `/design` não existe na lista
disponível, e `frontend-slides` serve para apresentações, não para ferramenta
operacional. A skill correta é `artifact-design`, e ela é obrigatória antes de
escrever qualquer artifact. O prompt já a invoca.

---

## E) Como testar

**Critério de sucesso**: um editor abre o painel, encontra um artigo pela
busca, lê o texto, corrige uma frase, move o card de Revisão para Aprovados,
exporta, e o CSV baixado abre no mesmo formato do original com o status novo.

| Caso de teste | O que ele pega |
|---|---|
| Mover um card para Online colando uma URL de outro slug | A trava de canonical. Deve recusar com mensagem explícita, não gravar. |
| Abrir o card `saida-de-praia` (sem arquivo em content/) | Estado vazio explicado. Textarea em branco sem aviso é falha. |
| Recarregar a página depois de editar um texto e não exportar | O texto editado precisa continuar lá. |
| Conferir se `surf-lycra` aparece em alguma raia | Não pode. Status `bloqueado` vive na faixa separada, somente leitura. |
