#-------------------------------------------------------------------------------
# Name:        add_client.py
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

client = socket.socket()   # Create a TCP/IP socket

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)
client.connect(server_address)

try:
    # Send data
    num1 = raw_input('Please input the 1st integer number: ')
    num2 = raw_input('Please input the 2nd integer number: ')
    message = '%s,%s' % (num1, num2)
    client.sendall(message)

    # print the response
    print('%s + %s = %s') % (num1, num2, client.recv(4096))

finally:
    # close the socket to clean up
    client.close()
