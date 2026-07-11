# Estado de transcripción publicada: PHerc 172 (Scroll 5) y PHerc 0139

Investigación web, 2026-07-07. Objetivo: contrastar nuestras zonas "oro" (índice de legibilidad propio
sobre mapas oficiales) contra lo que está efectivamente leído/publicado por Vesuvius Challenge y equipos
de papirología, para no reclamar "descubrimiento" de texto que ya es público.

Regla aplicada: distingo "publicado formalmente" (paper arXiv, anuncio oficial scrollprize.org/Substack
con lectura papirológica, prize award) de "observado por la comunidad" (repos GitHub de voluntarios,
posts técnicos sin transcripción, Discord). Si no encontré nada, digo "no encontrado" — no invento.

---

## 1. PHerc 172 / Scroll 5 — qué está leído/publicado

### 1.1 Título (línea final / subscriptio)
- **Título recuperado: "Περὶ Κακιῶν" ("On Vices" / Sobre los vicios), de Filodemo.** Primera vez que se
  recupera el título de un rollo de Herculano aún enrollado, sin abrirlo.
- Anunciado oficialmente en feb-2025 (Oxford/Bodleian) y premiado como **First Title Prize $60,000** a
  Marcel Roth y Micha Nowak (hallazgo independiente también por Sean Johnson, del equipo VC), anuncio
  formal ~may-2025.
- Fuentes:
  - https://scrollprize.substack.com/p/60000-first-title-prize-awarded
  - https://www.ox.ac.uk/news/2025-02-07-inside-herculaneum-scroll-seen-first-time-almost-2000-years
  - https://www.cnn.com/2025/05/06/science/herculaneum-scroll-title-author-decoded-intl-scli
  - https://www.bodleian.ox.ac.uk/about/media/feb25/herculaneum-scroll

### 1.2 Cuerpo del rollo — progreso oficial (equipo VC / Oxford)
- **11-sep-2025**, post oficial "Column of text from PHerc. 172 (Scroll 5)": el equipo (papirólogos
  Maria Chiara Robustelli, Daniel Delattre, Federica Nicolardi, Claudio Vergara) transcribió **una
  columna** ubicada en la **columna final, justo antes del título de cierre**. Contenido: cita de los
  *Caracteres* de Teofrasto (el βδέλυρος / "hombre repulsivo", cap. XI), con vocabulario de
  κουρεῖον/μυροπώλιον (barbería/perfumería) y μεθύσκεσθαι. Estado explícito: **preliminar, "not yet
  released for academic publication"**. El post no da IDs de segmento ni número de wrap.
  https://scrollprize.substack.com/p/column-of-text-from-pherc-172-scroll
- **9-oct-2025**, "Multiple scrolls now show Greek letters": PHerc 172 se menciona solo como referencia
  de resolución de escaneo (~9 µm), **no** como fuente de letras legibles nuevas en ese momento.
  https://scrollprize.substack.com/p/multiple-scrolls-now-show-greek-letters
- **13-ene-2026**, "~70% of PHerc. 172 is now digitally unwrapped": ~70% de la superficie (la mitad
  inferior, ~7 m de longitud, ~14 cm de altura) desenrollada digitalmente; el 30% superior sigue
  demasiado dañado. Los **wraps externos** muestran "fragmentos de columnas donde se pueden leer varias
  letras juntas"; zonas más profundas solo muestran márgenes de columna, renglones tenues y letras
  sueltas. **No se publica transcripción de cuerpo en este post.** Se dice explícitamente que
  "Oxford papyrologists are actively working toward an article discussing the newly legible material"
  (artículo aún no publicado a esa fecha).
  https://scrollprize.substack.com/p/70-of-pherc-172-is-now-digitally
- **19-mar-2026**, update técnico: modelo de detección de tinta 3D; nota general de que "outer scroll
  regions show higher ink detection predictions" e "inner core exhibits lower legibility" — **sin
  números de wrap ni segmento**, es una observación agregada del modelo, no transcripción.
  https://scrollprize.substack.com/p/we-are-cooking
