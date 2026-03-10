# 🦈 Estadísticas del Yuyu (Junior Edition)

Sencillo script en **Python** para gestionar y visualizar el rendimiento del "Tiburón". Este programa permite calcular puntos y balance de goles basándose en los resultados de los partidos ingresados.

---

## 💻 Entrada de Datos
El sistema interactúa con el usuario de la siguiente manera:
1. **Cantidad de partidos:** Introduce el número total de encuentros a evaluar.
2. **Registro por partido:** Por cada partido, el sistema te pedirá ingresar:
   * ⚽ **Goles a favor (GF)**
   * ⚽ **Goles en contra (GC)**

## 📊 Resultados
Al finalizar el ciclo de ingresos, el programa imprimirá automáticamente un resumen con:
* El total de **puntos** obtenidos.
* El total de **goles a favor**.
* El total de **goles en contra**.
* La **diferencia de goles** final.

---

## 📈 Lógica de Cálculo
El programa utiliza una estructura de control `if-elif` para determinar el resultado de cada encuentro y asignar el puntaje correspondiente:

> [!IMPORTANT]
> * **Victoria:** $gf > gc$ (Suma 3 puntos)
> * **Empate:** $gf == gc$ (Suma 1 punto)
> * **Derrota:** $gf < gc$ (Suma 0 puntos)

La fórmula utilizada para el balance es:
$$DG = GF - GC$$

---

## ⚙️ Requisitos
* **Lenguaje:** Python 3.x
* **Pasión:** Un corazón rojiblanco 🔴⚪

---
*Desarrollado para el análisis rápido de jornadas deportivas.*
