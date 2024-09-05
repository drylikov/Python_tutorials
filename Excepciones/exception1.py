#!/usr/bin/python

def input_numbers():
    a = float(raw_input("Ingresa un primer numero:"))
    b = float(raw_input("Ingresa un segundo numero:"))
    return a, b

x , y = input_numbers()

while True:
    try:
        print "%d / %d is %f" %(x ,y, x/y)
        break
    except ZeroDivisionError:
        print "No puedes dividir por cero"
        x , y = input_numbers()
