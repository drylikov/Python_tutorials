#!/usr/bin/python

class Libro:
    def __init__(self, titulo, autor, paginas):
        print "Un libro va a ser creado"
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Titulo:%s, autor:%s, paginas:%s" %\
                (self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas

    def __del__(self):
        print "Un libro sera vendido"

libro = Libro("Introduction Process Stochastic", "Fima Klebaner", 400)

print libro
print len(libro)
del libro


