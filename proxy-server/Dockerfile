# Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    openvpn \
    iptables \
    && rm -rf /var/lib/apt/lists/*

RUN pip install mitmproxy

WORKDIR /app
COPY proxy.py .
COPY openvpn.conf /etc/openvpn/server.conf

EXPOSE 8080
EXPOSE 1194/udp

CMD ["sh", "-c", "openvpn --config /etc/openvpn/server.conf & mitmdump -s proxy.py --listen-port 8080 --set block_global=false"]
