#!usr/bin/python

def input_numbers():
    a = float(raw_input("Ingresa el primer numero:"))
    b = float(raw_input("Ingresa el segundo numero:"))
    return a, b

x, y = input_numbers()
print "%d / %d is %f"%(x, y, x/y)
