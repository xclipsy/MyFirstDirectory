heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "poder": "Agilidad", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "poder": "Tecnologia", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "poder": "Inteligencia", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "poder": "Fuerza", "nivel": 98}
]
k=1
heroes_seleccionados = []
print("Bienvenido a la galeria de heroes, los heroes disponibles son\n")
otro_heroe = True
while otro_heroe == True:
    for i, c in enumerate (heroes, start= 1):
        print(f"{i} {c}")
        otro_heroe = False
    
    no_existe = True
    while no_existe:
        heroe = int(input(f"\nIngresa a tu heroe numero {k}: "))
        if 1 <= heroe <= len(heroes):
            seleccionado = heroes[heroe-1]
            heroes_seleccionados.append(seleccionado)
            print(f"El heroe seleccionado:{seleccionado["nombre"]}")
            k+=1
            print("Heroes seleccionados:")
            for h in heroes_seleccionados:
                print(h["nombre"])
            mas_heroes = input("¿Desea ingresar otro heroe? si/no ").lower()
            if mas_heroes == "si":
                pass
            elif mas_heroes == "no":
                break
            else:
                print("Respuesta no valida")
                break
        else:
            print("El heroe seleccionado no existe")
    