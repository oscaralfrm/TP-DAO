from tkinter import *

# Ventana Principal

class Principal:

    # El constructor inicializará la ventana, con sus dimensiones y elementos.

    def __init__(self):

        # Ventana #1: Principal
        self.ventanaPrincipal = Tk()
        self.ventanaPrincipal.geometry('500x500')
        self.ventanaPrincipal.title('Sistema de Préstamos Bibliotecarios - Principal')
        
        # Sección #1 - Creación de Socios...
        seccion_uno = LabelFrame(self.ventanaPrincipal, text='Registrar un Socio')
        seccion_uno.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # Ingresando los datos del nuevo Socio...
        Label(seccion_uno, text='Nombre del Socio: ').grid(row = 1, column = 0)


    
    # El método que se usará para mostrar el contenido de la ventana
    
    def mostrar(self):
        self.ventanaPrincipal.mainloop()
        


ventanaPrincipal = Principal()
ventanaPrincipal.mostrar()