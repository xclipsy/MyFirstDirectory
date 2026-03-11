# 🦸‍♂️ Galería de Héroes en Python

Este proyecto es un programa sencillo en **Python** que permite al usuario seleccionar héroes de una lista y mostrar los héroes que ha elegido.

## 📌 Descripción

El programa muestra una galería de héroes de **Marvel** y **DC**.  
El usuario puede seleccionar uno o varios héroes ingresando el número correspondiente.  
Cada héroe seleccionado se guarda en una lista y se muestra al usuario.

## 📂 Estructura del Programa

El programa utiliza:

- **Lista de diccionarios** para almacenar la información de los héroes.
- **Bucles `while` y `for`** para mostrar opciones y controlar la selección.
- **Entrada de usuario (`input`)** para elegir héroes.
- **Listas** para guardar los héroes seleccionados.

## 🦸 Héroes Disponibles

| Nombre | Universo | Poder | Nivel |
|------|------|------|------|
| Spider-Man | Marvel | Agilidad | 85 |
| Iron Man | Marvel | Tecnología | 90 |
| Batman | DC | Inteligencia | 88 |
| Superman | DC | Fuerza | 98 |

## ▶️ Funcionamiento

1. El programa muestra la lista de héroes disponibles.
2. El usuario ingresa el número del héroe que desea seleccionar.
3. El héroe se agrega a la lista de **héroes seleccionados**.
4. El programa pregunta si desea elegir otro héroe.
5. Si el usuario escribe **"si"**, puede seguir seleccionando.
6. Si escribe **"no"**, el programa termina.

## 💻 Código

```python
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
    for i, c in enumerate(heroes, start=1):
        print(f"{i} {c}")
        otro_heroe = False

    no_existe = True

    while no_existe:
        heroe = int(input(f"\nIngresa a tu heroe numero {k}: "))

        if 1 <= heroe <= len(heroes):

            seleccionado = heroes[heroe-1]
            heroes_seleccionados.append(seleccionado)

            print(f"El heroe seleccionado:{seleccionado['nombre']}")

            k += 1

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
