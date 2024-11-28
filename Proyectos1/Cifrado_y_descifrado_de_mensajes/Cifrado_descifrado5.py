def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isupper():
            resultado += chr((ord(letra) + desplazamiento - 65) % 26 + 65)

        elif letra.islower():
            resultado += chr((ord(letra) + desplazamiento - 97) % 26 + 97)

        else:
            resultado += letra

    return resultado

def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)

def main():
    mensaje = input("Ingrese el mensaje a cifrar: ")
    desplazamiento = int(input("Ingrese el número de desplazamiento: "))

    mensaje_cifrado = cifrar(mensaje, desplazamiento)
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    mensaje_descifrado = descifrar(mensaje_cifrado, desplazamiento)
    print(f"Mensaje descifrado: {mensaje_descifrado}")

if __name__ == "__main__":
    main()