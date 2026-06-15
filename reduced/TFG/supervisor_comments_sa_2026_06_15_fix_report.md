# Informe exacto de resolución de comentarios SA, 2026-06-15

Este informe corresponde solo a los comentarios nuevos del PDF `TFG--SA.pdf`,
las capturas y los mensajes posteriores del usuario. Los planes anteriores se
consideran ya resueltos.

## Resumen ejecutivo

- Los abstracts vuelven a estar dentro del límite práctico: catalán 146
  palabras, castellano 150, inglés 139.
- CKM se define al inicio del abstract y del Capítulo 1. HARP-Net CKM se
  expande al primer uso en abstracts e introducción.
- El Capítulo 1 añade una sección específica de motivación, ampliando el
  porqué práctico y científico del problema sin compactar la introducción.
- El work plan y el Gantt permanecen en el Capítulo 1 por override explícito
  del usuario.
- El texto tachado de la sección de two-ray fue eliminado.
- Todas las apariciones visibles de la forma sin guion se corrigieron a
  `two-ray`.
- El Capítulo 2 queda separado en un bloque de background técnico y un bloque
  de estado del arte para mapas densos.
- El Capítulo 3 añade una sección numerada de ruta de diseño y una subsección
  explícita de por qué se usan priors multilineales, OLS, ridge, U-Net, FiLM,
  GMM y residual learning.
- La Figura 3.12 queda antes de Evaluation Metrics; por la nueva sección de
  rationale, HARP-Net CKM pasa a la Sección 3.8 y Evaluation Metrics a la 3.9.
- El historial de revisión añade la revisión SA del 15/06/2026 y la versión
  final GMG del 16/06/2026.
- La síntesis de técnicas emergentes en el SOA añade una lectura específica
  para delay spread y angular spread.
- Los resultados del Capítulo 4 se reordenaron como: cualitativo, ciudad y
  perfiles, priors, perfiles finales del modelo, media final agregada, contexto
  SOA.
- Las tablas por ciudad se añadieron para validación y test, omitiendo train
  porque train no es comparable como generalización.

## Comentario por comentario

