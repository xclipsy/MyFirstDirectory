# 🧾 Calculadora de Costo de Producto (Python)

Este programa en **Python** permite ingresar información de un producto y calcular su costo total.
El sistema valida que la **cantidad** y el **precio** ingresados sean valores numéricos válidos antes de realizar el cálculo.

---

## 📌 Características

* Solicita al usuario:

  * Nombre del producto
  * Cantidad del producto
  * Precio del producto
* Valida que:

  * La **cantidad** sea un número entero positivo.
  * El **precio** sea un número positivo (permite decimales).
* Calcula automáticamente el **costo total**.
* Muestra un resumen con la información ingresada.

---

## ⚙️ Funcionamiento del Programa

1. El programa solicita el **nombre del producto**.
2. Luego pide la **cantidad**, validando que sea un número entero positivo.
3. Después solicita el **precio**, permitiendo números decimales positivos.
4. Cuando los datos son válidos, calcula:

```
costo_total = cantidad_producto * precios_producto
```

5. Finalmente muestra la información del producto y el total.

---

## 🛡️ Validaciones Implementadas

### Validación de Cantidad

Se usa `.isdigit()` para asegurar que el valor ingresado sea un número entero positivo.

```python
if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
```

Esto evita que el usuario ingrese:

* letras
* números negativos
* valores vacíos

---

### Validación de Precio

Se utiliza `.replace('.', '', 1)` para permitir **un punto decimal** en el número.

```python
if precios_producto.replace('.', '', 1).isdigit() and float(precios_producto) > 0:
```

Esto permite valores como:

* `10`
* `10.5`
* `99.99`

Pero evita valores inválidos como:

* `abc`
* `12..5`
* `-10`

---

## 💻 Ejemplo de Ejecución

```
Ingrese el nombre del producto: Manzana
Ingrese la cantidad del producto: 3
Ingrese el precio del producto: 2.5

Producto: Manzana | Precio: 2.5 | Cantidad: 3 | Total: 7.5
```

---

## 📂 Código del Programa

```python
nombre_producto = str(input("Ingrese el nombre del producto: "))

verifica_cantidad = True
verifica_precio = True

while verifica_cantidad:

    cantidad_producto = input("Ingrese la cantidad del producto: ")

    if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
        cantidad_producto = int(cantidad_producto)
        verifica_cantidad = False
    else:
        print(f"ven aca, cuando has visto tu que una cantidad sea '{cantidad_producto}', colocame un numero entero valido")


while verifica_precio:

    precios_producto = input("Ingrese el precio del producto: ")

    if precios_producto.replace('.', '', 1).isdigit() and float(precios_producto) > 0:
        precios_producto = float(precios_producto)
        verifica_precio = False
    else:
        print(f"ven aca, cuando has visto tu que un precio sea '{precios_producto}', colocame un numero valido")


costo_total = cantidad_producto * precios_producto

print(f"Producto: {nombre_producto} | Precio: {precios_producto} | Cantidad: {cantidad_producto} | Total: {costo_total}")
```

---

## 🧠 Autor

**Luis José Guerrero Bruges**



---

