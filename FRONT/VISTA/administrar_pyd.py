from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage
from tkcalendar import DateEntry
import sys
sys.path.append("path/to/TPDAO/TPDAO")
from BACK.MODELO import prestamo
from BACK.CONTROLADOR import conexion

class VentanaAdministrarPyd:
    
    conexion = conexion.Conexion
    
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x650')
        self.master.title('Grupo 13 - Codex Astralis - Sistema de Préstamos Bibliotecarios - Gestionar Préstamos, Devoluciones y Extravíos')
        
        # Personalización - General
        self.fuente_personalizable = font.Font(family='Helvetica', size=13, weight="bold", slant="italic")

        # Favicon de la Aplicación
        self.icon_path = 'TPDAO\FRONT\PICS\icono_codex.ico'
        self.icon_image = PhotoImage(file=self.icon_path)
        self.master.iconphoto(True, self.icon_image)
        
        # Personalización Sección CRUD
        
        self.icono_prestamo = "TPDAO\FRONT\PICS\\book_loan.png"
        self.logo_prestamo = PhotoImage(file=self.icono_prestamo)
        
        # Sección de Ingreso de Datos del Libro - CRUD
        
        self.seccion_crud = Frame(self.master, bg="#23b5d3",
                                  width=500, height=300)
        self.seccion_crud.pack(side=TOP, fill='both', expand=True)
        
        Label(self.seccion_crud, text='Gestionar Préstamos, Devoluciones y Extravíos', font=self.fuente_personalizable,
              bg="#23b5d3", fg='white', pady=10).pack()
        
        logo_prestamo_libreria = Label(self.seccion_crud, image=self.logo_prestamo, background="#23b5d3",
                                 pady=20)
        logo_prestamo_libreria.pack(pady=10)
        
        # Carga de Datos...
        
        # Variables de uso en el programa.
        
        self.id = IntVar()
        
        self.objeto_conexion = conexion.Conexion()
        
        
        # Etiquetas (Labels) y campos de texto (Entries)
        
        campo = Frame(self.seccion_crud, width=300, height=300, bg='#23b5d3', borderwidth=2, relief="solid", padx=20, pady=10)
        campo.pack()

        # Número de Documento del Socio

        socio_data = self.objeto_conexion.get_datos_socio()
        libro_data = self.objeto_conexion.get_datos_libro()

        # Combobox initialization for Socio
        Label(campo, text='Documento del Socio', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=0, column=0, sticky='e', pady=(0, 5))
        socio_combobox_values = [f"{socio.numeroDocumento}" for socio in socio_data]
        self.socio_combobox = ttk.Combobox(campo, values=socio_combobox_values, state="readonly")
        self.socio_combobox.actual_values = [socio.numeroDocumento for socio in socio_data]
        self.socio_combobox.grid(row=0, column=1, pady=10)
        self.socio_combobox.set('Seleccionar Socio:')  # Set initial display text

        # Combobox initialization for Libro
        Label(campo, text='ISBN del Libro', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=1, column=0, sticky='e', pady=(0, 5))
        libro_combobox_values = [f"{libro.isbn}" for libro in libro_data]
        self.libro_combobox = ttk.Combobox(campo, values=libro_combobox_values, state="readonly")
        self.libro_combobox.actual_values = [libro.isbn for libro in libro_data]
        self.libro_combobox.grid(row=1, column=1, pady=10)
        self.libro_combobox.set('Seleccionar Libro:')  # Set initial display text

        # Fecha de Préstamo
        Label(campo, text='Fecha de Préstamo', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=4, column=0, sticky='e', pady=(0, 5))
        self.fecha_prestamo = DateEntry(campo, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
        self.fecha_prestamo.grid(row=4, column=1, columnspan=3, pady=(0, 5))

        # Fecha de Devolución
        
        Label(campo, text='Fecha de Devolución', padx=20, font=self.fuente_personalizable, justify='center', anchor="center", bg='#23b5d3', fg='white').grid(row=5, column=0, sticky='e', pady=(0, 5))
        self.fecha_devolucion = DateEntry(campo, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
        self.fecha_devolucion.grid(row=5, column=1, columnspan=3, pady=(0, 5))
        
        # Mensaje de Texto que avisa la cantidad de días de un préstamo
        
        self.cantidad_dias_prestamo_label = Label(campo, text='Registre un Préstamo - Mostraremos la Cantidad de Días', fg='red', bg='#23b5d3')
        self.cantidad_dias_prestamo_label.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Botonera de la Sección CRUD

        botonera_seccion_crud = Frame(self.seccion_crud)
        
        registrar_prestamo = Button(botonera_seccion_crud, text="Préstamo", command=self.registrar_prestamo, fg="white",
                                    bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_prestamo.pack(side="left", anchor="nw")

        registrar_devolucion = Button(botonera_seccion_crud, text="Devolución", command=self.registrar_devolucion, fg="white",
                                    bg="#23b5d3", font=self.fuente_personalizable, width=10)
        registrar_devolucion.pack(side="left", anchor="nw")
        
        '''
        borrar_prestamos = Button(botonera_seccion_crud, text="Borrar Todo", command=self.borrar_registros, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=10)
        borrar_prestamos.pack(side="left", anchor="nw")
        '''
        
        botonera_seccion_crud.pack()
        
        
        # Sección de Visualización de Datos de todos los Socios - CRUD (Grilla)
        
        self.visualizacion_datos = Frame(self.master, bg="white",
                                  width=500, height=250)
        
        self.grilla = ttk.Treeview(self.visualizacion_datos, column=("ID", "Número de Documento", "ISBN", "Fecha Préstamo", "Fecha Devolución", "Cantidad de Días"), show='headings')
        self.grilla.column("ID", anchor=W, width=10)
        self.grilla.heading("ID", text="ID")
        self.grilla.column("Número de Documento", anchor=W, width=10)
        self.grilla.heading("Número de Documento", text="Número de Documento")
        self.grilla.column("ISBN", anchor=W, width=100)
        self.grilla.heading("ISBN", text="ISBN")
        self.grilla.column("Fecha Préstamo", anchor=W, width=100) 
        self.grilla.heading("Fecha Préstamo", text="Fecha Préstamo")  
        self.grilla.column("Fecha Devolución", anchor=W, width=100)
        self.grilla.heading("Fecha Devolución", text="Fecha Devolución")
        self.grilla.column("Cantidad de Días", anchor=E, width=50)
        self.grilla.heading("Cantidad de Días", text="Cantidad de Días")

        
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
    
        buscar_prestamo = Button(botonera_seccion_consultas, text="Buscar Préstamo", command=self.buscar_prestamo, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        buscar_prestamo.pack(side="left", anchor="ne")
        
        self.id_prestamo = Entry(botonera_seccion_consultas, width=30, bd=0, relief="solid", justify='center',textvariable=self.id)
        self.id_prestamo.pack(side="right")
        
        botonera_seccion_consultas.pack(side=BOTTOM, pady=15, padx=10)



    # Métodos del Préstamo

    # Método para limpiar las cajas de texto.
    def limpiar_cajas(self):
        self.codigo_libro.delete(0, END)
        self.titulo_libro.delete(0, END)
        self.precio_reposicion.set(0.0) 
        opciones_estado = ["Disponible", "Prestado", "Extraviado"]
        self.estado_var.set(opciones_estado[0])
        
    def limpiar_grilla(self):
        self.grilla.delete(*self.grilla.get_children())
        
    '''   
    def borrar_registros(self):
        objeto_conexion = conexion.Conexion()
        objeto_conexion.borrar_todo_prestamo()
        self.limpiar_grilla()
    '''
        
    def actualizar_prestamo(self):
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

    # A fines prácticos, eliminar_prestamo = registrar_devolucion
    def registrar_devolucion(self):
        seleccionado = self.grilla.focus()
        clave = self.grilla.item(seleccionado, 'text')
        objeto_conexion = conexion.Conexion()

        if clave == '':
            messagebox.showwarning('Devolver Préstamo:', 'Debe seleccionar primero un elemento. Gracias.')
        else:
            valores = self.grilla.item(seleccionado, 'values')
            data = ' ID:' + ' ' + str(clave) + ' , ' + valores[1] + ' ' + valores[2] + ' , ' + valores[3]
            respuesta = messagebox.askquestion('Devolver Préstamo:', '¿Realmente desea devolver el préstamo seleccionado? \n' + data)

            if respuesta == messagebox.YES:
                # Fetch the Prestamo object based on the selected ID
                prestamo = objeto_conexion.get_prestamo_by_id(clave)

                if prestamo:
                    # Check the number of days for overdue
                    if prestamo.cantidadDias <= 30:
                        # Update the associated libro's estado to 'Disponible'
                        sql_update_libro = "UPDATE libro SET estado = 'Disponible' WHERE isbn = ?"
                        objeto_conexion.execute_query(sql_update_libro, (prestamo.isbn,))
                    else:
                        # Update the associated libro's estado to 'Extraviado' for overdue loans
                        sql_update_libro = "UPDATE libro SET estado = 'Extraviado' WHERE isbn = ?"
                        objeto_conexion.execute_query(sql_update_libro, (prestamo.isbn,))

                    # Delete the Prestamo record
                    sql_delete_prestamo = "DELETE FROM prestamo WHERE id = ?"
                    objeto_conexion.execute_query(sql_delete_prestamo, (clave,))
                    
                    if prestamo.cantidadDias <= 30:
                        messagebox.showinfo('Devolver Préstamo:', 'El préstamo fue devuelto correctamente. Registrando como \'Disponible\'.')
                    else:
                        messagebox.showinfo('Devolver Préstamo:', 'Lo sentimos. El libro se encuentra extraviado. Registrando como \'Extraviado\'.')
                    self.limpiar_grilla()
                    self.refrescar()
                else:
                    messagebox.showinfo('Devolver Préstamo:', f'No se encontró un préstamo con el ID: {clave}')

    def buscar_prestamo(self):
        id = self.id.get()
        if not id:
            messagebox.showwarning('Buscar Préstamo:', 'Por favor, ingrese un ID para buscar.')
            return

        objeto_conexion = conexion.Conexion()
        prestamo_encontrado = objeto_conexion.buscar_prestamo_conexion(id)

        if prestamo_encontrado:
            messagebox.showinfo('Buscar Préstamo:', f'Detalles del Préstamo:\n\n'
                                                f'Número de Documento del Socio: {prestamo_encontrado[1]}\n'
                                                f'ISBN del Libro: {prestamo_encontrado[2]}\n'
                                                f'Fecha de Préstamo: {prestamo_encontrado[3]}\n'
                                                f'Fecha de Devolución: {prestamo_encontrado[4]}\n'
                                                f'Cantidad de Días del Préstamo: {prestamo_encontrado[5]}')
        else:
            messagebox.showinfo('Buscar Préstamo:', f'No se encontró un libro con el ISBN: {id}')
        

    def refrescar(self):
        self.grilla.delete(*self.grilla.get_children())
        objeto_conexion = conexion.Conexion()
        datos = objeto_conexion.consultar_prestamos()
        for row in datos:
                    self.grilla.insert("", END, text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5]))

    # Registrar Préstamo - Dar un Préstamo de Alta
    def registrar_prestamo(self):
        self.objeto_conexion = conexion.Conexion()

        # Get selected values from the comboboxes
        selected_socio_numeroDocumento = self.socio_combobox.actual_values[self.socio_combobox.current()]
        selected_libro_isbn = self.libro_combobox.actual_values[self.libro_combobox.current()]

        # Fetch the Socio object based on the selected document number
        selected_socio = self.objeto_conexion.get_socio_by_numeroDocumento(selected_socio_numeroDocumento)
        selected_libro = self.objeto_conexion.get_libro_by_isbn(selected_libro_isbn)

        # Get selected dates from the DateEntry widgets
        selected_fecha_prestamo = self.fecha_prestamo.get_date()
        selected_fecha_devolucion = self.fecha_devolucion.get_date()

        # Check if both Socio and Libro are selected
        if selected_socio and selected_libro_isbn:
            # Calculate the number of days between loan and return dates
            cantidad_dias_prestamo = (selected_fecha_devolucion - selected_fecha_prestamo).days

            # Create a Prestamo object
            nuevo_prestamo = prestamo.Prestamo(
                socio=selected_socio,
                libro=selected_libro,
                fechaPrestamo=selected_fecha_prestamo,
                fechaDevolucion=selected_fecha_devolucion,
                cantidadDias=cantidad_dias_prestamo
            )

            # Your existing code for inserting the Prestamo record
            objeto_conexion = conexion.Conexion()
            objeto_conexion.insertar_prestamo(nuevo_prestamo)

            self.refrescar()

            # Display the number of days in the label
            self.cantidad_dias_prestamo_label.config(text=f'Libro prestado por {cantidad_dias_prestamo} días', fg='red')
        else:
            # Display a message or handle accordingly if Socio or Libro is not selected
            messagebox.showwarning('Registrar Préstamo:', 'Seleccione un Socio y un Libro para registrar el Préstamo.')
    
    
    # Buscar Préstamo
    
    def buscar_prestamo(self):
        id = self.id.get()
        if not id:
            messagebox.showwarning('Buscar Préstamo:', 'Por favor, ingrese un ID para buscar.')
            return

        objeto_conexion = conexion.Conexion()
        prestamo_encontrado = objeto_conexion.buscar_prestamo_conexion(id)

        if prestamo_encontrado:
            messagebox.showinfo('Buscar Préstamo:', f'Detalles del Préstamo:\n\n'
                                                f'Número de Documento del Socio: {prestamo_encontrado[1]}\n'
                                                f'ISBN del Libro: {prestamo_encontrado[2]}\n'
                                                f'Fecha Préstamo: {prestamo_encontrado[3]}\n'
                                                f'Fecha Devolución: {prestamo_encontrado[4]}\n'
                                                f'Cantidad de Días del Préstamo: {prestamo_encontrado[5]}')
        else:
            messagebox.showinfo('Buscar Préstamo:', f'No se encontró un préstamo con el ID: {id}')
    

    
    def mostrar(self):
        self.master.mainloop()
        