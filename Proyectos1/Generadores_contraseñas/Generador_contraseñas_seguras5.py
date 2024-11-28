import random
import string

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

while True:
    try:
        longitud = int(input("Ingrese la logintud de la contraseña a generar: "))
        
        if longitud <= 0:
            print("Ingrese un número positivo por favor.")
        else:
            break
    except ValueError:
        print("Ingrese un número válido.")

contraseña = generar_contraseña(longitud)
print(f"Contraseña generada: {contraseña}")