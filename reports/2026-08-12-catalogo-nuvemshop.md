# Catálogo Nuvemshop — resposta às perguntas do lote T1

- **Coletado em**: 2026-08-12
- **Fonte**: API Nuvemshop `2025-03`, loja 5540626 (USEZEROHORA)
- **Natureza**: medido, leitura direta do catálogo
- **Dump bruto**: `data/2026-08-12-nuvemshop-catalogo.json`
- **Escopo**: 48 categorias, 140 produtos

## 1. As URLs que o lote linka

| URL | Tipo | Nome | Produtos | Citações no lote | Nota |
|---|---|---|---:|---:|---|
| `/rash-guard/` | **NÃO ENCONTRADO** | — | — | 6 | reserva 24.310 buscas/mês no registro; zero linha no baseline |
| `/masculino/lycra-surf/` | categoria | LYCRA SURF | 15 | 11 | ranqueia em 4 linhas do baseline |
| `/feminino/lycra-surf/` | categoria | LYCRA SURF | 15 | 5 | usuário confirmou como produto em 2026-08-11 |
| `/feminino/maio/` | categoria | MAIÔ | 25 | 2 | 42% do orgânico do domínio |
| `/quem-somos/` | **NÃO ENCONTRADO** | — | — | 2 |  |
| `/masculino/` | categoria | MASCULINO | 49 | 1 |  |
| `/feminino/` | categoria | FEMININO | 105 | 1 |  |
| `/feminino/poncho1/` | categoria | PONCHO | 17 | 0 | sufixo numérico: possível duplicata |
| `/masculino/poncho/` | categoria | PONCHO | 17 | 0 | 54% da receita da loja |

**2 URL(s) citada(s) no lote não existe(m) no catálogo.** Os links precisam de destino novo antes de publicar:
- `/rash-guard/` — 6 citações, 8 keywords reservadas
- `/quem-somos/` — 2 citações, 0 keywords reservadas

## 2. Árvore de categorias

| id | Nome | Handle | Pai | Produtos |
|---:|---|---|---:|---:|
| 34691370 | SURFNELAS | `surfnelas` | 0 | 8 |
| 34709846 | MASCULINO | `masculino` | 0 | 49 |
| 34709847 | FEMININO | `feminino` | 0 | 105 |
| 34709848 | INFANTIL | `infantil1` | 0 | 10 |
| 38098906 | OUTLET | `outlet` | 0 | 41 |
| 40155134 | NEOPRENE | `neoprene` | 0 | 3 |
| 34709877 | Lycra | `lycra1` | 34691370 | 0 |
| 34709874 | CAMISETA UV50+ | `camiseta-uv` | 34709846 | 5 |
| 34710003 | LYCRA SURF | `lycra-surf` | 34709846 | 15 |
| 34710004 | PONCHO | `poncho` | 34709846 | 17 |
| 34710005 | BERMUDA | `bermuda` | 34709846 | 3 |
| 34710006 | MOLETOM | `moletom1` | 34709846 | 7 |
| 36720790 | SUNGA | `sunga` | 34709846 | 2 |
| 34709875 | CAMISETA UV50+ | `camiseta-uv1` | 34709847 | 7 |
| 34709978 | BIQUINI | `biquini` | 34709847 | 18 |
| 34709979 | MAIÔ | `maio` | 34709847 | 25 |
| 34709980 | SAÍDA DE PRAIA | `saida-de-praia` | 34709847 | 18 |
| 34709981 | CONJUNTO | `conjunto` | 34709847 | 0 |
| 34709982 | MOLETOM | `moletom` | 34709847 | 9 |
| 34710007 | PONCHO | `poncho1` | 34709847 | 17 |
| 34710187 | LYCRA SURF | `lycra-surf1` | 34709847 | 4 |
| 35693991 | VESTIDO RESORT | `vestido-resort` | 34709847 | 4 |
| 38215044 | IOGA / FITNESS | `ioga-fitness` | 34709847 | 7 |
| 38993468 | AEROLOOK | `aerolook` | 34709847 | 3 |
| 34709876 | CAMISETA UV50+ | `camiseta-uv2` | 34709848 | 4 |
| 34710008 | PONCHO | `poncho2` | 34709848 | 4 |
| 37984101 | Maiô | `maio1` | 34709848 | 2 |
| 34710072 | Marquinha | `marquinha` | 34709978 | 9 |
| 34710073 | Asa Delta | `asa-delta` | 34709978 | 2 |
| 34710074 | Hot Pant | `hot-pant` | 34709978 | 4 |
| 34710075 | Sunkini | `sunkini` | 34709978 | 3 |
| 34710055 | Manga Longa | `manga-longa` | 34709979 | 18 |
| 34710056 | Gola Alta | `gola-alta` | 34709979 | 6 |
| 34710057 | Alças | `alcas` | 34709979 | 2 |
| 34710058 | Manga 3/4 | `manga-3-4` | 34709979 | 2 |
| 34710059 | Conjunto | `conjunto1` | 34709979 | 2 |
| 34710069 | Vestido Manga Longa | `vestido-manga-longa` | 34709980 | 6 |
| 34710070 | Vestido Regata | `vestido-regata` | 34709980 | 3 |
| 34710071 | Saia | `saia` | 34709980 | 7 |
| 34710584 | Conjunto Atoalhado | `conjunto-atoalhado` | 34709980 | 1 |
| 36011365 | Shorts | `shorts` | 34709980 | 1 |
| 38098937 | Feminino | `feminino1` | 38098906 | 31 |
| 38098938 | Masculino | `masculino1` | 38098906 | 9 |
| 38215047 | Calça | `calca` | 38215044 | 2 |
| 38216828 | Macaquinho | `macaquinho` | 38215044 | 1 |
| 38217400 | Macacão | `macacao` | 38215044 | 1 |
| 38217865 | Shorts | `shorts1` | 38215044 | 1 |
| 38218007 | Top | `top` | 38215044 | 2 |

