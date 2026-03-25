"""
Menú principal del sistema de inventario.
Permite al usuario interactuar con todas las funciones (CRUD, archivos y estadísticas)
a través de la consola, validando que no se cierre por errores.
"""
import servicios
import archivos

repetir_menu = True
Inventario = []
ruta = 'inventario.csv'

while repetir_menu:
    print("\nBienvenido al Inventario del supermercado :)")
    print("Menu de opciones")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Buscar un producto")
    print("4. Actualizar un producto")
    print ("5. Eliminar un producto")
    print("6. Calcular estadisticas")
    print("7. Guardar inventario")
    print("8. Cargar inventario")
    print("9. Salir")
 
    eleccion = (input("¿Que opcion le gustaria hacer?: "))

    if eleccion == "1":
        otro_producto = True
        while otro_producto:
            verifica_cantidad = True
            verifica_precio = True
            nombre_producto = str(input("Ingrese el nombre del producto: "))

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
            servicios.agregar_producto(Inventario, nombre_producto, precios_producto, cantidad_producto)
            print('El producto se guardo chamooooo.')
            
            respuesta = input("¿Desea agregar otro producto? (si/no): ")
            if respuesta != "si":
                otro_producto = False
        
            
    elif eleccion == "2":
        servicios.mostrar_inventario(Inventario)
    
    elif eleccion == "3":
        nombre_buscar = input('Ingrese el nombre del producto a buscar: ')
        producto = servicios.buscar_producto(Inventario, nombre_buscar)
        if producto == None:
            print(f'EL PRODUCTO {nombre_buscar} NO EXISTE EN EL INVENTARIO CHAMOOOOOOOOO')
        else:
            print('ENCONTRAMOS EL PRODUCTO CHAMOOOOOO')
            print(f'El producto {producto['nombre']}, con su precio {producto['precio']}, y su cantidad {producto['cantidad']}')
    
    elif eleccion == "4":
        nombre_existe = input('Ingrese el nombre del producto a actualizar: ')
        verificar = servicios.buscar_producto(Inventario, nombre_existe)
        if verificar != None:
            actualizar_precio = input(f'Ingrese el nuevo precio del producto {nombre_existe}: ')
            if actualizar_precio.replace('.', '', 1).isdigit() and float(actualizar_precio) > 0:
                actualizar_precio = float(actualizar_precio)
                nuevo_precio = servicios.actualizar_producto(Inventario, nombre_existe, actualizar_precio)
                print(f'El precio del producto {nombre_existe} fue actualizado a {actualizar_precio}')
            else:
                print(f"ven aca, cuando has visto tu que un precio sea '{actualizar_precio}', colocame un numero entero valido")
        else:
            print(f'EL PRODUCTO {nombre_existe} NO EXISTE CHAMOOOOO')
    
    elif eleccion == "5":
        nombre_eliminar = input('Ingrese el nombre del producto a eliminar: ')
        existe = servicios.buscar_producto(Inventario, nombre_eliminar)
        if existe != None:
            fue_eliminado = servicios.eliminar_producto(Inventario,nombre_eliminar)
            if fue_eliminado == True:
                print(f'El producto {nombre_eliminar} fue eliminado. NAWEBONAAAAAAAAAAAAAAAAAA')
            else:
                print(f'EL PRODUCTO {nombre_eliminar} NO EXISTE CHAMOOOOOOOOOOOOO')

    elif eleccion == "6":
       calculo = servicios.calcular_estadisticas(Inventario)
       if calculo == None:
           print('EL INVENTARIO ESTA VACIO NO HAY NAAAAAAAAAAAAAAAAAAAAAAAAAAA')
       else:
           print('LAS ESTADISTICAS SON CHAMO')
           print(f'Costo total: {calculo['costo total']}')
           print(f'Cantidad de Productos: {calculo['cantidad productos']}')
           print(f'Calculo total: {calculo['calculo total']}')
           print(f'El producto mas caro es: {calculo['producto mas caro']['nombre']}')
           print(f'El producto con mayor stock es: {calculo['precio mayor stock']['nombre']}')

    elif eleccion == "7":
        
        archivos.guardar_csv(Inventario, ruta)
           
    elif eleccion == "8":
        
        carga = archivos.cargar_csv(ruta)
        if carga[0] is not None:
            productos_almacenados = carga[0]
            filas_invalidas = carga[1]

            print(f'chamo lei {len(productos_almacenados)} productos q son validos del archivo ceseuve')
            print(f'¿Ute quiere sobreescribir o fusionar los datos?')
            print(f'Ojo que si sobreescribes se borra lo que habia ahi, ojo y borras la base de datos Didier')
            print(f'Si los fusionas los archivos nuevos se quedan y los viejos tambien papi ya')
            print(f'si el producto ya existe, en caso de fusion, se actualiza la cantidad y el precio al mas nuevo')
            print(f'Si no existe, papi se crea y ya')
            seleccion = input('Sobreescribir el archivo? Ojo y borras todo (si/no): ').lower()

            if seleccion == 'si':
                Inventario.clear()
                Inventario.extend(productos_almacenados)
                accion_elegida = "Reemplazar"
            
            else:
                accion_elegida = "Fusionar"
                for i in productos_almacenados:
                    nuevo_producto = servicios.buscar_producto(Inventario, i['nombre'])

                    if nuevo_producto != None:
                        nuevo_producto['cantidad'] += i['cantidad']
                        nuevo_producto['precio'] = i['precio']
                    else:
                        Inventario.append(i)
            print(f'Total de productos almacenados: {len(productos_almacenados)}')

            if filas_invalidas > 0:
                print(f'Las filas invalidas que no se tomaron en cuenta fueron: {filas_invalidas}')
                print(f'La accion realizada fue: {accion_elegida}')

    elif eleccion == "9":
        repetir_menu = False
    else:
        print("Elige un valor valido porfavor")
