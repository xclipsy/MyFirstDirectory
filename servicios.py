"""
Módulo de Servicios
Contiene toda la lógica de negocio y operaciones CRUD para el inventario.
"""
nombre_producto = ""
cantidad_producto = 0
precios_producto = 0.0

def agregar_producto(inventario, nombre_producto, precios_producto, cantidad_producto):
    """
    Agrega un nuevo producto al inventario.
    Recibe la lista del inventario, nombre, precio y cantidad, y lo añade como un diccionario.
    """
    producto = {
            "nombre": nombre_producto,
            "precio": precios_producto,
            "cantidad": cantidad_producto
        }
    inventario.append(producto)
    
def mostrar_inventario(inventario):
    """
    Recorre la lista del inventario y muestra cada producto en la consola.
    Avisa al usuario si el inventario se encuentra vacío.
    """
    if len(inventario) == 0:
        print("El inventario esta vacio chamoooo")
    else:
        for i in inventario:
            print(f"Producto: {i['nombre']} | Precio: {i['precio']} | Cantidad: {i['cantidad']}")

def calcular_estadisticas(inventario):
    """
    Calcula y retorna un diccionario con las estadísticas clave del inventario:
    - unidades_totales: Suma de las cantidades de todos los productos.
    - valor_total: Suma del (precio * cantidad) de todos los productos.
    - producto_mas_caro: El diccionario del producto con el precio más alto.
    - producto_mayor_stock: El diccionario del producto con más cantidad.
    Retorna None si el inventario está vacío.
    """
    if len(inventario) == 0:
        return None
    else:
        costo_total = 0
        for k in inventario:
            costo_total += k["cantidad"] * k["precio"]
            producto_mas_caro = max(inventario, key=lambda x: x['precio'])
            producto_mayor_stock = max(inventario, key=lambda y: y['cantidad'])
        cantidad_productos = len(inventario)
        calculo_total = costo_total / cantidad_productos
        
        return {
            "costo total": costo_total,
            "cantidad productos": cantidad_productos,
            "calculo total": calculo_total,
            "producto mas caro": producto_mas_caro,
            "precio mayor stock": producto_mayor_stock
        }

def buscar_producto(inventario, nombre_buscar):
    """
    Busca un producto por su nombre en la lista de inventario.
    Retorna el diccionario del producto si lo encuentra, o None si no existe.
    """
    for i in inventario:
        if i['nombre'] == nombre_buscar:
            return i
    else:
        None

def actualizar_producto(inventario, nombre_existe, actualizar_precio):
    """
    Busca un producto por su nombre y actualiza su precio.
    Retorna True si la actualización fue exitosa, o False si no encontró el producto.
    """
    for i in inventario:
        if i['nombre'] == nombre_existe:
           i['precio'] = actualizar_precio  
           return True
    else:
        return False
    
def eliminar_producto(inventario, nombre_eliminar):
    """
    Busca un producto por su nombre y lo elimina de la lista de inventario.
    Retorna True si lo eliminó exitosamente, o False si el producto no existía.
    """
    for i in inventario:
        if i['nombre'] == nombre_eliminar:
            inventario.remove(i)
            return True
    else:
        return False
