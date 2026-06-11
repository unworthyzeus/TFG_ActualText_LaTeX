# Nota sobre la actualización final de métricas 11/06/2026

Tras el rerun final de métricas en el split de test, los números reportados
cambian ligeramente respecto a la versión anterior. El cambio no viene de una
modificación conceptual del modelo, sino de usar la política final de rangos en
la evaluación:

- En path loss se eliminó el límite antiguo de 180 dB, que podía recortar valores
  válidos altos. El guard final queda en 185 dB, por encima del rango observado
  de receptores válidos, por lo que solo evita salidas físicamente fuera de
  rango y no perjudica valores válidos.
- En delay spread se usa el rango final hasta 910 ns, coherente con el rango
  físico usado para decodificar y evaluar el objetivo.
- Angular spread mantiene la misma interpretación de grados y no cambia por un
  nuevo límite de rango.

Por eso los resultados se mueven poco, alrededor de unas centésimas en path loss
y angular spread, y algo más en delay spread. La versión revisada debe usar
siempre los números finales siguientes.

| Target | Métrica | Antes | Final |
|---|---:|---:|---:|
| Path loss | Model RMSE | 1.6519 dB | 1.6737 dB |
| Path loss | Prior RMSE | 1.9383 dB | 1.9383 dB |
| Path loss | Delta RMSE | -0.2865 dB | -0.2646 dB |
| Path loss | Model MapCorr | 0.962556 | 0.961729 |
| Delay spread | Model RMSE | 26.5570 ns | 26.6888 ns |
| Delay spread | Prior RMSE | 28.1023 ns | 28.1211 ns |
| Delay spread | Delta RMSE | -1.5453 ns | -1.4323 ns |
| Delay spread | Model MapCorr | 0.415482 | 0.415563 |
| Angular spread | Model RMSE | 11.3854 deg | 11.4002 deg |
| Angular spread | Prior RMSE | 13.7416 deg | 13.7416 deg |
| Angular spread | Delta RMSE | -2.3562 deg | -2.3414 deg |
| Angular spread | Model MapCorr | 0.592630 | 0.593148 |

Los ficheros fuente de la tesis y del paper se actualizaron para que las tablas,
las conclusiones y el resumen usen estos valores finales.
