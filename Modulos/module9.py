#!/usr/bin/python

"""
Un modulo conteniendo la funcion de
Fibonacci

"""

def fib(n):
    a , b = 0 , 1
    while b < n:
        print b,
        (a , b) = (b, a + b)

#prueba

if __name__ == '__main__':
    fib(500)
