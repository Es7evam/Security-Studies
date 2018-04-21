#!/bin/python2

import socket

target_host = "127.0.0.1" #Set localhost
target_port = 80

#create a socket object
# SOCK_DGRAM -> Specity it is and UDP connection
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("AAABBBCCC", (target_host, target_port))

#receive some Data
# since UDP is a connectionless protocol we need to specify the connect
data, addr = client.recvfrom(4096)

print data
