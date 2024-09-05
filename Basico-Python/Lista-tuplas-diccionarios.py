a = "Python"
#Imprime  caracteres individuales en a
for c in a:
    print c
 
b =['Python', 'Node.js', 'C++', 'R']
#Imprime los miembros de una lista
for name in b:
    print name
 
c = {'Google':490.10,'IBM' :91.50,'AAPL': 123.15 }
#Imprime todos los miembros de un diccionario
for key in c:
    print key, c[key]
 
#Imprime todas las lineas en un archivo
f = open('res.txt')
for line in f:
    print line,
f.close()
