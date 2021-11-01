#!/usr/bin/env python3
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '0.0.0.0'
server_port = 31337
client_socket.connect((server_address, server_port))

message = 'Hello World'
client_socket.send(message.encode())
response = client_socket.recv(1024).decode()
print("Test passed" if message == response else "Test failed")