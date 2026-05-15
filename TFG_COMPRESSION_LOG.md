# Registro de compresion del TFG

Fecha: 2026-05-15

Este archivo deja constancia de que se ha movido, comprimido o sacado del PDF
compilado al convertir el TFG reducido largo en una version mucho mas cercana a
un paper, pero sin perder el argumento tecnico central.

Nota actualizada: despues de ajustar el objetivo al entorno de 120 paginas, la
version compilada activa ya no es la version ultracompacta. Se han restaurado
capitulos largos donde aportaban valor tecnico y se ha mantenido compacto solo
lo que duplicaba contenido o funcionaba mejor como material de repositorio.

## Resultado actual

- El PDF compilado activo queda en 119 paginas A4.
- No se ha tocado `.gitignore` para ocultar el TFG.
- No se han borrado del repositorio los capitulos compactos ni largos.
- `reduced/TFG/TFG.tex` compila ahora:
  - `introduction.tex`
  - `state_of_art.tex`
  - `methodology.tex`
  - `results.tex`
  - `sustainability_balanced.tex`
  - `conclusions.tex`
  - `appendices_compact.tex`
- Los archivos alternativos quedan como respaldo, notas de recorte o material
  extendido:
  - `introduction_compact.tex`
  - `state_of_art.tex`
  - `state_of_art_compact.tex`
  - `methodology.tex`
  - `methodology_compact.tex`
  - `results.tex`
  - `results_compact.tex`
  - `sustainability.tex`
  - `sustainability_compact.tex`
  - `conclusions_compact.tex`
  - `appendices.tex`
  - `appendices_compact.tex`
  - `prior_detail_try78.tex`
  - `prior_detail_try79.tex`
  - `prior_detail_try80.tex`

## Expansion a objetivo cercano a 120 paginas

Fecha: 2026-05-15

Tras revisar que el supervisor esperaba una memoria alrededor de 120 paginas, se
deshizo parte de la compresion mas agresiva:

- Se restauro la introduccion larga para recuperar contexto, objetivos,
  planificacion y narrativa de proyecto.
- Se restauro el estado del arte largo porque la version paper era demasiado
  seca para una memoria de TFG.
- Se restauro la metodologia larga, incluyendo el detalle de priors Try 78,
  Try 79 y Try 80, la separacion LoS/NLoS, la dependencia con altura y la GMM
  head residual.
- Se restauro el capitulo de resultados largo, con mas evolucion experimental
  y mas soporte para justificar el modelo final.
- Se restauro la conclusion larga y se dejo una sostenibilidad equilibrada:
  mas completa que la version compacta, pero menos extensa que el bloque
  original completo para mantener el PDF por debajo de 120 paginas.
- Se amplio el apendice compacto con tres paneles representativos
  (Segovia open/low, Nice mixed/mid y Tunis dense/mid) y con la figura de
  cuantizacion de spreads. No se recupero la galeria completa ni el manual
  entero del CKM Generator porque duplican material disponible en el repositorio.

## Criterio de compresion

Se ha usado el paper como referencia estructural: secciones compactas, menos
tablas repetidas, mas foco en la contribucion final y detalle tecnico solo
donde sostiene el modelo final. La tesis mantiene mas explicacion metodologica
que el paper, especialmente en priors, dependencia con altura, separacion
LoS/NLoS y funcionamiento de la GMM head residual.

No se ha intentado destruir contenido importante. Parte del material sale del
PDF compilado, pero queda en fuentes LaTeX, imagenes, logs o repositorios para
poder recuperarlo si hace falta.

## Movido fuera del flujo compilado

- Las derivaciones largas de los priors Try 78, Try 79 y Try 80 salen del
  capitulo metodologico compilado. Siguen en:
  - `reduced/TFG/prior_detail_try78.tex`
  - `reduced/TFG/prior_detail_try79.tex`
  - `reduced/TFG/prior_detail_try80.tex`
- El log completo de 80 intentos sale del PDF. Se mantiene en
  `reduced/TFG/appendices.tex`.
- El manual largo del CKM Generator, con formato mas de guia de uso y capturas,
  sale del apendice compilado. El apendice compacto conserva el contrato de
  reproducibilidad, entradas/salidas, pixeles por metro, politica de mascaras,
  mixed precision y rutas de repositorio. La version larga sigue en
  `reduced/TFG/appendices.tex` y en el README del generador.
