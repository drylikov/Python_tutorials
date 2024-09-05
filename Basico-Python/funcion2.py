def f1():
    print "Hi, yo soy el  lenguaje Python"

def f2():
    print "Hi, yo soy el lenguaje C, mucho gusto"

def f3():
    print "Hi, yo soy tmux!"

def error_f():
    print "Invalida opcion"

def test1():
    while 1:
        code = raw_input( 'Ingresa "uno", "dos", "tres", o "salir":')
        if code == 'salir':
            break
        if code == 'uno':
            f1()
        elif code == 'dos':
            f2()
        elif code == 'tres':
            f3()

        else:
           error_f()

def test2():
    mapper ={'uno':f1, 'dos':f2, 'tres': f3}
    while 1:
        code = raw_input( 'Ingresa "uno", "dos", "tres", o "salir":')
        if code == 'salir':
            break
        func = mapper.get(code, error_f)
        func()

def test():
    test1()
    print '-' * 50
    test2()


if __name__ == '__main__':
    test()
