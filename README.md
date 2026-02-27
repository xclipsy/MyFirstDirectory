# 📊 Calculadora de Promedio de Notas en Python

## 📌 Descripción

Este programa en Python permite calcular el promedio de varias notas ingresadas por el usuario desde la consola.

El usuario indica cuántas notas desea promediar, luego ingresa cada nota individualmente y el sistema muestra el promedio final.

---

## 🧠 ¿Cómo funciona?

1. Solicita la cantidad de notas a promediar.
2. Usa un ciclo `while` para pedir cada nota.
3. Acumula las notas en una variable.
4. Calcula el promedio.
5. Muestra el resultado en pantalla.

---

## 💻 Código Fuente

```python
n = float(input("Digite las notas a promediar: "))
suma = 0
i = 1

while i <= n:
    nota = float(input("Ingrese la nota: "))
    suma += nota
    i += 1

promedio = suma / n
print("El promedio de las notas es:", promedio)
```

---

## ▶️ Cómo Ejecutarlo

1. Guarda el archivo como:

```
promedio.py
```

2. Ejecuta en la terminal:

```bash
python promedio.py
```

---

## 📝 Ejemplo de Uso

```
Digite las notas a promediar: 3
Ingrese la nota: 4.5
Ingrese la nota: 3.8
Ingrese la nota: 4.2
El promedio de las notas es: 4.166666666666667
```

---

## ⚠️ Consideraciones

- Se recomienda ingresar un número entero para la cantidad de notas.
- El programa no valida errores (por ejemplo, división entre cero).
- Todas las notas deben ser valores numéricos.

---

## 🚀 Posibles Mejoras

- Agregar validación de datos.
- Manejar errores con `try/except`.
- Redondear el promedio a 2 decimales.
- Mejorar la experiencia del usuario.

---

## 👨‍💻 Autor

Tu Nombre  
Proyecto de práctica en Python.
