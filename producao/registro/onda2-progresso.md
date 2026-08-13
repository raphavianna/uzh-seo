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
  ESCRITA + validada (0 erro, 0 tic) + editor gerado. Nota: catálogo saída de praia
  = tule (sem crochê/kimono real); "como usar" adaptou para 5 peças reais.
- **Onda 2E (10)** — DISPARADA (escritores em background, auto-validação; última onda):
  yoga-em-casa, surf-para-iniciantes, como-se-proteger-do-sol, stand-up-paddle-iniciante,
  quanto-tempo-dura-protetor-solar, yoga-ou-pilates, quantas-vezes-pilates,
  como-escolher-biquini, maio-ou-biquini, kitesurf-como-comecar. Guardas anti-canibalização
  densas (clusters protetor/bem-estar/biquíni/esporte já populados).
  ESCRITA + validada (0 erro, 0 tic) + editor gerado.

## 50/50 ESCRITOS — Bloco 1 concluído
Todos os 50 artigos da Onda 2 escritos, mecanicamente validados (validar-anti-ia.py: 0 erro),
editores derivados, kw-donos com 74 KWs onda2 = "escrito", 5 commits (2A–2E) pushed.

## BLOCO 2 — auditoria adversarial anti-IA (rodada 1) CONCLUÍDA
7 editores adversariais (editor humano cético) leram os 50 artigos e corrigiram in loco o que
a varredura mecânica NÃO pega. 40 dos 50 tiveram correção; 10 já eram genuinamente naturais.
Achados sistêmicos (invisíveis por artigo, gritantes lado a lado):
- Placa de abertura "Abaixo você vê/tem o passo a passo..." (super-sinalização) — vários.
- Fórmula "não existe vencedor absoluto, existe..." / "não é X, é Y" nos comparativos.
- Molde definicional repetido "X é a peça que..." em seções seguidas.
- Ritmo metronômico (3 frases da mesma forma), aberturas em série "A"/"O".
- Throat-clear "vale a franqueza/honestidade", vazamento de brief no corpo ("a franqueza que o brief pede").
- 1 violação SEM PREÇO recuperada (loja-de-surf "o preço sem a margem do revendedor").
- 1 erro de concordância ("é o que fazem quem surfa" → "faz").
Editores regenerados p/ os 40. Validador: 50/50 = 0 erro.

### Pendência FORA de escopo (Onda 1/T1, sessão anterior) — reportar, não reescrever aqui:
- Links de post-irmão com {HASH} no corpo (cluster rash-guard/lycra/UV: blusa-com-protecao-uv,
  camisa-de-praia-feminina, camiseta-com-protecao-uv, o-que-e-rash-guard, rash-guard-infantil).
- feminino-lycra-surf e masculino-lycra-surf sem JSON-LD BlogPosting (usam schema de categoria).
- Avisos "de verdade" em sunga-masculina, vestido-de-praia.

## Próximo: BLOCO 2 — auditoria adversarial anti-IA
Depois dos 50 escritos, rodar revisores adversariais (subagentes) em rodadas sobre os
50 artigos, lendo holisticamente (ritmo, frase genérica, "cheiro" de IA que o validador
mecânico não pega), até zero sinal. Depois BLOCO 3: sweep final + guia copiar-colar
regenerado p/ Onda 2 + relatório de fechamento.

## Regras fixas (não esquecer)
- SEM PREÇO. Links de produto/categoria em `<strong><u>`. Marca: "Use Zero Hora,
  marca brasileira de surf e beachwear". Catálogo raso (canga 0, sapatilha 1,
  crochê = tule) declarado como CAP/ponte, nunca vitrine prometida.
- Anti-IA: sem "Este guia mostra", sem "não é X e sim Y", sem tricolon abstrato,
  sem travessão, sem verbo-muleta, aberturas variadas, voz ativa.
