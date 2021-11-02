#!/usr/bin/env python3
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '127.0.0.1'
server_port = 31337

message = 'Hello World'
client_socket.sendto(message.encode(), (server_address,server_port))
response = client_socket.recvfrom(1024)
print(response[0].decode())