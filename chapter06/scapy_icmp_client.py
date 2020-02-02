from scapy.all import *

ip = '192.168.2.101'
send(IP(dst=ip)/ICMP())
# response = sr1(IP(dst=ip)/ICMP())
# print(response)