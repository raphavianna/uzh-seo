# Backlog criativo — priorizado por volume (KD não veta)

- **Data**: 2026-08-13
- **Lente**: volume manda, KD desempata (não veta). Formatos variados — Q&A,
  comparativo, listicle, como-fazer, guia, sazonal — para exaurir o espaço de
  busca de maior volume, inclusive a cauda de PAA dos pilares já publicados.
- **Fontes de volume**: `data/2026-08-10-matriz-kws-classificada.csv` (Semrush BR,
  2026-08-09) e `data/2026-08-12-universo-esporte-MEDIDO.csv` (Semrush BR,
  2026-08-12). Base livre: 63 termos medidos ≥1.000 = 216.400 buscas/mês, mais
  spokes de PAA (volume não isolado, declarado).
- **Anticanibalização**: nenhuma pauta repete KW primária já em
  `producao/registro/kw-donos.csv` (147 travadas na Onda 1/T1). Spokes de pilar
  atacam long-tail distinto, não o termo-cabeça do pilar.
- **Regra de dado**: spoke sem volume isolado medido entra marcado
  **[vol PAA/n-d]** — capta a cauda do pilar, sem número inventado.
- **Catálogo raso declarado**: sapatilha (1 produto), canga (0), biquíni
  infantil/juvenil (sem categoria), crochê (não é o material — tule). Onde o
  catálogo é raso, a pauta é CAP (autoridade/ponte), nunca vitrine prometida.

Formatos: **Q&A** (pergunta única aprofundada) · **CMP** (comparativo X ou Y) ·
**LST** (listicle/tipos/N formas) · **HOW** (passo a passo) · **GUI** (guia de
escolha/compra) · **SAZ** (sazonal/tendência).

---

## HUB A — Sol e pele (autoridade → camiseta UV / lycra)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| A1 | CMP | protetor solar facial com cor | 8.100 | 28 | camiseta UV | com cor x sem cor: quando cada um, e por que a roupa cobre o corpo |
| A2 | Q&A | protetor solar em spray | 4.400 | 25 | camiseta UV | spray protege mesmo? erro de aplicação que anula o FPS |
| A3 | GUI | protetor solar para pele oleosa | 6.000 | 24-28 | camiseta UV | toque seco, gel, oil free — o que muda; +facial pele oleosa |
| A4 | LST | melhor protetor solar facial | 1.600 | 19 | camiseta UV | como escolher + tipos (bastão, spray, com cor) |
| A5 | Q&A | protetor solar facial bastão | 1.600 | 21 | camiseta UV | o que é, quando o bastão ganha (olhos, praia) |

## HUB B — Bem-estar / yoga e pilates (→ ioga-fitness)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| B1 | Q&A | hot yoga | 14.800 | 40 | ioga-fitness | o que é, benefícios, riscos, o que vestir no calor |
| B2 | GUI | tapete de yoga | 12.100 | 22 | ioga-fitness | espessura/material/aderência + a roupa que completa |
| B3 | CMP | yoga ou pilates | PAA/n-d | — | ioga-fitness | qual escolher por objetivo (postura, força, calma) |
| B4 | HOW | pilates para iniciantes | PAA/n-d | — | ioga-fitness | 1º mês: o que fazer, o que vestir, erros comuns |
| B5 | FRQ | quantas vezes por semana fazer pilates | PAA/n-d | — | ioga-fitness | frequência x resultado, com quanto tempo aparece |

## HUB C — Natação e água (→ maiô / camiseta UV)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| C1 | GUI | maiô para natação feminino | 5.400 | 24 | /feminino/maio/ | o maiô que não arrasta; body x regata na piscina |
| C2 | Q&A | hidroterapia | 5.400 | 29 | maiô | o que é, para quem, o que vestir na água aquecida |
| C3 | Q&A | polo aquático | 2.400 | 35 | maiô | o que é, regras, o traje que aguenta o jogo |
| C4 | HOW | nado peito | 2.400 | 32 | maiô | técnica passo a passo do nado mais fácil |
| C5 | GUI | roupa de natação | 1.900 | 16 | maiô | maiô, touca, óculos: o que é essencial; foco no maiô |
| C6 | Q&A | academia de natação | 1.000 | 45 | maiô | como escolher, o que levar na mochila |

