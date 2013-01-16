#-------------------------------------------------------------------------------
# Name:        add_server.py
# Purpose:
#
# Author:      Allen Su
#
# Created:     10/01/2013
# Copyright:   (c) allsu 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket
import sys

# Create a TCP/IP socket
server = socket.socket()

# Bind the socket to the port
server_address = ('localhost', 50000)
server.bind(server_address)

# Listen for incoming connections
server.listen(100)

try:

    while True:
        # Wait for a connection
        con, addr = server.accept()
        try:
            # Receive the data and send it back
            message = con.recv(4096)
            delimiter = ','
            num = message.split(delimiter)
            total = int(num[0]) + int(num[1])
            con.sendall(str(total))

        finally:
            # Clean up the connection
            con.close()

except KeyboardInterrupt:
    server.close()
    sys.exit()
