#!/usr/bin/env python3
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '10.147.18.58'
server_port = 31337
client_socket.connect((server_address, server_port))

message = 'Hello World'
client_socket.sendto(message.encode(), ("127.0.0.1",31337))
response = client_socket.recvfrom(1024)
print(response[0].decode())