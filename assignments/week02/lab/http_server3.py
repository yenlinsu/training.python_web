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

def client_error_response(method, protocol):
    msg = '400 Error: Bad Request.  Either %s or %s is not a supported request' % (method, protocol.split('/')[0])
    r = []
    r.append('HTTP/1.1 400 Bad Request')
    r.append(httpdate())
    r.append('Content Type: text/html')
    r.append('Content Length: %i' % len(msg))
    r.append('')
    r.append(msg)

    return '\r\n'.join(r)

def parse_request(r, h):
    """Parse a request and returns a URL"""
    lines = r.split('\r\n')

    method, URI, protocol = lines[0].split()

    print('URI requested is: %s') % URI

    if method != 'GET':
        response = client_error_response(method, protocol)
        print 'sending: '
        print response
        client.send(response)
        client.close()
        raise ValueError('This server currently can only process GET request')
    elif protocol.split('/')[0] != 'HTTP':
        response =  client_error_response(method, protocol)
        print 'sending: '
        print response
        client.send(response)
        client.close()
        raise ValueError('This server can only process HTTP request')
    else:
        return ok_response(h)

html = open('tiny_html.html', 'r').read()

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    request = client.recv(size)
    if request: # if the connection was closed there would be no data
        print "received: "
        print request
        response = parse_request(request, html)
        print 'sending: '
        print response
        client.send(response)
        client.close()
