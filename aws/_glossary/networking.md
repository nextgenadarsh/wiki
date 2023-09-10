# Networking

CIDR: /8/16/17/18/28

## Private Network Ranges

| CIDR Block        | Start address     | End address
| --                | --                | --
|  10.0.0..0/8      | 10.0.0.8          | 10.255.255.255
| 172.16.0.0/12     | 172.16.0.0        | 172.31.255.255
| 192.168.0.0/16    | 192.168.0.0       | 192.168.255.255

- Machine on private network reach internet using NAT (Network Address Translation)
- [AWS Public IP Address Ranges - shows the service specific ranges](https://ip-ranges.amazonaws.com/ip-ranges.json)