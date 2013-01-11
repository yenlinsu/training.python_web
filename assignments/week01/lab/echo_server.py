import socket
import sys

# Create a TCP/IP socket
server = socket.socket()

# Bind the socket to the port
server_address = ('localhost', 50000)
server.bind(server_address)

# Listen for incoming connections
server.listen(100)

while True:
    # Wait for a connection
    con, addr = server.accept()
    try:
        # Receive the data and send it back
        message = con.recv(4096)
        con.sendall(message)

    finally:
        # Clean up the connection
        con.close()
