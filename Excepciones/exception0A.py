#!/usr/bin/python

def input_numbers():
    a = float(raw_input("Ingresa el primer numero:"))
    b = float(raw_input("Ingresa el segundo numero:"))
    return a, b

x ,y = input_numbers()

while True:
    if y != 0:
        print "%d /%d is %f" %(x ,y, x/y)
        break
    else:
        print "No se puede dividir por cero"
        x ,y = input_numbers()
