# Implementa una funcion que toma dos argumentos. Una lista y un objeto
# Se aplica cada funcion de la lista para el argumento. Por ejemplo.

def f(obj):
    print 'Interesante -- %s -- Muy Interesante' % (obj, )

def plan(obj):
    print 'plan -- %s -- yo tengo un plan ' % (obj, )

Func_list = [f, plan, ]

def s(funcs, obj):
    for func in funcs:
        func(obj)

def main():
    a = {'aa': 11, 'bb': 22, }
    s(Func_list, a)

if __name__ == '__main__':
    main()
