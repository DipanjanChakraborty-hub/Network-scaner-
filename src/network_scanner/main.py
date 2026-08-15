"""Entry point for the network scanner."""
from .core.scanner import Scanner


def main():
    print("Network scanner starter")
    s = Scanner()
    s.run()


if __name__ == "__main__":
    main()
