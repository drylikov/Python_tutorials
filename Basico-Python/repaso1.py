# Comentarios de una linea comienzan con una almohadilla 
""" Strings multilinea pueden escribirse
    usando tres "'s, y comunmente son usados
    como comentarios.
"""

# 1. Tipos de datos primitivos y operadores.
# numeros
3 #=> 3

#Operaciones matematicas
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# La division es un poco complicada. Es division entera y toma la parte entera
# de los resultados automaticamente.
5 / 2 #=> 2

# Para arreglar la division necesitamos aprender sobre 'floats'
# (numeros de coma flotante).
2.0     # Esto es un 'float'
11.0 / 4.0 #=> 2.75 

# Refuerza la precedencia con parentesis
(1 + 3) * 2 #=> 8

# Valores 'boolean' (booleanos) en python 
True
False

# Negamos  con 'not'
not True #=> False
not False #=> True

# Igualdad es ==
1 == 1 #=> True
2 == 1 #=> False

# Desigualdad es !=
1 != 1 #=> False
2 != 1 #=> True

# Mas comparaciones
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

#Las comparaciones pueden ser concatenadas
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

# Las cadenas se crean con " o '
"Esto es un cadena."
'Esto tambien es una cadena' 

# Las cadenas  tambien pueden ser sumadas
"Hola " + "mundo!" #=> "Hola mundo!"

# Un cadena  puede ser tratado como una lista de caracteres
"Esto es una cadena"[0] #=> 'E'

# % pueden ser usados para formatear cadenas, como esto:
"%s pueden ser %s" % ("cadenas", "interpolados")

# Una forma mas reciente de formatear cadenas es el metodo 'format'.
# Este metodo es la forma preferida
"{0} pueden ser {1}".format("cadenas", "formateados")
# Puedes usar palabras claves si no quieres contar.
"{nombre} quiere comer {comida}".format(nombre="Cesar", comida="ceviche")

# None es un objeto
None #=> None

# No uses el simbolo de igualdad `==` para comparar objetos con None
# Usa `is` en lugar de
"etc" is None #=> False
None is None  #=> True

# El operador 'is' prueba la identidad del objeto. Esto no es
# muy util cuando se trata de datos, pero es
# muy util cuando se trata de objetos.

# None, 0, y cadenas/listas vacias, todas se evaluan como False.
# Todos los otros valores son True
0 == False  #=> True
"" == False #=> True


# 2. Variables y Colecciones

# Imprimir cosas 
print "Soy Python. Soy un poderoso lenguaje, mucho gusto"


# No hay necesidad de declarar las variables antes de asignarlas.
una_variable = 5    # La convencion es usar guiones_bajos_con_minusculas
una_variable #=> 5

# Acceder a variables no asignadas previamente es una excepcion.
otra_variable  # Levanta un error de nombre

# 'if' puede ser usado como una expresion
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"

# Listas sobre secuencias
lista = []
# Puedes empezar con una lista prellenada
otra_lista = [4, 5, 6]

# Agregamos  cosas al final de una lista con 'append'
lista.append(1)    #lista ahora es [1]
lista.append(2)    #lista ahora es [1, 2]
lista.append(4)    #lista ahora es [1, 2, 4]
lista.append(3)    #lista ahora es [1, 2, 4, 3]
# Remueve del final de la lista con 'pop'
lista.pop()        #=> 3 y lista ahora es [1, 2, 4]
# Pongamoslo de vuelta
lista.append(3)    # Nuevamente lista ahora es [1, 2, 4, 3].

# Accede a una lista como lo harias con cualquier arreglo
lista[0] #=> 1
# Mira el ultimo elemento
lista[-1] #=> 3

# Mirar fuera de los limites es un error 'IndexError'
lista[4] # Levanta la excepcion IndexError

# Puedes mirar por rango con la sintaxis de una parte de la lista 
lista[1:3] #=> [2, 4]
# Omite el inicio
lista[2:] #=> [4, 3]
# Omite el final
lista[:3] #=> [1, 2, 4]