- **Anuncio del 25-jun-2026 / paper arXiv 2606.29085** ("Complete virtual unwrapping and reading of a
  rolled Herculaneum papyrus"): el rollo **completamente leído es PHerc. 1667 (Scroll 4)**, no PHerc 172.
  PHerc 172 **no se menciona** en ese paper como objeto de lectura de cuerpo — el paper cubre PHerc 1667
  (primario, 22 columnas) y PHerc 139 (secundario, ver sección 2).
  https://arxiv.org/html/2606.29085v1 · https://scrollprize.org/firstscroll

**Conclusión 1.2:** a jul-2026, **no hay publicación formal/peer-reviewed de la lectura del cuerpo de
PHerc 172.** Solo existe (a) el título, formalmente publicado, y (b) una columna preliminar (cerca del
título) compartida en blog oficial pero explícitamente no publicada académicamente, sin ID de segmento.

### 1.3 Transcripción comunitaria — repo Bodillium/Herculaneum-Scroll-Labels
- https://github.com/Bodillium/Herculaneum-Scroll-Labels — de un voluntario individual ("polytrope" en
  Discord, N.A. Bodill), **no oficial de VC**, licencia CC BY-NC-SA, explícitamente "very preliminary",
  "not peer-reviewed", "everything should be taken with a grain of salt".
- Contiene el PDF "Preliminary Transcriptions of P.Herc. 172 - N.A. Bodill" (v0.1) con lecturas
  especulativas de estos **segmentos, todos fechados oct/nov-2024**:
  `20241025145341`, `20241025145701`, `20241025150211`, `20241028121111`, `20241030152031`,
  `20241102125650`, `20241102160330`, `20241108111522`, `20241108115232`, `20241108120732`,
  `20241113070770`, `20241113080880`, `20241113090990`.
- Último commit del repo: **7-dic-2024**. No hay actualizaciones en 2025 ni 2026.
  https://github.com/Bodillium/Herculaneum-Scroll-Labels/commits/main

**Cruce con nuestras zonas oro de S5:** nuestros segmentos w06-w08
(`20251107110950`, `20251110110112`, `20251113130119`, `20250926145427`) son de **sep-nov 2025**, un
año posterior a todos los segmentos cubiertos por el repo Bodillium (oct-nov 2024). **Ningún ID de
segmento coincide.** Este repo no cubre nuestras zonas.

---

## 2. PHerc 0139 — qué está leído/publicado

### 2.1 Título
- **Título recuperado: "Φιλοδήμου περὶ θεῶν Η" — "Filodemo, Sobre los dioses, libro 8" (Philodemus, On
  Gods, Book 8).** Primera evidencia de que *Sobre los dioses* de Filodemo era una obra de al menos 8
  libros (antes solo se conocía el libro 1, PHerc 26).
- Anunciado oficialmente el **25-jun-2026** en la Biblioteca Nazionale di Napoli, junto con el anuncio
  de PHerc 1667 completo. Publicado formalmente en el paper arXiv 2606.29085 como "secondary scroll" /
  "title-identification case".
- Cita textual del paper: *"the title-bearing sequence is read as ... Φ̣ι[λοδ]ή̣μου περὶ θεῶν Η̅"*.
  Fuera del título, el paper dice: *"In addition to the end title, the portions of text recovered thus
  far preserve a number of terms and expressions"* — cita sueltas: χωρὶς προνο[ί]α̣ς, ἀόρατα, καὶ τὸ
  κατ̣ὰ̣ φύσις — **sin números de columna, wrap ni segmento**, y explícitamente no es una transcripción
  de cuerpo completo, solo "términos y expresiones" sueltos cerca del título.
  https://arxiv.org/html/2606.29085v1 · https://scrollprize.org/firstscroll
