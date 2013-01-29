#!/usr/bin/env python

import socket
import email.utils
import time
import os

host = '' # listen on all connections (WiFi, etc)
port = 50000
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

root_dir = 'web'

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) )
s.listen(backlog)

mime_types = {}
mime_types['html'] = 'text/html'
mime_types['htm'] = 'text/html'
mime_types['txt'] = 'text/plain'
mime_types['py'] = 'text/plain'
mime_types['jpg'] = 'image/jpg'
mime_types['jpeg'] = 'image/jpg'
mime_types['png'] = 'image/png'

def httpdate():
    """Returns a date/time value in RFC1123 format"""
    now = time.gmtime()
    stamp = time.mktime(now)
    return email.utils.formatdate(stamp, False, True)

def ok_response(data, extension = 'html'):
    r = []
    r.append('HTTP/1.1 200 OK')
    r.append(httpdate())
    type = mime_types.get(extension, 'text/plain')
    r.append('Content Type: %s' % type)
    r.append('Content Length: %i' % len(data))
    r.append('')
    r.append(data)

    return '\r\n'.join(r)

def client_error_response():
    msg = '400 Error: Bad Request.  This is not a supported request!'
    r = []
    r.append('HTTP/1.1 400 Bad Request')
    r.append(httpdate())
    r.append('Content Type: text/plain')
    r.append('Content Length: %i' % len(msg))
    r.append('')
    r.append(msg)

    return '\r\n'.join(r)

def notfound_response(URI):
    """
    returns an HTTP 404 Not Found Error response:

    URI is the name of the entity not found
    """
    resp = []
    resp.append('HTTP/1.1 404 Not Found')
    resp.append(httpdate())
    resp.append('Content-Type: text/plain')

    msg = "404 Error:\n %s \n not found"%( URI )

    resp.append('Content-Length: %i'%( len(msg) ) )
    resp.append('')
    resp.append(msg)

    return "\r\n".join(resp)

def format_dir_list(u):
    """Format the Directory Listing as HTML with links"""

    dir = os.path.join(root_dir, u)
    names = os.listdir(dir)

    dirs = []
    files = []

    for d in names:
        if os.path.isdir(os.path.join(dir, d)):
            dirs.append(d)
        elif os.path.isfile(os.path.join(dir, d)):
            files.append(d)

    html =[]
    html.append("<html> <body>")
    html.append("<h2>%s</h2>" % u)
    print "URI:", u
    if u: # don't need the parent dir at the root
        html.append('<a href="..">Parent</a>' )
    html.append("<h3>Directories:</h3>")
    html.append("  <ul>")
    for d in dirs:
        path = (os.path.join(u, d)).replace('\\', '/')
        html.append('    <li> <a href="%s">%s </a></li>' % (path, d))
    html.append("  </ul>")
    html.append("<h3>Files:</h3>")
    html.append("  <ul>")
    for f in files:
        path = (os.path.join(u, f)).replace('\\', '/')
        html.append('    <li> <a href="%s"> %s </a> </li>' % (path, f))
    html.append("  </ul>")
    html.append("</body> </html>")
    return "\n".join(html)

def get_time_page(u):
    """Return a HTML page with current time listed in GMT format"""
    time = httpdate()
    html = "<html>  <body>  <h1> %s </h1> </body> </html>" % time
    return html

def resolve_uri(u):
    """Takes the URI and analyze it and return the proper HTTP code"""
    URI = u.lstrip('/')
    if URI.lower() == 'time-page':
        response = ok_response(get_time_page(URI), 'html')
        print 'sending: '
        print response, '\r\n'
        client.send(response)
        client.close()
    else:
        filename = os.path.join(root_dir, URI)
        print 'The path requested is: %s' % filename
        if os.path.isfile(filename):
            data = open(filename, 'rb').read()
            ext = os.path.splitext(filename)[1].strip('.')
            response =  ok_response(data, ext)
            print 'sending: '
            print response, '\r\n'
            client.send(response)
            client.close()
        elif os.path.isdir(filename):
            data = format_dir_list(URI)
            response = ok_response(data, 'html')
            print 'sending: '
            print response, '\r\n'
            client.send(response)
            client.close()
        else:
            response = notfound_response(u) + '\r\nNo such resource exist!'
            print 'sending: '
            print response, '\r\n'
            client.send(response)
            client.close()
            raise ValueError('No such resource exist!')

def parse_request(request):
    """Parse a request and analyze the method, URI, and protocol, and return the proper response to the client"""
    data = open('tiny_html.html', 'r').read()
    lines = request.split('\r\n')

    method, URI, protocol = lines[0].split()

    if method != 'GET':
        response = client_error_response() + '\r\nThis server currently can only process GET request'
        print 'sending: '
        print response, '\r\n'
        client.send(response)
        client.close()
        raise ValueError('This server currently can only process GET request')
    elif protocol.split('/')[0] != 'HTTP':
        response =  client_error_response() + '\r\nThis server can only process HTTP request'
        print 'sending: '
        print response, '\r\n'
        client.send(response)
        client.close()
        raise ValueError('This server can only process HTTP request')
    else:
        print('URI requested is: %s') % URI
        resolve_uri(URI)

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    request = client.recv(size)
    if request: # if the connection was closed there would be no data
        print "received: "
        print request
        parse_request(request)

