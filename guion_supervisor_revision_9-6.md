# Guion breve para enseñar la revisión al supervisor

## Apertura

He revisado los comentarios de metodología y he hecho una limpieza de estructura, redundancias y notación. La idea principal fue dejar el capítulo como el método final reproducible, no como el historial de desarrollo. El historial queda en el apéndice y aquí solo aparecen las piezas que se usan en el sistema final.

## Página 33

Aquí rehice la entrada del capítulo. Antes quedaba demasiado vacía y además el primer texto era más largo y redundante. Ahora empieza con un resumen directo del flujo final y añadí la Tabla 3.1 como guía del capítulo.

La tabla ya no usa la palabra "contract" y ahora sus filas coinciden con las secciones reales del capítulo, para que sirva como mapa de lectura.

## Página 34

En la figura grande cambié la explicación de "stages" a bloques del flujo. Esto evita que parezca que hay una tubería de entrenamiento por etapas cuando en realidad son bloques de cálculo, priors congelados y modelo residual.

También ajusté la notación visual: máscaras, distancias y ramas LoS/NLoS ahora coinciden mejor con el texto y con el código.

## Página 35

La sección de dataset y split quedó más clara. Ahora separa los campos HDF5, la posición del transmisor, el receptor a 1.5 m y la regla de que los edificios no son receptores.

También moví la discusión de métricas fuera de metodología. Aquí solo dejo la máscara y el split, y la fórmula exacta del RMSE está ahora en resultados.

## Página 37

La sección de framework pasó a ser la 3.2, como sugeriste. Ahora aparece antes de las definiciones de soporte y da la visión global del flujo completo: inputs, mapas derivados, priors, canales de entrada de HARP-Net CKM y outputs.

## Páginas 39 y 40

Limpié la parte de mapas de soporte, máscaras y morfología. La definición de receptores válidos queda ligada a \(\Omega_g\), y las máscaras LoS/NLoS se explican sin repetir la evaluación.

También aclaré la lógica de ray casting para CKMGenerator y la razón de las ventanas morfológicas. En la página 40 añadí la explicación de \(\log(401)\): es una saturación práctica de 400 m de diferencia Tx-Rx, no el máximo real del HDF5. Aunque hay muestras hasta unos 478 m, la cola alta tiene pocos ejemplos después del split por ciudades y regímenes.

## Páginas 41 a 43

Reescribí el overview de priors para que quede claro que "prior" aquí no significa prior bayesiano, sino estimador determinista congelado antes del modelo residual.

Añadí una tabla de notación para evitar ambigüedades: \(\rho\) queda reservado para la amplitud de reflexión LoS, \(\phi\) para la fase de reflexión en radianes, \(\beta_{\mathrm{LoS}}\) para el sesgo LoS, y \(\delta_k\) para densidad local. Así ya no se mezcla la \(b\) de bias con building mask ni con otras cantidades.

## Páginas 44 a 50

En la parte de Channel Attenuation Prior eliminé la repetición de geometría que ya estaba definida antes. Ahora el LoS prior referencia las distancias compartidas y se centra en FSPL, dos rayos, sesgo de altura y residual radial.

También aclaré explícitamente qué es \(\phi\): es el desfase efectivo ajustado del camino reflejado respecto al directo. Esto contesta la duda de si quedaba explicado.

## Páginas 51 a 59

En la rama NLoS quité el lenguaje de "stages" y lo convertí en bloques de cálculo. La rama queda como un prior calibrado con morfología local, obstrucción, elevación y regresión por régimen.

También reduje redundancias: ya no se redefinen geometría y máscaras, sino que se remite a los mapas compartidos. Cambié las densidades locales a \(\delta_{15}\) y \(\delta_{41}\), para que no se confundan con \(\rho\) de la reflexión LoS.

## Páginas 60 a 64

En el prior de delay spread y angular spread quité definiciones repetidas que ya estaban en las secciones compartidas. Ahora se dice que el vector de spread reutiliza esas features comunes y solo se detallan las partes nuevas: regresión ridge, claves de fallback, clipping y transformación inversa.

La idea que quiero transmitir aquí es que DS y AS comparten la misma maquinaria de prior, no dos explicaciones duplicadas.

## Páginas 65 a 72

En la parte de Training and Evaluation Protocol dejé el modelo final más ordenado: nueve canales de entrada, altura como escalar con FiLM, ramas LoS/NLoS, residual acotado y función de pérdida.

También aclaré un punto importante del código: `path_loss_nlos_prior` no significa que el mapa esté puesto a cero fuera de NLoS; es la rama calibrada NLoS, y la selección final la hacen las máscaras explícitas LoS/NLoS.

## Página 73

Moví la fórmula global de RMSE a Resultados. Queda mejor aquí porque es donde se interpretan todas las tablas numéricas.

Ahora el capítulo 4 define que el RMSE es pixel weighted sobre receptores válidos, y esa misma regla se usa para priors y modelo final en PL, DS y AS.

## Cierre

En resumen, he aplicado tus comentarios en cuatro líneas: reduje redundancias, moví la métrica al lugar donde se reportan los resultados, corregí la estructura de secciones, y revisé la notación para que sea consistente con el código y con los priors reales. La versión compilada ya está actualizada y no tiene referencias rotas.
