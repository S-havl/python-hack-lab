import os
import re

def explorar_directorios(ruta_directorio, Extensiones_sospechosas=None, tamaño_minimo=None, patron_nombre=None):
    archivos_sospechosos = []

    for carpeta_raiz, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_raiz, archivo)

            if Extensiones_sospechosas:
                if not archivo.lower().endswith(tuple(Extensiones_sospechosas)):
                    continue

            if tamaño_minimo:
                tamaño_archivo = os.path.getsize(ruta_archivo)
                if tamaño_archivo < tamaño_minimo:
                    continue

            if patron_nombre:
                if not re.search(patron_nombre, archivo):
                    continue

            archivos_sospechosos.append(ruta_archivo)

    return archivos_sospechosos

def main():
    ruta = input("Ingrese la ruta a explorar: ")
    extensiones_sospechosas = ['.exe', '.jpg', '.bat', '.png', '.pptx', '.pdf']
    tamaño_minimo = 1024
    patron_nombre = r'(captura|juego|cheat)'

    archivos_sospechosos = explorar_directorios(ruta, extensiones_sospechosas, tamaño_minimo, patron_nombre)

    if archivos_sospechosos:
        print("Archivos sospechosos encontrado: ")
        for archivo in archivos_sospechosos:
            print(archivo)

    else:
        print("No se encontro algún archivo sospechoso.")

if __name__ == "__main__":
    main()


