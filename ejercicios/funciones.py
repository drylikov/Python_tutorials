# Implementa una funcion que toma dos argumentos. Una funcion y un objeto
# Aplica el argumento de la funcion al objeto. Por ejemplo

def f(obj):
    print 'Interesante -- %s -- Interesante' % (obj, )

def plan(obj):
    print 'Tengo un plan -- %s -- tengo otro plan' % (obj, )

def  mostrar(func, obj):
    func(obj)

def main():
    a = {'aa': 11, 'bb': 22, }
    mostrar(f, a)
    mostrar(plan, a)

if __name__ == '__main__':
    main()


