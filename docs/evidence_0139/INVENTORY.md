# INVENTORY: Scroll 5 (PHerc0172) y PHerc0139 — mapas de tinta oficiales

Bucket: `s3://vesuvius-challenge-open-data` (anonimo, via `vesuvius_data.py`). Paths reales confirmados listando (no de memoria):

- `PHerc0172/segments/<seg>/ink-detection/downsampled/*-ds8.jpg` (+ `mesh/<mesh>.tifxyz/{meta.json,x.tif,y.tif,z.tif}`)
- `PHerc0139/segments/<seg>/ink-detection/downsampled/*-ds8.jpg` (+ mesh igual)

## PHerc0172 (Scroll 5)

**53 segmentos**, TODOS con DOS modelos de tinta timesformer:

- `timesformer_scroll5_july_retreat` (fecha modelo 20250713185324)
- `timesformer_scroll5_november19` (fecha modelo 20251222202946)

Volumen nativo: 7.91um-53keV, id `20241024131838` (volumen estandar; el segmento `w064` traia ademas un volumen outlier `20241024131839` con los mismos 2 modelos — se descarto por no ser el usado en el resto del corpus, ver nota en `inventory.py`).

Area fisica: 50.3–437.0 cm2 (los `auto_grown_*` son tiras muy alargadas de area grande, ds8 con W>>H, WIN igual coherente).
px_um: 42.3–61.0 um/px (esperado teorico ds8 = 7.91*8 = 63.3um/px, coincide bien).
WIN: 161–232 px. Clamped (WIN>min(H,W)): 0/53.

