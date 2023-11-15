from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from administrar_socio import *
from administrar_libro import *
from administrar_pyd import *

class Principal:
    def __init__(self, master):
        self.master = master
        self.master.geometry('750x500')
        self.master.title('Grupo 13 - Codex Astralis - Sistema de Préstamos Bibliotecarios - Principal')

        self.fuente_personalizable = font.Font(family='Helvetica', size=13, weight="bold", slant="italic")

        # Favicon de la Aplicación
        self.ico = 'TPDAO\FRONT\PICS\icono_codex.ico'
        self.icono = PhotoImage(file=self.ico)

        self.logo_buho = "TPDAO\FRONT\PICS\logo_codex_blanco.png"
        self.logo = PhotoImage(file=self.logo_buho)
        self.master.iconphoto(True, self.icono)

        # Sección #1 - Imagen y Logo del Grupo
        self.seccion_logo = Frame(self.master, bg="#23b5d3", width=300, height=500)
        self.seccion_logo.pack(side=LEFT, fill="both", expand=True)

        titulo_ventana = Label(self.seccion_logo, text="Bienvenido al Sistema Gestor de Préstamos Bibliotecarios",
                               font=self.fuente_personalizable, pady=30, padx=20, bg="#23b5d3", fg="white")
        titulo_ventana.pack()

        logo_buho_blanco = Label(self.seccion_logo, image=self.logo, background="#23b5d3", pady=20)
        logo_buho_blanco.pack()

        integrantes = Label(self.seccion_logo, text='Integrantes: ', bg="#23b5d3", fg="white",
                            font=self.fuente_personalizable, pady=10)
        integrantes.pack()

        santiago = Label(self.seccion_logo, text='Orona, Santiago; Legajo: 95342 ', bg="#23b5d3", fg="white",
                         font=self.fuente_personalizable, pady=2)
        santiago.pack()

        oscar = Label(self.seccion_logo, text='Romero Moreno, Oscar Alfonso; Legajo: 96454 ', bg="#23b5d3",
                      fg="white", font=self.fuente_personalizable, pady=2)
        oscar.pack()

        martin = Label(self.seccion_logo, text=' Spadaccini Benedetti, Martin Matias; Legajo: 95168 ', bg="#23b5d3",
                       fg="white", font=self.fuente_personalizable, pady=2)
        martin.pack()

        # Sección #2 - Opciones de Administración
        self.seccion_opciones = Frame(self.master, borderwidth=2, relief="solid", bg="#071013", width=300, height=500)
        self.seccion_opciones.pack(side=RIGHT, fill="both", expand=True)

        titulo_opciones = Label(self.seccion_opciones, text="Menú de Opciones", font=self.fuente_personalizable,
                                pady=30, padx=60, bg="#071013", fg="white")
        titulo_opciones.pack()

        botonera = Frame(self.seccion_opciones)

        espacio_logo_utn = Frame(self.seccion_opciones)

        self.logo_utn_blanco = "TPDAO\FRONT\PICS\logo_utn_peque.png"
        self.logo_utn = PhotoImage(file=self.logo_utn_blanco)

        admin_socios = Button(botonera, text="Administración de Socios", command=self.abrir_administrar_socio, fg="white",
                              bg="#23b5d3", font=self.fuente_personalizable, width=20)
        admin_socios.pack(fill="both", expand=True)

        admin_libros = Button(botonera, text="Administración de Libros", command=self.abrir_administrar_libro,
                             fg="white", bg="#23b5d3", font=self.fuente_personalizable, width=20)
        admin_libros.pack(fill="both", expand=True)

        registrar_pyd = Button(botonera, text="Gestionar Préstamos", command=self.abrir_administrar_pyd, fg="white",
                               bg="#23b5d3", font=self.fuente_personalizable, width=20)
        registrar_pyd.pack(fill="both", expand=True)

        generar_reportes = Button(botonera, text="Generar Reportes", command="", fg="white",
                                  bg="#23b5d3", font=self.fuente_personalizable, width=20)
        generar_reportes.pack(fill="both", expand=True)

        botonera.pack(fill="both", expand=True)

        espacio_logo_utn.pack(fill="both", expand=True)

        logo_utn_footer = Label(espacio_logo_utn, image=self.logo_utn, background="#071013", pady=20)
        logo_utn_footer.pack(fill="both", expand=True)

    def abrir_administrar_socio(self):
        ventana_socio = Toplevel(self.master)
        admin_socio = VentanaAdministrarSocio(ventana_socio)
        ventana_socio.mostrar()

    def abrir_administrar_libro(self):
        ventana_libro = Toplevel(self.master)
        admin_libro = VentanaAdministrarLibro(ventana_libro)
        ventana_libro.mostrar()
        
    def abrir_administrar_pyd(self):
        ventana_pyd = Toplevel(self.master)
        admin_pyd = VentanaAdministrarPyd(ventana_pyd)
        ventana_pyd.mostrar()

    def mostrar(self):
        self.master.mainloop()

if __name__ == '__main__':
    root = Tk()
    ventana_principal = Principal(root)
    ventana_principal.mostrar()
