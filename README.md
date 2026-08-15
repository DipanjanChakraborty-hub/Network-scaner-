# Network-scaner-
                 ┌─────────────────┐
                 │    CLI / API    │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │  Scan Manager   │
                 └────────┬────────┘
                          │
             ┌────────────┼────────────┐
             │            │            │
      ┌──────▼─────┐ ┌────▼─────┐ ┌───▼────────┐
      │ Discovery  │ │Port Scan │ │Fingerprint │
      └──────┬─────┘ └────┬─────┘ └───┬────────┘
             │            │           │
             └────────────┼───────────┘
                          │
                 ┌────────▼────────┐
                 │ Service Engine  │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │  Risk Engine    │
                 └────────┬────────┘
                          │
                ┌─────────▼─────────┐
                │  Report Generator │
                └───────────────────┘

                NETWORK SCANNER
────────────────────────────────────────

Target: 192.168.1.10
Status: UP
Latency: 2.4 ms
MAC: XX:XX:XX:XX:XX:XX

OPEN PORTS
────────────────────────────────────────

PORT     STATE      SERVICE
22       OPEN       SSH
80       OPEN       HTTP
443      OPEN       HTTPS
3306     OPEN       MySQL

SERVICE INFORMATION
────────────────────────────────────────

22/tcp    OpenSSH
80/tcp    Apache HTTP Server
443/tcp   HTTPS
3306/tcp  MySQL

RISK SUMMARY
────────────────────────────────────────

High       0
Medium     1
Low        2
Info       3