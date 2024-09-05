#!/usr/bin/python

import socket
name = "wwwax2.python.org"
try:
    host = socket.gethostbyname(name)
    print host
except socket.gaierror, err:
    print "No se encuentra el servidor:", name, err

