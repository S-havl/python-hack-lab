"""
Módulo para cifrar y descifrar mensajes utilizando la librería `cryptography.fernet`.

Funciones:
- cifrar_mensaje: Cifra un mensaje y guarda la clave y el mensaje cifrado en archivos.
- descifrar_mensaje: Descifra un mensaje cifrado utilizando una clave proporcionada.
- seleccionar_archivo: Selecciona archivos utilizando una interfaz gráfica de usuario.
- main: Interfaz principal para interactuar con el programa.

Dependencias:
- cryptography.fernet
- tkinter para selección de archivos.
"""

from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

def cifrar_mensaje(mensaje):
    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open("clave.key", "wb") as key_file:
        key_file.write(key)
    
    mensaje_bytes = mensaje.encode()
    mensaje_cifrado = cipher.encrypt(mensaje_bytes)

    with open("mensaje_cifrado.txt", "wb") as mensaje_file:
        mensaje_file.write(mensaje_cifrado)

    print("Clave guardada en 'clave.key'.")
    print("Mensaje cifrado en 'mensaje_cifrado.txt'.")

def descifrar_mensaje(key_file, mensaje_file):
    try:        
        with open(key_file, "rb") as key:
            clave = key.read()

        descifrar = Fernet(clave)

        with open(mensaje_file, "rb") as archivo_mensaje:
            mensaje_cifrado = archivo_mensaje.read()

        mensaje_descifrado = descifrar.decrypt(mensaje_cifrado)
        print("Mensaje descifrado:", mensaje_descifrado.decode())
        
    except Exception as e:
        print(f"Error al descifrar el mensaje: {e}")

def selecionar_archivo(tipo_archivo, descripcion):
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(title=descripcion, filetypes=[(tipo_archivo, f"*.{tipo_archivo}")])

    return archivo

def main():
    print("CIFRADO Y DESCIFRADO")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    seleccion = input("Eliga una opción: ")

    if seleccion == '1':
        mensaje = input("Ingrese el mensaje a cifrar: ")
        cifrar_mensaje(mensaje)
    
    elif seleccion == '2':
        print("Selecione el archivo de clave (clave.key)")
        key_file = selecionar_archivo("key", "Selecione la llave para descifrar el mensaje")
        if not key_file:
            print("No se selecciono una llave.")
            return
        
        print("Seleccione el archivo de mensaje cifrado (mensaje_cifrado.txt)")
        mensaje_file = selecionar_archivo("txt", "Seleccion el mensaje cifrado para descifrar")
        if not mensaje_file:
            print("No se selecciono un mensaje cifrado.")
            return
        
        descifrar_mensaje(key_file, mensaje_file)

if __name__ == "__main__":
    main()
    