| ID | Estado | Cómo se resolvió exactamente |
|---|---|---|
| SA-001 | Fixed | `summary.tex` define CKM y HARP-Net CKM en los tres abstracts. Tras la revisión final, los abstracts quedan aproximadamente en 137/128/133 palabras y ya no presentan los resultados numéricos finales. |
| SA-002 | Fixed | `introduction.tex` define CKM en la primera página y define UAV/UxNB antes de usarlos como acrónimos técnicos. También define DS/AS en el gap del Capítulo 1. |
| SA-003 | Fixed | `introduction.tex` reemplaza la frase redundante por: “In Third Generation Partnership Project (3GPP) terminology, a UAV mounted radio access node is called a UxNB”. `acronyms.tex` evita la forma con guion innecesario. |
| SA-004 | Fixed | `introduction.tex` usa “This thesis proposes and evaluates HARP-Net CKM” en vez de presentar el sistema como algo solo “estudiado”. |
| SA-005 | Fixed | El inicio de `introduction.tex` se reescribió en párrafos cortos: contexto 6G/CKM, UAV/UxNB, gap, sistema propuesto y terminología. |
| SA-006 | Fixed | La frase de los experimentos CKM se suavizó en `introduction.tex`: “For the CKM experiments, the line of sight and non line of sight ...”. |
| SA-007 | Fixed | La definición de HARP-Net CKM se concentra en un único bloque del Capítulo 1. Se añadió una frase explícita: CKM es el mapa denso a predecir y HARP-Net CKM es el sistema propuesto. |
| SA-008 | Fixed | La mención prematura a Chapter 4 en los goals fue reemplazada por “the results chapter” y el outline posterior ya enumera los capítulos en orden. |
| SA-009 | Fixed | Se corrigió el texto visible a `two-ray`/`Two-ray` en capítulos, plan e informe. La contribución queda como “LoS propagation based on the coherent two-ray model”. |
| SA-010 | Fixed | Se eliminaron usos confusos de “train calibrated” en prosa visible y se reemplazaron por “calibrated only on training cities” o “training city calibrated” cuando era necesario. |
| SA-011 | Fixed | Las figuras y tablas añadidas se referencian antes o inmediatamente después: Gantt en Capítulo 1, Figura 4.1 en Results, tablas por ciudad y tablas finales. |
| SA-012 | Resuelto por override | El comentario de mover el work plan a apéndice se ignoró por instrucción explícita del usuario. `introduction.tex` mantiene `\section{Work plan}` y `appendices_compact.tex` ya no duplica ese bloque. |
| SA-013 | Fixed | `state_of_art.tex` abre con un mapa del capítulo que menciona las secciones principales y no solo 2.1/2.2. |
| SA-014 | Fixed | CKM se define localmente en Chapter 2 como “channel knowledge map (CKM)” y también aparece definido antes en abstracts y Chapter 1. |
| SA-015 | Fixed | En `state_of_art.tex`, sección “Free space and two-ray propagation”, se eliminó el texto tachado sobre no reportar la ganancia numérica y evaluar el resultado en Chapter 4. |
| SA-016 | Fixed | `state_of_art.tex` separa estructuralmente la parte de background: `Propagation and Channel Statistics Background` contiene FSPL, two-ray, UAV A2G y definiciones de spread; `State of the Art for Dense Path Loss Maps` inicia el bloque de estado del arte. |
| SA-017 | Fixed | `introduction.tex` incluye `State of the art gap and thesis position`, que resume el SOA, explica cómo la tesis va más allá y conecta explícitamente con RQ1/RQ2/RQ3 y las contribuciones. |
| SA-018 | Fixed | `methodology.tex` añade `Design route and rationale` como Sección 3.1 y `Why these techniques` como Subsección 3.1.1. Ahí se explica cómo se llega al pipeline desde el gap: soporte geométrico, priors congelados, OLS/ridge multilineal, stack de entrada DL, U-Net/GroupNorm, FiLM para altura continua, GMM para colas y residual bounded para no borrar el prior. |
| SA-019 | Fixed | `methodology.tex`, sección de support maps, explica que `b_41`, `c_41` y `t_41` son aproximaciones de blocker depth, rooftop clearance y fracción de edificios más altos que el UAV, elegidas por inspección de ciudades de entrenamiento y juzgadas por ridge. |
| SA-020 | Fixed | `prior_detail_try78.tex` y `prior_detail_try79.tex` tienen captions por encima de las tablas afectadas. |
| SA-021 | Fixed | `prior_detail_try79.tex` amplía la procedencia de constantes: anchors redondeados desde la escala observada, offsets desde el orden de topologías, pesos como sensibilidades gruesas con signo esperado, y ridge como parte ajustada. |
| SA-022 | Fixed | `methodology.tex` mantiene `fig:try80_loss_terms` antes de `Evaluation Metrics`. Tras convertir el rationale en sección numerada, el orden queda: HARP-Net CKM en Sección 3.8, Figura 3.12 dentro de esa discusión de pérdidas, y Evaluation Metrics en Sección 3.9. |
| SA-023 | Fixed | `results.tex` explica cómo leer el RMSE: 1.6950 dB de atenuación es muy fuerte bajo este contrato, mientras DS/AS se interpretan contra targets y priors por falta de benchmarks densos por píxel equivalentes. |
| SA-024 | Fixed | `introduction.tex` Work goals y `results.tex` SOA context dicen explícitamente que PL/CA es muy bueno para este dataset y que DS/AS casi no se reportan como mapas densos por píxel comparables. |
| SA-025 | Fixed | `results.tex` añade tablas de validación y test por ciudad con muestras, Att., Delay, Angular, mix de topología y mix de altura. Se usan los CSV DirectML finales ya existentes. No se reporta train porque el modelo y los priors se ajustaron con esas ciudades. |
| SA-026 | Fixed | La figura representativa se movió al principio de Chapter 4 como “Qualitative Reader Map” y se explica como secuencia target, prior, residual, prediction y remaining error. |
| SA-027 | Fixed | Chapter 1 se reestructura como una introducción tipo paper: contexto general, contexto UAV, motivación ampliada, gap/SOA, propuesta, objetivos/RQs, contribuciones y outline. |
| SA-028 | Fixed | Chapter 3 incluye una guía inicial del capítulo, un rationale de diseño y mantiene el método final primero. La cronología larga permanece en apéndice. |
| SA-029 | Fixed | Chapter 4 se reordenó con lectura cualitativa primero, ciudad y perfiles después, y media agregada final después de perfiles. Dentro de HARP-Net CKM Results, los perfiles agrupados preceden a “Final aggregate test result”. |
| SA-030 | Fixed | Se revisaron acrónimos, captions, referencias y wording formal. Los abstracts están bajo límite, y las búsquedas no encuentran el texto tachado ni “train calibrated” en capítulos principales. |
| SA-031 | Fixed | `revision_history_en.tex` añade `3.9 & 15/06/2026 & SA` como revisión final de estructura, SOA, metodología y resultados, y `4.0 & 16/06/2026 & GMG` como versión final después de la revisión SA. La tabla de firma pasa a fecha de escritura 16/06/2026 y fecha de revisión y aprobación 17/06/2026. |
| SA-032 | Fixed | `state_of_art.tex`, en la síntesis de técnicas emergentes, añade un párrafo específico para delay spread y angular spread: TR 38.901/WINNER como log-domain large scale parameters, A2G scalar predictors, modelos probabilísticos, y la razón por la que en esta tesis se transfieren técnicas y no métricas DS/AS externas directamente comparables. |
| SA-033 | Fixed | `introduction.tex` añade `Motivation`, una sección nueva que explica con más detalle la utilidad operativa de un CKM surrogate rápido, la importancia científica de city holdout y altura UAV continua, por qué DS/AS son salidas de primer nivel y por qué el diseño final usa priors calibrados más residual learning. |
| SA-034 | Fixed | `methodology.tex` ajusta `Table 3.1` para que quepa en la primera página del Capítulo 3 sin dejar el bloque vacío grande. Después del último comentario visual, el espaciado interno de filas se abrió de `\arraystretch=0.78` a `0.92`, manteniendo `footnotesize`, de modo que la tabla respira más y sigue en la misma página. |
| SA-035 | Fixed | `methodology.tex` define OLS y ridge en la primera explicación narrativa: OLS minimiza la suma de errores cuadrados en píxeles de ciudades de entrenamiento; ridge usa el mismo predictor lineal pero añade penalización cuadrática de coeficientes para estabilizar regímenes pequeños o variables correlacionadas. La Figura 3.2 también expande el primer uso como ordinary least squares (OLS). |
| SA-036 | Fixed | Se redujo el uso repetido de la palabra `contract` en los capítulos incluidos en `TFG.tex`. Se sustituyó por `evaluation protocol`, `benchmark setup`, `simulation setting`, `evaluation rules` o `setting`, según el contexto. La única coincidencia restante en la búsqueda global de capítulos es `subcontracting`, que no pertenece a ese uso. |
| SA-037 | Fixed | `methodology.tex` reduce los bloques de Figure 3.1 y fija las flechas con anclas explícitas entre nodos. El flujo visual queda raw map -> morphology/priors -> HARP-Net CKM -> final maps, sin flechas aparentes en dirección contraria. |
| SA-038 | Fixed | `revision_history_en.tex` elimina la fila vacía final de la tabla de revisiones y reduce los espacios verticales entre bloques. La página renderizada confirma que revision history, distribution list y approval table caben en una sola página. |
| SA-039 | Fixed | `summary.tex` reescribe los tres abstracts para que expliquen objetivo, método y contribución, sin presentar los resultados numéricos finales. También se redujo el acrónimo `LoS/NLoS` en el abstract y se sustituyó por visibilidad / visibility state. |
| SA-040 | Fixed | `sustainability_balanced.tex` se alineó mejor con la guía ETSETB sin crear niveles `5.x.x.x`: el índice queda en `5.1.1` environmental, `5.1.2` economic y `5.1.3` social. Dentro de cada apartado se añadieron etiquetas en negrita para `Development of BT`, `Project execution` y `Risks and limitations`, además de la estimación de coste de explotación piloto, la limitación sobre códigos éticos de proveedores y el matiz de que los errores sistemáticos pueden afectar a usuarios en ciertos entornos. |