- La galeria cualitativa completa sale del PDF. Se mantienen tres paneles
  representativos:
  - open/low Segovia, `sample_13213`
  - mixed/mid Nice, `sample_10828`
  - dense/mid Tunis, `sample_14651`
  El resto de paneles y su manifest quedan en
  `reduced/TFG/img/thesis_figures/try80_appendix_panels/`.
- Las filas detalladas por ciudad/subexperto, algunos graficos de splits y
  tablas diagnosticas demasiado grandes salen del capitulo de resultados
  compilado. Siguen en el `results.tex` original, imagenes generadas y outputs
  de experimentos.

## Comprimido, no eliminado

- El estado del arte pasa de una revision enciclopedica a una seccion tipo
  paper. La version compacta conserva:
  - cautelas de comparacion justa;
  - familias de metodos relacionados;
  - comparacion con metricas cercanas de path loss;
  - por que esta tesis no es directamente equivalente: city holdout estricto,
    UAV centrado con altura variable, mapas densos 513x513 y prediccion conjunta
    de PL/DS/AS.
- La metodologia pasa de narrar muchos callejones a conservar solo la evolucion
  que justifica el modelo final:
  - primeras redes image-to-image;
  - reset metodologico del ground mask;
  - PMNet/PMHHNet residual;
  - leccion distribution-first con GMM;
  - priors calibrados congelados;
  - modelo final prior-anchored residual GMM.
- La explicacion de priors sigue siendo detallada, pero mas concentrada:
  - el prior LoS de path loss conserva FSPL, termino two-ray coherente,
    calibracion por bins de altura, residual radial suavizado e interpolacion
    con la altura real del UAV;
  - el prior NLoS conserva envolvente COST/A2G, vector de features `x_78`,
    terminos de morfologia/altura/visibilidad y calibracion OLS;
  - los priors de delay/angular spread conservan transformada `log(1+y)`,
    motivacion spike-plus-tail, vector `x_79`, calibracion ridge y estructura
    de fallbacks por regimen;
  - se aclaran los 114 regimenes como 57 claves por metrica, no como una unica
    multiplicacion cartesiana directa.
- La GMM head final conserva los puntos importantes:
  - los mapas de prior congelado entran como canales;
  - la altura del UAV se codifica y se inyecta con FiLM;
  - la red predice distribuciones residuales alrededor de los priors;
  - las medias de mezcla estan ancladas al prior y acotadas por residual caps;
  - el mapa determinista para metricas es la esperanza de la mezcla;
  - la loss mantiene NLL, moment matching, prior anchor, prior guard, outlier
    budget y terminos deterministas RMSE/MAE.
- El contrato de dataset/evaluacion se comprime pero queda explicito:
  - grid 513x513;
  - 1 m/pixel;
  - antena UAV centrada horizontalmente;
  - altura de antena UAV variable por muestra;
  - un receptor en cada pixel que no sea edificio;
  - receptor fijo a 1.5 m;
  - pixeles de edificio excluidos de loss y metricas;
  - city holdout estricto.
- Resultados se fusionan en menos tablas, pero mas densas:
  - modelo final vs prior congelado;
  - LoS/NLoS;
  - sanity check validation/test;
  - auditoria por altura/topologia;
  - auditoria compacta de splits/grupos;
  - comparacion SOA;
  - runtime.

## Sacado del PDF compilado

Estos elementos se han sacado del PDF, pero no del repositorio:

- Tablas completas fila a fila de los 80 intentos.
- Tablas repetidas que demostraban el mismo resultado final desde angulos muy
  parecidos.
- Galeria cualitativa completa mas alla de los tres paneles representativos.
- Manual largo con capturas del CKM Generator.
- Apendices de derivacion larga que duplicaban formulas compactas.
- Tablas diagnosticas enormes por ciudad/subexperto cuyo mensaje principal
  queda resumido en las tablas compactas.
- Panel open/high Nazareth de angular spread, porque el AS de ground truth queda
  casi plano y la escala robusta colapsa a un rango cercano a cero, generando
  una visualizacion enganosa.

## Claims tecnicos preservados

La reduccion no cambia la metodologia experimental de fondo:

