#!/usr/bin/python

class Animal:
    def __init__(self):
        print "Animalito creado"

    def whoAmI(self):
        print "Animalito!"

    def comer(self):
        print "Comer"

class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Perrito creado"

    def whoAmI(self):
        print "Perro"

    def ladrido(self):
        print "Woof!"

d = Perro()
d.whoAmI()
d.comer()
d.ladrido()
