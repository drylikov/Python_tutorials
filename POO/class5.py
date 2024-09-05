#!/usr/bin/python

class Cat:
    specie = 'Miau'

    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('Sazy', 3)
cat2 = Cat('Kaperuz', 5)

print cat1.name, cat1.age
print cat2.name, cat2.age

print Cat.specie
print cat1.__class__.specie
print cat2.__class__.specie
