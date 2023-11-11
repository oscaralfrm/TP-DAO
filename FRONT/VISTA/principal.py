from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage
from administrar_socio import *

# Ventana Principal

class Principal:

    # El constructor inicializará la ventana, con sus dimensiones y elementos.

    def __init__(self):

        # Ventana #1: Principal
        self.ventana_principal = Tk()
        self.ventana_principal.geometry('750x500')
        self.ventana_principal.title('Grupo 13 - Codex Astralis - Sistema de Préstamos Bibliotecarios - Principal')
       
        # Personalización - General
        self.fuente_personalizable = font.Font(family='Helvetica', size=13, weight="bold", slant="italic")

        # Favicon de la Aplicación
        self.ico = 'FRONT\PICS\icono_codex.ico'
        self.icono = PhotoImage(file=self.ico)
        


        # Personalización - Sección #1
        self.logo_buho = "FRONT\PICS\logo_codex_blanco.png"
        self.logo = PhotoImage(file=self.logo_buho)
        self.ventana_principal.iconphoto(True, self.icono)
        
       
        # Sección #1 - Imagen y Logo del Grupo
        self.seccion_logo = Frame(self.ventana_principal, bg="#23b5d3",
                                  width=300, height=500)
        self.seccion_logo.pack(side=LEFT, fill="both", expand=True)
        
        
        # Elementos dentro de la Sección #1
        titulo_ventana = Label(self.seccion_logo, text="Bienvenido al Sistema Gestor de Préstamos Bibliotecarios", font=self.fuente_personalizable,
                                    pady=30, padx=20, bg="#23b5d3", fg="white")
        titulo_ventana.pack()
        
        logo_buho_blanco = Label(self.seccion_logo, image=self.logo, background="#23b5d3",
                                 pady=20)
        logo_buho_blanco.pack()
        
        integrantes = Label(self.seccion_logo, text='Integrantes: ', bg="#23b5d3", fg="white",
                            font=self.fuente_personalizable, pady=10)
        integrantes.pack()
        
        santiago = Label(self.seccion_logo, text='Orona, Santiago; Legajo: 95342 ', bg="#23b5d3", fg="white",
                            font=self.fuente_personalizable, pady=2)
        santiago.pack()
        
        oscar = Label(self.seccion_logo, text='Romero Moreno, Oscar Alfonso; Legajo: 96454 ', bg="#23b5d3", fg="white",
                            font=self.fuente_personalizable, pady=2)
        oscar.pack()
        
        martin = Label(self.seccion_logo, text=' Spadaccini Benedetti, Martin Matias; Legajo: 95168 ', bg="#23b5d3", fg="white",
                            font=self.fuente_personalizable, pady=2)
        martin.pack()
        
        # Sección #2 - Opciones de Administración
        self.seccion_opciones = Frame(self.ventana_principal, borderwidth=2, relief="solid", bg="#071013",
                                   width=300, height=500)
        self.seccion_opciones.pack(side=RIGHT, fill="both", expand=True)
        
        # Elementos dentro de la Sección #2
        titulo_opciones = Label(self.seccion_opciones, text="Menú de Opciones", font=self.fuente_personalizable,
                                    pady=30, padx=60, bg="#071013", fg="white")
        titulo_opciones.pack()

        botonera = Frame(self.seccion_opciones)
        
        espacio_logo_utn = Frame(self.seccion_opciones)
        
        self.logo_utn_blanco = "FRONT\PICS\logo_utn_peque.png"
        self.logo_utn = PhotoImage(file=self.logo_utn_blanco)
        
        
        
        # Opciones de Administración y Funcionalidades de la Aplicación
        
        admin_socios = Button(botonera, text="Administración Socios", command=self.abrir_administrar_socio, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        admin_socios.pack()
        
        admin_libros = Button(botonera, text="Administración de Libros", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        admin_libros.pack()
        
        registrar_prestamos = Button(botonera, text="Registrar Préstamos", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        registrar_prestamos.pack()
        
        registrar_devoluciones = Button(botonera, text="Registrar Devoluciones", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        registrar_devoluciones.pack()
        
        registrar_extraviados = Button(botonera, text="Registrar Extraviados", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        registrar_extraviados.pack()
        
        botonera.pack(pady=50)
    
        espacio_logo_utn.pack()
    
        logo_utn_footer = Label(espacio_logo_utn, image=self.logo_utn, background="#071013",
                                 pady=20)
        logo_utn_footer.pack()
    
       
    # Ingresando los datos del nuevo Socio...
    def abrir_administrar_socio(self):
        ventana_socio = VentanaAdministrarSocio()
        ventana_socio.mostrar()
    
    # El método que se usará para mostrar el contenido de la ventana
    
    def mostrar(self):
        self.ventana_principal.mainloop()
        


ventana_principal = Principal()
ventana_principal.mostrar()