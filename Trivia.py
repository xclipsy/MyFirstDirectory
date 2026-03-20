import requests
import random
import csv
from datetime import datetime

request = requests.get('https://raw.githubusercontent.com/andres-barros-riwi/trivia-python/refs/heads/main/data.json')
data = request.json()
nombre = input('Ingrese su nombre para empezar: ')
print('Bienvenido a la trivia')
print('Responde las preguntas de forma correcta para obtener puntos, \n de ser incorrectas, no sumaran a tu puntaje')
cantidad = 5
score = 0
contador_correctas = 0
fecha_y_hora = datetime.now()

for i in range(cantidad):
    p_trivia = random.choice(data)
    print(f"Categoria: {p_trivia['categoria']}")
    print(f'Pregunta: {p_trivia['pregunta']}')
    print(f"A) {p_trivia['opciones']['A']}")
    print(f"B) {p_trivia['opciones']['B']}")
    print(f"C) {p_trivia['opciones']['C']}")
    print(f"D) {p_trivia['opciones']['D']}\n")
    respuesta = input('Ingrese su respuesta: ').upper()
    print(f"La respuesta correcta es: {p_trivia['respuesta_correcta']}")
    intento = p_trivia['respuesta_correcta']
    if intento == respuesta:
         print('Respuesta correcta')
         score += 20
         contador_correctas += 1
    else:
         print('Respuesta incorrecta')

print(f'Su puntaje obtenido fue de: {score}, \n y la cantidad de respuestas correctas fue {contador_correctas} eres cule malo')

with open('top10.csv', 'a', newline="") as alochino:
    writer = csv.writer(alochino)
    writer.writerow(["Nombre", "Punt", "Fecha_y_Hora"])
    writer.writerow([nombre, score, fecha_y_hora])

with open('top10.csv', 'r') as alochino:
    chocoplo = csv.DictReader(alochino)

    for i in chocoplo:
        print(f"{i['Nombre']} tiene {i['Punt']} y fue a la hora de {i["Fecha_y_Hora"]}")
