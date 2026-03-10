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
        cantidad =  int(input("Ingrese la cantidad de asientos: "))
        vuelo_seleccionado = vuelos[codigo]
        if  vuelo_seleccionado[1] >= 0 and cantidad <= vuelo_seleccionado[1]:
            print (f"Los numeros de asientos son {cantidad} para el vuelo {codigo}")
            vuelo_seleccionado[1] - cantidad
            reserva = [nombre,codigo,cantidad]
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