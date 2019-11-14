from scapy.all import *

#a = Ether()/IP(src="10.2.4.10", dst="obtaincreds.cse545.rev.fish")/TCP(sport=1234,dport=13337,flags="S",seq=1234)
a = IP(src="10.0.1.20",dst="obtaincreds.cse545.rev.fish")/TCP(sport=1234,dport=13337)
a.show()
#send(a)
see = sr1(a)
print see
