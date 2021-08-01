# !/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

    # broadcast mac address is a virtual mac address that doesn't really exists but when
    # you send something to it, all clients on the network will receive it

    arp_request.show()
    broadcast.show()

    # combination of both packets we created above, so ir contains an Ether part and an ARP part
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
    # print(arp_request_broadcast.summary())


scan("192.168.131.2/24")