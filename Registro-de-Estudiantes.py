##Cantidad de estudiantes -> Nombre del estudiante -> 3 notas del estudiante -> 
# Promedio de cada estudiante con su nota y un mensaje de diga si desaprobo o aprobo y el promedio general de todo el grupo de estudiantes.

grupo = int(input("Ingrese el numero de estudiantes: "))
promedio_del_grupo = 0.0
aprobado = 0
desaprobado = 0
for i in range(grupo):
    nombre = str(input(f"Ingrese el nombre del estudiante {i + 1}: "))
    nota1 = float(input(f"Ingrese la primera nota de {nombre}: "))
    nota2 = float(input(f"Ingrese la segunda nota de {nombre}: "))
    nota3 = float(input(f"Ingrese la tercera nota de {nombre}: "))
    if nota1 < 0 or nota1 > 5 or nota2 < 0 or nota2 > 5 or nota3 < 0 or nota3 > 5:
        print("Error: Las notas deben estar entre 0 y 5. Intente nuevamente.")
        break
    promedio = (nota1 + nota2 + nota3) / 3
    print (f"El promedio de {nombre} es: {promedio:.2f}")
    if promedio >= 3.0:
        print(f"El estudiante {nombre} ha Aprobado")
        aprobado += 1
    else:
        print(f"El estudiante {nombre} ha Desaprobado")
        desaprobado += 1
    promedio_del_grupo += promedio
print(f"Han aprobado {aprobado} estudiantes.")
print(f"Han desaprobado {desaprobado} estudiantes.")
print(f"El promedio general del grupo es: {promedio_del_grupo / grupo:.2f}")
