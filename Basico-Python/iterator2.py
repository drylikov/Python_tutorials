#!/usr/bin/python

f = open('file1.txt', 'r')

for line in f:
    print line,

f.close()
