#!/usr/bin/python

import time
import sys

def fib():
    a ,b = 0, 1
    while True:
        yield b
        a, b = b, a + b

iter = fib()

try:
    for i in iter:
       print i,
       time.sleep(1)
       sys.stdout.flush()
except KeyboardInterrupt:
    print "Operacion terminada"
