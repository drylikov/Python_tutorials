# Escribir el siguiente y explicar que son significan
# por ejemplo el nombre que empieza con un guion.

#!/usr/bin/python

from Tkinter import *

class B_demo(Frame):

    def __init__(self):


        """Establecemos ventanas y widgets """
        Frame.__init__(self)

        self.master.title("Un boton Demo")
        self.grid()
        self._label.grid()
        self._button = Button (self,
                text = " Haz click",
                command = self._switch)
        self._button.grid()

    def _s(self):
        """ Manejador de eventos para el boton"""
        if self._label["text"] == "Hola":
            self._label["text"] == "Python-UNI"
        else:
            self._label["text"] == "Hola"

