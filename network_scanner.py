# !/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("192.168.131.2/24")
# /24 is a common way of specifying the whole subnet