- Cobertura de prensa (confirma alcance, no agrega nuevos datos de wraps): CNN, Smithsonian,
  archaeologymag, ESRF/Diamond Light Source.
  https://www.cnn.com/2026/06/26/science/papyrus-scroll-vesuvius-ai-scli-intl
  https://www.smithsonianmag.com/smart-news/scientists-have-deciphered-the-surviving-fragments-of-a-2000-year-old-philosophical-treatise-frozen-in-time-by-mount-vesuvius-eruption-180989036/

### 2.2 Progreso previo (comunidad/técnico, pre-anuncio)
- **9-oct-2025**, "Multiple scrolls now show Greek letters": PHerc 139 mostraba la **señal de tinta más
  fuerte** entre los rollos probados; letra tau (τ) visible en escaneo de 2 µm. Estado explícito:
  **"not formally transcribed"**, observaciones preliminares comparables a los "first letters" de 2023.
  Sin IDs de segmento ni wrap.
  https://scrollprize.substack.com/p/multiple-scrolls-now-show-greek-letters
- **19-mar-2026**: un modelo de detección de tinta entrenado con datos de PHerc 139 generalizó bien a
  PHerc 1667 — nota técnica de infraestructura, no transcripción.
  https://scrollprize.substack.com/p/we-are-cooking
- No encontré ningún repositorio GitHub comunitario tipo Bodillium dedicado a PHerc 139 (búsqueda sin
  resultados relevantes).

**Conclusión 2.2:** a jul-2026, lo único publicado formalmente de PHerc 139 es **el título/colofón +
un puñado de términos sueltos cercanos**, en el paper arXiv 2606.29085 (25-jun-2026). No hay
transcripción publicada de columnas del cuerpo del rollo, y no se identifican wraps/segmentos
específicos en ninguna fuente encontrada.

**Cruce con nuestras zonas oro de 0139:** el título ya lo sabíamos leído (nota previa del usuario:
segmento `20260422000000-title...`, abr-2026, anterior al anuncio público de jun-2026 — consistente
con que el equipo VC ya lo tenía internamente). Nuestros segmentos w02, w03, w04, w05 y w043 (varios
timestamps `2026xxxx-w0N`) son **etiquetas de wrap distintas** a la del título — no encontré ninguna
fuente que indique que esas columnas específicas (fuera de la zona del título) hayan sido leídas o
publicadas por nadie, comunidad o equipo oficial.

---

## 3. Veredicto por zona

| Zona nuestra | Grupo | Veredicto | Evidencia |
|---|---|---|---|
| PHerc0139 — zona del título (`20260422000000-title...`) | 0139 | **Transcripto (publicado formalmente)** | Título "Φιλοδήμου περὶ θεῶν Η" / On Gods Book 8, arXiv 2606.29085 + anuncio 25-jun-2026 (scrollprize.org/firstscroll). Coincide con lo que el usuario ya sabía. |
| PHerc0139 — w02, w03, w04, w05, w043 | 0139 | **Sin transcripción pública encontrada** | Único material publicado de 0139 es el título + términos sueltos sin ID de wrap/segmento (arXiv 2606.29085). Observación comunitaria de "señal de tinta fuerte" (oct-2025) es genérica, no formalmente transcripta, y tampoco identifica wraps. No se encontró repo ni paper que cubra estas columnas específicas. |
| PHerc172/S5 — w06, w07, w08 (segmentos `20251107110950`, `20251110110112`, `20251113130119`, `20250926145427`) | S5 | **Sin transcripción pública encontrada** (parcialmente incierto) | Título de PHerc172 ("On Vices") sí está publicado, pero es una zona distinta (subscriptio final). El único cuerpo de texto compartido oficialmente — la "columna final antes del título" (11-sep-2025) — es preliminar, sin ID de segmento publicado, por lo que **no se puede confirmar ni descartar** solapamiento con w06-w08. El repo comunitario Bodillium (única transcripción de cuerpo con IDs de segmento verificables) cubre solo segmentos oct/nov-2024, ninguno de los cuales coincide con nuestros IDs de sep/nov-2025. A ene-2026 el equipo oficial decía explícitamente que el artículo papirológico de Oxford sobre el material recién legible **todavía no estaba publicado**, y no encontré ninguna publicación posterior (hasta jul-2026) que lo supere. |

