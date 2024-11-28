import random
import string

def generar_contraseña(longitud, incluir_numeros=True):
    caracteres = string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

while True:
    try:
        longitud = int(input("Ingrese la longitud que desee: "))
        if longitud <= 0:
            print("Por favor, ingrese un número positivo.")
        else:
            break
    except ValueError:
        print("Ingrese un número válido.")

contraseña = generar_contraseña(longitud)
print(f"Contraseña generada: {contraseña}")
