"""El siguiente programa calcula todos los numeros
    que satisfacen el teorema de pitagoras  menor
    que un numero dado"""

#!/usr/bin/env python
from math import sqrt     #Importamos el modulo math
n = raw_input("Numero maximo?")
n = int(n) +1
for a in range(1,n):
    for b in range (a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square -c**2)==0):
            print a, b, c

