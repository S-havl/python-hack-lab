import string
import itertools

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña_objetivo = input("Ingrese la contraseña a adivinar: ")

def fuerza_bruta(contraseña_objetivo):
    for longitud in range(1, len(contraseña_objetivo) + 1):
        for intento in itertools.product(caracteres, repeat=longitud):
            intento = ''.join(intento)
            if intento == contraseña_objetivo:
                return intento
            
resultado = fuerza_bruta(contraseña_objetivo)
print(f"Contraseña encontrada: {resultado}")