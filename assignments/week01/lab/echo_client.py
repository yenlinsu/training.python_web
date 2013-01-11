import socket
import sys

client = socket.socket()   # Create a TCP/IP socket

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)
client.connect(server_address)

try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    client.sendall(message)

    # print the response
    print(client.recv(4096))

finally:
    # close the socket to clean up
    client.close()
