correo = input(str("Ingrese el correo electronico: "))
passw =  input(str("Ingresa la contraseña: "))

def verificar_datos(correo,passw):

    if len(passw) < 8 or len(correo) < 6:
        return False
    
    elif " " in correo:
        return False
    
    elif "." in correo and "@" in correo:
        return True


    numeros = 0
    mayusculas = 0
    especiales = 0

    for carac in passw:
        if carac.isspace():
            return False
        elif not carac.isalnum():
            especiales += 1
        elif carac.isdigit():
            numeros += 1
        elif carac.isupper():
            mayusculas += 1

    return (numeros >= 1 and mayusculas >=1 and especiales >=1)

if verificar_datos (correo,passw):
    print("El correo y la contraseña son validos")
else:
    print("El correo o la contraseña son invalidos")