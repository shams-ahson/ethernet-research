FROM python:3.9-slim
WORKDIR /app

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y \
    libpcap-dev \
    tcpdump \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

COPY client.py .
RUN pip install scapy

CMD ["python", "client.py"]