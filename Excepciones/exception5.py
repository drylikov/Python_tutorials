#!/usr/bin/python

class B_Error(Exception):
    def __init__(self, value):
        print "B_Error:B caracter encontrado en la posicion %d" %value

cadena = " Aprender a programar en Python Basico"

pos = 0
for i in cadena:
    if i == 'B':
        raise B_Error, pos
    pos = pos + 1
