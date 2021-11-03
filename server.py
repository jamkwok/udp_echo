import socket
import time
import asyncio

async def echo(socket):
	payload, client_address = socket.recvfrom(1024)
	await asyncio.sleep(10)
	print("Echoing data back to " + str(client_address))
	socket.sendto(payload, client_address)

async def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server_address = '0.0.0.0'
	server_port = 31337

	server = (server_address, server_port)
	sock.bind(server)
	print("Listening on " + server_address + ":" + str(server_port))

	while True:
		await asyncio.sleep(0.1)
		asyncio.create_task(echo(sock))

asyncio.run(main())