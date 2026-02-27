📘 Calculadora de Promedio de Notas
📌 Descripción

Este programa en Python permite calcular el promedio de un conjunto de notas ingresadas por el usuario desde la consola.

El usuario primero indica cuántas notas desea promediar y luego ingresa cada una de ellas. Finalmente, el sistema muestra el promedio calculado.

🚀 Funcionamiento

El programa solicita cuántas notas se van a ingresar.

Se ingresan las notas una por una.

El sistema suma todas las notas.

Calcula el promedio.

Muestra el resultado en pantalla.

🧮 Código del Programa
n = float(input("Digite las notas a promediar: "))
suma = 0
i = 1
while i <= n:
    nota = float(input("Ingrese la nota: "))
    suma += nota
    i += 1
promedio = suma / n
print("El promedio de las notas es:", promedio)
▶️ Cómo Ejecutarlo

Asegúrate de tener instalado Python 3.

Guarda el archivo como:

promedio.py

Ejecuta el programa en la terminal:

python promedio.py

o

python3 promedio.py
📋 Ejemplo de Uso
Digite las notas a promediar: 3
Ingrese la nota: 4.5
Ingrese la nota: 3.8
Ingrese la nota: 4.2
El promedio de las notas es: 4.166666666666667
⚠️ Consideraciones

El programa no valida si el número de notas es cero.

Se recomienda ingresar un número entero para la cantidad de notas.

Todas las notas deben ser valores numéricos.

📦 Requisitos

Python 3.x

Si quieres, puedo mejorarlo agregándole:

✔ Validación de errores

✔ Manejo de excepciones

✔ Versión más optimizada

✔ Interfaz gráfica