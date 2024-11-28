from scapy.all import sniff

def process_packet(packet):

    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst

        if packet.haslayer('TCP'):
            port_src = packet['TCP'].sport
            port_dst = packet['TCP'].dport
            protocol = 'TCP'
        elif packet.haslayer('UDP'):
            port_src = packet['UDP'].sport
            port_dst = packet['UDP'].dport
            protocol = 'UDP'
        else:
            return
        
        packet_info = (ip_src, ip_dst, port_src, port_dst, protocol)
        captured_packets.append(packet_info)

        print(f"Origen: {ip_src}:{port_src} -> Destino: {ip_dst}:{port_dst} (Protocolo:) {protocol}")

captured_packets = []

print("Iniciando sniffer de red...")
sniff(prn=process_packet, filter="ip", count=10)