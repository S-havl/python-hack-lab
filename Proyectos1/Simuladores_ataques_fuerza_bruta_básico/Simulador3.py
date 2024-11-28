import string
import itertools

def fuerza_bruta(contraseña_objetivo):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    for longitud in range(1, len(contraseña_objetivo) + 1):
        for intento in itertools.product(caracteres, repeat=longitud):
            intento = ''.join(intento)
            if intento == contraseña_objetivo:
                return intento
            
while True:
    try:
        print("SIMULADOR DE FUERZA BRUTA")
        print("1. Iniciar prueba")
        print("2. Cerrar script")

        seleccion = input(": ")

        if seleccion == '1':
            contraseña_objetivo = input("Ingrese la contraseña a adivinar: ")
            resultado = fuerza_bruta(contraseña_objetivo)
            print(f"\nContraseña adivinada: {resultado}\n")

        if seleccion == '2':
            print("Saliste del script.")
            break

    except ValueError:
        print("Ingrese un valor válido, por favor.")
