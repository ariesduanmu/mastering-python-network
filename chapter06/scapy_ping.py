from scapy.all import *

def icmp_ping(destination):
	ans, unans = sr(IP(dst=destination)/ICMP())
	return ans

def tcp_ping(destination, dport):
	ans, unans = sr(IP(dst=destination)/TCP(dport=dport, flags='S'))
	return ans

def udp_ping(destination):
	ans, unans = sr(IP(dst=destination)/UDP(dport=0))
	return ans

def answer_summary(answer_list):
	for sending, returned in answer_list:
		print(returned)
		returned.sprintf(f"{IP.src} is alive")

ip = '192.168.2.102'
port = 22
print("***ICMP Ping***")
ans = icmp_ping('192.168.2.101-102')
answer_summary(ans)
print("***TCP Ping***")
ans = tcp_ping(ip, port)
answer_summary(ans)
print("***UDP Ping***")
ans = udp_ping('192.168.2.101-102')
answer_summary(ans)