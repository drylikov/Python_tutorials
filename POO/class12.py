#!/usr/bin/python

class Vector:
    
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

    def __add__(self,otro):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] + otro.data[j])

        return Vector(data)

    def __sub__(self, otro):
        data =[]
        for j in range(len(self.data)):
            data.append(self.data[j] - otro.data[j])

        return Vector(data)

x = Vector([1,4,8])
y = Vector([3,0, 2])
print x + y
print y - x
