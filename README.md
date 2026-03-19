# 🎮 Juego de Trivia en Python (API & CSV)

Este es un juego de trivia interactivo desarrollado en Python por consola. El programa extrae preguntas dinámicamente desde un archivo JSON alojado en la web, evalúa las respuestas del jugador en tiempo real y guarda el historial de puntuaciones utilizando manejo de archivos CSV.

## 🚀 Características Principales

* **Consumo de Datos Web:** Utiliza la librería `requests` para obtener un banco de preguntas en formato JSON desde un repositorio remoto.
* **Preguntas Aleatorias:** Selecciona 5 preguntas al azar en cada partida usando la librería `random`, asegurando que cada juego sea único.
* **Sistema de Puntuación:** Otorga 20 puntos por cada respuesta correcta (A, B, C o D) y muestra un resumen al finalizar.
* **Registro de Historial:** Guarda el nombre del jugador, su puntaje y la fecha/hora exacta de la partida en un archivo `top10.csv`.
* **Lectura de Datos:** Al finalizar, lee el archivo CSV para mostrar el historial de todos los jugadores que han participado.

## 📁 Estructura del Proyecto
```text
📦 trivia-game
 ┣ 📜 Trivia.py   # Código principal del juego
 ┣ 📜 top10.csv   # Base de datos local generada automáticamente (Historial)
 ┗ 📜 README.md   # Documentación del proyecto
```
## ⚙️ Requisitos y Dependencias

Este proyecto utiliza librerías nativas de Python (`random`, `csv`, `datetime`), pero requiere instalar la librería externa `requests` para hacer las peticiones HTTP.

Puedes instalarla ejecutando el siguiente comando en tu terminal:
```bash
pip install requests
```

## ▶️ Cómo Jugar

1. Clona este repositorio o descarga los archivos.
2. Abre tu terminal y navega hasta la carpeta del proyecto.
3. Ejecuta el archivo principal:
```bash
python Trivia.py
```
4. Ingresa tu nombre, lee atentamente la categoría de cada pregunta y selecciona la letra correcta (A, B, C o D). *¡No te preocupes por las mayúsculas o minúsculas, el sistema lo ajusta automáticamente!*

## 💻 Ejemplo de Ejecución

```text
Ingrese su nombre para empezar: Luis
Bienvenido a la trivia
Responde las preguntas de forma correcta para obtener puntos, 
de ser incorrectas, no sumaran a tu puntaje

Categoria: Historia
Pregunta: ¿En qué año descubrió Colón América?
A) 1492
B) 1512
C) 1498
D) 1500

Ingrese su respuesta: a
La respuesta correcta es: A
Respuesta correcta
...
...
Su puntaje obtenido fue de: 80, 
y la cantidad de respuestas correctas fue 4 eres cule malo

El Usuario: Luis Obtuvo: 80 Puntos A la Fecha y Hora: 2026-03-19 17:25:30.123456
```

## 🧠 Autor

**Luis Guerrero**
