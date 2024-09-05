#!/usr/bin/python

import sys

class Object:
    def __init__(self):
        pass
    def examine(self):
        print self

o = Object()

print dir(o)
print dir([])
print dir({})
print dir(1)
print dir()
print dir(len)
print dir(sys)
print dir("Cadena")
