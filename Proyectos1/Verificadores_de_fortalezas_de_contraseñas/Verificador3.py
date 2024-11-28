import string
import random

def verificar_contraseña(contraseña_usuario):
    longitud_ok = len(contraseña_usuario) > 8
    tiene_mayusculas = any(c.isupper() for c in contraseña_usuario)
    tiene_minusculas = any(c.islower() for c in contraseña_usuario)
    tiene_numeros = any(c.isdigit() for c in contraseña_usuario)
    tiene_digitos = any(c in string.punctuation for c in contraseña_usuario)

    puntaje = sum([longitud_ok, tiene_mayusculas, tiene_minusculas, tiene_numeros, tiene_digitos])

    if puntaje == 5:
        return "Fuerte"
    elif puntaje >= 3:
        return "Moderada"
    else:
        return "Débil"
    
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

while True:
    try:
        print("MENU")
        print("1. Generar contraseña segura")
        print("2. Verificar contraseña")
        print("3. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
            if longitud <= 0:
                print("Ingrese un número positivo.")
            else:               
                contraseña = generar_contraseña(longitud)
                print(f"\nContraseña generada: {contraseña}\n")

        if opcion == '2':
            contraseña_usuario = input("Ingrese su contraseña a verificar: ")
            seguridad = verificar_contraseña(contraseña_usuario)

            print(f"\nSeguridad de su contraseña: {seguridad}\n")
        if opcion == '3':
            print("\nSaliste del programa.\n")
            break

    except ValueError:
        print("Ingrese un número válido.")
    
