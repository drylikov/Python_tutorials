#!/usr/bin/python

"""
Este es un modulo para usar dir() built

"""

import math, sys

version = 1.0

names = ['Python', 'C', 'JavaScript', 'Java']

def mostrar_names():
    for i in names:
        print i

print dir(sys.modules['__main__'])
