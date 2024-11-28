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
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        if longitud <= 0:
            print("La longitud debe ser un número positivo.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

contraseña = generar_contraseña(longitud)
print(f"Tu contraseña segura es: {contraseña}")




