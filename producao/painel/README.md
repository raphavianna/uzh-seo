# Painel gerencial de conteúdos

`painel-conteudos.html` é gerado, não editado à mão. A fonte é
`template.html` mais o estado real do repositório.

```
python3 scripts/gerar-painel.py
```

## O ciclo de atualização

O painel roda no navegador e **não escreve no repositório**. Não existe
armazenamento compartilhado nem conector de GitHub disponível para a página, e
o estado vive no `localStorage` de quem está usando. O caminho de volta é um
arquivo, e é determinístico:

```
     ┌─ repositório ─────────────────┐
     │ grade + content/ + kw-donos   │
     └───────────────┬───────────────┘
                     │  python3 scripts/gerar-painel.py
                     ▼
              painel-conteudos.html  ──►  publicado como artifact
                     │
                     │  o editor aprova, edita, publica, cola URLs
                     ▼
              botão Exportar  ──►  patch-painel.json
                     │
                     │  python3 scripts/aplicar-patch-painel.py patch-painel.json
                     ▼
     ┌─ repositório atualizado ──────┐
     │ commit, e regera o painel     │
     └───────────────────────────────┘
```

Passo a passo:

1. **Trabalhe no painel.** Mova cards, edite texto, cole as URLs reais dos
   posts. Tudo fica salvo no navegador e sobrevive a recarregar a página.
2. **Exportar.** Baixa um `patch-painel.json` com a grade já atualizada, os
   textos que mudaram e as URLs publicadas. É um arquivo só, em `.json` de
   propósito: é a extensão que o visualizador sempre aceita.
3. **Aplicar no repositório.**
   ```
   python3 scripts/aplicar-patch-painel.py patch-painel.json --dry-run
   python3 scripts/aplicar-patch-painel.py patch-painel.json
   ```
   Ele escreve a grade, os arquivos de `content/`, a `url_dona` em
   `kw-donos.csv` e `urls-publicadas.csv`. Recusa arquivo que não existe,
   URL que não bate com o slug, e texto com `{HASH}` num artigo marcado como
   publicado.
4. **Commit** e `python3 scripts/gerar-painel.py` de novo, para o painel voltar
   a refletir o repositório.
5. **Republique** o artifact com o arquivo novo.

Alternativa sem arquivo: o botão **Copiar resumo** dá um texto com o que mudou,
para colar direto na sessão. Serve para mudanças pequenas; o patch serve para
levar texto editado.

O botão **Importar** faz o caminho inverso: cole o CSV da grade e o painel
relê status, datas e URLs a partir dele, preservando os textos editados.

## O que o painel faz

Mostra os artigos da grade em cinco raias, por dia e por território. Abre o
HTML em código ou prévia, com contador de `title` e de `meta description` ao
vivo. Move cada peça pelas etapas com as travas do fluxo. E fecha as URLs em
E5, que é a parte que antes só existia no terminal.

## Estados

| Raia | `status` |
|---|---|
| 1. Criados | `rascunho` |
| 2. Revisão | `em_revisao` |
| 3. Prorrogado | `prorrogado` (estado novo, exige motivo e data posterior) |
| 4. Aprovados | `aprovado` e `agendado` |
| 5. Online | `publicado` |

`bloqueado` fica fora das raias, na faixa de leitura do topo, junto do
conteúdo de `content/` que não tem linha na grade.

## Como o painel fecha as URLs em E5

A URL de post do blog é `/blog/posts/SLUG-HASH`, e o hash de 12 caracteres só
nasce no CMS na publicação. Por isso os arquivos de `content/` carregam o
marcador `{HASH}`.

Quando você move um card para **Online** e cola a URL real, o painel:

1. confere que o slug da URL bate com o do artigo, e recusa se não bater;
2. troca aquele marcador **em todos os textos do lote**, na forma absoluta e
   na relativa — é a mesma troca de `scripts/publicar-fechar-urls.py`;
3. acerta `datePublished` e `dateModified` no schema, que nascem com a data
   prevista da grade e costumam estar no futuro;
4. substitui o cabeçalho de aviso da versão editor, que mandava trocar o
   marcador à mão, por uma nota com a URL real. Instrução obsoleta colada no
   CMS confunde mais do que ajuda.

A gaveta tem a seção **Links e placeholders**: quantos marcadores restam em
cada versão, para qual slug cada um aponta e em que etapa esse slug está.
Quando um card mostra `{HASH} 0`, ele está pronto para colar no CMS.

`scripts/publicar-fechar-urls.py` continua valendo para quem preferir o
terminal. Os dois fazem a mesma troca e chegam ao mesmo resultado.

## Travas embutidas

- Publicar exige URL `/blog/posts/SLUG-HASH` com SLUG idêntico ao da linha e
  HASH de 12 caracteres alfanuméricos.
- Prorrogar exige motivo e data **posterior** à atual.
- Devolver para Criados exige o motivo da reprovação.
- **Sair de Online exige motivo**, porque apaga a `url_final` da grade. Para
  só corrigir o endereço, use *Corrigir URL* na gaveta e não mova o card.
- `aprovado_em` sobrevive à publicação e só se apaga quando o artigo volta
  para antes da aprovação.
