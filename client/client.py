from scapy.all import *
import time
import random

def send_message(dst_ip="server", dst_port=6000, vlan_id=100):
    message = f"Automotive message {random.randint(1000,9999)}"
    pkt = Ether()/Dot1Q(vlan=vlan_id)/IP(dst=dst_ip)/UDP(sport=12345, dport=dst_port)/message
    sendp(pkt, iface="eth0")
    print(f"Sent: {message} to {dst_ip}")

while True:
    send_message()
    time.sleep(2)