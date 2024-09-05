# Escriba la funcion count_words, la cual debe tomar como
# entrada un string y retornar el numero de palabras que este contiene.
# Se define a las palabras como a los strings de caracteres separados
# por espacios.

# Ademas escriba la funcion print_range, la cual debe tomar como entradas
# un string y ademas un entero inicio y uno fin. Con dichos enteros se
# debera imprimir el string dado en el rango inicio:fin-1

from urllib2 import urlopen


def count_words(words):
    #
    # YOUR CODE HERE.
    #


def print_range(words, start, end):
    #
    # YOUR CODE HERE.
    #


# Test 1
zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
"""
print count_words(zen_of_python)
#>>> 137
print_range(zen_of_python, 0, 30)
#>>> Beautiful is better than ugly.

print '\n', 50 * '=', '\n'

# Test 2

kitten = urlopen('http://placekitten.com/')
response = kitten.read()

print count_words(response)
#>>> 439
print_range(response, 559, 1000)
#>>> A little kitty. Surprise! :)
