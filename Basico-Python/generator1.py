#!/usr/bin/python

def gen():
    x, y = 1,2
    yield x, y
    x += 1
    yield x, y

it = gen()

print it.next()
print it.next()

try:
    print it.next()
except StopIteration:
    print "Iteracion terminada"

