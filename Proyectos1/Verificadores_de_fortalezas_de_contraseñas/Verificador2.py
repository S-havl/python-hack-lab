import string
import random

def verificar_fortaleza(contraseña):
    longitud_ok = len(contraseña) >= 8
    tiene_mayusculas = any(c.isupper() for c in contraseña)
    tiene_minusculas = any(c.islower() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)

    puntaje = sum([longitud_ok, tiene_mayusculas, tiene_minusculas, tiene_numeros, tiene_simbolos])

    if puntaje == 5:
        return "Fuerte"
    elif puntaje >= 3:
        return "Moderada"
    else:
        return "Débil"
    
def generar_contraseña(longitud):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

while True:
    try:
        print("CONTRASEÑAS SEGURAS!")
        print("1. Verificar seguridad de contraseña.")
        print("2. Generar contraseña segura.")
        print("3. Salir del programa.")

        seleccion = input("Selecione una opción: ")

        if seleccion == '1':
            contraseña = input("Ingrese la contraseña a verificar: ")
            fortaleza = verificar_fortaleza(contraseña)
        
            print(f"\nLa seguridad de su contraseña es: {fortaleza}\n")
        if seleccion == '2':
            longitud = int(input("Ingrese la longitud de la contraseña a generar: "))
            if longitud <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                contraseña = generar_contraseña(longitud)
                print(f"\nSu contraseña generada es {contraseña}\n")
        
        if seleccion == '3':
            print("Saliste del programa.")
            break
    
    except ValueError:
        print("Ingrese un número válido")