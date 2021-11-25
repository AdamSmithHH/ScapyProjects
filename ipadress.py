from scapy.all import *

ip = get_if_addr(conf.iface)
ip = get_if_addr("eth0")
print(ip)