from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage
import sys
sys.path.append("path/to/TPDAO/TPDAO")
from BACK.MODELO import libro
from BACK.CONTROLADOR import conexion

class VentanaAdministrarLibro:
    
    conexion = conexion.Conexion
    
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x650')
        self.master.title('Grupo 13 - Codex Astralis - Sistema de Préstamos Bibliotecarios - Administrar Libro')
        
        # Personalización - General
        self.fuente_personalizable = font.Font(family='Helvetica', size=13, weight="bold", slant="italic")

        # Favicon de la Aplicación
        self.icon_path = 'TPDAO\FRONT\PICS\icono_codex.ico'
        self.icon_image = PhotoImage(file=self.icon_path)
        self.master.iconphoto(True, self.icon_image)
        
        # Personalización Sección CRUD
        
        self.icono_libro = "TPDAO\FRONT\PICS\star-book.png"
        self.logo_libro = PhotoImage(file=self.icono_libro)
        
        # Sección de Ingreso de Datos del Libro - CRUD
        
        self.seccion_crud = Frame(self.master, bg="#23b5d3",
                                  width=500, height=300)
        self.seccion_crud.pack(side=TOP, fill='both', expand=True)
        
        Label(self.seccion_crud, text='Ingresar Datos del Libro', font=self.fuente_personalizable,
              bg="#23b5d3", fg='white', pady=10).pack()
        
        logo_libro_libreria = Label(self.seccion_crud, image=self.logo_libro, background="#23b5d3",
                                 pady=20)
        logo_libro_libreria.pack(pady=10)
        
        # Carga de Datos...
        
        # Variables asociadas a cada Entry:
        # Éstas variables son las que serán modificadas en el CRUD.
        
        self.isbn = IntVar()
        
        self.titulo = StringVar()

        self.precio_reposicion = DoubleVar()
        
        self.estado = StringVar()
        
        
        # Etiquetas (Labels) y campos de texto (Entries)
        
        
        campo = Frame(self.seccion_crud, width=300, height=300, bg='#23b5d3', borderwidth=2, relief="solid", padx=20, pady=10)
        campo.pack()

        # ISBN
        Label(campo, text='ISBN', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=0, column=0, sticky='e', pady=(0, 5))
        self.codigo_libro = Entry(campo, width=30, textvariable=self.isbn)
        self.codigo_libro.grid(row=0, column=1, columnspan=3)

        # Título
        Label(campo, text='Título', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=1, column=0, sticky='e', pady=(0, 5))
        self.titulo_libro = Entry(campo, width=30, textvariable=self.titulo)
        self.titulo_libro.grid(row=1, column=1, columnspan=3)

        # Precio de Reposición
        Label(campo, text='Precio de Reposición', font=self.fuente_personalizable, padx=20, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=2, column=0, sticky='e', pady=(0, 5))
        self.precio_reposicion_libro = Entry(campo, width=30, textvariable=self.precio_reposicion)
        self.precio_reposicion_libro.grid(row=2, column=1, columnspan=3)

        # Estado
        
        opciones_estado = ["Disponible", "Prestado", "Extraviado"]
        self.estado_var = StringVar()
        self.estado_var.set(opciones_estado[0])

        Label(campo, text='Estado', font=self.fuente_personalizable, padx=20, justify='center',
              anchor="center", bg='#23b5d3', fg='white').grid(row=3, column=0, sticky='e', pady=(0, 5))

        estado_dropdown = OptionMenu(campo, self.estado_var, *opciones_estado)
        estado_dropdown.config(width=15, font=self.fuente_personalizable)
        estado_dropdown.grid(row=3, column=1, columnspan=3, pady=(0, 5))
    
        # Botonera de la Sección CRUD

        botonera_seccion_crud = Frame(self.seccion_crud)
        
        registrar_alta_libro = Button(botonera_seccion_crud, text="Registrar", command=self.agregar_libro, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_alta_libro.pack(side="left", anchor="nw")
        
        limpiar_campos = Button(botonera_seccion_crud, text="Limpiar", command=self.limpiar_cajas, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        limpiar_campos.pack(side="left", anchor="nw")
        
        registrar_baja_libro = Button(botonera_seccion_crud, text="Eliminar", command=self.eliminar_libro, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_baja_libro.pack(side="left", anchor="nw")
        
        actualizar_libro = Button(botonera_seccion_crud, text="Actualizar", command=self.actualizar_libro, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        actualizar_libro.pack(side="left", anchor="nw")
        
        borrar_libros = Button(botonera_seccion_crud, text="Borrar Todo", command=self.borrar_registros, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        borrar_libros.pack(side="left", anchor="nw")
        
        botonera_seccion_crud.pack(side=BOTTOM, pady=10, padx=10)
        
        # Sección de Visualización de Datos de todos los Socios - CRUD (Grilla)
        
        self.visualizacion_datos = Frame(self.master, bg="white",
                                  width=500, height=250)
        
        self.grilla = ttk.Treeview(self.visualizacion_datos, column=("ID", "ISBN", "Título", "Precio de Reposición", "Estado"), show='headings')
        self.grilla.column("ID", anchor=W, width=10)
        self.grilla.heading("ID", text="ID")
        self.grilla.column("ISBN", anchor=W, width=100)
        self.grilla.heading("ISBN", text="ISBN")
        self.grilla.column("Título", anchor=W, width=100)
        self.grilla.heading("Título", text="Título")
        self.grilla.column("Precio de Reposición", anchor=W, width=100)
        self.grilla.heading("Precio de Reposición", text="Precio de Reposición")
        self.grilla.column("Estado", anchor=E, width=50)
        self.grilla.heading("Estado", text="Estado")
        
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
    
        buscar_libro = Button(botonera_seccion_consultas, text="Buscar Libro", command=self.buscar_libro, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        buscar_libro.pack(side="left", anchor="ne")
        
        self.codigo_libro = Entry(botonera_seccion_consultas, width=30, bd=0, relief="solid", justify='center',textvariable=self.isbn)
        self.codigo_libro.pack(side="right")
        
        botonera_seccion_consultas.pack(side=BOTTOM, pady=25, padx=10)


    # Método para limpiar las cajas de texto.
    def limpiar_cajas(self):
        self.codigo_libro.delete(0, END)
        self.titulo_libro.delete(0, END)
        self.precio_reposicion.set(0.0) 
        opciones_estado = ["Disponible", "Prestado", "Extraviado"]
        self.estado_var.set(opciones_estado[0])
        
    def limpiar_grilla(self):
        self.grilla.delete(*self.grilla.get_children())
        
    def borrar_registros(self):
        objeto_conexion = conexion.Conexion()
        objeto_conexion.borrar_todo_libro()
        self.limpiar_grilla()

    def agregar_libro(self):
        nuevo_isbn = self.isbn.get()
        nuevo_titulo = self.titulo.get()
        nuevo_precio_reposicion = self.precio_reposicion.get()
        nuevo_estado = self.estado_var.get()
        nuevo_libro = libro.Libro(nuevo_isbn, nuevo_titulo, nuevo_precio_reposicion, nuevo_estado)
        objeto_conexion = conexion.Conexion()
        objeto_conexion.insertar_libro(nuevo_libro)
        self.refrescar()
        
    def actualizar_libro(self):
        seleccionado = self.grilla.focus()
        clave = self.grilla.item(seleccionado, 'text')

        if clave == '':
            messagebox.showwarning('Actualizar: ', 'Debe seleccionar primero un elemento. Gracias.')
        else:
            id_libro = clave
            nuevo_isbn = self.isbn.get()
            nuevo_titulo = self.titulo.get()
            nuevo_precio_reposicion = self.precio_reposicion.get()
            nuevo_estado = self.estado_var.get()

            objeto_conexion = conexion.Conexion()
            objeto_conexion.modificar_libro(id_libro, nuevo_isbn, nuevo_titulo, nuevo_precio_reposicion, nuevo_estado)

            self.refrescar()

    def eliminar_libro(self):
        seleccionado = self.grilla.focus()
        clave = self.grilla.item(seleccionado, 'text')
        objeto_conexion = conexion.Conexion()
        
        if clave == '':
            messagebox.showwarning('Eliminar: ', 'Debe seleccionar primero un elemento. Gracias.')
        else:
            valores = self.grilla.item(seleccionado, 'values')
            data = ' ISBN:' + ' ' + str(clave) + ' , ' + valores[2] + ' ' + valores[3] + ' , ' + valores[4]
            respuesta = messagebox.askquestion('Eliminar: ', '¿Realmente desea eliminar el registro seleccionado? \n' + data)
            
            if respuesta == messagebox.YES:
                n = objeto_conexion.eliminar_libro(clave)
                if n == 1:
                    messagebox.showinfo('Eliminar: ', 'Su registro fue eliminado correctamente.')
                    self.limpiar_grilla()
                    self.refrescar()
                else:
                    messagebox.showinfo('Eliminar: ', 'Lo sentimos. No fue posible borrar su registro.')

    def buscar_libro(self):
        isbn = self.isbn.get()
        if not isbn:
            messagebox.showwarning('Buscar Libro:', 'Por favor, ingrese un ISBN para buscar.')
            return

        objeto_conexion = conexion.Conexion()
        libro_encontrado = objeto_conexion.buscar_libro_conexion(isbn)

        if libro_encontrado:
            messagebox.showinfo('Buscar Libro:', f'Detalles del Libro:\n\n'
                                                f'ISBN: {libro_encontrado[1]}\n'
                                                f'Título: {libro_encontrado[2]}\n'
                                                f'Precio de Reposición: {libro_encontrado[3]}\n'
                                                f'Estado: {libro_encontrado[4]}')
        else:
            messagebox.showinfo('Buscar Libro:', f'No se encontró un libro con el ISBN: {isbn}')
        

    def refrescar(self):
        self.grilla.delete(*self.grilla.get_children())
        objeto_conexion = conexion.Conexion()
        datos = objeto_conexion.consultar_libros()
        for row in datos:
                    self.grilla.insert("", END, text=row[0], values=(row[0], row[1], row[2], row[3], row[4]))


    def mostrar(self):
        self.master.mainloop()
        