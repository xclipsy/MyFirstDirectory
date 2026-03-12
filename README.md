# 📊 Calculadora de Promedio de Notas (Python)

Este programa en **Python** permite calcular el **promedio de varias notas ingresadas por el usuario**.
Primero se solicita la cantidad de notas que se desean promediar y luego se ingresan una por una para finalmente calcular el promedio.

---

# 📁 Archivos del Proyecto

El proyecto requiere únicamente los siguientes archivos:

```
📦 promedio-notas
 ┣ 📜 main.py
 ┗ 📜 README.md
```

### Descripción

| Archivo     | Descripción                                               |
| ----------- | --------------------------------------------------------- |
| `main.py`   | Contiene el programa que calcula el promedio de las notas |
| `README.md` | Documentación del proyecto                                |

---

# ⚙️ Requisitos

Para ejecutar este programa necesitas:

* **Python 3.8 o superior**
* Una terminal o consola
* Un editor de código opcional (Visual Studio Code, PyCharm, etc.)

Puedes verificar tu versión de Python con:

```bash
python --version
```

o

```bash
python3 --version
```

---

# ▶️ Cómo Ejecutar el Programa

1. Descarga o clona el repositorio.

```bash
git clone https://github.com/tu-usuario/promedio-notas.git
```

2. Entra en la carpeta del proyecto.

```bash
cd promedio-notas
```

3. Ejecuta el programa.

```bash
python main.py
```

---

# 📌 Funcionamiento del Programa

El programa sigue estos pasos:

1. Solicita al usuario la **cantidad de notas** que desea promediar.
2. Utiliza un **ciclo `while`** para ingresar cada nota.
3. Acumula las notas en una variable llamada `suma`.
4. Calcula el promedio usando la fórmula:

```
promedio = suma / n
```

5. Finalmente muestra el resultado en pantalla.

---

# 🔁 Uso del Ciclo `while`

El programa utiliza un ciclo `while` para repetir el ingreso de notas hasta alcanzar la cantidad indicada por el usuario.

```python
while i <= n:
```

Esto permite controlar cuántas notas se ingresan.

---

# 💻 Ejemplo de Ejecución

```
Digite las notas a promediar: 3
Ingrese la nota: 4.0
Ingrese la nota: 3.5
Ingrese la nota: 5.0

El promedio de las notas es: 4.166666666666667
```

---

# 📂 Código del Programa

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

# 🧠 Autor

**Luis José Guerrero Bruges**
Desarrollador en formación y escritor.




---

