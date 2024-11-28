"""
Módulo para generar contraseñas seguras.

Funciones:
- generar_contraseña: Crea una contraseña basada en parámetros específicos (mayúsculas, minúsculas, números, caracteres especiales).
- contraseña_vocabulario: Genera contraseñas utilizando caracteres de un archivo de vocabulario.
- main: Interfaz principal para seleccionar opciones de generación de contraseñas.

Características:
- Permite la personalización de contraseñas según los tipos de caracteres.
- Incluye una opción para generar contraseñas a partir de vocabularios personalizados.
- Utiliza `tkinter` para seleccionar archivos desde una interfaz gráfica.

Dependencias:
- random y string para generar contraseñas.
- tkinter para selección de archivos.

Advertencias:
- Asegúrate de seleccionar correctamente el archivo del vocabulario si usas esa opción.
"""


import random
import string
import tkinter as tk
from tkinter import filedialog

def generar_contraseña(longitud, mayusculas, minusculas, numeros, caracteres_especiales):
    caracteres = ""
    
    if mayusculas.lower() == 's':
        caracteres += string.ascii_uppercase

    if minusculas.lower() == 's':
        caracteres += string.ascii_lowercase

    if numeros.lower() == 's':
        caracteres += string.digits

    if caracteres_especiales.lower() == 's':
        caracteres += string.punctuation

    if caracteres:
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contraseña
    else:
        print("Debe elegir al menos un tipo de carácteres.")
        
def contraseña_vocabulario(caracteres_vocabulario, longitud):
    contraseña = ''.join(random.choice(caracteres_vocabulario) for _ in range(longitud))
    print(f"Su contraseña generada por vocabulario es: {contraseña}")

def main():   
    print("GENERADOR DE CONTRASEÑAS SEGURAS")
    print("1. Generar contraseña con carácteres")
    print("2. Generar contraseña con vocabulario")
    seleccion = input("Seleccione una opción: ")

    if seleccion == '1':

        longitud = int(input("Longitud de su contraseña: "))
        mayusculas = str(input("Mayúsculas?(s/n): "))
        minusculas = str(input("Minúsculas?(s/n): "))
        numeros = str(input("Números?(s/n): "))
        caracteres_especiales = input("Carácteres especiales?(s/n): ")
        contraseña_generada = generar_contraseña(longitud, mayusculas, minusculas, numeros, caracteres_especiales)
        print(f"Su contraseña generada es: {contraseña_generada}")
    
    if seleccion == '2':
        root = tk.Tk()
        root.withdraw()
        ruta_archivo = filedialog.askopenfilename(title="Seleccione el archivo del vocabulario")

        if ruta_archivo:
            longitud = int(input("Ingrese la longitud de su contraseña: "))
            try:
                with open(ruta_archivo, "r", encoding="utf-8") as vocabulario:
                    contenido = vocabulario.read().replace("\n", "")
                    caracteres_vocabulario = set(contenido)
                    cadena_caracteres = ''.join(caracteres_vocabulario)
                    contraseña_vocabulario(cadena_caracteres, longitud)

            except FileNotFoundError:
                print("Archivo no encontrado.")
            except FileExistsError:
                print("El archivo no existe.")
        

if __name__ == "__main__":
    main()