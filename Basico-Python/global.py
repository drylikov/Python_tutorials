NAME = 'Erika'

def mostrar_global():
    name =NAME
    print '(mostrar_global) name:%s' %name

def s_global():
    NAME = 'YO'
    name = NAME 
    print '(s_global) name: %s' %name

mostrar_global()
s_global()
mostrar_global()