## 3. Os SKUs citados nos artigos

### `itamambuca` — lacuna: grade de tamanhos, cores e composição

**CAMISETA LYCRA FEMININA ITAMAMBUCA** (id 355991468, handle `camiseta-lycra-feminina-itamambuca-89fkm`)
- Categorias: FEMININO (`feminino`), LYCRA SURF (`lycra-surf1`)
- Atributos de variante: cor, Tamanho
- 8 variante(s):
  - Roxa / P — R$ 299.00, estoque 11, 0.220 kg
  - Roxa / M — R$ 299.00, estoque 22, 0.220 kg
  - Roxa / G — R$ 299.00, estoque 22, 0.220 kg
  - Roxa / GG — R$ 299.00, estoque 11, 0.220 kg
  - Branca / P — R$ 299.00, estoque 11, 0.220 kg
  - Branca / M — R$ 299.00, estoque 24, 0.220 kg
  - Branca / G — R$ 299.00, estoque 26, 0.220 kg
  - Branca / GG — R$ 299.00, estoque 12, 0.220 kg
- Descrição: Lycra Feminina Itamambuca UV50+ – Use Zero Hora Inspirada na energia das praias de Ubatuba e desenvolvida para mulheres que vivem o mar, a Lycra Feminina Itamambuca UV50+ combina proteção, conforto e performance em uma peça versátil para surf, beach tennis, stand up paddle, corrida, caminhadas e atividades ao ar livre. Sua modelagem anatômica proporciona ajuste perfeito ao corpo sem limitar os movimentos, enquanto o tecido tecnológico de alta elasticidade acompanha cada remada, mergulho ou treino com máximo conforto. O design exclusivo conta com recortes ergonômicos e costuras anatômicas em contraste, valorizando a silhueta feminina e garantindo excelente caimento. O punho com abertura para o polegar oferece maior proteção para as mãos e evita que a manga deslize durante a prática esportiva. Destaques do Produto ✔ Proteção UV50+ permanente ✔ Bloqueia até 98% dos raios solares nocivos ✔ Modelagem feminina anatômica e ajustada ao corpo ✔ Manga longa com abertura para o polegar ✔ Tecido leve, respirável e de secagem rápida ✔ Alta elasticidade para total liberdade de movimentos ✔ Costuras reforçadas para maior durabilidade ✔ Toque macio e confortável na pele ✔ Excelente cobertura mesmo

### `neon` — lacuna: composição do tecido e comprimento de manga

**CAMISETA UV INFANTIL NEON** (id 331018836, handle `camiseta-uv-infantil-neon-nd9jy`)
- Categorias: INFANTIL (`infantil1`), CAMISETA UV50+ (`camiseta-uv2`)
- Atributos de variante: Cor, Tamanho
- 10 variante(s):
  - Rosa / 2 — R$ 149.00, estoque 10, 0.120 kg
  - Rosa / 4 — R$ 149.00, estoque 10, 0.120 kg
  - Rosa / 6 — R$ 149.00, estoque 10, 0.120 kg
  - Rosa / 8 — R$ 149.00, estoque 10, 0.120 kg
  - Rosa / 10 — R$ 149.00, estoque 10, 0.120 kg
  - Azul / 2 — R$ 149.00, estoque 10, 0.120 kg
  - Azul / 4 — R$ 149.00, estoque 10, 0.120 kg
  - Azul / 6 — R$ 149.00, estoque 10, 0.120 kg
  - Azul / 8 — R$ 149.00, estoque 10, 0.120 kg
  - Azul / 10 — R$ 149.00, estoque 10, 0.120 kg
