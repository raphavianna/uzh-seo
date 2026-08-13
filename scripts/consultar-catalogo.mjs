#!/usr/bin/env node
/**
 * Consulta o catálogo da Nuvemshop e responde exatamente as perguntas abertas
 * do lote T1: as URLs que os artigos linkam e as lacunas de "dado indisponível"
 * que são atributo de produto.
 *
 * Não escreve nada na loja. Só GET.
 *
 * COMO USAR
 *   Precisa das credenciais no ambiente (ou no .env do repo integracao-nuvemshop):
 *     NUVEMSHOP_STORE_ID, NUVEMSHOP_ACCESS_TOKEN
 *
 *   node scripts/consultar-catalogo.mjs
 *
 * SAÍDA
 *   reports/AAAA-MM-DD-catalogo-nuvemshop.md   relatório legível
 *   data/AAAA-MM-DD-nuvemshop-catalogo.json    dump bruto, para conferência
 *
 * O QUE ELE RESPONDE
 *   1. Cada uma das 9 URLs que o lote linka existe? É categoria ou produto?
 *   2. A árvore inteira de categorias, com contagem de produtos.
 *   3. Os atributos dos SKUs citados nos artigos: composição, manga, fator de
 *      proteção, lavagem, grade de tamanhos e cores.
 *
 * O QUE ELE NÃO RESPONDE
 *   Gramatura, lavagens testadas, norma do UV50+ e tempo de secagem. Nada
 *   disso é dado de catálogo; vem do fornecedor ou de laboratório.
 */
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';

const REPO_INTEGRACAO = process.env.REPO_INTEGRACAO || '/workspace/integracao-nuvemshop';
const BASE = resolve(dirname(new URL(import.meta.url).pathname), '..');
const HOJE = new Date().toISOString().slice(0, 10);

// As URLs que os cinco artigos do lote linkam, contadas nos arquivos.
const URLS_DO_LOTE = [
  { caminho: '/rash-guard/', citacoes: 6, kws: 8, nota: 'reserva 24.310 buscas/mês no registro; zero linha no baseline' },
  { caminho: '/masculino/lycra-surf/', citacoes: 11, kws: 5, nota: 'ranqueia em 4 linhas do baseline' },
  { caminho: '/feminino/lycra-surf/', citacoes: 5, kws: 0, nota: 'usuário confirmou como produto em 2026-08-11' },
  { caminho: '/feminino/maio/', citacoes: 2, kws: 0, nota: '42% do orgânico do domínio' },
  { caminho: '/quem-somos/', citacoes: 2, kws: 0, nota: '' },
  { caminho: '/masculino/', citacoes: 1, kws: 0, nota: '' },
  { caminho: '/feminino/', citacoes: 1, kws: 0, nota: '' },
  { caminho: '/feminino/poncho1/', citacoes: 0, kws: 0, nota: 'sufixo numérico: possível duplicata' },
  { caminho: '/masculino/poncho/', citacoes: 0, kws: 0, nota: '54% da receita da loja' },
];

// Peças citadas nos artigos, com a lacuna que cada uma precisa fechar.
const SKUS_ALVO = [
  { busca: 'itamambuca', lacuna: 'grade de tamanhos, cores e composição' },
  { busca: 'neon', lacuna: 'composição do tecido e comprimento de manga' },
  { busca: 'engana mamãe', lacuna: 'percentuais da composição' },
  { busca: 'cepilho', lacuna: 'fator de proteção (a ficha diz "conforme composição" sem trazer a composição)' },
  { busca: 'lycra', lacuna: 'instruções de lavagem' },
  { busca: 'térmica', lacuna: 'existe versão feminina?' },
  { busca: 'rash', lacuna: 'quais peças a loja chama de rash guard' },
];

const txt = (v) => (v && typeof v === 'object' ? (v.pt || v.es || v.en || Object.values(v)[0] || '') : (v ?? ''));
const limpar = (h) => String(h || '').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();

