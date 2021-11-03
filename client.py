#!/usr/bin/env python3
import socket
import asyncio

async def receiveReply(socket):
    try:
        socket.settimeout(2)
        response = socket.recvfrom(1024)
        print(response[0].decode())
    except Exception as e:
        print("timeout")

async def sendMessage(socket, address, port, message):
    socket.sendto(message.encode(), (address,port))


async def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = '127.0.0.1'
    server_port = 31337

    message = 'Hello World'
    while True:
        await sendMessage(client_socket, server_address, server_port, message)
        asyncio.create_task(receiveReply(client_socket))
        await asyncio.sleep(0.2)

asyncio.run(main())