# Remueve elementos arbitrarios de una lista con 'del'
del lista[2] # lista ahora es [1, 2, 3]

# Puedes sumar listas
lista + otra_lista #=> [1, 2, 3, 4, 5, 6] - Nota: lista y otra_lista no se tocan

# Concatenar listas con 'extend'
lista.extend(otra_lista) # lista ahora es [1, 2, 3, 4, 5, 6]

# Chequea la existencia en una lista con
1 in lista #=> True

# Examina el largo de una lista con 'len'
len(lista) #=> 6


# Tuplas son como listas pero son inmutables.
tupla = (1, 2, 3)
tupla[0] #=> 1
tupla[0] = 3  # Levanta un error TypeError

# Tambien puedes hacer todas esas cosas que haces con listas
len(tupla) #=> 3
tupla + (4, 5, 6) #=> (1, 2, 3, 4, 5, 6)
tupla[:2] #=> (1, 2)
2 in tupla #=> True

# Puedes desempacar tuplas (o listas) en variables
a, b, c = (1, 2, 3)     # a ahora es 1, b ahora es 2 y c ahora es 3
# Tuplas son creadas por defecto si omites los parentesis
d, e, f = 4, 5, 6
# Ahora mira que facil es intercambiar dos valores
e, d = d, e     # d ahora es 5 y e ahora es 4


# Diccionarios almacenan mapeos
dicc_vacio = {}
# Aqui esta un diccionario prellenado
dicc_1 = {"uno": 1, "dos": 2, "tres": 3}

# Busca valores con []
dicc_1["uno"] #=> 1

# Obten todas las llaves como una lista
dicc_1.keys() #=> ["tres", "dos", "uno"]
# Nota - El orden de las llaves del diccionario no esta garantizada.

# Obten todos los valores como una lista
dicc_1.values() #=> [3, 2, 1]
# Nota - Lo mismo que con las llaves, no se garantiza el orden.

# Verifica la existencia de una llave en el diccionario con 'in'
"uno" in dicc_1 #=> True
1 in dicc_1 #=> False

# Buscar una llave inexistente deriva en KeyError
dicc_1["cuatro"] # KeyError

# Usa el metodo 'get' para evitar la excepcion KeyError
dicc_1.get("uno") #=> 1
dicc_1.get("cuatro") #=> None
# El metodo 'get' soporta un argumento por defecto cuando el valor no existe.
dicc_1.get("uno", 4) #=> 1
dicc_1.get("cuatro", 4) #=> 4

# El metodo 'setdefault' es una manera segura de agregar nuevos pares
# llave-valor en un diccionario
dicc_1.setdefault("cinco", 5) #dicc_1["cinco"] es puesto con valor 5
dicc_1.setdefault("cinco", 6) #dicc_1["cinco"] todavia es 5


# Sets (conjuntos) almacenan  conjuntos
conjunto_vacio = set()
# Inicializar un conjunto con monton de valores
un_conjunto = set([1,2,2,3,4]) # un_conjunto ahora es set([1, 2, 3, 4])

# Desde Python 2.7, {} puede ser usado para declarar un conjunto
conjunto_1 = {1, 2, 2, 3, 4} # => {1 2 3 4}

# Agregamos  mas valores a un conjunto
conjunto_1.add(5) # conjunto_1 ahora es {1, 2, 3, 4, 5}

# Haz interseccion de conjuntos con &
otro_conjunto = {3, 4, 5, 6}
conjunto_1 & otro_conjunto #=> {3, 4, 5}

# Haz union de conjuntos con |
conjunto_1 | otro_conjunto #=> {1, 2, 3, 4, 5, 6}

# Haz diferencia de conjuntos con -
{1,2,3,4} - {2,3,5} #=> {1, 4}

# Verifica la existencia en un conjunto con 'in'
2 in conjunto_1 #=> True
10 in conjunto_1 #=> False


# 3. Control de Flujo

# Creamos  una variable
una_variable = 5

# Aqui  una declaracion  'if'. La indentacion es significativa en Python!

