# ethernet-research

## About
Dockerized container simulating Automotive Ethernet client, server and Wireshark packet sniffer.

## Setup Instructions
To start, run
```bash
docker-compose up --build
```
After that, the containers should be up. If not, run 
```bash
docker-compose exec server python server.py
docker-compose exec client python client.py
```
You can find the captured packets (pcap) files in the ./captures directory. Existing captures are as follows: 
- auto_20250505_194211.pcap is full pcap with no filtering, showing client/server communication.
- auto_20250505_194343.pcap is filtered pcap for UDP traffic between client/server.
- auto_20250505_194651.pcap is filtered pcap for labeled client/server IP addresses.

To change filtering, go to wireshark/Dockerfile.