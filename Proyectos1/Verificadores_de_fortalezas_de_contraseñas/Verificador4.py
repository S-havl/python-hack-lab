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

def verificar_seguridad(contraseña):
    longitud_ok = len(contraseña) >= 8
    tiene_mayusculas = any(c.isupper() for c in contraseña)
    tiene_minusculas = any(c.islower() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)

    puntuancion = sum([longitud_ok, tiene_mayusculas, tiene_minusculas, tiene_numeros, tiene_simbolos])

    if puntuancion == 5:
        return "Fuerte"
    
    if puntuancion >= 3:
        return "Moderada"
    
    else:
        return "Débil"
    
while True:
    try:
        print("VERIFICADOR DE CONTRASEÑAS")
        print("1. Verificar contraseña")
        print("2. Generar contraseña segura")
        print("3. Cerrar script")

        seleccion = input(": ")

        if seleccion == '1':
            contraseña = input("Ingrese la contraseña a verificar: ")
            contraseña_verificada = verificar_seguridad(contraseña)
            print(f"\nSu contraseña es: {contraseña_verificada}\n")

        if seleccion == '2':
            longitud = int(input("Ingrese la longitud deseada: "))
            if longitud <= 0:
                print("Ingrese un número positivo.")
            else:
                contraseña_generada = generar_contraseña(longitud)
                print(f"\nSu contraseña generada es: {contraseña_generada}\n")

        if seleccion == '3':
            print("Cerraste el script.")
            break
    except ValueError:
        print("Ingrese un número válido.")