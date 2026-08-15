"""Port range parser."""

def parse_ports(text):
    # naive parser for ranges like "1-1024"
    if "-" in text:
        a,b = text.split("-",1)
        return list(range(int(a), int(b)+1))
    return [int(p) for p in text.split(',') if p]
