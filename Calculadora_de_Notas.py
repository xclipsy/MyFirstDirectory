n = float(input("Digite las notas a promediar: "))
suma = 0
i = 1
while i <= n:
    nota = float(input("Ingrese la nota: "))
    suma += nota
    i += 1
promedio = suma / n
print("El promedio de las notas es:", promedio)