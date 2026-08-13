# Parking lot

Frentes decididas mas adiadas, com a data e o motivo. Nada aqui entra em
produção até o item que a destrava fechar.

---

## Frente ampla: territórios além do produto

- **Estacionada em**: 2026-08-11, a pedido do usuário
- **Destrava quando**: o lote T1 de agosto fechar
- **Pré-requisito duro**: refresh de E1 com coleta nova no Semrush. As
  unidades da API estão esgotadas e **nenhuma dessas frentes é dimensionável
  hoje**.

O usuário propôs em 2026-08-11 abrir o blog para territórios de altíssimo
volume fora do produto: surf, esportes adjacentes (yoga, musculação, natação)
e uma editoria de eventos esportivos pelas principais cidades.

### O que a matriz atual já diz

`data/2026-08-10-matriz-kws-classificada.csv`, 860 KWs, Semrush BR, coleta de
2026-08-09.

| Termo procurado | Termos na matriz |
|---|---:|
| yoga / ioga | 0 |
| musculação | 0 |
| corrida | 0 |
| crossfit | 0 |
| pilates | 0 |
| treino | 0 |
| evento / campeonato | 0 |
| academia | 2 (`maio para academia`, 20) |
| fitness | 2 (`biquini fitness`, 40) |

**Zero não é evidência de ausência de demanda.** A matriz nasceu de sementes
de produto, então o silêncio dela sobre yoga e musculação significa **não
coletado**, não inexistente. Só uma coleta nova resolve.

### O que já está medido e sustenta decisão

| Frente | Dado medido | Leitura |
|---|---|---|
| **Natação** | 92 KWs, **31.680 buscas/mês**, 55 PAA e 7 AIO — o maior índice de pergunta da base inteira | Maior alavanca. Hoje é atributo por decisão de 2026-08-10; vale promover a território próprio. |
| **Surf lifestyle** | `melhores praias para surfar no brasil`: 90, KD 11, **PAA + AIO**. `como começar a surfar`: 20. | Autoridade natural da marca. Volume real não coletado. |
| **Corrida, ciclismo, beach tennis, pesca** | Zero na matriz, mas **a ficha técnica lista os quatro** como indicação de uso dos SKUs | Entram como uso dentro de lycra, não como território próprio. |
| **Yoga e musculação** | Zero na matriz **e zero na ficha técnica** | Fora até existir produto. |

### O filtro proposto

A ficha técnica já declara quais esportes o produto alcança: surf, bodyboard,
stand up paddle, kitesurf, windsurf, jet ski, natação, pesca esportiva, beach
tennis, corrida, trekking, ciclismo, motociclismo e mergulho recreativo.
**Yoga e musculação não estão na lista. Corrida e ciclismo estão.**

Isso importa por causa da regra já registrada em `producao/00-workflow.md`
para `vestido de praia curto`: cluster sem produto tem fator de catálogo zero,
e prometer o que não se entrega gera visita que não compra. Conteúdo de yoga
para vender beachwear tem a mesma forma, e o critério de sucesso do projeto é
venda, não visita.

### Ordem recomendada quando destravar

1. **Natação**, promovida de atributo a território. É a maior e a mais segura.
2. **Surf lifestyle**: praias, como começar, eventos por cidade.
3. **Corrida, ciclismo, beach tennis e pesca**, como uso dentro de lycra.
4. **Yoga e musculação**, só se o catálogo abrir para esses públicos.

### Ressalva sobre a editoria de eventos

É a ideia com maior potencial de volume e de link, e a mais distante da venda.
Tem custo de manutenção que as outras não têm: calendário de evento
desatualizado vira página morta e passa a pesar contra o domínio. Se entrar,
entra com dono e com data de revisão definidos.
