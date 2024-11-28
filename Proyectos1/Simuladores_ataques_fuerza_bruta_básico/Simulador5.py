import string
import itertools

def fuerza_bruta(contraseña_objetivo):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    for longitud in range(1, len(contraseña_objetivo) + 1):
        for intento in itertools.product(caracteres, repeat=longitud):
            intento = ''.join(intento)
            if intento == contraseña_objetivo:
                return intento
            
contraseña_objetivo = input("Contraseña objetivo: ")
resultado_busqueda = fuerza_bruta(contraseña_objetivo)
print(f"Contraseña encontrada: {resultado_busqueda}")