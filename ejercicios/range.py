# -*- coding: utf-8 -*-

# El rango de un conjunto de valores es el valor máximo menos el mínimo
# valor. Definir el procedimiento, set_range, que devuelve el rango para
# tres entradas: a, b y c.


def set_range
    #
    # Your code here
    #


def write_in_file(filename, result):
    f = open(filename, 'w')
    f.write(str(result))
    f.close()


# Tests.

result1 = set_range(10, 4, 7)
print result1
write_in_file('rango1.txt', result1)
# >>> 6  # since 10 - 4 = 6

result2 = set_range(1.1, 7.4, 18.7)
print result2
write_in_file('rango2.txt', result2)
# >>> 17.6 # since 18.7 - 1.1 = 17.6
