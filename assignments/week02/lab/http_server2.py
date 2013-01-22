#!/usr/bin/env python

import socket
import email.utils
import time

host = '' # listen on all connections (WiFi, etc)
port = 50000
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) )
s.listen(backlog)

def httpdate():
    """Returns a date/time value in RFC1123 format"""
    now = time.gmtime()
    stamp = time.mktime(now)
    return email.utils.formatdate(stamp, False, True)

def ok_response(data):
    r = []
    r.append('HTTP/1.1 200 OK')
    r.append(httpdate())
    r.append('Content Type: text/html')
    r.append('Content Length: %i' % len(data))
    r.append('')
    r.append(data)

    return '\r\n'.join(r)

html = open('tiny_html.html', 'r').read()

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    request = client.recv(size)
    response = ok_response(html)
    if request: # if the connection was closed there would be no data
        print "received: "
        print request
        print 'sending: '
        print response
        client.send(response)
        client.close()
