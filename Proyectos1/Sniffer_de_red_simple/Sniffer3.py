from scapy.all import sniff

def procesar_paquetes(packet):

    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst

        if packet.haslayer('TCP'):
            port_src = packet['TCP'].sport
            port_dst = packet['TCP'].dport
            protocolo = 'TCP'
        elif packet.haslayer('UDP'):
            port_src = packet['UDP'].sport
            port_dst = packet['UDP'].dport
            protocolo = 'UDP'
        else:
            return
        
        packet_info = (ip_src, ip_dst, port_src, port_dst, protocolo)
        capturar_paquetes.append(packet_info)

        print(f"Origen: {ip_src}:{port_src} -> Destino: {ip_dst}:{port_dst} (Protocolo): {protocolo}")

capturar_paquetes = []

print("Iniciando sniff de red...")
sniff(prn=procesar_paquetes, filter='ip', count=20)