## HUB D — Calçado aquático / sapatilha (CAP: ~28k busca, 1 produto)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| D1 | GUI | sapatilha aquática | 12.100 | 20 | sapatilha neoprene (produto) | para que serve, quando usar, como achar o tamanho |
| D2 | Q&A | sapatilha para beach tennis | 3.200 | 14-15 | sapatilha | precisa de sapatilha no beach tennis? o que muda |
| D3 | Q&A | sapatilha de neoprene | 4.200 | 17-29 | sapatilha | por que neoprene no pé; costão, pedra, frio |

## HUB E — Canga e mergulho (alto volume, ponte)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| E1 | LST | canga de praia (como usar) | 14.800 | 19 | saída de praia / poncho | N formas de amarrar a canga (vestido, saia, top) |
| E2 | GUI | roupa de mergulho | 6.600 | 24 | neoprene / lycra | wetsuit, lycra, o que a UZH cobre; sem prometer cilindro |

## HUB F — Biquíni sub-estilos (→ /feminino/biquini/)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| F1 | GUI | biquíni fio dental | 6.600 | 14 | /feminino/biquini/ | o que é, para quem, marquinha; regulagem |
| F2 | GUI | biquíni asa delta | 2.900 | 14 | /feminino/biquini/asa-delta/ | o corte que valoriza o colo; top fixo |
| F3 | Q&A | sunkini | 1.600 | 13 | /feminino/biquini/sunkini/ | o que é sunkini; meio-termo entre biquíni e maiô |

## HUB G — Maiô e saída sub (→ maiô / saída)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| G1 | GUI | maiô manga longa | 1.900 | 12 | /feminino/maio/manga-longa/ | quando manga longa ganha; dedal, punho, UV |
| G2 | CMP | maiô ou biquíni | PAA/n-d | — | maiô / biquíni | qual escolher por atividade e conforto |
| G3 | HOW | como usar saída de praia | PAA/n-d | — | saída de praia | 5 looks com a mesma saída, da areia ao almoço |

## HUB H — Moda praia e surfwear (categoria + marca)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| H1 | GUI | roupa de praia feminina | 2.900 | 36 | /feminino/ | montar o guarda-roupa de praia por ocasião |
| H2 | GUI | roupa de praia masculina | 2.400 | 21 | /masculino/ | sunga, bermuda, lycra: o kit do homem na praia |
| H3 | SAZ | moda praia feminina 2026 | 2.400+880 | 49 | /feminino/ | tendência da estação ancorada no que a loja tem |
| H4 | GUI | roupa de surf | 1.600 | 21 | /masculino/lycra-surf/ | o que o surfista veste da água ao pós-surf |
| H5 | Q&A | loja de surf (surfwear brasileiro) | 2.400 | 50 | home | o que é surfwear de fabricação própria; marca |

## HUB I — Sunga/bermuda extras (→ sunga / bermuda)

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| I1 | GUI | short de praia feminino | 2.900 | 9 | /feminino/ | short de praia da mulher: modelos e caimento |
| I2 | Q&A | sunga slip x sunga preta | 2.000 | 14 | /masculino/sunga/ | o que é slip; por que o preto é o coringa |
| I3 | GUI | bermuda de praia masculina | 1.600 | 25 | /masculino/bermuda/ | comprimento e forro; distinta do hub de short |

## HUB J — Esporte novo com volume + sazonal

| # | Fmt | KW primária | Vol | KD | Destino/ponte | Ângulo |
|---|---|---|---:|---:|---|---|
| J1 | Q&A | prancha de wakeboard | 1.000 | 5 | lycra / neoprene | o que olhar numa prancha; a roupa que protege |
| J2 | SAZ | look de praia | 1.300 | 32 | beachwear | montar o look completo com peças da loja |

---

## Total do backlog

**33 pautas** priorizadas por volume, cobrindo ~180 mil buscas/mês medidas +
cauda de PAA. Formatos: 12 GUI, 8 Q&A, 3 CMP, 3 LST/HOW/FRQ, 2 SAZ, restante
misto. Nenhuma colide com as 147 KWs já travadas.

Ordem de ataque sugerida: hubs por volume — Canga+mergulho (E), Sol e pele (A),
Bem-estar (B), Natação (C), Sapatilha (D), depois Biquíni/Maiô/Moda praia.
