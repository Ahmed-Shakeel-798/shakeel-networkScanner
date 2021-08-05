# !/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # returns two lists we only need one

    # print(answered_list.summary()) | prints basic summary in easy words

    for element in answered_list:
        # print(element[1]) | simply printing this one would give unreadable data so use .show() method from scapy
        # print(element[1].show()) | The elements printed can also be viewed individually as follows
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("----------------------------------")


scan("192.168.131.1/24")