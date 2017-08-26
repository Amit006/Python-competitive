# owning  A network with scapy
from scapy.all import *
# our packet Call back
def packet_callback(packet):
	print packet.show()

# fire up our sniffer 	
sniff(prn=packet_callback,count=1) 