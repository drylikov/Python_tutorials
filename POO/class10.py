#!/usr/bin/python

class Animal:
    def __init__(self, name=''):
        self.name = name

    def hablar(self):
        pass

class Cat(Animal):
    def hablar(self):
        print "Meow"

class Perro(Animal):
    def hablar(self):
        print "Woof"

a = Animal()
a.hablar()

c = Cat('Sazy')
c.hablar()

d = Perro('R')
d.hablar()
