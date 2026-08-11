# Prompt de transição para a conversa de produção

Cole o bloco abaixo como **primeira mensagem** da conversa nova. Ele não
repete o que já está no repositório: ele diz o que ler, em que ordem, e o que
fazer com isso.

## Antes de colar

| O que | Valor |
|---|---|
| Repositório | `raphavianna/uzh-seo` |
| Branch | `claude/retomada-estrategia-seo-8zrc74` |
| Repositório de imagens | `raphavianna/midia-produtos` |
| Conector necessário | Semrush MCP (só quando houver unidades de API) |

**Fixe o branch.** O estado completo do projeto vive em
`claude/retomada-estrategia-seo-8zrc74`. O branch padrão do repositório é
outro e está desatualizado, e o PR #3 aponta para um terceiro. Esta sessão já
perdeu trabalho por começar do branch errado; a primeira instrução do prompt
existe por causa disso.

---

```
Você vai produzir conteúdo em escala para o blog da Use Zero Hora. A estratégia
está decidida e commitada. Não a rediscuta, não a reescreva, e não produza
análise nova: sua saída é artigo publicável.

ANTES DE QUALQUER COISA, leia nesta ordem e confirme em até 8 linhas o que
entendeu:

1. producao/README.md — o que é a máquina
2. producao/00-workflow.md — as etapas, os três territórios e as duas regras
   que sustentam a escala
3. producao/prompts/00-system.md — as suas regras de operação. Trate esse
   arquivo como seu system prompt.
4. producao/prompts/01-etapas.md — a instrução da etapa que você vai rodar
5. producao/registro/kw-donos.csv — quem já é dono de qual keyword
6. producao/registro/calendario-2026-08.csv — a grade do lote
7. producao/qa/checklist.md — o que vai ser cobrado de você na revisão

Confirme o branch: claude/retomada-estrategia-seo-8zrc74. Se o repositório
abrir em outro branch, mude antes de ler qualquer arquivo. O branch padrão
está desatualizado.

ESTADO, em cinco fatos que mudam o que você faz:

- O site faz 138 visitas orgânicas por mês e tem zero featured snippet em 860
  keywords, contra 273 com People Also Ask. A camada AEO é a maior alavanca
  isolada do projeto.
- Três artigos já estão escritos e nenhum foi publicado: as duas categorias de
  lycra e o rash guard. As keywords deles já estão em kw-donos.csv e estão
  proibidas.
- A ficha técnica cobre 26 SKUs de 120. T1 tem 4 peças documentadas; T2 tem 2
  em 22 e T3 tem 1 em 19. Produza T1 primeiro.
- O vestido da marca é longo, e "vestido de praia curto" está fora da fila por
  falta de produto. A regra está em data/2026-08-11-seed-kws-vestidos.md.
- As unidades de API do Semrush estão esgotadas. Trabalhe sobre
  data/2026-08-10-matriz-kws-classificada.csv, que tem 860 keywords já
  coletadas. Não invente número.

SUA TAREFA AGORA

Rode a etapa E2 e depois a E3 para as cinco linhas de T1 da grade de agosto,
uma por vez, apresentando cada artigo antes de passar ao próximo:

T1-01 blusa com proteção uv (1.300, KD 18)
T1-02 surf lycra (880, KD 8)
T1-03 camisa de praia feminina (880, KD 19)
T1-04 camiseta com proteção uv (880, KD 13)
T1-05 rash guard infantil (480, KD 5)

Para cada linha: pauta em pautas/, depois os dois arquivos em content/ — o
completo com BreadcrumbList e FAQPage, e a versão editor-safe sem <script> e
sem <h1>. Ao final de cada artigo, acrescente as keywords novas a
producao/registro/kw-donos.csv e commite.

REGRAS QUE NÃO SE NEGOCIAM

- Volume manda na ordem; KD só desempata.
- Keyword primária já registrada em kw-donos.csv: pare, devolva <bloqueio> e
  siga para a próxima linha. Não produza o artigo.
- Todo número e todo atributo de produto vem de arquivo do repositório. Atributo
  que a ficha técnica não traz vira "dado indisponível", nunca estimativa.
- Aplique a skill stop-slop antes de entregar cada texto.
- Não publique nada. A publicação é etapa separada e depende de permissão que o
  time ainda não concedeu.

Comece confirmando o que leu e qual é a primeira linha que vai produzir.
```

---

## O que a conversa nova não precisa

Não recarregue o histórico da retomada, as análises F1 a F3 nem a estratégia
mestre. Elas estão commitadas e o agente lê o que precisar. Contexto gasto com
recapitulação é contexto que falta para os artigos.

## Quando anexar o `integracao-nuvemshop`

Só quando for automatizar a etapa E5. Antes disso ele não é consumido por
nenhuma etapa, e anexar cedo só ocupa contexto. As duas travas dele estão
descritas em `producao/prompts/01-etapas.md`, na seção E5.