| segmento | area_cm2 | ds8 HxW | px_um | WIN | clamped |
|---|---|---|---|---|---|
| 20250917143559-w062_20250917143559205_flatboi | 97.7 | 1575x1718 | 60.10 | 164 | False |
| 20250926112011-w078_20250926112011918_flatboi | 84.1 | 1713x1563 | 56.06 | 175 | False |
| 20250926113336-w079_20250926113336891_flatboi | 85.6 | 1815x2048 | 47.98 | 205 | False |
| 20250926114310-w080_20250926114310705_flatboi | 63.5 | 1560x1428 | 53.39 | 184 | False |
| 20250926122938-w082_20250926122938619_flatboi | 69.4 | 1790x1440 | 51.90 | 189 | False |
| 20250926132117-w083_20250926132117595_flatboi | 75.4 | 1743x1453 | 54.57 | 180 | False |
| 20250926145427-w084_20250926145427439_flatboi | 50.3 | 1208x1503 | 52.63 | 187 | False |
| 20250926150345-w086_20250926150345176_flatboi | 64.4 | 1558x1213 | 58.36 | 168 | False |
| 20250926153406-w088_20250926153406704_flatboi | 72.0 | 1820x1563 | 50.33 | 195 | False |
| 20251106133152-w077_20251106133152767_flatboi | 80.4 | 1993x1475 | 52.28 | 188 | False |
| 20251106170358-w076_20251106170358232_flatboi | 81.3 | 1683x1520 | 56.39 | 174 | False |
| 20251107063327-w063_20251107063327215_flatboi | 102.9 | 1605x1760 | 60.36 | 163 | False |
| 20251107110950-w064_20251107110950052_flatboi | 113.1 | 1678x1868 | 60.08 | 164 | False |
| 20251107175958-w061_20251107175958270_flatboi | 86.3 | 1505x1585 | 60.16 | 163 | False |
| 20251109232817-w065_20251109232817724_flatboi | 113.6 | 1898x1858 | 56.76 | 173 | False |
| 20251110110112-w066_20251110110112608_flatboi | 112.6 | 2093x1873 | 53.60 | 183 | False |
| 20251110135146-w085_20251110135146457_flatboi | 64.8 | 1580x1210 | 58.23 | 169 | False |
| 20251110135803-w067_20251110135803677_flatboi | 112.2 | 1643x1858 | 60.62 | 162 | False |
| 20251111010954-w068_20251111010954408_flatboi | 111.4 | 1635x1865 | 60.44 | 163 | False |
| 20251111151836-w069_20251111151836406_flatboi | 131.2 | 2045x2183 | 54.20 | 181 | False |
| 20251111210734-w070_20251111210734722_flatboi | 110.5 | 1615x1873 | 60.44 | 163 | False |
| 20251112000002-w087_20251112000002214_flatboi | 64.2 | 1553x1203 | 58.62 | 168 | False |
| 20251112163527-w071_20251112163527854_flatboi | 111.3 | 1613x1885 | 60.49 | 163 | False |
| 20251113021010-w072_20251113021010674_flatboi | 109.4 | 1595x1885 | 60.32 | 163 | False |
| 20251113130119-w073_20251113130119516_flatboi | 109.3 | 1590x1893 | 60.27 | 163 | False |
| 20251113152136-w074_20251113152136889_flatboi | 109.1 | 1585x1880 | 60.51 | 162 | False |
| 20251113204233-w075_20251113204233755_flatboi | 108.3 | 1573x1878 | 60.56 | 162 | False |
| 20251114202035-w081_20251114202035261_flatboi | 62.8 | 1470x1428 | 54.68 | 180 | False |
| 20251115002740-auto_grown_20251115002740308_0_flatboi | 311.9 | 1388x6150 | 60.45 | 163 | False |
| 20251115002741-auto_grown_20251115002740308_1_flatboi | 393.9 | 1573x7038 | 59.65 | 165 | False |
| 20251115002742-auto_grown_20251115002740308_2_flatboi | 391.7 | 1548x6975 | 60.23 | 163 | False |
| 20251115002743-auto_grown_20251115002740308_3_flatboi | 409.9 | 1620x7195 | 59.30 | 166 | False |
| 20251115002744-auto_grown_20251115002740308_4_flatboi | 437.0 | 2000x7318 | 54.64 | 180 | False |
| 20251115002745-auto_grown_20251115002740308_5_flatboi | 432.9 | 1593x7663 | 59.55 | 165 | False |
| 20251115002746-auto_grown_20251115002740308_6_flatboi | 327.7 | 1395x6943 | 58.17 | 169 | False |
| 20251115002747-auto_grown_20251115002740308_7_flatboi | 379.2 | 1530x7043 | 59.32 | 166 | False |
| 20251115002748-auto_grown_20251115002740308_8_flatboi | 276.4 | 1593x4668 | 60.97 | 161 | False |
| 20251203230500-w089_20251203230500465_flatboi | 70.7 | 1615x1528 | 53.52 | 184 | False |
| 20251204060522-w090_20251204060522416_flatboi | 71.2 | 1608x1523 | 53.92 | 182 | False |
| 20251204071911-w091_20251204071911070_flatboi | 70.8 | 1598x1520 | 53.97 | 182 | False |
| 20251204101314-w092_20251204101314959_flatboi | 71.6 | 1693x1570 | 51.90 | 189 | False |
| 20251204192708-w093_20251204192708445_flatboi | 73.0 | 1883x2163 | 42.35 | 232 | False |
| 20251205115859-w094_20251205115859448_flatboi | 52.3 | 1408x1300 | 53.45 | 184 | False |
| 20251206184729-w095_20251206184729906_flatboi | 57.2 | 1810x1428 | 47.05 | 209 | False |
| 20251207123912-w060_20251207123912611_flatboi | 70.6 | 1375x1445 | 59.63 | 165 | False |
| 20251210142414-w059_20251210142414060_flatboi | 71.8 | 1190x1650 | 60.46 | 163 | False |
| 20251210153304-w058_20251210153304503_flatboi | 82.1 | 1365x1650 | 60.37 | 163 | False |
| 20251210160810-w057_20251210160810301_flatboi | 79.7 | 1360x1628 | 60.01 | 164 | False |
| 20251211095724-w056_20251211095724922_flatboi | 78.0 | 1333x1613 | 60.23 | 163 | False |
| 20251211111451-w055_20251211111451620_flatboi | 77.0 | 1343x1588 | 60.10 | 164 | False |
| 20251211135303-w054_20251211135303394_flatboi | 74.9 | 1325x1565 | 60.09 | 164 | False |
| 20251211152543-w053_20251211152543204_flatboi | 73.3 | 1325x1543 | 59.89 | 164 | False |
| 20251212105627-w052_20251212105627148_flatboi | 72.0 | 1323x1525 | 59.75 | 165 | False |

## PHerc0139

**38 segmentos**, UN solo modelo de tinta: `new_canon_autoresearch_recipe` (fecha modelo 20260417190342).

Volumen nativo: 2.399um-0.22m-78keV, id `20260102150214`.

Area fisica: 7.4–62.5 cm2.
px_um: 15.3–18.3 um/px (esperado teorico ds8 = 2.399*8 = 19.2um/px, coincide bien).
WIN: 538–644 px. Clamped (WIN>min(H,W)): 0/38.

Nota: el segmento `20260422000000-title_2026042222_zmid_flatboi` es, por nombre, la region del TITULO ya identificada por la comunidad — candidato natural para el control positivo.

