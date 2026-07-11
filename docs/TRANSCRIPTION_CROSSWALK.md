# Crosswalk: ventanas oro del atlas S1 vs transcripción formal publicada

Fecha: 2026-07-11. Cierra la limitación declarada en
`../WRITEUP_S1_INDEX.md` ("checking each flagged
region against the team's actual reading progress ... is outside the scope of
this index"): ahora está dentro del scope, con una frontera proxy PROVISIONAL.

> **Corrección (2026-07-11, peer review, mismo día):** la primera versión de
> este documento (commit 0e80e7d) tenía tres errores, corregidos acá:
> (1) la unión de series estaba mal deduplicada — el segmento June w104-106
> no tiene mapa de tinta publicado y el panel July que cubre ese rango (131
> oro) quedaba excluido como redundante;
> los números canónicos son 5,678/4,424 = 77.9%, no 5,547/4,293 = 77.4%, y
> el bucket "clásicos" contenía re-renders duplicados (ver
> `CLASSIC_EQUIVALENCE.md`); (2) la frontera w037 se presentaba como "la
> región formalmente transcripta" sin anclaje visual del bloque GP — es un
> proxy provisional; (3) el "desenrollado completo de Paris 4,
> ~130 wraps / ~140 columnas" estaba atribuido a fuentes oficiales que no lo
> dicen de Paris 4 — la evidencia de cobertura completa es la observación
> directa del bucket, no esa cita de prensa.

## 1. Estado de transcripción formal de PHerc Paris 4 (Scroll 1) a 2026-07-11

Regla de TRANSCRIPTION_STATUS.md: "formal" = paper / anuncio oficial con
lectura papirológica; lo comunitario/informal no cuenta.

- **Grand Prize 2023 (anunciado 2024-02-05):** 11 columnas, ~2000
  caracteres, ~5% del rollo; edición formal en ZPE ("The Final Columns of
  PHerc. Paris. 4 Revealed Through Virtual Unwrapping" — 16 porciones de
  columnas finales). El texto es el FINAL de la obra → físicamente en los
  wraps más internos.
  Fuentes: https://scrollprize.org/grandprize ,
  https://en.wikipedia.org/wiki/PHerc._Paris._4 ,
  https://www.academia.edu/125007883/
- **Junio 2026 (anuncio firstscroll, 2026-06-25):** el rollo leído completo
  de punta a punta es **PHerc 1667**, no Paris 4. Para Paris 4 el anuncio
  afirma: tinta directamente visible en el CT de alta resolución, verificada
  1:1 contra la lectura del GP. No afirma desenrollado completo ni cuenta de
  columnas nuevas de Paris 4. (Una nota de prensa menciona "~130 wraps /
  ~140 columnas" de "un rollo" sin identificarlo; no se usa como fuente.)
- **Observación directa (nuestra, verificable):** el bucket oficial
  (`vesuvius-challenge-open-data`, `PHercParis4/segments/`) contiene mapas
  de tinta oficiales para paneles rotulados **w010–w129** (series jun-23 y
  jul-01), es decir, cobertura de mapa de tinta a lo largo de ~120 wraps del
  rollo. Eso es lo que este atlas indexa. La transcripción formal publicada
  sigue siendo únicamente el bloque GP/columnas finales.

Consecuencia: todo lo que el índice marca fuera del bloque GP es territorio
con mapa de tinta oficial publicado y formalmente NO transcripto (aún), con
el equipo oficial escalando su pipeline de lectura (1667 completo ya leído).

## 2. Orientación del eje wrap (verificación física, local)

Circunferencia ∝ radio: si w crece hacia afuera, el ancho por wrap de los
paneles debe crecer con w. Medido sobre los 16 paneles de la serie jun-23
(ancho_px / n_wraps, a 19.2 µm/px):

w010-027: 1182 px/wrap → w028-037: 2210 → w038-045: 2896 → w046-052: 3443 →
w053-058: 3888 → w059-063: 4326 → w064-068: 4786 → w069-072: 5182 →
w073-076: 5478 → w077-080: 5785 → w081-084: 6132 → w085-088: 6462 →
w089-091: 6853 → w092-094: 7093 → w095-097: 7310 → w098-100: 7483

Monótono creciente sin excepción ⇒ **w010 = wrap más interno**. Radio
implícito: w010 ≈ 3.6 mm, w100 ≈ 23 mm — consistente con un rollo real.
El final de la obra (= bloque GP transcripto) está en los wraps internos.

## 3. Frontera proxy PROVISIONAL y clasificación

**Frontera: w037 — un proxy provisional, no la extensión medida del bloque
GP.** Lo demostrado: el bloque transcripto está en los wraps internos (§2)
y consta de 11 columnas (~16 porciones de columnas finales en la edición).
Cota física de la elección: el papiro acumulado de w010 a w037 mide
(21,270 + 22,100) px × 19.2 µm ≈ **83 cm**; 11 columnas herculanenses a
~6-8 cm por columna con intercolumnio ≈ **65-90 cm**. Es decir, w037 es la
frontera de panel más chica que plausiblemente contiene el bloque — pero el
margen es fino y NO está demostrado que sea generosa ("conservadora"): si
el bloque real terminara antes, los candidatos suben; si llegara a rozar
w037+, bajan algo. Por eso el nombre correcto es proxy provisional.
Pendiente concreto: match visual banner GP↔panel para reemplazar el proxy
por la frontera medida.

Sobre `full_index_complete.json` (repo de dataset en HF) (score proxy_v4 ≥ 0.9), **unión
deduplicada de la serie wrap** (June w010–w129 + el único panel July cuyo
rango carece de mapa June publicado, w104-106; `_jordi` y el resto de July quedan como
confirmatorios; ver `CLASSIC_EQUIVALENCE.md` (mismo directorio)):

| Bucket | Oro | Veredicto |
|---|---|---|
| Serie wrap w010-w037 (interna) | 1,254 | conocido/en-lectura (proxy provisional) |
| Serie wrap w038-w129 (unión June+July_w104-106) | 4,424 | **candidato no transcripto** |
| **Serie wrap, total deduplicado** | **5,678** | **4,424 candidatos = 77.9%** |
| Clásicos: 18 superficies físicas (23 paneles) | 2,460 (reps) | bucket separado — solapamiento físico con la serie NO resuelto; NO entra al denominador |
| Redundantes/confirmatorios (224 + 739 + 6,285) | 7,248 | validación cruzada, nunca sumados |

Si se agregan provisionalmente los representantes clásicos al denominador
(solapamiento sin resolver): 4,424/8,138 = 54.4%. Invariante de control:
5,678 + 2,460 + 224 + 739 + 6,285 = 15,386 oro totales / 125,298 ventanas.

## 4. Qué cambia para el claim de publicación

- Claim sostenido y fundado: **4,424 de 5,678 ventanas oro (77.9%) de la
  serie deduplicada están más allá de la frontera proxy provisional w037**, en
  territorio sin transcripción formal publicada.
- REENCUADRE OBLIGATORIO (sin cambios): el equipo oficial está escalando la
  lectura (1667 completo); el valor del índice es **triage hoy**, no
  prioridad de descubrimiento. Publicar rápido o el claim se evapora solo.
- Pendientes que refuerzan (no bloquean, pero deben declararse): match
  banner GP↔panel (reemplaza el proxy w037 por frontera medida) y
  resolución del solapamiento clásicos↔serie (habilitaría un denominador
  global).

## 5. Reproducir

```
python3 - <<'PY'
import json, re
d = json.load(open('full_index_complete.json'))  # del dataset HF
wr = lambda p: re.search(r'w(\d+)-(\d+)', p)
june = [w for w in d if wr(w['panel']) and w['panel'].startswith('202606') and '_jordi' not in w['panel']]
extra = [w for w in d if w['panel'] == '20260701183141-w104-106']
gold = [w for w in june+extra if w['v3'] >= 0.9]
outer = [w for w in gold if int(wr(w['panel']).group(1)) >= 38]
print(len(gold), len(outer))   # 5678 4424
PY
```
