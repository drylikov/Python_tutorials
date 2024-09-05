#!/usr/bin/python

import sys
import textwrap

sp = sorted(sys.path)
dname = ', '.join(sp)

print textwrap.fill(dname)