- mismo dataset CKM;
- misma idea de city holdout;
- mismo ground-only receiver mask;
- mismo pipeline final Try 80;
- mismos priors Try 78/79 congelados como fuente de los mapas de prior finales;
- mismos resultados globales reportados;
- misma aclaracion de hardware de runtime: AMD Ryzen 5 5600H y NVIDIA RTX 3050
  Ti Laptop GPU.

Lo que si cambia es el encuadre metodologico:

- Estilo anterior: "esta fue toda la evolucion, incluidas muchas lecciones
  intermedias y callejones".
- Estilo compacto: "esta es la ruta que justifica la evidencia final, con la
  evolucion suficiente para explicar por que Try 80 es el punto de llegada".

## Si hay que reducir todavia mas

- La tesis compacta ya esta cerca de formato paper con apendice. Recortar mucho
  mas deberia afectar a front matter, paneles de apendice o tablas de resultados
  antes que al bloque de priors/GMM.
- La explicacion de priors y GMM head es ahora el principal portador de novedad.
  Cortarla mucho mas haria que el resultado parezca mas black-box.
- El SOA debe quedarse compacto: expandirlo recuperaria paginas rapido sin
  reforzar demasiado la claim final.
- Los proximos cortes menos peligrosos serian:
  - dejar solo el panel de Tunis;
  - mover la auditoria residual compacta fuera del PDF;
  - mover el apendice del CKM Generator entero al README;
  - acortar front matter o formato de bibliografia si la normativa lo permite.

## Segunda pasada de compresion

Fecha: 2026-05-15

Tras releer el paper, se aplico una segunda compresion para que el TFG reducido
se pareciera aun mas a una memoria-paper. El criterio fue no tocar el nucleo de
novedad tecnica (priors Try 78/79, GMM head Try 80, resultados globales y
LoS/NLoS), y recortar material administrativo o visual que ya queda en el repo.

Cambios aplicados:

- `TFG.tex` pasa a compilar tambien:
  - `introduction_compact.tex`
  - `sustainability_compact.tex`
  - `conclusions_compact.tex`
- La introduccion compacta elimina el Gantt del PDF y deja el plan como ruta
  metodologica en texto. El Gantt completo sigue en `introduction.tex`.
- Sostenibilidad se comprime a una matriz y dos parrafos de alcance etico/SDG.
  La tabla economica larga y el desglose ambiental detallado siguen en
  `sustainability.tex`.
- Conclusiones se comprimen siguiendo el cierre del paper: resultado final,
  respuestas a RQ1/RQ2/RQ3, contribuciones, negativos importantes y futuro.
  La version larga sigue en `conclusions.tex`.
- El apendice de paneles pasa de tres paneles completos a un solo panel PDF:
  Tunis dense/mid. Segovia open/low y Nice mixed/mid quedan referenciados en la
  tabla y disponibles en la carpeta de imagenes.
- Appendix D conserva la figura de distribucion GMM y deja la cuantizacion de
  spreads como registro textual/archivo disponible, porque la explicacion ya
  esta en Results.

Resultado de esta pasada: el PDF reducido baja de 50 paginas a 39 paginas.

## Pasada de maquetacion: 119 a 114 paginas

Fecha: 2026-05-15

Despues de volver a una memoria extensa cercana a 120 paginas, se hizo una
pasada de maquetacion para recuperar paginas sin recortar contenido tecnico.
El objetivo fue aprovechar mejor el espacio disponible, no volver a comprimir
SOA, metodologia o resultados.

Cambios aplicados:

- Se elimino la pagina final artificial en blanco del template.
- La bibliografia y el back matter vuelven a usar espaciado compacto.
- Las tablas y figuras de metodologia/resultados dejaron de estar forzadas con
  `[H]` y pasaron a `[!htbp]`, permitiendo que LaTeX rellene huecos grandes.
- Los apendices conservan las letras A/B/C/D, pero usan encabezados compactos
  en lugar de `\chapter` completo para cada bloque corto.
- Las dos figuras diagnosticas del Appendix D se agruparon en una figura
  compuesta con subfiguras.
- La bibliografia se compacto con fuente `small` y menor separacion entre
  entradas.
- La lista de acronimos se compacto ligeramente; no cambio su contenido.

Resultado actual de esta pasada: el PDF activo compila en 114 paginas A4, sin
citas o referencias indefinidas y sin `Overfull \hbox`. La reduccion de paginas
respecto a la version de 119 paginas es puramente de maquetacion.