**Resumen:** las zonas w06-w08 de S5 y w02-w05/w043 de 0139 (nuestras zonas "oro" de cuerpo, no de
título) **no tienen transcripción pública confirmada** con las fuentes revisadas. La única superposición
de riesgo real es la columna preliminar de PHerc172 (11-sep-2025, sin ID de segmento) — no se puede
confirmar si cae dentro de w06-w08 o no; tratar como posible pero no verificado.

---

## Top-3 fuentes clave

1. **arXiv 2606.29085 — "Complete virtual unwrapping and reading of a rolled Herculaneum papyrus"**
   (25-jun-2026). Fuente primaria formal: PHerc 1667 completo + título de PHerc 139.
   https://arxiv.org/html/2606.29085v1
2. **scrollprize.substack.com — "~70% of PHerc. 172 is now digitally unwrapped"** (13-ene-2026).
   Estado más reciente encontrado del cuerpo de Scroll 5: sin transcripción publicada, artículo de
   Oxford aún en preparación. https://scrollprize.substack.com/p/70-of-pherc-172-is-now-digitally
3. **github.com/Bodillium/Herculaneum-Scroll-Labels** — única transcripción de cuerpo de PHerc 172 con
   IDs de segmento verificables (oct/nov-2024, no oficial, no peer-reviewed); permite descartar
   solapamiento directo con nuestras zonas w06-w08 (sep/nov-2025).
   https://github.com/Bodillium/Herculaneum-Scroll-Labels

Fuentes adicionales usadas: https://scrollprize.substack.com/p/60000-first-title-prize-awarded ·
https://scrollprize.substack.com/p/column-of-text-from-pherc-172-scroll ·
https://scrollprize.substack.com/p/multiple-scrolls-now-show-greek-letters ·
https://scrollprize.org/firstscroll · https://scrollprize.org/winners ·
https://www.cnn.com/2026/06/26/science/papyrus-scroll-vesuvius-ai-scli-intl


---

## REFRESH 2026-07-11 (post-ciclo de noticias PHerc 1667)

Re-verificación de los veredictos de este documento, 4 días después:

- **PHerc 0139**: arXiv 2606.29085 sigue en **v1** (27-jun) — solo título +
  atribución ("Φ̣ι[λοδ]ή̣μου περὶ θεῶν Η̅") y términos sueltos sin ubicación.
  La página oficial (scrollprize.org/firstscroll) describe el valor de leer
  títulos "before a single column of its body is studied" — lenguaje sobre
  el valor general de los títulos, NO una prueba de que el cuerpo de 0139
  nunca fue examinado (el paper cita términos sueltos recuperados). El
  claim defendible: sin transcripción pública ubicable por wrap a hoy. Prensa jun/jul-2026 (Smithsonian, UKNow,
  greekcitytimes, CNN) repite título+atribución, sin transcripción de
  cuerpo. **Veredicto del 07-jul SE SOSTIENE: las 52 ventanas clear-text
  fuera del título siguen sin transcripción pública localizable.**
- **PHerc 172 / Scroll 5**: sin novedades formales del cuerpo desde el
  post de sep-2025 (una columna junto al título); artículo de Oxford sigue
  sin aparecer publicado.
- Contexto nuevo relevante: el mismo anuncio de jun-2026 desenrolló Paris 4
  completo (~130 wraps) y leyó 1667 entero — la capacidad de transcripción
  oficial está acelerando; los claims "sin transcripción pública" son
  correctos hoy y perecederos (misma lógica que el crosswalk de S1,
  `data/letters/s1_atlas/TRANSCRIPTION_CROSSWALK.md`).
