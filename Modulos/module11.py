#!/usr/bin/python
import sys
import textwrap


def myfun():
    pass

gl = globals()
gnames = ' , '.join(gl)

print textwrap.fill(gnames)
