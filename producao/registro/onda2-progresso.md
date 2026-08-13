# Onda 2 — progresso da produção autônoma (6h)

- **Início**: 2026-08-13. Mandato: 50 artigos criativos (volume-first) + auditoria
  anti-IA exaustiva (várias passadas até zero sinal). Trabalho autônomo.
- **Grade**: `producao/registro/grade-onda-2.csv` (50 pautas, +74 KWs travadas).
- **Briefing dos escritores**: `producao/registro/brief-onda-2.md`.
- **Fontes**: catálogo `data/2026-08-12-nuvemshop-catalogo.json`, categorias
  `data/2026-08-12-categorias-urls.json`, matriz + universo MEDIDO.

## Pipeline por artigo
1. Escritor (subagente) redige `content/<slug>.html` do briefing.
2. Eu aterro: confiro dado real, links destacados `<strong><u>`, sem preço, sem
   `{HASH}` no corpo, sem link de post-irmão, sem travessão.
3. Anti-IA: detecção mecânica + revisor adversarial + correção.
4. `scripts/gerar-editor.py <slug>`; validação (title≤60, meta≤155, 3 JSON-LD).
5. Commit da onda; atualizo este arquivo.

## Blocos das 6h
- Bloco 1 (~3h): produção, 5 ondas de 10.
- Bloco 2 (~2h): auditoria anti-IA adversarial em rodadas até zero sinal.
- Bloco 3 (~1h): sweep final, guia de copiar-colar regenerado, relatório.

## Status das ondas
- **Onda 2A (10)** — DISPARADA (escritores em background): como-amarrar-canga,
  hot-yoga, sapatilha-aquatica, tapete-de-yoga, protetor-solar-com-cor,
  biquini-fio-dental, roupa-de-mergulho, saida-de-praia-croche,
  maio-natacao-feminino, hidroterapia.
- **Onda 2B (10)** — ESCRITA + validada + editor gerado: protetor-solar-pele-oleosa,
  protetor-solar-spray, biquini-asa-delta, roupa-de-praia-feminina,
  short-de-praia-feminino, polo-aquatico, nado-peito, roupa-de-praia-masculina,
  moda-praia-feminina, loja-de-surf. Validador `scripts/validar-anti-ia.py`: 0 erro.
- **Onda 2C (10)** — DISPARADA (escritores em background, com auto-validação):
  roupa-de-natacao, maio-manga-longa, moda-praia-masculina, melhor-protetor-solar-facial,
  protetor-solar-bastao, sapatilha-beach-tennis, sapatilha-de-neoprene, sunkini,
  roupa-de-surf, bermuda-de-praia-masculina. ESCRITA + validada (0 erro, 0 tic;
  auto-validação dos escritores) + editor gerado.
- **Onda 2D (10)** — DISPARADA (escritores em background, auto-validação): look-de-praia,
  academia-de-natacao, sunga-slip-ou-preta, bermuda-natacao, prancha-de-wakeboard,
  o-que-levar-para-a-praia, pilates-para-iniciantes, yoga-para-ansiedade,
  pilates-dor-nas-costas, como-usar-saida-de-praia. Cluster bem-estar com guarda
  anticanibalização contra pilares yoga.html/pilates.html/mindfulness.html.
- Onda 2E (10) — pendente (menor volume: yoga-em-casa, surf-para-iniciantes,
  como-se-proteger-do-sol, stand-up-paddle-iniciante, quanto-tempo-dura-protetor-solar,
  yoga-ou-pilates, quantas-vezes-pilates, como-escolher-biquini, maio-ou-biquini,
  kitesurf-como-comecar).

## Regras fixas (não esquecer)
- SEM PREÇO. Links de produto/categoria em `<strong><u>`. Marca: "Use Zero Hora,
  marca brasileira de surf e beachwear". Catálogo raso (canga 0, sapatilha 1,
  crochê = tule) declarado como CAP/ponte, nunca vitrine prometida.
- Anti-IA: sem "Este guia mostra", sem "não é X e sim Y", sem tricolon abstrato,
  sem travessão, sem verbo-muleta, aberturas variadas, voz ativa.
