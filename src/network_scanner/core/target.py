"""Target representation."""
from dataclasses import dataclass


@dataclass
class Target:
    address: str
    hostname: str | None = None
    mac: str | None = None
