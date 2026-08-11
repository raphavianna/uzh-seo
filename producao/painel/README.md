# Painel gerencial de conteúdos

`painel-conteudos.html` é gerado, não editado à mão. A fonte é
`template.html` mais o estado real do repositório.

```
python3 scripts/gerar-painel.py
```

Rode isso toda vez que a grade, um texto de `content/` ou `kw-donos.csv`
mudar. O painel é estático: ele não lê o repositório em tempo de execução,
os dados vão embutidos no HTML.

## O que o painel faz e o que ele não faz

Faz: mostra os artigos em cinco raias por dia e por território, permite ler
e editar o HTML com prévia, valida as transições de etapa, e exporta a grade
atualizada mais os textos alterados.

Não faz: publicar no blog e gravar no repositório. O estado do editor vive no
`localStorage` do navegador dele. O caminho de volta é o botão **Exportar**,
que baixa a grade em CSV e os arquivos editados, ou o botão **Copiar resumo**,
que dá o texto para colar na sessão.

## Estados

As cinco raias mapeiam a coluna `status` da grade:

| Raia | `status` |
|---|---|
| 1. Criados | `rascunho` |
| 2. Revisão | `em_revisao` |
| 3. Prorrogado | `prorrogado` (estado novo, exige motivo e data posterior) |
| 4. Aprovados | `aprovado` e `agendado` |
| 5. Online | `publicado` |

`bloqueado` fica fora das raias, na faixa de leitura do topo, junto do
conteúdo de `content/` que não tem linha na grade.

## Travas embutidas

- Publicar exige URL no formato `/blog/posts/<slug>-<hash de 12>`, com o slug
  idêntico ao da linha. URL de outro artigo é recusada.
- Publicar é recusado enquanto restar `{HASH}` no texto: canonical com o
  marcador quebra a indexação da página.
- Prorrogar exige motivo e data posterior à atual.
- Devolver para Criados exige o motivo da reprovação.
