#!/usr/bin/python

class Seq1:
    def __init__(self):
        self.x = 0

    def next(self):
        self.x += 1
        if self.x > 14:
            raise StopIteration
        return self.x**self.x

    def __iter__(self):
        return self

s = Seq1()

for i in s:
    print i
