from scapy.all import *
import sys

def tcp_scan(destination, dport):
	ans, unans = sr(IP(dst=destination)/TCP(sport=666,dport=dport,flags='S'))
	
	for sending, returned in ans:
		if 'SA' in str(returned[TCP].flags):
			return f"{destination} port {sending[TCP].dport} is open"
		else:
			return f"{destination} port {sending[TCP].dport} is not open"

print(tcp_scan('192.168.2.102',22))