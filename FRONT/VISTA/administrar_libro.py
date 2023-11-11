from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage
# from BACK.MODELO.libro import Libro
# from BACK.CONTROLADOR.conexion import *

class VentanaAdministrarLibro:
    def __init__(self):
        self.ventana_socio = Tk()
        self.ventana_socio.geometry('800x650')
        self.ventana_socio.title('Grupo 13 - Codex Astralis - Sistema de Préstamos Bibliotecarios - Administrar Libro')
        
        # Personalización - General
        self.fuente_personalizable = font.Font(family='Helvetica', size=13, weight="bold", slant="italic")

        # Favicon de la Aplicación
        self.icon_path = 'FRONT\PICS\icono_codex.ico'
        self.icon_image = PhotoImage(file=self.icon_path)
        self.ventana_socio.iconphoto(True, self.icon_image)
        
        # Personalización Sección CRUD
        
        self.icono_socio = "FRONT\PICS\icono_socio.png"
        self.logo_socio = PhotoImage(file=self.icono_socio)
        
        # Sección de Ingreso de Datos del Socio - CRUD
        
        self.seccion_crud = Frame(self.ventana_socio, bg="#23b5d3",
                                  width=500, height=300)
        self.seccion_crud.pack(side=TOP, fill='both', expand=True)
        
        Label(self.seccion_crud, text='Ingresar Datos del Socio', font=self.fuente_personalizable,
              bg="#23b5d3", fg='white', pady=10).pack()
        
        logo_socio_libreria = Label(self.seccion_crud, image=self.logo_socio, background="#23b5d3",
                                 pady=20)
        logo_socio_libreria.pack(pady=10)
        
        # Etiquetas (Labels) y campos de texto (Entries)
        campo = Frame(self.seccion_crud, width=300, height=300, bg='#23b5d3', borderwidth=2, relief="solid", padx=20, pady=10)
        
        Label(campo, text='Nombre', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=0, column=0, sticky='e', pady=(0, 5))
        self.nombre_usuario = Entry(campo, width=30).grid(row=0, column=1, columnspan=3)
        
        Label(campo, text='Apellido', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=1, column=0, sticky='e', pady=(0, 5))
        self.apellido_usuario = Entry(campo, width=30).grid(row=1, column=1, columnspan=3)
        
        Label(campo, text='Tipo de Documento', font=self.fuente_personalizable , padx=20, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=2, column=0, sticky='e', pady=(0, 5))
        self.apellido_usuario = Entry(campo, width=30).grid(row=2, column=1, columnspan=3)
        
        Label(campo, text='Número de Documento', font=self.fuente_personalizable ,padx=20, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=3, column=0, sticky='e', pady=(0, 5))
        self.apellido_usuario = Entry(campo, width=30).grid(row=3, column=1, columnspan=3)
        
        campo.pack()
        
        # Botonera de la Sección CRUD

        botonera_seccion_crud = Frame(self.seccion_crud)
        
        registrar_alta_socio = Button(botonera_seccion_crud, text="Registrar", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_alta_socio.pack(side="left", anchor="nw")
        
        limpiar_campos = Button(botonera_seccion_crud, text="Limpiar", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        limpiar_campos.pack(side="left", anchor="nw")
        
        registrar_baja_socio = Button(botonera_seccion_crud, text="Eliminar", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_baja_socio.pack(side="left", anchor="nw")
        
        actualizar_socio = Button(botonera_seccion_crud, text="Actualizar", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        actualizar_socio.pack(side="left", anchor="nw")
        
        botonera_seccion_crud.pack(side=BOTTOM, pady=10, padx=10)
        
        
        # Sección de Visualización de Datos de todos los Socios - CRUD (Grilla)
        
        
        self.visualizacion_datos = Frame(self.ventana_socio, bg="white",
                                  width=500, height=250)
        
        
        self.grilla = ttk.Treeview(self.visualizacion_datos, column=("Nombre", "Apellido", "Tipo de Documento", "Número de Documento"), show='headings')
        self.grilla.column("Nombre", anchor=W, width=100)
        self.grilla.heading("Nombre", text="Nombre")
        self.grilla.column("Apellido", anchor=W, width=100)
        self.grilla.heading("Apellido", text="Apellido")
        self.grilla.column("Tipo de Documento", anchor=W, width=100)
        self.grilla.heading("Tipo de Documento", text="Tipo de Documento")
        self.grilla.column("Número de Documento", anchor=E, width=50)
        self.grilla.heading("Número de Documento", text="Número de Documento")
        self.grilla.pack(fill=BOTH, expand=True)
        
        self.visualizacion_datos.pack(fill='both', expand=True)
        
        # Sección de Reporters y Consultas
        
        self.seccion_reportes_consultas = Frame(self.ventana_socio, bg="#23b5d3",
                                  width=500, height=20)
        self.seccion_reportes_consultas.pack(side=BOTTOM, fill='both', expand=True)
        
        botonera_seccion_reportes = Frame(self.seccion_reportes_consultas)
        
        solicitar_reportes = Button(botonera_seccion_reportes, text="Generar Reportes", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        solicitar_reportes.pack(side="left", anchor="nw")
        
        consultar_socio = Button(botonera_seccion_reportes, text="Consultar Socio", command="", fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        consultar_socio.pack(side="right", anchor="ne")
        
        botonera_seccion_reportes.pack(side=BOTTOM, pady=25, padx=10)


    def mostrar(self):
        self.ventana_socio.mainloop()

new = VentanaAdministrarLibro()
new.mostrar()