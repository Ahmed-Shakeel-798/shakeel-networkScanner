# !/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary())
    # lists the packet summary

    scapy.ls(scapy.ARP())
    # lists all the available options of a class


scan("192.168.131.2/24")
# /24 is a common way of specifying the whole subnet
