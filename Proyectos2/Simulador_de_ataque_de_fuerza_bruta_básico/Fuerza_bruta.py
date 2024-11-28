"""
Módulo para realizar fuerza bruta sobre una contraseña utilizando un diccionario.

Funciones:
- fuerza_bruta: Intenta adivinar una contraseña probando cada palabra del diccionario.
- main: Interfaz principal para recibir la contraseña objetivo y cargar el diccionario.

Características:
- Utiliza hilos (`threading`) para ejecutar el proceso principal.
- Incluye una interfaz gráfica para seleccionar el archivo del diccionario.

Dependencias:
- tkinter para selección de archivos.
- threading para manejar la ejecución principal.

Advertencias:
- Diseñado para aprendizaje y propósitos educativos, no para uso malicioso.
"""


import tkinter as tk
from tkinter import filedialog
import threading

def fuerza_bruta(contraseña, diccionario):
    for palabra in diccionario:
        if palabra == contraseña:
            print(f"Contraseña adivinada: {palabra}")
            return
    print("Contraseña no adivinada o encontrada en el diccionario.")

def main():
    pass_adivinar = input("Ingrese la contraseña a adivinar: ")
    root = tk.Tk()
    root.withdraw()

    diccionario = filedialog.askopenfilename(title="Selecione el diccionario")
    with open(diccionario, "r", encoding="utf-8") as diccionario:
        contenido = diccionario.read()
        palabras_diccionario = contenido.split()

    fuerza_bruta(pass_adivinar, palabras_diccionario)

hilo_main = threading.Thread(target=main)
hilo_main.start()
hilo_main.join()

