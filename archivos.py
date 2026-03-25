"""
Módulo de Archivos
Se encarga de la persistencia de datos del inventario.
Permite guardar la información en un archivo CSV y cargarla de vuelta,
manejando validaciones de estructura y errores de lectura/escritura.
"""
import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda la lista del inventario en un archivo CSV.
    Incluye el encabezado (nombre,precio,cantidad) y maneja errores de permisos.
    """
    if len (inventario) == 0:
        print('EL INVENTARIO ESTA VACIO CHAMOOO')
        return False
    
    try:
        with open(ruta, 'w', newline='') as file:
            writer = csv.writer(file)

            if incluir_header == True:
                writer.writerow(['nombre', 'precio', 'cantidad'])

            for producto in inventario:
                writer.writerow([producto['nombre'],producto['precio'],producto['cantidad']])
        print(f'SI FUNCIONO CHAMO Y SE GUARDO EN {ruta}')
        return True

    except PermissionError:
        print(f"¡NO TENGO PERMISOS CHAMOOOO! No pude guardar en '{ruta}' mano :'(")

def cargar_csv (ruta):
    """
    Lee un archivo CSV, valida que cada fila tenga 3 columnas y valores no negativos.
    Maneja excepciones y retorna una tupla: (lista_de_productos, contador_filas_invalidas).
    """
    productos_almacenados = []
    filas_invalidas = 0

    try:
        with open (ruta, "r") as file:
            reader = csv.reader(file)

            try:
                encabezado = next(reader)
            except StopIteration:
                print('EL ARCHIVO TA COMPLETAMENTE VACIO CHAMOOOOO')
                return None, 0
            
            if encabezado != ['nombre', 'precio', 'cantidad']:
                print('El encabezado no ha cumplido con las estructuras establecidas, por favor vuelva y lo intenta (voz de español)')
                print('pistica :P, el formato debe ser: nombre,precio,cantidad')
                return None, 0
            
            for i in reader:

                if len(i) != 3:
                    filas_invalidas += 1
                    continue
            
                try:
                    nombre = i[0].strip()
                    precio = float(i[1])
                    cantidad = int(i[2])

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    productos_almacenados.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                
                except ValueError:
                    filas_invalidas += 1
                    continue
        return productos_almacenados, filas_invalidas
    except FileNotFoundError:
        print(f'EL ARCHIVO {ruta} NO EXISTEEEE, TENEI QUE GUARDARLO PRIMERO CHAMO')
        return None, 0
    except UnicodeDecodeError:
        print(f"EL ARCHIVO {ruta} TIENE CARACTERES EXTRAÑOS, MIRA ESO")
        return None, 0