- Descrição: Camiseta Infantil Lycra UV50+ Proteção Solar Use Zero Hora Para Praia, Piscina e Esportes ao Ar Livre - Tecido Leve - Logo Metalizado - Cores Lisas Descrição A camiseta infantil da Use Zero Hora é a escolha ideal para quem busca proteção solar, conforto e estilo em atividades ao ar livre. Fabricada em lycra leve e com proteção UV50+ , ela bloqueia até 98% dos raios UVA e UVB, protegendo sua pele com máxima eficiência. Com design moderno e discreto, conta com logo metalizado exclusivo no peito e está disponível em três cores lisas que combinam com qualquer ocasião ao ar livre. Principais Características Tecido em lycra leve de alta qualidade Proteção UV50+ , ideal para exposição solar prolongada Secagem rápida e excelente respirabilidade Logo metálico estampado no peito com acabamento premium Design esportivo com caimento confortável Cores disponíveis : Azul Claro, Azul Turquesa, Rosa Tamanhos : P, M, G Modelagem infantil Indicações de Uso Praia e banho de sol Pesca esportiva e lazer Motociclismo Corrida, trekking, ciclismo e outros esportes outdoor Atividades prolongadas sob o sol Garantia e Envio Produto novo e original Pronta entrega com envio rápido Embalagem segura Suporte ao c

### `engana mamãe` — lacuna: percentuais da composição

Nenhum produto encontrado com esse termo.

### `cepilho` — lacuna: fator de proteção (a ficha diz "conforme composição" sem trazer a composição)

**MAIO CEPILHO INFANTIL** (id 355997375, handle `maio-cepilho-infantil-1id8r`)
- Categorias: FEMININO (`feminino`), MAIÔ (`maio`), Manga Longa (`manga-longa`), Gola Alta (`gola-alta`), INFANTIL (`infantil1`), Maiô (`maio1`)
- Atributos de variante: Cor, Tamanho
- 8 variante(s):
  - Marinho / 6 — R$ 299.00, estoque 11, 0.230 kg
  - Marinho / 8 — R$ 299.00, estoque 11, 0.230 kg
  - Marinho / 10 — R$ 299.00, estoque 11, 0.230 kg
  - Marinho / 12 — R$ 299.00, estoque 10, 0.230 kg
  - Vermelho / 6 — R$ 299.00, estoque 9, 0.230 kg
  - Vermelho / 8 — R$ 299.00, estoque 8, 0.230 kg
  - Vermelho / 10 — R$ 299.00, estoque 8, 0.230 kg
  - Vermelho / 12 — R$ 299.00, estoque 7, 0.230 kg
- Descrição: O Maiô Infantil Cepilho foi desenvolvido para oferecer conforto, liberdade de movimentos e proteção durante momentos de lazer, praia, piscina e atividades aquáticas. Com modelagem pensada para acompanhar os movimentos com praticidade, é uma peça ideal para crianças que precisam de segurança e bem-estar em contato com a água. Confeccionado em tecido de alta qualidade, proporciona toque agradável, secagem rápida e excelente ajuste ao corpo, contribuindo para maior conforto durante o uso. Seu design funcional facilita o vestir e garante praticidade no dia a dia, sendo uma ótima opção para passeios, viagens e brincadeiras ao ar livre. Modelo: Maiô Infantil Cepilho Categoria: Maiô infantil para praia e piscina Modelagem: Confortável e anatômica Gênero: Feminino Marca: USEZEROHORA Tipo de traje de banho: Maiô body surf Proteção Solar: Conforme composição do tecido Origem: Produto nacional Garantia: 30 dias contra defeitos de fabricação, mediante conservação adequada e sem uso Ideal para praia, piscina, natação recreativa, passeios ao ar livre e momentos de lazer com conforto e praticidade. Observação: As medidas podem apresentar pequenas variações de produção, especialmente por se tratar

### `lycra` — lacuna: instruções de lavagem