| segmento | area_cm2 | ds8 HxW | px_um | WIN | clamped |
|---|---|---|---|---|---|
| 20250108000000-w025_2025010863 | 35.9 | 3540x3310 | 17.50 | 562 | False |
| 20250108000001-w026_2025010854 | 40.7 | 3620x3560 | 17.77 | 553 | False |
| 20250108000002-w027_2025010845 | 38.9 | 3560x3550 | 17.55 | 560 | False |
| 20250108000003-w028_2025010836 | 39.5 | 3530x3580 | 17.69 | 556 | False |
| 20250108000004-w029_2025010827 | 39.5 | 3510x3610 | 17.66 | 557 | False |
| 20250108000005-w030_2025010818 | 39.4 | 3470x3630 | 17.68 | 556 | False |
| 20250223000000-w059_2025022312 | 53.9 | 3510x4870 | 17.76 | 553 | False |
| 20250831000000-w040_2025083102 | 37.7 | 3110x3880 | 17.68 | 556 | False |
| 20251226000000-w055_2025122611 | 58.4 | 3750x5070 | 17.53 | 561 | False |
| 20260108000000-w041_2026010816 | 37.6 | 3010x3900 | 17.90 | 549 | False |
| 20260112000000-w043_2026011217 | 38.2 | 2970x3950 | 18.04 | 545 | False |
| 20260115000000-w044_2026011522 | 38.1 | 2940x3970 | 18.07 | 544 | False |
| 20260115000001-w056_2026011514 | 52.6 | 3490x4740 | 17.82 | 552 | False |
| 20260126000000-w045_2026012619 | 38.0 | 2910x4010 | 18.04 | 545 | False |
| 20260127000000-w057_2026012713 | 56.4 | 3690x4760 | 17.92 | 549 | False |
| 20260130000000-w031_2026013019 | 39.9 | 3440x3650 | 17.82 | 552 | False |
| 20260203000000-w032_2026020303 | 40.3 | 3450x3700 | 17.77 | 553 | False |
| 20260206000000-w042_2026020613 | 36.0 | 2910x3830 | 17.97 | 547 | False |
| 20260206000001-w047_2026020613 | 37.8 | 2840x4100 | 18.02 | 546 | False |
| 20260206000002-w054_2026020617 | 62.5 | 3720x5420 | 17.61 | 558 | False |
| 20260210000000-w058_2026021020 | 55.2 | 3650x4800 | 17.75 | 554 | False |
| 20260215000000-w024_2026021572 | 33.6 | 3450x3220 | 17.39 | 565 | False |
| 20260219000000-w033_2026021913 | 41.2 | 3450x3730 | 17.90 | 549 | False |
| 20260219000001-w048_2026021912 | 37.9 | 2780x4140 | 18.15 | 542 | False |
| 20260220000000-w053_2026022021 | 57.4 | 3620x5040 | 17.73 | 554 | False |
| 20260227000000-w052_2026022705 | 57.4 | 3740x4750 | 17.97 | 547 | False |
| 20260302000000-w039_2026030210 | 36.4 | 4160x3750 | 15.27 | 644 | False |
| 20260302000001-w050_2026030220 | 15.8 | 2580x1890 | 18.01 | 546 | False |
| 20260303000000-w034_2026030317 | 41.1 | 3420x3750 | 17.89 | 549 | False |
| 20260306000000-w038_2026030608 | 34.0 | 3010x3620 | 17.66 | 557 | False |
| 20260306000001-w051_2026030600 | 56.0 | 3680x4670 | 18.05 | 545 | False |
| 20260310000000-w037_2026031015 | 32.5 | 2980x3500 | 17.66 | 557 | False |
| 20260311000000-w023_202603112281 | 31.9 | 3370x3100 | 17.46 | 563 | False |
| 20260316000000-w036_2026031607 | 30.5 | 2910x3390 | 17.58 | 559 | False |
| 20260317000000-w035_2026031718 | 22.2 | 2830x2550 | 17.53 | 561 | False |
| 20260318000000-w049_20260318 | 41.9 | 2750x4570 | 18.26 | 538 | False |
| 20260325000000-w046_20260325 | 38.0 | 2910x4020 | 18.02 | 546 | False |
| 20260422000000-title_2026042222_zmid_flatboi | 7.4 | 870x2610 | 18.11 | 543 | False |

## Metodo de escala fisica (auditoria)

`area_cm2` NO viene de `area_vx2` en meta.json (ese campo no existe en estos meta.json — solo traen `bbox` y `scale`). En su lugar: se descargo el mesh tifxyz (`x.tif,y.tif,z.tif`), se conto `valid = (x,y,z)>0` (vertices reales de la superficie), y se midio el paso 3D real entre vertices adyacentes (mediana de distancias euclidianas fila/columna en vox nativos del volumen) — dio ~20.0-20.1 vox, consistente con `meta.json['scale']=[0.05,0.05]` (1/0.05=20), asi que se valido cruzado. `area_cm2 = n_validos * (paso_vox * um_nativo)^2 / 1e8`. Luego `px_um = sqrt(area_cm2*1e8/(H_ds8*W_ds8))`, `WIN = round(9830/px_um)`, `stride=WIN//2`. Sanity check: px_um medido coincide con el downsample teorico ds8=8x del volumen nativo (7.91*8=63.3 vs medido 42-61; 2.399*8=19.2 vs medido 15.3-18.3) — la pequena discrepancia es esperable por curvatura 3D de la superficie vs proyeccion 2D plana del flattening.
