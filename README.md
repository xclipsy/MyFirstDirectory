# 📊 Calculadora de Promedios de Estudiantes en Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Descripción

Este programa en **Python** permite registrar las notas de un grupo de estudiantes, calcular el promedio de cada uno y determinar si **aprueba o desaprueba** según su promedio.

Además, al final del proceso muestra:

* ✅ Cantidad de estudiantes **aprobados**
* ❌ Cantidad de estudiantes **desaprobados**
* 📊 **Promedio general del grupo**

Las notas se validan para que estén dentro del rango permitido **(0 a 5)**.

---

## ⚙️ Funcionamiento

El programa realiza los siguientes pasos:

1. Solicita el número total de estudiantes.
2. Para cada estudiante:

   * Pide su **nombre**.
   * Solicita **tres notas**.
3. Verifica que las notas estén entre **0 y 5**.
4. Calcula el **promedio del estudiante**.
5. Determina si el estudiante **aprueba (≥ 3.0)** o **desaprueba (< 3.0)**.
6. Guarda estadísticas del grupo.
7. Al final muestra los resultados generales.

---

## 🧮 Código del Programa

```python
grupo = int(input("Ingrese el numero de estudiantes: "))
promedio_del_grupo = 0.0
aprobado = 0
desaprobado = 0

for i in range(grupo):
    nombre = str(input(f"Ingrese el nombre del estudiante {i + 1}: "))
    
    nota1 = float(input(f"Ingrese la primera nota de {nombre}: "))
    nota2 = float(input(f"Ingrese la segunda nota de {nombre}: "))
    nota3 = float(input(f"Ingrese la tercera nota de {nombre}: "))

    if nota1 < 0 or nota1 > 5 or nota2 < 0 or nota2 > 5 or nota3 < 0 or nota3 > 5:
        print("Error: Las notas deben estar entre 0 y 5. Intente nuevamente.")
        break

    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio de {nombre} es: {promedio:.2f}")

    if promedio >= 3.0:
        print(f"El estudiante {nombre} ha Aprobado")
        aprobado += 1
    else:
        print(f"El estudiante {nombre} ha Desaprobado")
        desaprobado += 1

    promedio_del_grupo += promedio

print(f"Han aprobado {aprobado} estudiantes.")
print(f"Han desaprobado {desaprobado} estudiantes.")
print(f"El promedio general del grupo es: {promedio_del_grupo / grupo:.2f}")
```

---

## 📊 Ejemplo de Ejecución

```
Ingrese el numero de estudiantes: 2

Ingrese el nombre del estudiante 1: Juan
Ingrese la primera nota de Juan: 4
Ingrese la segunda nota de Juan: 3.5
Ingrese la tercera nota de Juan: 4.2
El promedio de Juan es: 3.90
El estudiante Juan ha Aprobado

Ingrese el nombre del estudiante 2: Ana
Ingrese la primera nota de Ana: 2
Ingrese la segunda nota de Ana: 2.5
Ingrese la tercera nota de Ana: 3
El promedio de Ana es: 2.50
El estudiante Ana ha Desaprobado

Han aprobado 1 estudiantes.
Han desaprobado 1 estudiantes.
El promedio general del grupo es: 3.20
```

---

## 🛠 Requisitos

* Python **3.x**
* Terminal o consola para ejecutar el script

---

## ▶️ Cómo ejecutar

1. Guarda el archivo como:

```
promedios_estudiantes.py
```

2. Ejecuta el programa:

```bash
python promedios_estudiantes.py
```

---

## 📚 Conceptos de Python utilizados

* `input()` para entrada de datos
* `for` para iteración
* `if / else` para decisiones
* Validación de datos
* Operadores lógicos
* Formateo de números (`:.2f`)
* Variables acumuladoras

---

## 👨‍💻 Autor

Proyecto educativo realizado para practicar **estructuras de control y manejo de datos en Python**.

---

⭐ Si te sirvió este proyecto, ¡no olvides darle **Star** en GitHub!
