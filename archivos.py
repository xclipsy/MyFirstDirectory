print("Bienvenido al sistema de Parqueadero")
parqueadero = []
try: 
    with open ('registro_parqueadero.txt', 'r') as file:
        parqueadero = [line.strip() for line in file.readlines()]
except:
    pass
if len(parqueadero) == 0:
    parqueadero = ["_"] * 10

wailtru = True
while wailtru:
    respuesta = input("\n¿Desea ingresar o sacar un vehículo? (ingresar/sacar): ").lower()
    
    if respuesta == "ingresar":
        if "_" in parqueadero:
            placa = input("Ingrese la placa: ")
            indice = parqueadero.index("_")
            parqueadero[indice] = placa
            print(f"Vehículo {placa} ingresado en el espacio {indice + 1}.")
        else:
            print("Lo sentimos, el parqueadero está lleno.")
        
    elif respuesta == "sacar":
        placa = input("Ingrese la placa del vehículo a retirar: ")
        if placa in parqueadero:
            indice = parqueadero.index(placa)
            parqueadero[indice] = "_"
            print(f"Vehículo {placa} retirado con éxito.")
        else:
            print("Esa placa no se encuentra en el sistema.")
    
    print(f"Estado actual: {parqueadero}")

    if input("¿Desea realizar otra operación? (si/no): ").lower() == "no":
        print("Gracias por usar el sistema.")
        break

with open ("registro_parqueadero.txt", "w") as file:
    for vehiculo in parqueadero:
        file.write(vehiculo +"\n")
with open ("registro_parqueadero.txt", "r") as file:
        for vehiculo in parqueadero:
            print(f"Vehiculo guardado, placa:{vehiculo}", end="")