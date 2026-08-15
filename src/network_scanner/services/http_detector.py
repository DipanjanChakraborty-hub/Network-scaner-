"""Simple HTTP detector."""

def is_http(port):
    return port in (80, 8080, 443)
