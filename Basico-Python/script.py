"""
Script para imprimir valores de una funcion en unos pocos puntos.
La impresion solo se hace si el archivo es ejecutado como script, no
si es importado como modulo.

"""
import numpy as np

def f(x):
    """
    Una funcion cuadratica .
    """
    y = x**2 + 1.
    return y

def print_table():
    print "     x        f(x)"
    for x in np.linspace(0,4,3):
        print "%8.3f  %8.3f" % (x, f(x))

if __name__ == "__main__":
    print_table()
