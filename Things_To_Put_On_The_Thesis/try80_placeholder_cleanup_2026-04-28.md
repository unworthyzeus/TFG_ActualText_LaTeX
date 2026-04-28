# Try 80 placeholder cleanup - 2026-04-28

Checkpoint usado: `C:\TFG\TFGPractice\cluster_outputs\TFGEightiethTry80\try80_joint_huge_pathloss_finetune\best_model.pt`.

Artefactos usados:

- `deep_breakdown_try80_best_model_all_and_unseen_test.json`
- `deep_breakdown_try80_best_model_test_unseen_only.json`
- `deep_breakdown_try80_best_model_validation_only.json`
- `deep_breakdown_try80_best_model_train_only.json`
- `try80_comparison_report.md`
- `try80_comparison_summary.json`
- `try80_comparison_split_global.csv`
- `try80_comparison_subexperts.csv`
- `try80_comparison_cities.csv`
- `try80_comparison_city_subexperts.csv`

## Placeholders eliminados en el TFG

| Archivo | Placeholder visto | Cambio aplicado |
| --- | --- | --- |
| `TFG/summary.tex` | Try 80 aparecia como extension en curso en los tres resumenes. | Sustituido por el checkpoint final: 1.65 dB PL, 26.56 ns DS y 11.39 grados AS en ciudades de test no vistas. |
| `TFG/introduction.tex` | El outline decia que resultados incluia el "Try 80 validation snapshot". | Cambiado a evaluacion final de Try 80 sobre ciudades no vistas. |
| `TFG/results.tex` | Cabecera: Try 80 "in-flight" y snapshot de validacion. | Reescrito para decir que Try 80 es el modelo final prior-anchored, evaluado en 2590 muestras de 14 ciudades de test no vistas. |
| `TFG/results.tex` | Fila de cronologia: "Validation snapshot ... final test pending". | Cambiada por resultados finales de test para PL, DS y AS. |
| `TFG/results.tex` | Tabla de evolucion RMSE: fila "Try 80 validation" no final. | Cambiada por fila "Try 80 final test" con los tres outputs. |
| `TFG/results.tex` | `tab:try80_placeholder` con valores de validacion. | Sustituida por tablas finales: test global, LoS/NLoS, comparacion train/val/test/all y subexpertos. |
| `TFG/results.tex` | `fig:try80_val_placeholder` con barras de validacion. | Sustituida por grafico TikZ de barras con RMSE finales de test contra los priors. |
| `TFG/results.tex` | Texto de historia de entrenamiento y caption decian que era placeholder. | Reescrito como diagnostico de entrenamiento; la claim final queda en las tablas de test. |
| `TFG/results.tex` | Limitaciones decia que faltaba checkpoint congelado y evaluacion final. | Cambiado por caveat correcto: single seed, city-holdout y simulador; no field measurements. |
| `TFG/state_of_art.tex` | Fila Try 80: 1.77 dB validation snapshot; final test pending. | Cambiada por 1.65 dB en ciudades de test no vistas y nota de mejora tambien en DS/AS. |
| `TFG/conclusions.tex` | Try 80 quedaba como extension in-flight hasta congelar checkpoint. | Cambiado por resultado final: 1.6519 dB PL, 26.5570 ns DS y 11.3854 grados AS. |
| `TFG/appendices.tex` | "near-final huge checkpoint" en paneles. | Cambiado a checkpoint final. |
| `TFG/appendices.tex` | Capitulo `Final-Result Placeholder`. | Sustituido por `Final Try 80 Evaluation Artifacts`, con lista de JSON/CSV/MD de auditoria. |
| `TFG/sustainability.tex` | Decia que los resultados finales Try 80 quedaban como placeholders. | Cambiado por caveat de alcance: generalizacion en simulador a ciudades no vistas, no despliegue real certificado. |

## Placeholders vistos en `.md`

Estos `.md` son notas historicas de planificacion/auditoria. No los he borrado para no perder trazabilidad; este archivo los supersede para Try 80 final.

| Archivo | Lineas vistas | Nota |
| --- | --- | --- |
| `Things_To_Put_On_The_Thesis/per_city_holdout_and_try80_freeze.md` | 1, 14, 22, 26-43 | Lista antigua de acciones: congelar checkpoint, exportar test, reemplazar placeholders o reformular como in-flight. |
| `Things_To_Put_On_The_Thesis/static_audit_2026-04-26.md` | 30 | Avisaba que seguian placeholders Try 80 en `results.tex`, `appendices.tex`, `summary.tex` y `conclusions.tex`. |
| `Things_To_Put_On_The_Thesis/summary.md` | 43 | Instruccion antigua: dejar resultados finales de Try 80 como placeholders porque el modelo seguia entrenando. |
| `Things_To_Put_On_The_Thesis/thesis_completion_checklist.md` | 8, 44 | Checklist con Try 80 pendiente de confirmacion y resultados finales como placeholders. |
| `Things_To_Put_On_The_Thesis/things_to_fix_and_what_I_said.md` | 5, 42, 49, 72, 104 | Notas antiguas sobre leakage de placeholders, fila Try 80 en SOTA, capitulo final placeholder y peticion anterior de no tocar todavia el placeholder final. |
| `Things_To_Put_On_The_Thesis/title_reframing_note.md` | 10 | Nota de framing: Try 80 como extension neural prior-anchored. No es placeholder critico. |

## Resultado final incorporado

El TFG ahora separa explicitamente el resultado final de test del resto:

- Test split: 2590 muestras, 14 ciudades no vistas.
- Train/val/test/all: comparacion contra prior para los 3 outputs.
- LoS/NLoS: desglose de RMSE en test.
- Subexpertos del prior: tabla global all-city por los 9 subexpertos.
- Formula: `model_rmse` es el RMSE de un output concreto, no la suma de PL + DS + AS.

La interpretacion de delay spread queda en `results.tex`: mejora RMSE aunque empeore un poco MAE porque se eliminan alucinaciones/artefactos altos de delay spread que pesan mucho en error cuadratico; el incremento medio de MAE es pequeno y no cambia la utilidad practica de los mapas.