async function main() {
  const { loadConfig, loadDotEnv } = await import(`${REPO_INTEGRACAO}/src/core/config.ts`);
  const { NuvemshopClient } = await import(`${REPO_INTEGRACAO}/src/core/client.ts`);
  const { Resources } = await import(`${REPO_INTEGRACAO}/src/resources/index.ts`);

  loadDotEnv(`${REPO_INTEGRACAO}/.env`);
  const cfg = loadConfig();
  if (!cfg.storeId || !cfg.accessToken) {
    console.error('Faltam NUVEMSHOP_STORE_ID e NUVEMSHOP_ACCESS_TOKEN.');
    console.error('Coloque no ambiente ou em ' + REPO_INTEGRACAO + '/.env');
    process.exit(1);
  }
  const api = new Resources(new NuvemshopClient(cfg));

  const loja = await api.store.get();
  console.log(`Loja: ${txt(loja.name)} (id ${loja.id})\n`);

  console.log('Baixando categorias...');
  const categorias = await api.categories.list({ per_page: 200 });
  console.log(`  ${categorias.length} categoria(s)\n`);

  console.log('Baixando produtos...');
  const produtos = await api.products.list({ per_page: 200 });
  console.log(`  ${produtos.length} produto(s)\n`);

  // ---- resolve as URLs do lote -------------------------------------------
  const porHandle = new Map();
  for (const c of categorias) porHandle.set(txt(c.handle).toLowerCase(), c);
  const prodPorHandle = new Map();
  for (const p of produtos) prodPorHandle.set(txt(p.handle).toLowerCase(), p);

  const contagem = new Map();
  for (const p of produtos)
    for (const c of p.categories || []) contagem.set(c.id, (contagem.get(c.id) || 0) + 1);

  const resolvidas = URLS_DO_LOTE.map((u) => {
    const partes = u.caminho.split('/').filter(Boolean);
    const ultimo = (partes[partes.length - 1] || '').toLowerCase();
    const cat = porHandle.get(ultimo);
    const prod = prodPorHandle.get(ultimo);
    return {
      ...u,
      tipo: cat ? 'categoria' : prod ? 'produto' : 'NÃO ENCONTRADO',
      id: cat?.id ?? prod?.id ?? null,
      nome: cat ? txt(cat.name) : prod ? txt(prod.name) : null,
      produtos: cat ? (contagem.get(cat.id) || 0) : null,
      pai: cat?.parent ?? null,
    };
  });

  // ---- os SKUs que os artigos citam --------------------------------------
  const achadosSku = SKUS_ALVO.map((alvo) => {
    const termo = alvo.busca.toLowerCase();
    const hits = produtos.filter(
      (p) => txt(p.name).toLowerCase().includes(termo) || limpar(txt(p.description)).toLowerCase().includes(termo),
    );
    return {
      ...alvo,
      encontrados: hits.map((p) => ({
        id: p.id,
        nome: txt(p.name),
        handle: txt(p.handle),
        publicado: p.published,
        atributos: (p.attributes || []).map(txt),
        variantes: (p.variants || []).map((v) => ({
          valores: (v.values || []).map(txt).join(' / '),
          sku: v.sku, preco: v.price, estoque: v.stock, peso: v.weight,
        })),
        categorias: (p.categories || []).map((c) => ({ id: c.id, nome: txt(c.name), handle: txt(c.handle) })),
        descricao: limpar(txt(p.description)),
      })),
    };
  });

  // ---- grava --------------------------------------------------------------
  const bruto = { coletado_em: HOJE, loja: { id: loja.id, nome: txt(loja.name) }, categorias, produtos };
  const jsonPath = resolve(BASE, `data/${HOJE}-nuvemshop-catalogo.json`);
  mkdirSync(dirname(jsonPath), { recursive: true });
  writeFileSync(jsonPath, JSON.stringify(bruto, null, 2), 'utf8');

  const L = [];
  L.push(`# Catálogo Nuvemshop — resposta às perguntas do lote T1\n`);
  L.push(`- **Coletado em**: ${HOJE}`);
  L.push(`- **Fonte**: API Nuvemshop \`${cfg.apiVersion}\`, loja ${loja.id} (${txt(loja.name)})`);
  L.push(`- **Natureza**: medido, leitura direta do catálogo`);
  L.push(`- **Dump bruto**: \`data/${HOJE}-nuvemshop-catalogo.json\``);
  L.push(`- **Escopo**: ${categorias.length} categorias, ${produtos.length} produtos\n`);

  L.push(`## 1. As URLs que o lote linka\n`);
  L.push(`| URL | Tipo | Nome | Produtos | Citações no lote | Nota |`);
  L.push(`|---|---|---|---:|---:|---|`);
  for (const r of resolvidas)
    L.push(`| \`${r.caminho}\` | ${r.tipo === 'NÃO ENCONTRADO' ? '**NÃO ENCONTRADO**' : r.tipo} | ${r.nome ?? '—'} | ${r.produtos ?? '—'} | ${r.citacoes} | ${r.nota} |`);

  const ausentes = resolvidas.filter((r) => r.tipo === 'NÃO ENCONTRADO' && r.citacoes > 0);
  if (ausentes.length) {
    L.push(`\n**${ausentes.length} URL(s) citada(s) no lote não existe(m) no catálogo.** Os links precisam de destino novo antes de publicar:`);
    for (const a of ausentes) L.push(`- \`${a.caminho}\` — ${a.citacoes} citações, ${a.kws} keywords reservadas`);
  }

  L.push(`\n## 2. Árvore de categorias\n`);
  L.push(`| id | Nome | Handle | Pai | Produtos |`);
  L.push(`|---:|---|---|---:|---:|`);
  for (const c of categorias.sort((a, b) => (a.parent ?? 0) - (b.parent ?? 0) || a.id - b.id))
    L.push(`| ${c.id} | ${txt(c.name)} | \`${txt(c.handle)}\` | ${c.parent ?? '—'} | ${contagem.get(c.id) || 0} |`);

  L.push(`\n## 3. Os SKUs citados nos artigos\n`);
  for (const a of achadosSku) {
    L.push(`### \`${a.busca}\` — lacuna: ${a.lacuna}\n`);
    if (!a.encontrados.length) { L.push(`Nenhum produto encontrado com esse termo.\n`); continue; }
    for (const p of a.encontrados.slice(0, 6)) {
      L.push(`**${p.nome}** (id ${p.id}, handle \`${p.handle}\`${p.publicado ? '' : ', **não publicado**'})`);
      if (p.categorias.length) L.push(`- Categorias: ${p.categorias.map((c) => `${c.nome} (\`${c.handle}\`)`).join(', ')}`);
      if (p.atributos.length) L.push(`- Atributos de variante: ${p.atributos.join(', ')}`);
      if (p.variantes.length) {
        L.push(`- ${p.variantes.length} variante(s):`);
        for (const v of p.variantes.slice(0, 24))
          L.push(`  - ${v.valores || '(única)'} — R$ ${v.preco ?? '—'}, estoque ${v.estoque ?? 'infinito'}, ${v.peso ?? '—'} kg`);
        if (p.variantes.length > 24) L.push(`  - ... e mais ${p.variantes.length - 24}`);
      }
      L.push(`- Descrição: ${p.descricao.slice(0, 1200) || '(vazia)'}`);
      L.push('');
    }
  }

  L.push(`\n## 4. O que esta coleta não fecha\n`);
  L.push(`Gramatura em g/m², número de lavagens testadas, norma técnica do UV50+ e`);
  L.push(`tempo de secagem em minutos não são dado de catálogo. Seguem como`);
  L.push(`"dado indisponível" nos textos até o fornecedor responder.\n`);

  const mdPath = resolve(BASE, `reports/${HOJE}-catalogo-nuvemshop.md`);
  mkdirSync(dirname(mdPath), { recursive: true });
  writeFileSync(mdPath, L.join('\n'), 'utf8');

  console.log(`\nEscrito:`);
  console.log(`  reports/${HOJE}-catalogo-nuvemshop.md`);
  console.log(`  data/${HOJE}-nuvemshop-catalogo.json`);
  if (ausentes.length) {
    console.log(`\nATENÇÃO: ${ausentes.length} URL(s) citada(s) no lote não existe(m):`);
    for (const a of ausentes) console.log(`  ${a.caminho}  (${a.citacoes} citações)`);
  }
}

main().catch((e) => { console.error('\nFalhou:', e?.message || e); process.exit(1); });