**Camiseta Lycra Surf UV50 Manga Longa Verde Liso** (id 270617788, handle `camiseta-lycra-surf-uv50-manga-longa-verde-liso`)
- Categorias: MASCULINO (`masculino`), LYCRA SURF (`lycra-surf`)
- Atributos de variante: Tamanho
- 3 variante(s):
  - P — R$ 249.99, estoque 0, 0.340 kg
  - M — R$ 249.99, estoque 0, 0.340 kg
  - G — R$ 249.99, estoque 0, 0.340 kg
- Descrição: Camiseta Lycra UV50 Manga Longa com Punho Dedal – Use Zero Hora Proteção, desempenho e estilo para quem vive o mar. A camiseta de lycra da Use Zero Hora foi desenvolvida para atender surfistas exigentes, unindo tecnologia têxtil, conforto e funcionalidade em uma peça de alta performance. Diferenciais do Produto: Proteção Solar de Alta Eficiência: Com FPS 98% e fator UV50 , garante proteção total contra os raios UVA e UVB durante longas sessões ao sol. Gramatura Premium de 240g: Uma lycra encorpada, resistente e durável, muito superior às opções mais finas do mercado. Proporciona maior conforto térmico, mais estrutura e melhor acabamento. Tecido Tecnológico: Composição de 90% poliamida e 10% elastano . A poliamida entrega maior resistência ao sal e cloro, secagem rápida, toque macio e durabilidade superior em relação ao elastano e ao poliéster. Modelagem Justa e Segura: Ajuste ao corpo que evita que a peça escorregue durante a remada ou na queda. Ideal para performance dentro d’água. Punho Duplo com Abertura para o Dedo (Dedal): Garante que a manga fique firme, protegendo até o punho com segurança. Elástico Ajustável na Barra: Evita que a lycra suba ao furar ondas ou cair da prancha

**Camiseta Lycra Surf UV50 Manga Longa Azul Liso** (id 270617797, handle `camiseta-lycra-surf-uv50-manga-longa-azul-liso`)
- Categorias: MASCULINO (`masculino`), LYCRA SURF (`lycra-surf`)
- Atributos de variante: Tamanho
- 3 variante(s):
  - P — R$ 249.99, estoque 0, 0.340 kg
  - M — R$ 249.99, estoque 0, 0.340 kg
  - G — R$ 249.99, estoque 0, 0.340 kg
- Descrição: Camiseta Lycra UV50 Manga Longa com Punho Dedal – Use Zero Hora Proteção, desempenho e estilo para quem vive o mar. A camiseta de lycra da Use Zero Hora foi desenvolvida para atender surfistas exigentes, unindo tecnologia têxtil, conforto e funcionalidade em uma peça de alta performance. Diferenciais do Produto: Proteção Solar de Alta Eficiência: Com FPS 98% e fator UV50 , garante proteção total contra os raios UVA e UVB durante longas sessões ao sol. Gramatura Premium de 240g: Uma lycra encorpada, resistente e durável, muito superior às opções mais finas do mercado. Proporciona maior conforto térmico, mais estrutura e melhor acabamento. Tecido Tecnológico: Composição de 90% poliamida e 10% elastano . A poliamida entrega maior resistência ao sal e cloro, secagem rápida, toque macio e durabilidade superior em relação ao elastano e ao poliéster. Modelagem Justa e Segura: Ajuste ao corpo que evita que a peça escorregue durante a remada ou na queda. Ideal para performance dentro d’água. Punho Duplo com Abertura para o Dedo (Dedal): Garante que a manga fique firme, protegendo até o punho com segurança. Elástico Ajustável na Barra: Evita que a lycra suba ao furar ondas ou cair da prancha

**Camiseta Lycra Surf UV50 Manga Longa Rosa Liso** (id 270617805, handle `camiseta-lycra-surf-uv50-manga-longa-rosa-liso`)
- Categorias: MASCULINO (`masculino`), LYCRA SURF (`lycra-surf`)
- Atributos de variante: Tamanho
- 3 variante(s):
  - P — R$ 249.99, estoque 3, 0.340 kg
  - M — R$ 249.99, estoque 0, 0.340 kg
  - G — R$ 249.99, estoque 2, 0.340 kg
