# Resumo de leitura — export BaseLinker de produtos

## Proveniência

| Campo | Valor |
|---|---|
| Arquivos | `exportprod01_20260809_22_35.csv` e `exportproduto02_20260809_22_38.csv` |
| Origem | BaseLinker, Produtos → Importar/Exportar, perfil montado nesta sessão |
| Data | 2026-08-09, 22h35 e 22h38 |
| Enviado por | Raphael Vianna, 2026-08-10 |
| Saída utilizável | `data/2026-08-10-ficha-tecnica-26-skus.csv` |

Os arquivos originais **não foram arquivados em `data/`** por estarem malformados
(ver defeito abaixo). Arquivar depois da reexportação corrigida.

## Defeito de exportação

Falta quebra de linha no fim do código de cada seção. O BaseLinker concatenou
todos os registros em uma linha lógica só. O arquivo A aparenta 60.888 linhas,
mas isso são as quebras internas das descrições em HTML, não separação de
registros.

**Recuperação**: como a tag `[SKU]` não resolveu e saiu literal em toda linha, a
string `"[SKU]";` serviu de marcador de início de registro. Dividindo por ela,
recuperei **1.098 registros do arquivo A** e **6.267 do arquivo B** sem perda.

**Tags que não resolveram** (nome errado): `[SKU]`, `[EAN]`,
`[nome_da_categoria]`, `[caminho_da_categoria_1]`.

**Tags que resolveram**: `[ID_produto]`, `[nome_do_produto]`,
`[preco_padrao_56777]`, `[quantidade]`, `[peso]`, `[descricao]`,
`[size_chart_127178]`, `[ncm_121167]`, `[foto_1]`, e no arquivo B
`[SKU_variacao]`, `[EAN_variacao]`, `[variacao_id_da_categoria]`,
`[variacao_foto_1]`, `[tipo_fonte_link]`, `[link_nome_origem]`,
`[ID_link_produto]`, `[ID_link_variacao]`.

## Correção da leitura anterior

Na sessão eu havia sinalizado que o BaseLinker tinha 1.098 produtos contra 120 do
Nuvemshop, e levantado a hipótese de que o catálogo real fosse muito maior.
**Os dados desmentem isso.**

Entre os 1.098 registros há apenas **79 descrições distintas**. Os registros são
réplicas em nível de variação, uma por combinação de cor e tamanho por canal —
"PONCHO CLASSICO Cor:Vaca;Tamanho:P" é um registro, "PONCHO CLASSICO
Cor:Vaca;Tamanho:M" é outro.

O arquivo B confirma, pela distribuição de links por canal:

| Canal | Registros |
|---|---:|
| UZH Mercado Livre | 1.610 |
| UZH Bling | 990 |
| Shopee UseZeroHora | 890 |
| UZH NuvemShop | 806 |
| UZH Shein | 544 |
| UZH TikTok | 493 |

Dos 806 registros linkados à NuvemShop, **795 têm "Cor:" no nome** — são réplicas
de variação, não produtos. Apenas 9 são nomes de produto limpos.

**Conclusão**: o catálogo de produtos-mãe fica na casa de 79 a 120, coerente com
os 120 do relatório do Nuvemshop. A decisão de seguir com os 120 está correta e o
alarme anterior foi meu erro de leitura, corrigido aqui.

## O join entre os dois sistemas não fecha

Três tentativas, com o resultado de cada:

| Método | Resultado | Veredito |
|---|---:|---|
| Nome idêntico normalizado | 26 de 120 | **Seguro. Adotado.** |
| Similaridade de nome (Jaccard ≥ 0,6) | 58 de 120 | **Descartado** |
| Ponte pelos links de canal da NuvemShop | 5 de 120 | Descartado |

A similaridade foi descartada por produzir falsos positivos que colocariam a
ficha técnica de um produto em outro. Exemplos medidos:

- "Poncho Premium Infantil" casou com "PONCHO RESORT PREMIUM INFANTIL" a 0,90 —
  mas os dois existem separadamente no catálogo do Nuvemshop, então o casamento
  está errado.
- Três produtos distintos de "Camiseta Lycra Surf UV50 Manga Longa" (Preto com
  Verde, Verde com Preto, Azul com Preto) casaram todos com o mesmo registro.

Pela regra de dados do projeto, conteúdo só afirma atributo que existe na base do
produto. Uma ficha técnica atribuída ao produto errado faz o conteúdo mentir, o
que é pior que não ter ficha. Por isso só os 26 exatos entraram.

**O que fecharia o join**: SKU nos dois lados. O relatório de vendas do Nuvemshop
não traz SKU, e a tag de SKU do BaseLinker não resolveu. Um export de catálogo do
Nuvemshop (não o de vendas) com SKU, mais a tag correta de SKU no BaseLinker,
resolvem de uma vez.

## O que a ficha técnica dos 26 entrega

**Descrições ricas e específicas**, de 792 a 3.094 caracteres, com exatamente o
tipo de atributo que o conteúdo precisa afirmar. Do MAIO STORM:

> mangas longas, gola alta, abertura para o dedo nos punhos e fechamento frontal
> por zíper YKK®, modelagem anatômica

Isso é dado citável. Resolve parcialmente o bloqueio de ficha técnica que estava
registrado nas pautas da F3.

**Cobertura por cluster**, dos 26:

| Cluster | SKUs com ficha |
|---|---:|
| Maiô | 8 |
| Lycra, camiseta UV | 5 |
| Poncho | 4 |
| Saída de praia | 3 |
| Neoprene | 2 |
| Sunga e bermuda | 2 |
| Biquíni | 1 |
| Sapatilha | 1 |

## Duas limitações da ficha

**1. A tabela de medidas é imagem, não texto.** Os 1.098 registros têm
`size_chart` preenchido, e **os 1.098 apontam para URL de imagem** em
`upload.cdn.baselinker.com`. Nenhum traz medida em texto.

Consequência direta: **não há como extrair centímetro por tamanho para o
conteúdo**. As pautas de rash guard, saída de praia e sunga pedem medida
concreta, e ela não existe em forma legível. Ou o time digita a tabela, ou o
conteúdo fica sem essa camada — e medida em imagem também não é lida por motor de
resposta, então é perda dupla.

**2. Interface do ChatGPT colada dentro de duas descrições.** PONCHO RESORT
PREMIUM FEMININO e PONCHO RESORT PREMIUM INFANTIL trazem o DOM da janela do
ChatGPT — `data-message-author-role`, `data-message-id`,
`data-message-model-slug="gpt-4o-mini"`. No arquivo inteiro são 102 ocorrências.

Os dois produtos compartilham a mesma descrição de 3.094 caracteres, então é uma
descrição poluída replicada em dois produtos. Limpar antes de qualquer trabalho
de conteúdo: `data-message-model-slug="gpt-4o-mini"` servido na página é
assinatura literal de conteúdo gerado por IA.

## Próximo passo para fechar

1. Reexportar com quebra de linha no fim de cada bloco de seção.
2. Rodar o bloco de diagnóstico para descobrir os nomes corretos de SKU, EAN,
   categoria e caminho de categoria.
3. Exportar o **catálogo** do Nuvemshop com SKU, não o relatório de vendas.
4. Com SKU dos dois lados, o join fecha para os 120 e a ficha técnica vale para o
   catálogo inteiro.
