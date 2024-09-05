class Myclass():
    """Propiedades de la 
    clase y los metodos son 
    puestos aqui
    """
    pass

    prop1 = "Yo soy una variable de clase"

    def __init__(self):
        print ("La clase {0} fue iniciada").format(self.__class__)


    def setPropiedad(self, nval):
        self.prop1 = nval

    def getPropiedad(self):
        return self.prop1

#Creamos dos objetos

obj = Myclass()
obj2 = Myclass()


print (obj)
print (obj.prop1)

print (obj2)
print (obj2.prop1)

#Ponemos nuevos valores a ambos objetos

obj.setPropiedad("Yo soy un nuevo valor de la variable de clase!")
obj2.setPropiedad("Yo soy parte de la segunda instancia")

#Salida de ambos objetos

print (obj.getPropiedad())
print (obj2.getPropiedad())
print ("Fin del archivo")
