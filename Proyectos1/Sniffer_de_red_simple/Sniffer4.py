from scapy.all import sniff

def capturar_paquetes(paquete):

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
        
        info_paquete = (ip_src, ip_dst, port_src, port_dst, protocolo)
        Packets_capturados.append(info_paquete)

        print(f"Origen: {ip_src}:{port_src} -> Destino: {ip_dst}:{port_dst} (Protocolo): {protocolo}")

Packets_capturados = []

print("Iniciando captura de paquetes...")
sniff(prn=capturar_paquetes, filter='ip', count=30)