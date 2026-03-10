# ✈️ Sistema de Reservas de Vuelos - Aerolínea Chocorramo

Este proyecto es un programa sencillo en **Python** que simula un **sistema de reservas de vuelos desde consola**.  
Permite a un usuario ver vuelos disponibles, seleccionar uno mediante su código y reservar asientos si hay disponibilidad.

---

# 📌 Características

- Mostrar los vuelos disponibles
- Seleccionar un vuelo mediante su código
- Reservar una cantidad de asientos
- Verificar disponibilidad de asientos
- Permitir realizar múltiples reservas

---

# 🧠 Lógica del Programa

El programa utiliza:

- **Diccionarios (`dict`)** para almacenar los vuelos
- **Listas (`list`)** para guardar las reservas
- **Bucles `while`** para repetir el proceso de reserva
- **Condicionales `if`** para validar la información ingresada por el usuario

---

# 📂 Código del Programa

```python
vuelos = {
    "AV101": ("Bogota", 5, 300),
    "AV202": ("Medellin", 3, 200),
    "AV303": ("Cartagena", 4, 250),
    "AV404": ("Cali", 2, 220)
}

reserva = []

def Mostrar():
    for codigo, (destino, asientos, precio) in vuelos.items():
        print(f"Codigo de vuelo: {codigo}, Destino: {destino}, Asientos: {asientos}")

print("="*50)
print("Bienvenido a la aerolinea chocorramo")
print("="*50)

otra_vez = True
nombre = input(("Ingrese su nombre porfavor: "))

while otra_vez == True:

    print(f"Los vuelos disponibles son:")
    print(Mostrar())

    repeat = True

    while repeat == True:

        codigo = input(("Ingrese el codigo del vuelo: "))

        if codigo in vuelos:
            pass
            repeat = False

        else:
            print("El codigo del vuelo seleccionado no existe\n porfavor digitelo devuelta")

    while repeat == False:

        cantidad = int(input("Ingrese la cantidad de asientos: "))
        vuelo_seleccionado = vuelos[codigo]

        if vuelo_seleccionado[1] >= 0 and cantidad <= vuelo_seleccionado[1]:

            print(f"Los numeros de asientos son {cantidad} para el vuelo {codigo}")

            vuelo_seleccionado[1] - cantidad

            reserva = [nombre, codigo, cantidad]
            reserva =+ reserva

            print(f"Su reserva es{reserva}")

        else:

            print(f"No hay suficientes asientos para el vuelo {codigo}")

        otro = input("¿Desea reservar otro vuelo?: si/no: ").lower

        if otro == "si":

            cantidad_de_reservas += 1
            subtotal = vuelo_seleccionado * cantidad
            dinero_recaudado += subtotal

            pass

        else:

            cantidad_de_reservas += 1
            subtotal = vuelo_seleccionado * cantidad
            dinero_recaudado += subtotal

            otra_vez = False
```

---

# ▶️ Funcionamiento del Programa

1. El programa muestra un mensaje de bienvenida.
2. Solicita el **nombre del usuario**.
3. Muestra los **vuelos disponibles**.
4. El usuario introduce el **código del vuelo**.
5. El sistema valida si el código existe.
6. El usuario introduce la **cantidad de asientos**.
7. El sistema verifica si hay suficientes asientos.
8. Si hay disponibilidad, se guarda la reserva.
9. El usuario puede decidir si desea **reservar otro vuelo**.

---

# 💻 Ejemplo de Ejecución

```
==================================================
Bienvenido a la aerolinea chocorramo
==================================================

Ingrese su nombre porfavor: Juan

Los vuelos disponibles son:

Codigo de vuelo: AV101, Destino: Bogota, Asientos: 5
Codigo de vuelo: AV202, Destino: Medellin, Asientos: 3
Codigo de vuelo: AV303, Destino: Cartagena, Asientos: 4
Codigo de vuelo: AV404, Destino: Cali, Asientos: 2

Ingrese el codigo del vuelo: AV101
Ingrese la cantidad de asientos: 2

Los numeros de asientos son 2 para el vuelo AV101
Su reserva es ['Juan', 'AV101', 2]
```

---

# ⚠️ Posibles Mejoras

El proyecto puede ampliarse agregando:

- Actualización real de los asientos disponibles
- Lista de todas las reservas realizadas
- Cálculo del dinero total recaudado
- Manejo de errores con `try / except`
- Menú interactivo
- Guardar reservas en archivos `.txt` o `.json`
- Interfaz gráfica con **Tkinter**

---

# 🚀 Cómo Ejecutar el Programa

1. Instalar **Python 3**
2. Guardar el archivo como:

```
reservas_vuelos.py
```

3. Ejecutar el programa:

```bash
python reservas_vuelos.py
```

---

# 👨‍💻 Autor

Proyecto educativo desarrollado para practicar:

- Python básico
- Diccionarios
- Listas
- Condicionales
- Bucles

---

# 📜 Licencia

Este proyecto es de uso **educativo y libre**.
