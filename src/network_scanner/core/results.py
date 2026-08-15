"""Scan results container."""
class Results:
    def __init__(self):
        self.hosts = []

    def add(self, r):
        self.hosts.append(r)
