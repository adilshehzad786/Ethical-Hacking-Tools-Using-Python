import time

print("Please Allow to Continue ")

time.sleep(2)
import nmap


scanner=nmap.PortScanner()

print("Welcome to NMAP Port Scanner ")
print("------------------------------")
ip_address=raw_input("Please Enter The Ip Address:")

print("The IP Address is :", ip_address)

type(ip_address)

resp=raw_input("""\n Please Enter the Type of Scan You want to PErform

    1. SYN ACK Scan
    2. UDP Scan
    3. Comprehensive Scan \n 
    > """)

print("You Have Selected Following Option ",resp)

if resp =='1':
    print("Nmap Version",scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP Status : ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports:",scanner[ip_address]['tcp'].keys())

elif resp =='2':

    print("Nmap Version :",scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("Ip Status:",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Opne Ports:",scanner[ip_address]['udp'].keys())

elif resp=='3':
    print("Nmap Version :",scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sU -sV -sS -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status:",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Opne Ports:",scanner[ip_address]['tcp'].keys())

elif resp >=4:
    print("Invalid Entry")
