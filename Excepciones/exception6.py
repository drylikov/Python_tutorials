#/usr/bin/python

f = None

try:
    f = file('file1.txt','r')
    contenido = f.readlines()
    for i in contenido:
        print i,

except IOError:
    print "Error al abrir el archivo"
finally:
    if f:
        f.close()
