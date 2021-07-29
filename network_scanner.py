# !/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # also we can do: arp_request.pdst = ip
    print(arp_request.summary())


scan("192.168.131.2/24")
# /24 is a common way of specifying the whole subnet
