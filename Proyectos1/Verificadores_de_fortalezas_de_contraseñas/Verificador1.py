import string

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
    
contraseña = input("Ingresa tu contraseña: ")
fortaleza = verificar_fortaleza(contraseña)
print(f"La fortaleza de la contraseña es: {fortaleza}")