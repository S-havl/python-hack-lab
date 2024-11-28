import string
import random

def generar_contraseña(longitud, contiene_mayusculas=True, contiene_numeros=True, contiene_simbolos=True):
    caracteres = string.ascii_lowercase

    if contiene_mayusculas:
        caracteres += string.ascii_uppercase

    if contiene_numeros:
        caracteres += string.digits

    if contiene_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def verificar_contraseña(contraseña):
    longitud_ok = len(contraseña) >= 8
    contiene_minusculas = any(c.islower() for c in contraseña)
    contiene_mayusculas = any(c.isupper() for c in contraseña)
    contiene_numeros = any(c.isdigit() for c in contraseña)
    contiene_simbolos = any(c in string.punctuation for c in contraseña)

    puntuacion = sum([longitud_ok, contiene_mayusculas, contiene_minusculas, contiene_numeros, contiene_simbolos])

    if puntuacion == 5:
        return "Fuerte"
    elif puntuacion >= 3:
        return "Moderada"
    else:
        return "Débil"
    
while True:
    try:
        print("S-HAVL SCRIPT")
        print("1. Generar contraseña")
        print("2. Verificar fortaleza de contraseña")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            longitud = int(input("Ingrese la longitud de su contraseña deseada: "))
            if longitud <= 0:
                print("Ingrese un número positivo, por favor.")
            else:
                paswd_generada = generar_contraseña(longitud)
                print(f"Su contraseña generada es: {paswd_generada}")

        if opcion == '2':
            contraseña = input("Ingrese la contraseña que desee verificar: ")
            fortaleza = verificar_contraseña(contraseña)
            print(f"Fortaleza de su contraseña: {fortaleza}")

        if opcion == '3':
            print("Saliste del script...")
            break
    except ValueError:
        print("Ingrese un número válido, por favor.")