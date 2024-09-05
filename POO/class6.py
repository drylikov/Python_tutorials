#!/usr/bin/python

class Circle:
    pi = 3.141592

    def __init__(self, radius=1):
        self.radius =  radius

    def area(self):
        return self.radius * self.radius *Circle.pi

    def sRadius(self, radius):
        self.radius = radius

    def gRadius(self):
        return self.radius

c = Circle()

c.sRadius(5)
print c.gRadius()
print c.area()
