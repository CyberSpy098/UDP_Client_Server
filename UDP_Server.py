import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Specifying the socket to a specific address and port
server_address = ('127.0.0.1', 12345)
sock.bind(server_address)

print('UDP server is up and listening on {}'.format(server_address))

while True:
    # receive data from a client
    print('\nWaiting to receive message...')
    data, address = sock.recvfrom(4096)

    # print the received data
    print('Received {} bytes from {}:'.format(len(data), address))
    print(data.decode())

    # send back a response message to the client
    message = 'Acknowledged, Hi UDP Client'
    sock.sendto(message.encode(), address)

