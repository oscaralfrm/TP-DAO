from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage
import sys
sys.path.append("path/to/TPDAO/TPDAO")
from BACK.MODELO import socio
from BACK.CONTROLADOR import conexion

class VentanaAdministrarSocio:
    
    conexion = conexion.Conexion
    
    def __init__(self, master):
        
        
        self.master = master
        self.master.geometry('800x650')
        self.master.title('Grupo 13 - Codex Astralis - Sistema de Préstamos Bibliotecarios - Administrar Socio')
        
        # Personalización - General
        self.fuente_personalizable = font.Font(family='Helvetica', size=13, weight="bold", slant="italic")

        # Favicon de la Aplicación
        self.icon_path = 'TPDAO\FRONT\PICS\icono_codex.ico'
        self.icon_image = PhotoImage(file=self.icon_path)
        self.master.iconphoto(True, self.icon_image)
        
        # Personalización Sección CRUD
        
        self.icono_socio = "TPDAO\FRONT\PICS\icono_socio.png"
        self.logo_socio = PhotoImage(file=self.icono_socio)
        
        # Sección de Ingreso de Datos del Socio - CRUD
        
        self.seccion_crud = Frame(self.master, bg="#23b5d3",
                                  width=500, height=300)
        self.seccion_crud.pack(side=TOP, fill='both', expand=True)
        
        Label(self.seccion_crud, text='Ingresar Datos del Socio', font=self.fuente_personalizable,
              bg="#23b5d3", fg='white', pady=10).pack()
        
        logo_socio_libreria = Label(self.seccion_crud, image=self.logo_socio, background="#23b5d3",
                                 pady=20)
        logo_socio_libreria.pack(pady=10)
        
        # Carga de Datos...
        
        # Variables asociadas a cada Entry:
        # Éstas variables son las que serán modificadas en el CRUD.
        
        # Sección de Ingreso de Datos del Socio - CRUD
        self.nombre = StringVar()
        self.apellido= StringVar()
        self.numeroDocumento = IntVar()

        campo = Frame(self.seccion_crud, width=300, height=300, bg='#23b5d3', borderwidth=2, relief="solid", padx=20, pady=10)
        campo.pack()

        Label(campo, text='Nombre', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=0, column=0, sticky='e', pady=(0, 5))
        self.nombre_entry = Entry(campo, width=30, textvariable=self.nombre)
        self.nombre_entry.grid(row=0, column=1, columnspan=3)

        Label(campo, text='Apellido', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=1, column=0, sticky='e', pady=(0, 5))
        self.apellido_entry = Entry(campo, width=30, textvariable=self.apellido)
        self.apellido_entry.grid(row=1, column=1, columnspan=3)

        opciones_tipoDocumento = ["DNI", "Pasaporte", "CUIL"]
        self.tipoDocumento = StringVar()
        self.tipoDocumento.set(opciones_tipoDocumento[0])

        Label(campo, text='Tipo de Documento', font=self.fuente_personalizable, padx=20, justify='center',
              anchor="center", bg='#23b5d3', fg='white').grid(row=2, column=0, sticky='e', pady=(0, 5))

        tipoDocumento_dropdown = OptionMenu(campo, self.tipoDocumento, *opciones_tipoDocumento)
        tipoDocumento_dropdown.config(width=15, font=self.fuente_personalizable)
        tipoDocumento_dropdown.grid(row=2, column=1, columnspan=3, pady=(0, 5))

        Label(campo, text='Número de Documento', font=self.fuente_personalizable, padx=20, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=3, column=0, sticky='e', pady=(0, 5))
        self.numeroDocumento_entry = Entry(campo, width=30, textvariable=self.numeroDocumento)
        self.numeroDocumento_entry.grid(row=3, column=1, columnspan=3)
        
        # Botonera de la Sección CRUD

        botonera_seccion_crud = Frame(self.seccion_crud)
        
        registrar_alta_socio = Button(botonera_seccion_crud, text="Registrar", command=self.agregar_socio, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_alta_socio.pack(side="left", anchor="nw")
        
        limpiar_campos = Button(botonera_seccion_crud, text="Limpiar", command=self.limpiar_cajas, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        limpiar_campos.pack(side="left", anchor="nw")
        
        registrar_baja_socio = Button(botonera_seccion_crud, text="Eliminar", command=self.eliminar_socio, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_baja_socio.pack(side="left", anchor="nw")
        
        actualizar_socio = Button(botonera_seccion_crud, text="Actualizar", command=self.actualizar_socio, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        actualizar_socio.pack(side="left", anchor="nw")
        
        borrar_socios = Button(botonera_seccion_crud, text="Borrar Todo", command=self.borrar_registros, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        borrar_socios.pack(side="left", anchor="nw")
        
        botonera_seccion_crud.pack(side=BOTTOM, pady=10, padx=10)
        
        
        # Sección de Visualización de Datos de todos los Socios - CRUD (Grilla)
        
        
        self.visualizacion_datos = Frame(self.master, bg="white",
                                  width=500, height=250)
        
        
        self.grilla = ttk.Treeview(self.visualizacion_datos, column=("ID", "Nombre", "Apellido", "Tipo de Documento", "Número de Documento"), show='headings')
        self.grilla.column("ID", anchor=W, width=10)
        self.grilla.heading("ID", text="ID")
        self.grilla.column("Nombre", anchor=W, width=100)
        self.grilla.heading("Nombre", text="Nombre")
        self.grilla.column("Apellido", anchor=W, width=100)
        self.grilla.heading("Apellido", text="Apellido")
        self.grilla.column("Tipo de Documento", anchor=W, width=100)
        self.grilla.heading("Tipo de Documento", text="Tipo de Documento")
        self.grilla.column("Número de Documento", anchor=E, width=50)
        self.grilla.heading("Número de Documento", text="Número de Documento")
        
        # Barra Scroll
        scrollbar = Scrollbar(self.visualizacion_datos, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.grilla.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.grilla.yview)
        
        self.grilla.pack(fill=BOTH, expand=True)
        self.visualizacion_datos.pack(fill='both', expand=True)
        
        
        # Se refresca la tabla para mostrar lo que ya tiene. 
        self.refrescar()
        
        # Sección de Consultas
        
        self.seccion_reportes_consultas = Frame(self.master, bg="#23b5d3",
                                  width=500, height=20)
        self.seccion_reportes_consultas.pack(side=BOTTOM, fill='both', expand=True)
        
        botonera_seccion_consultas = Frame(self.seccion_reportes_consultas)
    
        buscar_socio = Button(botonera_seccion_consultas, text="Buscar Socio", command=self.buscar_socio, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        buscar_socio.pack(side="left", anchor="ne")
        
        self.codigo_socio = Entry(botonera_seccion_consultas, width=30, bd=0, relief="solid", justify='center',textvariable=self.numeroDocumento)
        self.codigo_socio.pack(side="right")
        
        
        
        botonera_seccion_consultas.pack(side=BOTTOM, pady=25, padx=10)


    # Método para limpiar las cajas de texto.
    def limpiar_cajas(self):
        self.nombre_entry.delete(0, END)
        self.apellido_entry.delete(0, END)
        self.numeroDocumento_entry.delete(0, END)
        opciones_tipoDocumento = ["DNI", "Pasaporte", "CUIL"]
        self.tipoDocumento.set(opciones_tipoDocumento[0]) 


        
    def limpiar_grilla(self):
        self.grilla.delete(*self.grilla.get_children())
        
    def borrar_registros(self):
        objeto_conexion = conexion.Conexion()
        objeto_conexion.borrar_todo_socio()
        self.limpiar_grilla()


    def agregar_socio(self):
        nuevo_nombre = self.nombre.get()
        nuevo_apellido = self.apellido.get()
        nuevo_tipoDocumento = self.tipoDocumento.get()
        nuevo_numeroDocumento = self.numeroDocumento.get()

        nuevo_socio = socio.Socio(nuevo_nombre, nuevo_apellido, nuevo_tipoDocumento, nuevo_numeroDocumento)
        
        objeto_conexion = conexion.Conexion()
        objeto_conexion.insertar_socio(nuevo_socio)
        self.refrescar()

    def actualizar_socio(self):
        seleccionado = self.grilla.selection()
        if not seleccionado:
            messagebox.showwarning('Actualizar: ', 'Debe seleccionar primero un elemento. Gracias.')
            return
        
        valores = self.grilla.item(seleccionado, 'values')
        
        id_socio = valores[0] 
        nuevo_nombre = self.nombre.get()
        nuevo_apellido = self.apellido.get()
        nuevo_tipoDocumento = self.tipoDocumento.get()
        nuevo_numeroDocumento = self.numeroDocumento.get()

        objeto_conexion = conexion.Conexion()
        objeto_conexion.modificar_socio(id_socio, nuevo_nombre, nuevo_apellido, nuevo_tipoDocumento, nuevo_numeroDocumento)

        self.refrescar()

    def eliminar_socio(self):
        seleccionado = self.grilla.selection()
        if not seleccionado:
            messagebox.showwarning('Eliminar: ', 'Debe seleccionar primero un elemento. Gracias.')
            return

        objeto_conexion = conexion.Conexion()

        for item in seleccionado:
            valores = self.grilla.item(item, 'values')
            clave = valores[0]  

            data = ' Número de Documento:' + ' ' + str(clave) + ' , ' + valores[1] + ' ' + valores[2] + ' , ' + valores[3]
            respuesta = messagebox.askquestion('Eliminar: ', '¿Realmente desea eliminar el registro seleccionado? \n' + data)

            if respuesta == messagebox.YES:
                n = objeto_conexion.eliminar_socio(clave)
                if n == 1:
                    messagebox.showinfo('Eliminar: ', 'Su registro fue eliminado correctamente.')
                    self.limpiar_grilla()
                    self.refrescar()
                else:
                    messagebox.showinfo('Eliminar: ', 'Lo sentimos. No fue posible borrar su registro.')



    def buscar_socio(self):
        numeroDocumento = self.numeroDocumento.get()
        if not numeroDocumento:
            messagebox.showwarning('Buscar Socio:', 'Por favor, ingrese un Número de Documento para buscar.')
            return

        objeto_conexion = conexion.Conexion()
        socio_encontrado = objeto_conexion.buscar_socio_conexion(numeroDocumento)

        if socio_encontrado:
            messagebox.showinfo('Buscar Socio:', f'Detalles del Socio:\n\n'
                                                f'Nombre: {socio_encontrado[1]}\n'
                                                f'Apellido: {socio_encontrado[2]}\n'
                                                f'Tipo de Documento: {socio_encontrado[3]}\n'
                                                f'Número de Documento: {socio_encontrado[4]}')
        else:
            messagebox.showinfo('Buscar Socio:', f'No se encontró un socio con el Número de Documento: {numeroDocumento}')
        

    def refrescar(self):
        self.grilla.delete(*self.grilla.get_children())
        objeto_conexion = conexion.Conexion()
        datos = objeto_conexion.consultar_socios()
        for row in datos:
            self.grilla.insert("", END, text="", values=(row[0], row[1], row[2], row[3], row[4]))

    def mostrar(self):
        self.master.mainloop()
        