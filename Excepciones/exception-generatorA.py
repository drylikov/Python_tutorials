#!/usr/bin/python

class it:
    def __init__(self):
        # Empezamos en -1 tal que conseguimos 0 cuando agregamos 1
        self.count = -1

    # El metodo __iter__ es llamado para el bucle for
    # todo ocurre sobre el objeto que devuelve este metodo
    # en este caso es el objeto en si mismp

    def __iter__(self):
        return self

    # El metodo next es llamado repetidamente por el bucle for
    # hasta que el aparezca StopIteration

    def next(self):
        self.count += 1
        if self.count < 4:
            return self.count
        else:
            # StopIteration es lanzada (raise)
            raise StopIteration

def una_funcion():
    return it()

for i in una_funcion():
    print i


