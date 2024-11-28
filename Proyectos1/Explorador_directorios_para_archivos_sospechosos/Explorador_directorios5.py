import os
import re

def explorar_directorios(ruta_directorio, extensiones_sospechosas=None, tamaño_minimo=None):
    archivos_sospechosos = []

    for carpeta_raiz, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_raiz, archivo)

            if extensiones_sospechosas:
                if not archivo.lower().endswith(tuple(extensiones_sospechosas)):
                    continue

            if tamaño_minimo:
                tamaño_archivo = os.path.getsize(ruta_archivo)
                if tamaño_archivo < tamaño_minimo:
                    continue

            archivos_sospechosos.append(ruta_archivo)

    return archivos_sospechosos

def main():
    ruta = input("Ingrese la ruta a explorar: ")
    extensiones_sospechosas = ['.exe', '.bat', '.jpg', '.png']
    tamaño_minimo = 1024

    archivos_sospechosos = explorar_directorios(ruta, extensiones_sospechosas, tamaño_minimo)

    if archivos_sospechosos:
        print("Archivos sospechosos encontrados:")
        for archivo in archivos_sospechosos:
            print(archivo)

    else:
        print("No se encontraron archivos sospechosos.")

if __name__ == "__main__":
    main()