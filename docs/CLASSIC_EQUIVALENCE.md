# Manifest de equivalencias físicas — panel(es) clásicos del índice S1

Fecha: 2026-07-11. Motivado por peer review: el bucket de 23 "clásicos" del
índice contenía re-renders y un duplicado explícito contados como territorio
distinto. Este manifest agrupa los 23 paneles por linaje de nombre (misma
superficie física = mismo segmento base y mismo offset de wrap).

Método: parsing del nombre. `5753_-N` = re-segmentación oficial de
20230702185753 desplazada N wraps (offsets distintos = wraps distintos =
territorio distinto entre sí); sufijos `_vN` / `_v2_flatboi` = re-proceso de
la MISMA superficie; `_copy` = duplicado de subida.

## Grupos con más de un render (los demás 14 clásicos son 1:1)

| Superficie física (base, offset) | Renders en el índice | Oro rep. | Oro dup. |
|---|---|---:|---:|
| 20230702185753, offset 0 | `20230702185753` (rep), `20260602225659-5753_0`, `20260602230115-20230702185753_v14` | 163 | 143 |
| 20230702185753, offset −1 | `20260603005223-5753_-1` (rep), `20260603193311-5753_-1_copy` | 14 | 19 |
| 20231005123336, offset 0 | `20231005123336` (rep), `20260603222816-20231005123336_v2_flatboi` | 401 | 35 |
| 20231210121321, offset 0 | `20231210121321` (rep), `20260604223808-20231210121321_v8` | 201 | 27 |

**Resultado: 23 paneles → 18 superficies físicas.** Oro clásico
2,684 = 2,460 en representantes + 224 en re-renders duplicados.

## Advertencia estructural (por qué los clásicos NO entran al denominador)

Los clásicos son segmentaciones era-2023/2026 de la franja legible; la serie
de paneles w010–w129 cubre el rollo entero. El solapamiento físico entre
clásicos y paneles NO está resuelto (requeriría registrar cada clásico contra
la serie por coordenadas o fingerprint). Hasta entonces, ningún número
"territorio distinto global" que sume clásicos + paneles es defendible: los
clásicos se reportan como bucket separado de confirmación, y el denominador
canónico es la unión deduplicada de la serie wrap.

## Números canónicos del índice (recomputados 2026-07-11)

- Serie wrap, unión deduplicada June+July: la serie June abarca w010–w129
  pero su segmento w104–106 no tiene mapa de tinta ds8 publicado; el panel
  July `20260701183141-w104-106` (2,648 ventanas, 131 oro) cubre ese rango. **Unión: 5,678 oro**; más allá de w037: **4,424 = 77.9%**.
- Clásicos (18 superficies): 2,460 oro en representantes, bucket separado.
- Redundantes/confirmatorios: 224 (re-renders clásicos) + 739 (`_jordi`) +
  6,285 (serie July en wraps ya cubiertos) = 7,248.
- Invariante: 5,678 + 2,460 + 224 + 739 + 6,285 = 15,386 oro totales sobre
  125,298 ventanas — sin cambios en los conteos brutos.

Reproducir:

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