- Descrição: Camiseta Lycra UV50 Manga Longa com Punho Dedal – Use Zero Hora Proteção, desempenho e estilo para quem vive o mar. A camiseta de lycra da Use Zero Hora foi desenvolvida para atender surfistas exigentes, unindo tecnologia têxtil, conforto e funcionalidade em uma peça de alta performance. Diferenciais do Produto: Proteção Solar de Alta Eficiência: Com FPS 98% e fator UV50 , garante proteção total contra os raios UVA e UVB durante longas sessões ao sol. Gramatura Premium de 240g: Uma lycra encorpada, resistente e durável, muito superior às opções mais finas do mercado. Proporciona maior conforto térmico, mais estrutura e melhor acabamento. Tecido Tecnológico: Composição de 90% poliamida e 10% elastano . A poliamida entrega maior resistência ao sal e cloro, secagem rápida, toque macio e durabilidade superior em relação ao elastano e ao poliéster. Modelagem Justa e Segura: Ajuste ao corpo que evita que a peça escorregue durante a remada ou na queda. Ideal para performance dentro d’água. Punho Duplo com Abertura para o Dedo (Dedal): Garante que a manga fique firme, protegendo até o punho com segurança. Elástico Ajustável na Barra: Evita que a lycra suba ao furar ondas ou cair da prancha

**Camiseta Lycra Surf UV50 Manga Longa Preto Liso** (id 270617813, handle `camiseta-lycra-surf-uv50-manga-longa-preto-liso`)
- Categorias: MASCULINO (`masculino`), LYCRA SURF (`lycra-surf`)
- Atributos de variante: Tamanho
- 4 variante(s):
  - P — R$ 249.99, estoque 24, 0.340 kg
  - M — R$ 249.99, estoque 2, 0.340 kg
  - G — R$ 249.99, estoque 0, 0.340 kg
  - GG — R$ 249.99, estoque 4, 0.340 kg
- Descrição: Camiseta Lycra UV50 Manga Longa com Punho Dedal – Use Zero Hora Proteção, desempenho e estilo para quem vive o mar. A camiseta de lycra da Use Zero Hora foi desenvolvida para atender surfistas exigentes, unindo tecnologia têxtil, conforto e funcionalidade em uma peça de alta performance. Diferenciais do Produto: Proteção Solar de Alta Eficiência: Com FPS 98% e fator UV50 , garante proteção total contra os raios UVA e UVB durante longas sessões ao sol. Gramatura Premium de 240g: Uma lycra encorpada, resistente e durável, muito superior às opções mais finas do mercado. Proporciona maior conforto térmico, mais estrutura e melhor acabamento. Tecido Tecnológico: Composição de 90% poliamida e 10% elastano . A poliamida entrega maior resistência ao sal e cloro, secagem rápida, toque macio e durabilidade superior em relação ao elastano e ao poliéster. Modelagem Justa e Segura: Ajuste ao corpo que evita que a peça escorregue durante a remada ou na queda. Ideal para performance dentro d’água. Punho Duplo com Abertura para o Dedo (Dedal): Garante que a manga fique firme, protegendo até o punho com segurança. Elástico Ajustável na Barra: Evita que a lycra suba ao furar ondas ou cair da prancha

**Camiseta Lycra Surf UV50 Manga Longa Preto com Rosa** (id 270617822, handle `camiseta-lycra-surf-uv50-manga-longa-preto-com-rosa`)
- Categorias: MASCULINO (`masculino`), LYCRA SURF (`lycra-surf`)
- Atributos de variante: Tamanho
- 3 variante(s):
  - P — R$ 249.99, estoque 10, 0.340 kg
  - M — R$ 249.99, estoque 9, 0.340 kg
  - G — R$ 249.99, estoque 2, 0.340 kg
- Descrição: Camiseta Lycra UV50 Manga Longa com Punho Dedal – Use Zero Hora Proteção, desempenho e estilo para quem vive o mar. A camiseta de lycra da Use Zero Hora foi desenvolvida para atender surfistas exigentes, unindo tecnologia têxtil, conforto e funcionalidade em uma peça de alta performance. Diferenciais do Produto: Proteção Solar de Alta Eficiência: Com FPS 98% e fator UV50 , garante proteção total contra os raios UVA e UVB durante longas sessões ao sol. Gramatura Premium de 240g: Uma lycra encorpada, resistente e durável, muito superior às opções mais finas do mercado. Proporciona maior conforto térmico, mais estrutura e melhor acabamento. Tecido Tecnológico: Composição de 90% poliamida e 10% elastano . A poliamida entrega maior resistência ao sal e cloro, secagem rápida, toque macio e durabilidade superior em relação ao elastano e ao poliéster. Modelagem Justa e Segura: Ajuste ao corpo que evita que a peça escorregue durante a remada ou na queda. Ideal para performance dentro d’água. Punho Duplo com Abertura para o Dedo (Dedal): Garante que a manga fique firme, protegendo até o punho com segurança. Elástico Ajustável na Barra: Evita que a lycra suba ao furar ondas ou cair da prancha

