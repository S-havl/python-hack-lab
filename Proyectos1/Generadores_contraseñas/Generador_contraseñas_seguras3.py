import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

while True:
    try:
        longitud = int(input("Longitud: "))
        if longitud <= 0:
            print("Ingrese un número positivo.")
        else:
            break
    except ValueError:
        print("Ingrese un número válido.")

contraseña = generar_contraseña(longitud)
print(f"Contraseña generada: {contraseña}")
