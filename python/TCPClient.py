#!/bin/python2
import socket

target_host = "www.google.com"
target_port = 80

#create socket object
# AF_INET -> Say that we use IPv4 address or hostname
# SOCK_STREAM -> Indicate this will be a TCP connection.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client
client.connect((target_host, target_port))

#send Data
client.send("GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

#receive data
response = client.recv(4096) #recv 4096 bytes

print response
