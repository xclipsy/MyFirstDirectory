# 🛒 Sistema de Inventario de Supermercado (Python)

Este programa interactivo en **Python** permite gestionar el inventario de un supermercado mediante un menú de opciones. El sistema permite registrar múltiples productos, validando que las cantidades y precios ingresados sean valores numéricos correctos, guardando todo en una estructura de lista con diccionarios.

## 📁 Archivos del Proyecto

El proyecto solo necesita un archivo principal:

📦 inventario-supermercado
 ┣ 📜 main.py
 ┗ 📜 README.md

| Archivo | Descripción |
| :--- | :--- |
| `main.py` | Contiene el código principal y la lógica del menú interactivo |
| `README.md` | Documentación del proyecto |

## ⚙️ Requisitos

Para ejecutar este programa necesitas:
* Python 3.12 o superior (requerido para el formateo f-string avanzado)
* Un intérprete de Python instalado en el sistema
* Terminal o consola para ejecutar el programa

Puedes verificar tu versión de Python en la consola con:
`python --version` o `python3 --version`

## ▶️ Cómo Ejecutar el Programa

1. Descarga o clona el repositorio.
`git clone https://github.com/tu-usuario/inventario-supermercado.git`

2. Entra en la carpeta del proyecto.
`cd inventario-supermercado`

3. Ejecuta el archivo principal.
`python main.py`

## 📌 Características

El programa despliega un menú interactivo con las siguientes opciones:
1. **Agregar un producto:** Permite registrar nombre, cantidad y precio, almacenándolos como un diccionario. Pregunta si se desea añadir otro producto sin salir de la opción.
2. **Mostrar inventario:** Recorre la lista de productos y los muestra con un formato claro. Detecta si el inventario está vacío.
3. **Calcular estadísticas:** Calcula y muestra el valor total acumulado del inventario y la cantidad de tipos de productos registrados.
4. **Salir:** Finaliza la ejecución del bucle principal.

*Nota:* El programa incluye mensajes de error personalizados para guiar al usuario cuando ingresa datos erróneos.

## 🛡️ Validaciones Implementadas

### Validación de Cantidad (Números Enteros)
Se usa `.isdigit()` para asegurar que el valor ingresado sea un número entero y mayor a 0.

### Validación de Precio (Números Decimales)
Se usa `.replace('.', '', 1).isdigit()` para permitir números de punto flotante válidos y mayores a 0.

*Ambas validaciones evitan que el programa colapse si el usuario ingresa letras, valores vacíos o números negativos.*

## 💻 Ejemplo de Ejecución

```text
Bienvenido al Inventario del supermercado :)
Menu de opciones
1. Agregar un producto
2. Mostrar inventario
3. Calcular estadisticas
4. Salir
¿Que opcion le gustaria hacer?: 1

Ingrese el nombre del producto: Arepa
Ingrese la cantidad del producto: diez
ven aca, cuando has visto tu que una cantidad sea 'diez', colocame un numero entero valido
Ingrese la cantidad del producto: 10
Ingrese el precio del producto: 2.50
¿Desea agregar otro producto? (si/no): no
```
## 👨‍💻 Autor

Luis Guerrero  
Inventory.py
