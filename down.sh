#!/bin/sh
iptables -t nat -D PREROUTING -i tun0 -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -D PREROUTING -i tun0 -p tcp --dport 443 -j REDIRECT --to-port 8080
