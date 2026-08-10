#!/usr/bin/env python3
"""
Extrai o catálogo completo da Nuvemshop pela API v1 e grava dois CSVs
prontos para entrar no pipeline de SEO deste repositório.

Rode na sua máquina (esta sessão não tem saída de rede para a API da Nuvemshop).

    pip install requests
    export NUVEMSHOP_STORE_ID=123456
    export NUVEMSHOP_TOKEN=seu_access_token
    export NUVEMSHOP_CONTATO="raphael.ferreira@nsx.bet"
    python3 nuvemshop-catalogo.py

Saída:
    nuvemshop-produtos-AAAA-MM-DD.csv   uma linha por produto
    nuvemshop-variantes-AAAA-MM-DD.csv  uma linha por variante

Onde pegar as credenciais: painel da Nuvemshop → Meus aplicativos, ou o
app já autorizado que gerou o token. O store_id é o número da loja.
"""

import csv, os, re, sys, time, datetime
try:
    import requests
except ImportError:
    sys.exit("Falta a biblioteca requests. Rode: pip install requests")

STORE = os.environ.get("NUVEMSHOP_STORE_ID")
TOKEN = os.environ.get("NUVEMSHOP_TOKEN")
CONTATO = os.environ.get("NUVEMSHOP_CONTATO", "seu-email@dominio.com")

if not STORE or not TOKEN:
    sys.exit("Defina NUVEMSHOP_STORE_ID e NUVEMSHOP_TOKEN nas variáveis de ambiente.")

BASE = f"https://api.nuvemshop.com.br/v1/{STORE}"
# A Nuvemshop usa o cabeçalho 'Authentication', não 'Authorization'.
# O User-Agent com contato é obrigatório: requisição sem ele é recusada.
HEADERS = {
    "Authentication": f"bearer {TOKEN}",
    "User-Agent": f"UseZeroHora SEO ({CONTATO})",
    "Content-Type": "application/json",
}

def i18n(v):
    """Campos multilíngues vêm como dict {'pt': '...'}. Extrai o pt."""
    if isinstance(v, dict):
        return v.get("pt") or v.get("pt-BR") or next(iter(v.values()), "") or ""
    return v or ""

def sem_html(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t or "")).strip()

def buscar(caminho, params=None):
    """Pagina até o fim, respeitando o limite de requisições da API."""
    itens, pagina = [], 1
    while True:
        p = dict(params or {}); p.update({"page": pagina, "per_page": 200})
        r = requests.get(f"{BASE}{caminho}", headers=HEADERS, params=p, timeout=60)
        if r.status_code == 429:                      # limite atingido
            espera = int(r.headers.get("Retry-After", 10))
            print(f"  limite da API atingido, aguardando {espera}s")
            time.sleep(espera); continue
        r.raise_for_status()
        lote = r.json()
        if not lote:
            break
        itens.extend(lote)
        print(f"  página {pagina}: {len(lote)} itens (total {len(itens)})")
        if len(lote) < 200:
            break
        pagina += 1
        time.sleep(0.6)                               # folga no rate limit
    return itens

print("Buscando categorias...")
categorias = {c["id"]: i18n(c.get("name")) for c in buscar("/categories")}
print(f"  {len(categorias)} categorias")

print("Buscando produtos...")
produtos = buscar("/products")
print(f"  {len(produtos)} produtos")

hoje = datetime.date.today().isoformat()
arq_p = f"nuvemshop-produtos-{hoje}.csv"
arq_v = f"nuvemshop-variantes-{hoje}.csv"

COLS_P = ["id", "sku_principal", "nome", "handle", "url", "categorias", "publicado",
          "marca", "preco_min", "preco_max", "estoque_total", "qtd_variantes",
          "peso_kg", "tags", "seo_title", "seo_description",
          "descricao_texto", "descricao_chars", "descricao_html_bruto",
          "atributos", "foto_principal", "qtd_fotos", "criado_em"]

COLS_V = ["produto_id", "produto_nome", "variante_id", "sku", "ean",
          "valores", "preco", "preco_promocional", "estoque",
          "peso_kg", "altura_cm", "largura_cm", "comprimento_cm"]

linhas_p, linhas_v = [], []

for p in produtos:
    nome = i18n(p.get("name"))
    handle = i18n(p.get("handle"))
    desc_html = i18n(p.get("description"))
    variantes = p.get("variants") or []
    precos = [float(v["price"]) for v in variantes if v.get("price")]
    estoques = [v.get("stock") or 0 for v in variantes if v.get("stock") is not None]
    cats = " | ".join(categorias.get(c.get("id"), "") for c in (p.get("categories") or []))
    imgs = p.get("images") or []
    atribs = " | ".join(i18n(a) for a in (p.get("attributes") or []))

    linhas_p.append({
        "id": p.get("id"),
        "sku_principal": (variantes[0].get("sku") if variantes else "") or "",
        "nome": nome,
        "handle": handle,
        "url": p.get("canonical_url") or f"https://usezerohora.com.br/produtos/{handle}/",
        "categorias": cats,
        "publicado": p.get("published"),
        "marca": p.get("brand") or "",
        "preco_min": min(precos) if precos else "",
        "preco_max": max(precos) if precos else "",
        "estoque_total": sum(estoques) if estoques else "",
        "qtd_variantes": len(variantes),
        "peso_kg": (variantes[0].get("weight") if variantes else "") or "",
        "tags": p.get("tags") or "",
        "seo_title": i18n(p.get("seo_title")),
        "seo_description": i18n(p.get("seo_description")),
        "descricao_texto": sem_html(desc_html),
        "descricao_chars": len(sem_html(desc_html)),
        "descricao_html_bruto": desc_html,
        "atributos": atribs,
        "foto_principal": (imgs[0].get("src") if imgs else "") or "",
        "qtd_fotos": len(imgs),
        "criado_em": p.get("created_at") or "",
    })

    for v in variantes:
        linhas_v.append({
            "produto_id": p.get("id"), "produto_nome": nome,
            "variante_id": v.get("id"), "sku": v.get("sku") or "",
            "ean": v.get("barcode") or "",
            "valores": " / ".join(i18n(x) for x in (v.get("values") or [])),
            "preco": v.get("price") or "", "preco_promocional": v.get("promotional_price") or "",
            "estoque": v.get("stock"), "peso_kg": v.get("weight") or "",
            "altura_cm": v.get("height") or "", "largura_cm": v.get("width") or "",
            "comprimento_cm": v.get("depth") or "",
        })

for arq, cols, linhas in ((arq_p, COLS_P, linhas_p), (arq_v, COLS_V, linhas_v)):
    with open(arq, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader(); w.writerows(linhas)
    print(f"gravado: {arq} ({len(linhas)} linhas)")

# Diagnóstico rápido, para você ver na hora se algo está errado
sem_seo = [l for l in linhas_p if not l["seo_title"]]
sem_desc = [l for l in linhas_p if l["descricao_chars"] < 100]
lixo = [l for l in linhas_p if "data-message-author-role" in (l["descricao_html_bruto"] or "")]
sem_sku = [l for l in linhas_v if not l["sku"]]

print(f"""
Diagnóstico
  produtos ................ {len(linhas_p)}
  variantes ............... {len(linhas_v)}
  sem seo_title ........... {len(sem_seo)}
  descrição < 100 chars ... {len(sem_desc)}
  com lixo do ChatGPT ..... {len(lixo)}
  variantes sem SKU ....... {len(sem_sku)}
""")
