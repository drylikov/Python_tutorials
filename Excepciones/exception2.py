#!/usr/bin/python

try:
    3/0

except ZeroDivisionError, e:
    print "No se puede dividir por cero"
    print "Mensaje:", e.message
    print "Class:", e.__class__
