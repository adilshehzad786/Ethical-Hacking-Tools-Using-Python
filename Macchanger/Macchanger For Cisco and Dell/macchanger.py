import re

import subprocess
from random import choice,randint

print ('                                                                    ')
print ('                                                                    ')
print ('            #################################################       ')
print ('            #                                               #       ')
print ('            #                 Mac Changer                  #       ')
print ('            #                                               #       ')
print ('            #               created By AdilShehzad          #       ')


print ('            #################################################       ')

print ('                                                                    ')

print("Mac Changer Only For Dell & Cisco")


def mac_random():
    
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])
    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = (str(one + two))
        mac_address.append(three)
    return ":".join(mac_address)


def change_mac(interface, new_mac):
    """Use Linux commands to change the mac"""
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(interface) +
                     " hw ether " + str(new_mac) + " "], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)


def CurrentMac():
   
    output = subprocess.check_output(["ifconfig " +
                                      args.interface], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
return current_mac