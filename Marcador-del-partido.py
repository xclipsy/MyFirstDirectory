print("Bienvenido a las estadisticas del yuyu: (Junior)")
pj = int(input("Ingrese la cantidad de partidos jugados: "))

puntos = 0
pg = 0
pe = 0
pp = 0
gf = 0 
gc = 0
dg = 0

for i in range (1, pj, +1):
    gf = int(input("Ingrese la cantidad de goles a favor: "))
    gc = int(input("Ingrese la cantidad de goles en contra: "))
    if gf > gc:
        pg += 1
    elif gf == gc:
        pe += 1
    elif gf < gc:
        pp += 1

    if pg > 0:
        puntos += 3
    elif pe > 0:
        puntos += 1
    elif pp > 0:
        pass
    dg = gf - gc
print("El total de puntos es: ", puntos)
print("El total de goles a favor es: ", gf)
print("El total de goles en contra es: ", gc)
print("El total de diferencia de goles es: ", dg)
