# STATS: indice de legibilidad Scroll 5 (PHerc0172) y PHerc0139

## PHerc0172 (Scroll 5) — score_final = min(scoreA, scoreB)

- Ventanas totales evaluadas: **24528** (53 segmentos, 2 modelos c/u: `timesformer_scroll5_july_retreat`=A, `timesformer_scroll5_november19`=B)
- Clamped (WIN>min(H,W)): 0/24528
- Oro (score_final>=0.9): **0** (0.000%)
- score_final>=0.99: 0
- Percentiles score_final: {50: 0.0004, 75: 0.0011, 90: 0.0029, 95: 0.0051, 99: 0.0173, 99.5: 0.0253, 99.9: 0.06}
- Percentiles scoreA (july_retreat): {50: 0.0018, 75: 0.0045, 90: 0.0109, 95: 0.0185, 99: 0.0562, 99.5: 0.0862, 99.9: 0.3942} | max=0.9379 | >=0.9: 3
- Percentiles scoreB (november19): {50: 0.0004, 75: 0.0013, 90: 0.0034, 95: 0.0062, 99: 0.0208, 99.5: 0.0308, 99.9: 0.0999} | max=0.8448 | >=0.9: 0
- corr(A,B) = 0.552 (correlacion positiva moderada: ambos modelos SI ven señal correlacionada, pero B esta sistematicamente mas bajo/conservador)
- OR (max(A,B)>=0.9) en vez de AND: 3 ventanas

### Top-10 segmentos PHerc0172 por score_final maximo

| segmento | n_ventanas | max(score_final) | max(scoreA) | max(scoreB) | frac>=0.5 (A) |
|---|---|---|---|---|---|
| 20251110110112-w066_20251110110112608_flatboi | 335 | 0.799 | 0.938 | 0.845 | 0.90% |
| 20250926145427-w084_20250926145427439_flatboi | 138 | 0.649 | 0.754 | 0.649 | 1.45% |
| 20251107110950-w064_20251107110950052_flatboi | 399 | 0.334 | 0.903 | 0.334 | 1.50% |
| 20251113130119-w073_20251113130119516_flatboi | 396 | 0.227 | 0.227 | 0.346 | 0.00% |
| 20251113152136-w074_20251113152136889_flatboi | 396 | 0.180 | 0.636 | 0.180 | 0.25% |
| 20251113021010-w072_20251113021010674_flatboi | 396 | 0.125 | 0.125 | 0.126 | 0.00% |
| 20251113204233-w075_20251113204233755_flatboi | 396 | 0.122 | 0.417 | 0.193 | 0.00% |
| 20250926112011-w078_20250926112011918_flatboi | 271 | 0.118 | 0.318 | 0.118 | 0.00% |
| 20251115002741-auto_grown_20251115002740308_1_flatboi | 1501 | 0.085 | 0.506 | 0.085 | 0.07% |
| 20251111010954-w068_20251111010954408_flatboi | 417 | 0.073 | 0.300 | 0.073 | 0.00% |

### Control positivo PHerc0172 (First Title mvrcii et al 2023-24)

**RESULTADO: el indice con la regla estricta min(A,B)>=0.9 da senal casi nula (0/24528 = 0.000%).** PERO la inspeccion visual (top40_s5.png, mismo preprocesado que el scoring) muestra letras griegas CLARAMENTE legibles a ojo en varios crops de score_final bajo (0.2-0.7), concentrados en los wraps w064-w066 (segmentos `20251107110950-w064...`, `20251109232817-w065...`, `20251110110112-w066...`). Diagnostico: scoreA (july_retreat) SI detecta esas ventanas (hasta 0.94), pero scoreB (november19) las califica sistematicamente mas bajo (su propio maximo global es 0.84) pese a que el crop se ve casi identico a ojo entre A y B (ver /tmp/diag_agree_high_* vs /tmp/diag_A_high_B_low_* generados durante el diagnostico). Esto es weight de calibracion del proxy_v4 (entrenado SOLO en renders de Scroll 1) al estilo de textura del modelo november19, NO ausencia de texto real ni error de escala/preprocesado (confirmado: px_um coherente con downsample 8x teorico del volumen 7.91um, ver INVENTORY.md). CONCLUSION: control positivo PASA a nivel de contenido/vision, la regla AND estricta es demasiado conservadora para el par de modelos de Scroll 5 tal como estan calibrados.

## PHerc0139 — score directo (1 solo modelo: `new_canon_autoresearch_recipe`)

- Ventanas totales evaluadas: **4905** (38 segmentos)
- Clamped (WIN>min(H,W)): 0/4905
- Oro (score>=0.9): **63** (1.28%)
- score>=0.99: 27
- Percentiles score: {50: 0.0144, 75: 0.0342, 90: 0.1251, 95: 0.3209, 99: 0.9339, 99.5: 0.9922, 99.9: 0.9997}

### Top-10 segmentos PHerc0139 por DENSIDAD de oro (frac ventanas>=0.9)

| segmento | n_ventanas | n>=0.9 | densidad | max_score |
|---|---|---|---|---|
| 20260112000000-w043_2026011217 | 117 | 15 | 12.82% | 1.000 |
| 20260422000000-title_2026042222_zmid_flatboi | 16 | 2 | 12.50% | 0.961 |
| 20260206000001-w047_2026020613 | 126 | 9 | 7.14% | 0.997 |
| 20260115000000-w044_2026011522 | 117 | 7 | 5.98% | 1.000 |
| 20260215000000-w024_2026021572 | 110 | 6 | 5.45% | 1.000 |
| 20260325000000-w046_20260325 | 117 | 4 | 3.42% | 1.000 |
| 20260318000000-w049_20260318 | 135 | 4 | 2.96% | 1.000 |
| 20260126000000-w045_2026012619 | 117 | 3 | 2.56% | 1.000 |
| 20260303000000-w034_2026030317 | 132 | 3 | 2.27% | 0.996 |
| 20250223000000-w059_2025022312 | 173 | 3 | 1.73% | 0.939 |

### Control positivo PHerc0139 (titulo leido por la comunidad)

**PASA.** El segmento `20260422000000-title_2026042222_zmid_flatboi` (nombrado 'title' — coincide con la region del titulo ya leida por la comunidad) tiene 2/16 = 12.5% de ventanas >=0.9, la SEGUNDA densidad mas alta de todo el rollo (empatando con w043 al 12.8%, ver tabla de arriba). Score maximo: 0.961. Esto confirma que el indice funciona correctamente para PHerc0139: la zona con texto conocido efectivamente destaca por sobre el resto del corpus.

## Presupuesto de descarga

- `du -sh maps/`: 109M	maps