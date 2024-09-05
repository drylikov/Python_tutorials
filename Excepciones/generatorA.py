#!/usr/bin/python

def una_funcion():
    for i in xrange(4):
        yield i

for i in una_funcion():
    print i
