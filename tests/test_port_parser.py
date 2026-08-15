from src.network_scanner.ports.port_parser import parse_ports


def test_parse_range():
    assert 80 in parse_ports('1-1024')
