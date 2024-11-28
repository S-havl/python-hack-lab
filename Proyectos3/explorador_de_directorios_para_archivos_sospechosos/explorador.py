import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
import subprocess

def seleccionar_directorio():
    ventana = tk.Tk()
    ventana.withdraw()
    directorio = filedialog.askdirectory(initialdir="/home", title="Directorio a explorar")
    if not directorio:
        messagebox.showinfo("Información", "No seleccionó ningún directorio.")
    
    return directorio

def identificar_patrones(directorio):
   archivos_sospechosos = []
   patron_virus = r'.*\.(exe|bat|cmd|vbs|js|wsf|scr|pif|msc|jar|ps1|dll|zip|rar|7z|sh|py|pl|php|bin|run|appimage|tar\.gz|deb|rpm|so|o)$'
   regex = re.compile(patron_virus)
   
   for raiz, _, archivos in os.walk(directorio):
       for archivo in archivos:
           if regex.match(archivo):
               archivos_sospechosos.append(os.path.join(raiz, archivo))

   return archivos_sospechosos

def mostrar_resultados(archivos_sospechosos):
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, "archivos_sospechosos.txt")
    try:
        if archivos_sospechosos:
            with open(ruta_archivo, "w") as informe:
                for archivo in archivos_sospechosos:
                    informe.write(f"{archivo}\n")

            messagebox.showinfo("Resultados", f"Se encontraron {len(archivos_sospechosos)} archivos sospechosos."
                                              f"Revisa el archivo: {ruta_archivo}")

        else:
            messagebox.showinfo("Resultados", "No se encontraron archivos sospechosos.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el archivo de resultados: {e}")
        
def main():
    directorio = seleccionar_directorio()
    if directorio:
        archivos_sospechosos = identificar_patrones(directorio)
        mostrar_resultados(archivos_sospechosos)

if __name__ == "__main__":
    main()

