# FROM ubuntu:22.04
# RUN apt-get update && apt-get install -y wireshark tshark
# RUN groupadd wireshark && usermod -aG wireshark root
# RUN chmod +x /usr/bin/dumpcap
# CMD ["tshark", "-i", "eth0"]


FROM ubuntu:22.04
RUN apt-get update && apt-get install -y tshark
RUN mkdir -p /captures
#change the line below -f for filtering
CMD ["sh", "-c", "tshark -i any -f 'host 172.20.0.10 and host 172.20.0.20' -w /captures/auto_$(date +%Y%m%d_%H%M%S).pcap"] 