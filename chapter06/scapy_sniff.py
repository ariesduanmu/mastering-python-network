from scapy.all import *

a = sniff(filter='icmp and host 192.168.2.100', count=5)
print(a.show())