import socket

# Created a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Specifying the server address and port number
server_address = ('127.0.0.1', 12345)

# Send a message to the server
message = 'Hello, UDP server!'
print('Sending message: {}'.format(message))
sock.sendto(message.encode(), server_address)

# Receive an acknowledgment from the server
print('\nWaiting to receive acknowledgment...')
data, address = sock.recvfrom(4096)
print('Received {} bytes from {}:'.format(len(data), address))
print(data.decode())

# Close the socket
sock.close()