## Restauracion de Appendix C: CKMGenerator

Fecha: 2026-05-15

Se detecto que la pasada de maquetacion habia dejado CKMGenerator demasiado
compactado: aparecia como una tabla de contrato, no como un apendice real. Se
restauro un Appendix C con estilo de TFG antiguo y con contenido suficiente para
que la herramienta quede defendible sin pegar el README completo.

Cambios aplicados:

- Los apendices vuelven a usar `\chapter{...}` bajo `\appendix`, por lo que el
  PDF recupera el estilo visual antiguo de apendices A/B/C/D.
- `TFG.tex` activa `\userelaxedappendixspacing` antes de los apendices.
- Appendix C pasa a llamarse `CKMGenerator Interface and Reproducibility Tool`
  y se expande con:
  - finalidad y repositorios fuente;
  - modos Streamlit/CLI;
  - ejemplos de ejecucion;
  - contrato de inputs;
  - ajuste a la malla `513x513` de `1 m/pixel`;
  - convencion de antena centrada, altura UAV variable y Rx en cada pixel de
    suelo a `1.5 m`;
  - politicas de mascaras LoS/NLoS;
  - ruta prior + modelo residual GMM;
  - outputs numericos/visuales, metadata, runtime y mixed precision.
- Se mantiene una version media: mas completa que la tabla compacta, pero no el
  manual completo de `appendices.tex`, que sigue siendo material de README/repo.
- Se anadio `\label{chap:methodology}` para resolver la referencia cruzada
  desde el nuevo Appendix C.

Resultado actual: `reduced/TFG/TFG.pdf` compila en 120 paginas A4, sin
referencias indefinidas ni `Overfull \hbox`. El fichero PDF sigue sin estar
ignorado por Git.

## Ajuste visual de figuras CKMGenerator

Fecha: 2026-05-15

Tras revisar el PDF, la figura compuesta inicial de CKMGenerator no era
legible: el screenshot de controles tenia demasiada zona blanca y la sidebar se
veia demasiado pequena. Ademas no estaban incluidas todas las capturas
disponibles en `img/thesis_figures/ckm_generator/`.

Cambios aplicados:

- La captura de controles se muestra recortada a la sidebar para que sea
  legible.
- Se anade una nota aclarando que esa captura corresponde a una posicion de
  scroll de la sidebar; los controles superiores quedan descritos en texto y en
  los ejemplos CLI.
- Se incluyen las seis capturas disponibles:
  - controles de Streamlit;
  - resumen de ejecucion de la app;
  - prediccion conjunta PL/DS/AS;
  - productos visuales guardados;
  - arbol de outputs;
  - metadata y contenido del `.npz`.

Resultado actual: el PDF compila en 123 paginas A4, sin referencias indefinidas
ni `Overfull \hbox`. El aumento de paginas es deliberado para que las figuras
del Appendix C sean legibles y completas.

## Rebalance final de apendices A/C/D

Fecha: 2026-05-15

Se ajustaron los apendices tras la revision visual del PDF y las capturas nuevas
de CKMGenerator.

Cambios aplicados:

- Appendix A se expandio con notas de fase mas narrativas y despues se compacto
  localmente en fuente `small`: se mantiene la evolucion que justifica el modelo
  final, pero sin volver al registro completo de 80 intentos ni dejar una pagina
  final casi vacia.
- Appendix C mantiene el estilo antiguo de apendice y usa la captura final
  `img/thesis_figures/ckm_generator/1CKM.png` para documentar los controles de
  CKMGenerator. Se retiraron los composites temporales y las capturas generadas
  automaticamente que no quedaban bien.
- Appendix D se comprimio deliberadamente a una pagina: conserva dos figuras
  diagnosticas y envia la galeria completa, el log fila a fila y trazas largas
  al repositorio.
- Appendix C tambien se compacto localmente en fuente `small`, eliminando la
  pagina final que solo contenia el cierre del texto de runtime.
- Se verifico que la figura C.1 aparece en la pagina 118 del PDF, Appendix C
  termina en la pagina 122 y Appendix D queda en la pagina 123.

Resultado actual: `reduced/TFG/TFG.pdf` compila en 123 paginas A4, sin
referencias indefinidas ni aviso de rerun de referencias. El unico aviso global
persistente es el recordatorio de MiKTeX sobre actualizaciones.