**Camiseta Lycra Surf UV50 Manga Longa Preto com Verde** (id 270617831, handle `camiseta-lycra-surf-uv50-manga-longa-preto-com-verde`)
- Categorias: MASCULINO (`masculino`), LYCRA SURF (`lycra-surf`)
- Atributos de variante: Tamanho
- 3 variante(s):
  - P — R$ 249.99, estoque 12, 0.340 kg
  - M — R$ 249.99, estoque 0, 0.340 kg
  - G — R$ 249.99, estoque 0, 0.340 kg
- Descrição: Camiseta Lycra UV50 Manga Longa com Punho Dedal – Use Zero Hora Proteção, desempenho e estilo para quem vive o mar. A camiseta de lycra da Use Zero Hora foi desenvolvida para atender surfistas exigentes, unindo tecnologia têxtil, conforto e funcionalidade em uma peça de alta performance. Diferenciais do Produto: Proteção Solar de Alta Eficiência: Com FPS 98% e fator UV50 , garante proteção total contra os raios UVA e UVB durante longas sessões ao sol. Gramatura Premium de 240g: Uma lycra encorpada, resistente e durável, muito superior às opções mais finas do mercado. Proporciona maior conforto térmico, mais estrutura e melhor acabamento. Tecido Tecnológico: Composição de 90% poliamida e 10% elastano . A poliamida entrega maior resistência ao sal e cloro, secagem rápida, toque macio e durabilidade superior em relação ao elastano e ao poliéster. Modelagem Justa e Segura: Ajuste ao corpo que evita que a peça escorregue durante a remada ou na queda. Ideal para performance dentro d’água. Punho Duplo com Abertura para o Dedo (Dedal): Garante que a manga fique firme, protegendo até o punho com segurança. Elástico Ajustável na Barra: Evita que a lycra suba ao furar ondas ou cair da prancha

### `térmica` — lacuna: existe versão feminina?

**Blusa Casaco Moletom Frio Canguru Capuz Surf Unissex** (id 273297752, handle `blusa-casaco-moletom-frio-canguru-capuz-surf-unissex`)
- Categorias: FEMININO (`feminino`), MOLETOM (`moletom`), MASCULINO (`masculino`), MOLETOM (`moletom1`), OUTLET (`outlet`), Masculino (`masculino1`)
- Atributos de variante: Tamanho, Cor
- 3 variante(s):
  - P / Marrom — R$ 249.00, estoque 3, 0.500 kg
  - M / Marrom — R$ 249.00, estoque 5, 0.500 kg
  - G / Marrom — R$ 249.00, estoque 3, 0.500 kg
- Descrição: Descrição do Produto O Moletom Masculino Canguru Use Zero Hora é a escolha ideal para quem busca conforto, estilo e praticidade nos dias frios. Com capuz em tecido duplo sem ajuste , ele proporciona proteção térmica e visual moderno. Seu bolso estilo canguru frontal garante funcionalidade, enquanto as três opções de cores com estampas exclusivas reforçam a identidade e autenticidade da peça. O interior flanelado e a composição de algodão com poliéster garantem um toque macio e excelente durabilidade. Principais Características Moletom com interior flanelado para maior conforto térmico Capuz em tecido duplo, sem ajuste Bolso frontal estilo canguru Estampa exclusiva em cada cor Modelagem masculina com ótimo caimento Tecido resistente e macio ao toque Cores disponíveis: Preto, Marrom e Off White Tamanhos disponíveis: P, M, G Ideal para uso urbano, casual e dias frios Ficha Técnica Marca: Use Zero Hora Modelo: Moletom Masculino Canguru com Capuz Material: 50% Poliéster / 50% Algodão Capuz: Duplo, sem ajuste Bolso: Frontal tipo canguru Estampa: Exclusiva por cor Interior: Flanelado Tamanhos disponíveis: P, M, G Cores disponíveis: Preto, Marrom, Off White Indicação: Dia a dia, casual, ur

**Blusa Casaco Moletom Frio Canguru Capuz Surf Unissex** (id 273297759, handle `blusa-casaco-moletom-frio-canguru-capuz-surf-unissex1`)
- Categorias: FEMININO (`feminino`), MOLETOM (`moletom`), MASCULINO (`masculino`), MOLETOM (`moletom1`), OUTLET (`outlet`), Masculino (`masculino1`)
- Atributos de variante: Tamanho, Cor
- 3 variante(s):
  - P / Preto — R$ 249.00, estoque 0, 0.500 kg
  - M / Preto — R$ 249.00, estoque 0, 0.500 kg
  - G / Preto — R$ 249.00, estoque 0, 0.500 kg
