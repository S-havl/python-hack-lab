from scapy.all import sniff
from scapy.layers.inet import IP, TCP
from scapy.layers.http import HTTPRequest

def proccess_packet(packet):
    if packet.haslayer('IP'):
        protocolo = None

        if packet.haslayer(HTTPRequest):
           protocolo = "HTTP"
        elif packet.haslayer(TCP) and (packet[TCP].sport == 21 or packet[TCP].dport == 21):
           protocolo = "FTP"
        
        if protocolo:
            info_packet = (packet.summary(), protocolo)
            paquetes_capturados.append(info_packet)
            print(f"Paquete: {info_packet}")

paquetes_capturados = []

print("Iniciando sniffer...")

sniff(prn=proccess_packet, filter='ip', count=1000)

with open("informe_sniff.txt", "w") as informe:
    informe.write("Lista de paquetes capturados:\n")
    for paquete in paquetes_capturados:
        informe.write(f"{paquete}\n")