# imprime "una_variable es menor que 10"
if una_variable > 10:
    print "una_variable es mas grande que 10."
elif una_variable < 10:    # Este condicion 'elif' es opcional.
    print "una_variable es menor  que 10."
else:           # Esto tambien es opcional.
    print "una_variable es de hecho 10."


"""
For itera sobre listas
imprime:
   Python es un lenguaje
   JavaScript es un lenguaje
   C es un lenguaje 
"""
for leng  in ["Python", "JavaScript", "C"]:
    # Puedes usar % para interpolar cadenas  formateadas
    print "%s es un lenguaje" %leng 

"""
`range(numero)` retorna una lista de numeros
desde cero hasta el numero dado
imprime:
    0
    1
    2
    3
"""
for i in range(4):
    print i

"""
While itera hasta que una condicion no se cumple.
imprime:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print x
    x += 1  # version corta de x = x + 1

# Maneja excepciones con un bloque try/except

# Funciona desde Python 2.6 en adelante:
try:
    # Usa raise para levantar un error
    raise IndexError("Este es un error de indice")
except IndexError as e:
    pass    # Pass no hace nada. Usualmente harias alguna recuperacion aqui.


# 4. Funciones

# Usa 'def' para crear nuevas funciones
def add(x, y):
    print "x es %s y y es %s" % (x, y)
    return x + y    # Retorna valores con una la declaracion return

# Llamando funciones con parametros
add(5, 6) #=> imprime "x es 5 y y es 6" y retorna 11

# Otra forma de llamar funciones es con argumentos de palabras claves
add(y=6, x=5)   # Argumentos de palabra clave pueden ir en cualquier orden.

# Puedes definir funciones que tomen un numero variable de argumentos
def varargs(*args):
    return args

varargs(1, 2, 3) #=> (1,2,3)


# Puedes definir funciones que toman un numero variable de argumentos
# de palabras claves
def keyword_args(**kwargs):
    return kwargs

#Veamos como funciona esto   
keyword_args(pie="grande", lago="ness") #=> {"pie": "grande", "lago": "ness"}

# Puedes hacer ambas a la vez si quieres
def todos_los_argumentos(*args, **kwargs):
    print args
    print kwargs
"""
todos_los_argumentos(1, 2, a=3, b=4) imprime:
    (1, 2)
    {"a": 3, "b": 4}
"""

# Cuando llames funciones, puedes hacer lo opuesto a varargs/kwargs!
# Usa * para expandir tuplas y usa ** para expandir argumentos de palabras claves.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
todos_los_argumentos(*args) # es equivalente a foo(1, 2, 3, 4)
todos_los_argumentos(**kwargs) # es equivalente a foo(a=3, b=4)
todos_los_argumentos(*args, **kwargs) # es equivalente a foo(1, 2, 3, 4, a=3, b=4)

# Python tiene funciones de primera clase
def crear_suma(x):
    def suma(y):
        return x + y
    return suma

sumar_10 = crear_suma(10)
sumar_10(3) #=> 13

# Tambien hay funciones anonimas
(lambda x: x > 2)(3) #=> True

# Hay funciones integradas de orden superior
map(sumar_10, [1,2,3]) #=> [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7]) #=> [6, 7]

# Podemos usar listas por comprension para mapeos y filtros agradables
[add_10(i) for i in [1, 2, 3]]  #=> [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5] #=> [6, 7]


# 6. Modulos

# Puedes importar modulos
import math
print math.sqrt(16) #=> 4

# Puedes obtener funciones especificas desde un modulo
from math import ceil, floor
print ceil(3.7)  #=> 4.0
print floor(3.7) #=> 3.0

# Puedes importar todas las funciones de un modulo
from math import *

# Puedes acortar los nombres de los modulos
import math as m
math.sqrt(16) == m.sqrt(16) #=> True

# Los modulos de Python son solo archivos ordinarios de Python.
# Puedes escribir tus propios modulos e importarlos. El nombre del modulo
# es el mismo del nombre del archivo.

# Puedes encontrar que funciones y atributos definen un modulo.
import math
dir(math)


