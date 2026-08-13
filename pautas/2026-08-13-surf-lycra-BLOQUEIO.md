# Bloqueio — T1-02 `surf lycra`

- **ID na grade**: T1-02 · **Território**: T1
- **Data**: 2026-08-13
- **Status**: bloqueado em E2. Artigo não produzido.
- **Regra aplicada**: `producao/prompts/00-system.md`,
  `<regra_de_dono_de_keyword>` e `producao/00-workflow.md` ("remova toda
  keyword já presente em kw-donos.csv e toda variante gráfica de uma keyword
  já na grade").

## O conflito

`surf lycra` é variante de ordem de palavras de `lycra surf`, registrada em
`producao/registro/kw-donos.csv` para `/masculino/lycra-surf/`
(`content/masculino-lycra-surf.html`).

Fonte: `data/2026-08-10-matriz-kws-classificada.csv` (Semrush BR, coleta de
2026-08-09).

| Métrica | `surf lycra` | `lycra surf` |
|---|---:|---:|
| Volume/mês | 880 | 880 |
| CPC | R$ 0,10 | R$ 0,10 |
| KD | 8 | 9 |
| Cluster | Lycra, camiseta UV e rash | Lycra, camiseta UV e rash |
| Intenção | Informacional, Comercial | Comercial |

Volume e CPC idênticos apontam para a mesma consulta subjacente na base do
Semrush. A diferença de KD (8 contra 9) e de intenção classificada fica
dentro da variação que a ferramenta produz para o mesmo termo em grafias
diferentes.

## Por que a matriz não pegou

A coluna `norm` de `data/2026-08-10-matriz-kws-classificada.csv` traz
`surf lycra` e `lycra surf` como normalizações distintas, e a coluna
`variante_de` está vazia nas duas linhas. O script
`scripts/classificacao-kws.py` normaliza acento e caixa, e não ordem de
palavras.

**Correção pendente para E1**: acrescentar ao classificador uma chave de
token ordenado (`sorted(tokens)`) para detectar permutação. Sem isso, a
próxima grade volta a sortear os dois termos.

## O custo de produzir mesmo assim

`content/masculino-lycra-surf.html` já cita "lycra surf" 29 vezes, mais
"lycra de surf" e "lycra para surf". `content/feminino-lycra-surf.html` cita
17 vezes e `content/rash-guard.html`, 4.

Um artigo novo para `surf lycra` colocaria duas URLs disputando a mesma
intenção no cluster de maior prioridade do projeto (585,
`analysis/21-editorias.md`). É o mesmo defeito que o cluster de poncho tem
hoje, com três URLs, e que a máquina de produção existe para não repetir.

## Ação tomada

Registrei as duas variantes como propriedade da URL que já as cobre, para
travar o sorteio em lotes futuros:

| Keyword | Volume | URL dona | status |
|---|---:|---|---|
| surf lycra | 880 | `/masculino/lycra-surf/` | variante-de-lycra-surf |
| surf lycras | 590 | `/masculino/lycra-surf/` | variante-de-lycra-surf |

`surf lycras` (590, KD 10) entrou junto por ser o plural do mesmo termo e
estar livre até agora.

Status de T1-02 em `producao/registro/calendario-2026-08.csv`: `bloqueado`.

## Candidato para a substituição, a decidir em E1

A substituição é etapa E1, e `producao/00-workflow.md` fixa que a grade não
cresce no meio do mês. Não substituí por conta própria.

`camiseta surf` (720, KD 8, Comercial, livre) é a keyword de maior volume
livre em T1 fora do lote de agosto.

**Ressalva antes de promover**: `/masculino/lycra-surf/` já é dona de
`camiseta surf masculina` (480) e `/feminino/lycra-surf/` de
`camiseta para surf feminina` (210). O termo genérico fica entre as duas
páginas e precisa de leitura de SERP para decidir se vira hub próprio ou se
entra como seção dentro de uma das categorias.

Alternativa sem esse risco: `camiseta proteção solar` (480, KD 21,
Comercial, PAA), que cabe na editoria E2 e não toca o cluster de lycra.
