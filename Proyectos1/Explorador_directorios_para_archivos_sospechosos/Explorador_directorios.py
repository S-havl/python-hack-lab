import os
import re

def explorar_directorio(ruta_directorio, extensiones_sospechosas=None, tamaño_minimo=None, patron_nombre=None):
    archivos_sospechosos = []

    for carpeta_raíz, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_raíz, archivo)

            if extensiones_sospechosas:
                if not archivo.lower().endswith(tuple(extensiones_sospechosas)):
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
    ruta = input("Introduce la ruta del directorio a explorar: ")

    extensiones_sospechosas = ['.exe', '.bat', '.vbs', '.dll']
    tamaño_minimo = 1024
    patron_nombre = r'(malware|virus|hack)'

    archivos_sospechosos = explorar_directorio(ruta, extensiones_sospechosas, tamaño_minimo, patron_nombre)

    if archivos_sospechosos:
        print("Archivos sospechosos encontrados: ")
        for archivo in archivos_sospechosos:
            print(archivo)

    else:
        print("No se encontraron archivos sospechosos.")

if __name__ == "__main__":
    main()