- Descrição: Descrição do Produto O Moletom Masculino Canguru Use Zero Hora é a escolha ideal para quem busca conforto, estilo e praticidade nos dias frios. Com capuz em tecido duplo sem ajuste , ele proporciona proteção térmica e visual moderno. Seu bolso estilo canguru frontal garante funcionalidade, enquanto as três opções de cores com estampas exclusivas reforçam a identidade e autenticidade da peça. O interior flanelado e a composição de algodão com poliéster garantem um toque macio e excelente durabilidade. Principais Características Moletom com interior flanelado para maior conforto térmico Capuz em tecido duplo, sem ajuste Bolso frontal estilo canguru Estampa exclusiva em cada cor Modelagem masculina com ótimo caimento Tecido resistente e macio ao toque Cores disponíveis: Preto, Marrom e Off White Tamanhos disponíveis: P, M, G Ideal para uso urbano, casual e dias frios Ficha Técnica Marca: Use Zero Hora Modelo: Moletom Masculino Canguru com Capuz Material: 50% Poliéster / 50% Algodão Capuz: Duplo, sem ajuste Bolso: Frontal tipo canguru Estampa: Exclusiva por cor Interior: Flanelado Tamanhos disponíveis: P, M, G Cores disponíveis: Preto, Marrom, Off White Indicação: Dia a dia, casual, ur

**Blusa Casaco Moletom Frio Canguru Capuz Surf Unissex** (id 273297762, handle `blusa-casaco-moletom-frio-canguru-capuz-surf-unissex2`)
- Categorias: FEMININO (`feminino`), MOLETOM (`moletom`), MASCULINO (`masculino`), MOLETOM (`moletom1`), OUTLET (`outlet`), Masculino (`masculino1`)
- Atributos de variante: Tamanho, Cor
- 3 variante(s):
  - P / Bege — R$ 249.00, estoque 3, 0.500 kg
  - M / Bege — R$ 249.00, estoque 0, 0.500 kg
  - G / Bege — R$ 249.00, estoque 2, 0.500 kg
- Descrição: Descrição do Produto O Moletom Masculino Canguru Use Zero Hora é a escolha ideal para quem busca conforto, estilo e praticidade nos dias frios. Com capuz em tecido duplo sem ajuste , ele proporciona proteção térmica e visual moderno. Seu bolso estilo canguru frontal garante funcionalidade, enquanto as três opções de cores com estampas exclusivas reforçam a identidade e autenticidade da peça. O interior flanelado e a composição de algodão com poliéster garantem um toque macio e excelente durabilidade. Principais Características Moletom com interior flanelado para maior conforto térmico Capuz em tecido duplo, sem ajuste Bolso frontal estilo canguru Estampa exclusiva em cada cor Modelagem masculina com ótimo caimento Tecido resistente e macio ao toque Cores disponíveis: Preto, Marrom e Off White Tamanhos disponíveis: P, M, G Ideal para uso urbano, casual e dias frios Ficha Técnica Marca: Use Zero Hora Modelo: Moletom Masculino Canguru com Capuz Material: 50% Poliéster / 50% Algodão Capuz: Duplo, sem ajuste Bolso: Frontal tipo canguru Estampa: Exclusiva por cor Interior: Flanelado Tamanhos disponíveis: P, M, G Cores disponíveis: Preto, Marrom, Off White Indicação: Dia a dia, casual, ur

