# Variables iniciales y lista vacía para guardar los datos
nombre_producto = ""
cantidad_producto = 0
precios_producto = 0.0
repetir_menu = True
Inventario = []

# Función para registrar un producto nuevo
def agregar_producto():
    otro_producto = True
    while otro_producto:
        verifica_cantidad = True
        verifica_precio = True
        nombre_producto = str(input("Ingrese el nombre del producto: "))

        # Validación: Asegura que la cantidad sea un número entero positivo
        while verifica_cantidad:
            cantidad_producto = input("Ingrese la cantidad del producto: ")
            if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
                cantidad_producto = int(cantidad_producto)
                verifica_cantidad = False
            else:
                print(f"ven aca, cuando has visto tu que una cantidad sea '{cantidad_producto}', colocame un numero entero valido")

        # Validación: Asegura que el precio sea un número válido (puede tener decimales)
        while verifica_precio:
            precios_producto = input("Ingrese el precio del producto: ")
            if precios_producto.replace('.', '', 1).isdigit() and float(precios_producto) > 0:
                precios_producto = float(precios_producto)
                verifica_precio = False
            else:
                print(f"ven aca, cuando has visto tu que un precio sea '{precios_producto}', colocame un numero valido")
        
        # Guarda los datos validados en un diccionario y lo añade a la lista
        producto = {
            "nombre": nombre_producto,
            "precio": precios_producto,
            "cantidad": cantidad_producto
        }
        Inventario.append(producto)
        
        respuesta = input("¿Desea agregar otro producto? (si/no): ")
        if respuesta != "si":
            otro_producto = False

# Función para ver los productos registrados
def mostrar_inventario():
    if len(Inventario) == 0:
        print("El inventario esta vacio chamoooo")
    else:
        # Bucle para recorrer y mostrar cada producto con un formato claro
        for i in Inventario:
            print(f"Producto: {i['nombre']} | Precio: {i['precio']} | Cantidad: {i['cantidad']}")

# Función para calcular los totales de dinero y cantidad de items
def calcular_estadisticas():
    if len(Inventario) == 0:
        print("EL INVENTARIO ESTA VACIO NO PODEI CALCULAR NAAAAA")
    else:
        costo_total = 0
        # Bucle para sumar el valor (precio x cantidad) de todo el inventario
        for k in Inventario:
            costo_total += k["cantidad"] * k["precio"]
        print(f"El valor total del inventario es de: {costo_total} y la cantidad de productos registrados es de: {len(Inventario)}")


# Bucle principal: Mantiene el menú funcionando hasta que se elija la opción 4
while repetir_menu:
    print("\nBienvenido al Inventario del supermercado :)")
    print("Menu de opciones")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")
 
    eleccion = (input("¿Que opcion le gustaria hacer?: "))

    # Condicionales para ejecutar la función según la elección del usuario
    if eleccion == "1":
        agregar_producto()
            
    elif eleccion == "2":
        mostrar_inventario()

    elif eleccion == "3":
       calcular_estadisticas() 

    elif eleccion == "4":
        repetir_menu = False
    else:
        print("Elige un valor valido porfavor")

# OBJETIVOS LOGRADOS ESTA SEMANA:
# - Menú interactivo.
# - Guardar historial de productos (Listas y Diccionarios).
# - Código limpio y ordenado en funciones. 