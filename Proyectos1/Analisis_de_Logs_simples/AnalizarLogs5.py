import re
from datetime import datetime

def analizar_logs(archivo_log, tipo_evento=None, buscar_palabra=None, desde_fecha=None, hasta_fecha=None):

    with open(archivo_log, "r") as archivo:
        for linea in archivo:
            match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (.+)", linea)
            if match:
                fecha, tipo, mensaje = match.groups()
                fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")

                if tipo_evento and tipo != tipo_evento.upper():
                    continue

                if buscar_palabra and buscar_palabra.lower() not in mensaje.lower():
                    continue

                if desde_fecha and fecha < desde_fecha:
                    continue

                if hasta_fecha and fecha > hasta_fecha:
                    continue

                print(f"{fecha} - {tipo} - {mensaje}")

if __name__ == "__main__":
    tipo_evento = "ERROR"
    buscar_palabra = "acceso"
    desde_fecha = datetime(2024, 10, 8, 14, 20)
    hasta_fecha = datetime(2024, 10, 8, 14, 24)

    analizar_logs("ejemplo_log.text", tipo_evento, buscar_palabra, desde_fecha, hasta_fecha)