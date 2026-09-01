from mitmproxy import http

def request(flow):
    print(f"[REQUEST] {flow.request.method} {flow.request.pretty_url}")
    print(f"[HEADERS] {flow.request.headers}")
    if flow.request.content:
        print(f"[BODY] {flow.request.content.decode('utf-8', errors='ignore')}")
    print("---")

def response(flow):
    print(f"[RESPONSE] {flow.response.status_code}")
    print(f"[HEADERS] {flow.response.headers}")
    if flow.response.content:
        print(f"[BODY] {flow.response.content.decode('utf-8', errors='ignore')}")
    print("---")