## Fuentes concretas usadas para las tablas por ciudad

No se lanzó una recalculación nueva porque el usuario aclaró que podían usarse
los CSV finales ya existentes. La evaluación per city procede de:

- `C:/TFG/TFGpractice/TFGEightiethTry80/outputs/rmse_mae_mapcorr_val_test_dml_b1_after_range_update/val/rmse_mae_mapcorr_model_prior_comparison.csv`
- `C:/TFG/TFGpractice/TFGEightiethTry80/outputs/rmse_mae_mapcorr_val_test_dml_b1_after_range_update/test/rmse_mae_mapcorr_model_prior_comparison.csv`
- `C:/TFG/TFGpractice/TFGEightiethTry80/outputs/rmse_mae_mapcorr_val_test_dml_b1_after_range_update/run_metadata.json`

Las proporciones de topología y altura proceden del CSV de subexperts finales
porque son metadatos de composición de ciudad y no dependen del target:

- `C:/TFG/TFGpractice/cluster_outputs/TFGEightiethTry80/try80_joint_huge_pathloss_finetune/try80_comparison_city_subexperts.csv`

## Verificación final

- Compilación verificada con el motor correcto indicado por `TFG.tex`:
  `lualatex`, `biber`, `lualatex`, `lualatex`. Para evitar interferencia del
  autocompilador de VS Code, la verificación limpia se hizo en
  `codex_build/TFG_codex.*` y el PDF validado se copió después a `TFG.pdf`.
- PDF final generado en `C:/TFG/FINAL_THESIS/reduced/TFG/TFG.pdf`.
- `codex_build/TFG_codex.log` no contiene referencias indefinidas, citas
  indefinidas, labels por rerun, errores fatales ni overfull boxes relevantes.
- `codex_build/TFG_codex.aux` confirma:
  - `sec:methodology_rationale` = Sección 3.1, página 38.
  - `sec:methodology_dataset_split` = Sección 3.2, página 39.
  - `sec:try80_detail` = Sección 3.8, página 68.
  - `fig:try80_loss_terms` = Figura 3.12, página 75.
  - `sec:evaluation_metrics` = Sección 3.9, página 76.
  - `sec:soa_emerging` = Sección 2.6.7, página 33.
  - `sec:city_profile_audit` = Sección 4.2.
  - `tab:try80_val_city_audit` = Tabla 4.1.
  - `tab:try80_test_city_audit` = Tabla 4.2.
  - `tab:try80_final_test_overall` = Tabla 4.13, después de los perfiles
    agrupados.
- Búsquedas de cierre sin coincidencias en capítulos principales:
  `train calibrated`, `The numerical gain`, `fitted CKM result`,
  `UAV-mounted`, `path loss like`, `???`, `TODO`.
