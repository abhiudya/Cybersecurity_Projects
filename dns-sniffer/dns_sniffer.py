from scapy.all import sniff, DNSQR, DNS

def process_packet(packet):
if packet.haslayer(DNSQR):
print(f"[+] DNS Request: {packet[DNSQR].qname.decode()}")

sniff(filter="udp port 53", prn=process_packet, store=False)