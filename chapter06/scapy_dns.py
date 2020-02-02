from scapy.all import *

p = sr1(IP(dst='8.8.8.8')/UDP()/DNS(rd=1,qd=DNSQR(qname='www.baidu.com')))
print(p)