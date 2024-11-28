import socket
import threading
import tkinter as tk
from tkinter import PhotoImage
import platform
from pathlib import Path
import os

Desktop_windows = Path.home() / "Desktop"
Desktop_linux = os.environ.get("XDG_DESKTOP_DIR", os.path.join(os.path.expanduser("~"), "Desktop"))

common_ports = {
    20: "FTP", 
    21: "FTP", 
    22: "SSH", 
    23: "Telnet", 
    25: "SMTP", 
    53: "DNS", 
    80: "HTTP", 
    110: "POP3", 
    143: "IMAP", 
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

def scan_port(address_ip, port):
    objetive = (address_ip, port)
    SO = platform.system()

    if SO == 'Windows':
        ruta = os.path.join(Desktop_windows, "Informe_scan.txt")
    elif SO == 'Linux':
        ruta = os.path.join(Desktop_linux, "Informe_scan.txt")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conecction_test:
            conecction_test.settimeout(1)
            result = conecction_test.connect_ex(objetive)
            if result == 0:
                service = common_ports.get(port, "Unknown service") 
                with open(ruta, "a") as informe:
                    informe.write("Informe:")
                    informe.write("Iniciando escáneo de puertos:")
                    informe.write(f"Port: {port} open -> Service: {service}\n")
            else:
                with open(ruta, "a") as informe:
                    informe.write(f"Port: {port}: filtered or closed\n")
    
    except socket.error as e:
        with open(ruta, "a") as informe:
            informe.write(f"Port: {port} - Error desconocido: {e}\n")
            

def scan_ports(address_ip, since, to):
    threads = []
    for port in range(since, to):
        thread = threading.Thread(target=scan_port, args=(address_ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

ventana = tk.Tk()
ventana.title("Escáner de puertos")
ventana.geometry("400x300")
ventana.resizable(False, False)
ventana.configure(bg="gray")
icono = PhotoImage(file="/home/ValentinyLarry/Desktop/PythonArchivements/Perfil.png")
ventana.iconphoto(True, icono)
#------------------------------------------------------------------------------------------
label_IP = tk.Label(ventana, text="Ingrese la dirección IP a escánear:", bg="Gray", fg="Black", font=("Arial", 100))
port_inicial = tk.Label(ventana, text="Ingrese el puerto inicial:", bg="Gray", fg="Black", font=("Arial", 100))
port_final = tk.Label(ventana, text="Ingrese el puerto final:", bg="Gray", fg="Black", font=("Arial", 100))
entrada_IP = tk.Entry(ventana, width=30, bg="Black", fg="Green")
port_inicial_entrada = tk.Entry(ventana, width=30, bg="Black", fg="Green")
port_final_entrada = tk.Entry(ventana, width=30, bg="Black", fg="Green")
boton_scan = tk.Button(ventana, text="Iniciar escáneo", bg="Black", fg="Green", command=lambda: scan_ports(entrada_IP.get(), int(port_inicial_entrada.get()), int(port_final_entrada.get())))
by = tk.Label(ventana, text="By S-havl", bg="Gray", fg="Purple")
#------------------------------------------------------------------------------------------
entrada_IP.place(x=50, y=50)
port_inicial_entrada.place(x=50, y=90)
port_final_entrada.place(x=50, y=130)
label_IP.place(x=20, y=30)
port_inicial.place(x=20, y=70)
port_final.place(x=20, y=110)
boton_scan.place(x=140, y=210)
by.place(x=170, y=280)
ventana.mainloop()

   
    


