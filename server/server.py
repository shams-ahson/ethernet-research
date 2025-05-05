from scapy.all import *
import time

def handle_packet(pkt):
    if pkt.haslayer('UDP') and pkt[UDP].dport == 6000:
        vlan = pkt[Dot1Q].vlan if pkt.haslayer(Dot1Q) else 0
        msg = pkt[Raw].load.decode() if pkt.haslayer(Raw) else ""
        print(f"VLAN {vlan} received: {msg}")
        
        # Send response
        response = Ether()/Dot1Q(vlan=vlan)/IP(dst=pkt[IP].src)/UDP(sport=6000, dport=pkt[UDP].sport)/f"ACK: {msg}"
        sendp(response, iface="eth0")

print("Server started, waiting for packets...")
sniff(prn=handle_packet, filter="udp port 12345", iface="eth0")