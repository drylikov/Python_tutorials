#!/usr/bin/python

class M:
    def __init__(self):
        self.name = "M"

    def gName(self):
        return self.name

m = M()

print m.gName()
print M.gName(m)
