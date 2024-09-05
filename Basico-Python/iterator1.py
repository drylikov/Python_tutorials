def t(coleccion):
    icoleccion = iter(coleccion)
    for item in icoleccion:
        yield '||%s ||' %item 
        
def test():
    coleccion = [111, 222, 333,]
    for x in t(coleccion): 
        print x

test()
    
