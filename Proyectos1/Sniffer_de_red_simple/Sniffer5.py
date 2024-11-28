from scapy.all import sniff

def procesar_paquetes(paquete):

    if paquete.haslayer('IP'):
        ip_src = paquete['IP'].src
        ip_dst = paquete['IP'].dst

        if paquete.haslayer('TCP'):
            port_src = paquete['TCP'].sport
            port_dst = paquete['TCP'].dport
            protocolo = 'TCP'
        elif paquete.haslayer('UDP'):
            port_src = paquete['UDP'].sport
            port_dst = paquete['UDP'].dport
            protocolo = 'UDP'
        else:
            return
        
        paquete_info = (ip_src, ip_dst, port_src, port_dst, protocolo)
        Paquetes_capturados.append(paquete_info)

        print(f"Origen: {ip_src}:{port_src} -> Destino: {ip_dst}:{port_dst} (Protocolo): {protocolo}")

Paquetes_capturados = []
print("Iniciando sniff de red...")
sniff(prn=procesar_paquetes, filter='ip', count=30)
print("Sniff...finalizado.")

with open("Informe_sniff.text", "w") as informe:
    informe.write("Paquetes capturados en total (Ip_origen - Ip_destino - Puerto_origen - Puerto_destino - Protocolo)")
    for packet in Paquetes_capturados:
        informe.write(f"{packet}\n")