**Camiseta Térmica Manga Longa Infantil Proteção Uv50 6 ao 14** (id 285644347, handle `camiseta-termica-manga-longa-infantil-protecao-uv50-6-ao-14`)
- Categorias: INFANTIL (`infantil1`), CAMISETA UV50+ (`camiseta-uv2`)
- Atributos de variante: Cor, Tamanho
- 15 variante(s):
  - Azul Turquesa / 6 — R$ 149.00, estoque 0, 0.120 kg
  - Azul Turquesa / 8 — R$ 149.00, estoque 0, 0.120 kg
  - Azul Turquesa / 10 — R$ 149.00, estoque 0, 0.120 kg
  - Azul Turquesa / 12 — R$ 149.00, estoque 0, 0.120 kg
  - Azul Turquesa / 14 — R$ 149.00, estoque 0, 0.120 kg
  - Azul Claro / 6 — R$ 149.00, estoque 10, 0.120 kg
  - Azul Claro / 8 — R$ 149.00, estoque 13, 0.120 kg
  - Azul Claro / 10 — R$ 149.00, estoque 6, 0.120 kg
  - Azul Claro / 12 — R$ 149.00, estoque 3, 0.120 kg
  - Azul Claro / 14 — R$ 149.00, estoque 0, 0.120 kg
  - Rosa / 6 — R$ 149.00, estoque 4, 0.120 kg
  - Rosa / 8 — R$ 149.00, estoque 2, 0.120 kg
  - Rosa / 10 — R$ 149.00, estoque 2, 0.120 kg
  - Rosa / 12 — R$ 149.00, estoque 2, 0.120 kg
  - Rosa / 14 — R$ 149.00, estoque 0, 0.120 kg
- Descrição: Camiseta Infantil Lycra UV50+ Proteção Solar Use Zero Hora Para Praia, Piscina e Esportes ao Ar Livre - Tecido Leve - Logo Metalizado - Cores Lisas Descrição A camiseta infantil da Use Zero Hora é a escolha ideal para quem busca proteção solar, conforto e estilo em atividades ao ar livre. Fabricada em lycra leve e com proteção UV50+ , ela bloqueia até 98% dos raios UVA e UVB, protegendo sua pele com máxima eficiência. Com design moderno e discreto, conta com logo metalizado exclusivo no peito e está disponível em três cores lisas que combinam com qualquer ocasião ao ar livre. Principais Características Tecido em lycra leve de alta qualidade Proteção UV50+ , ideal para exposição solar prolongada Secagem rápida e excelente respirabilidade Logo metálico estampado no peito com acabamento premium Design esportivo com caimento confortável Cores disponíveis : Azul Claro, Azul Turquesa, Rosa Tamanhos : P, M, G Modelagem infantil Indicações de Uso Praia e banho de sol Pesca esportiva e lazer Motociclismo Corrida, trekking, ciclismo e outros esportes outdoor Atividades prolongadas sob o sol Garantia e Envio Produto novo e original Pronta entrega com envio rápido Embalagem segura Suporte ao c

**CAMISETA NEOPRENE CABO FRIO** (id 358900038, handle `camiseta-neoprene-cabo-frio-17xyv`)
- Categorias: MASCULINO (`masculino`), LYCRA SURF (`lycra-surf`), NEOPRENE (`neoprene`)
- Atributos de variante: Cor, Tamanho
- 4 variante(s):
  - Preto / P — R$ 499.99, estoque 3, 0.330 kg
  - Preto / M — R$ 499.99, estoque 9, 0.330 kg
  - Preto / G — R$ 499.99, estoque 8, 0.330 kg
  - Preto / GG — R$ 499.99, estoque 6, 0.330 kg
- Descrição: # Camiseta Técnica Masculina Neoprene Hybrid UV50+ – Use Zero Hora Desenvolvida para quem busca máxima performance dentro e fora da água, a Camiseta Técnica Masculina Neoprene Hybrid da **Use Zero Hora** combina tecnologia, mobilidade e conforto em uma construção híbrida exclusiva. O corpo da peça é confeccionado em **Neoprene Span/Flex 1,5 mm**, proporcionando isolamento térmico, excelente elasticidade e ajuste anatômico ao corpo. Já as mangas, gola e recortes laterais são produzidos em **poliamida premium com elastano e proteção UV50+**, oferecendo maior liberdade de movimentos durante a remada, surf, wing foil, kitesurf, mergulho, stand up paddle e demais esportes aquáticos. Sua construção ergonômica utiliza **costura técnica Flatlock**, que reduz o atrito com a pele, aumenta a resistência da peça e garante um acabamento premium. O resultado é uma camiseta extremamente confortável, leve, flexível e resistente, desenvolvida para acompanhar seus movimentos sem limitar sua performance. --- ## Diferenciais * Corpo em **Neoprene Span/Flex 1,5 mm** de alta elasticidade * Mangas, gola e recortes em **poliamida premium com elastano** * Proteção solar permanente **UV50+** * Excelente con

### `rash` — lacuna: quais peças a loja chama de rash guard

Nenhum produto encontrado com esse termo.


## 4. O que esta coleta não fecha

Gramatura em g/m², número de lavagens testadas, norma técnica do UV50+ e
tempo de secagem em minutos não são dado de catálogo. Seguem como
"dado indisponível" nos textos até o fornecedor responder.
