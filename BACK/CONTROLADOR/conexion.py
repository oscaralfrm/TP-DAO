import sqlite3
from BACK.MODELO import libro
from BACK.MODELO import socio
from BACK.MODELO import estado

# Usamos el Patrón Singleton...

class Conexion:

    # Métodos Query Específicos - Socio
    
        # Sobrecarga del método __str__(), borrar, es sólo de prueba
    def __str__(self):
        datos = self.consultar_socios()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux
    
    # Consultar Libros
    def consultar_socios(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        seleccionar_tabla = 'SELECT * FROM socio'
        cursor.execute(seleccionar_tabla)
        datos = cursor.fetchall()
        cursor.close()    
        conn.close()
        return datos
        
    def buscar_socio_conexion(self, numeroDocumento):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM socio WHERE numeroDocumento = {}".format(numeroDocumento)
        cursor.execute(sql)
        datos = cursor.fetchone()
        cursor.close()    
        conn.close()
        return datos
    
    # Conseguir los datos del socio para la tabla préstamo
    
    def get_datos_socio(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, apellido, tipoDocumento, numeroDocumento FROM socio ORDER BY numeroDocumento ASC")
        socio_data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return [socio.Socio(nombre, apellido, tipoDocumento, numeroDocumento) for nombre, apellido, tipoDocumento, numeroDocumento in socio_data]

    
    # Registrar Alta Socio
    
    # Paráms de Socio: Id, nombre, apellido, tipoDocumento, numeroDocumento
    
    def insertar_socio(self, socio):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db', isolation_level=None)
        cursor = conn.cursor()
        sql='''INSERT INTO socio (nombre, apellido, tipoDocumento, numeroDocumento) 
        VALUES('{}', '{}', '{}', '{}')'''.format(socio.nombre, socio.apellido, socio.tipoDocumento, 
                                                 socio.numeroDocumento)
        cursor.execute(sql)
        n = cursor.rowcount
        conn.commit()    
        cursor.close()
        conn.close()
        return n    

    # Registrar Baja Socio
    def eliminar_socio(self, id_socio):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = "DELETE FROM socio WHERE id = ?"
        cursor.execute(sql, (id_socio,))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount  

    
    def borrar_todo_socio(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        
        sql_delete_all = 'DELETE FROM socio'
        cursor.execute(sql_delete_all)
        
        sql_reset_auto_increment = 'DELETE FROM sqlite_sequence WHERE name="socio"'
        cursor.execute(sql_reset_auto_increment)
        
        n = cursor.rowcount

        conn.commit()
        cursor.close()
        conn.close()
        return n

    # Actualizar Socio
    def modificar_socio(self, id_socio, nuevo_nombre, nuevo_apellido, nuevo_tipoDocumento, nuevo_numeroDocumento):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = """UPDATE socio
                SET nombre = ?, apellido = ?, tipoDocumento = ?, numeroDocumento = ?
                WHERE id = ?"""
        cursor.execute(sql, (nuevo_nombre, nuevo_apellido, nuevo_tipoDocumento, nuevo_numeroDocumento, id_socio))
        conn.commit()
        cursor.close()
        conn.close()

    # Métodos Query Específicos - Libro
    
    # Sobrecarga del método __str__(), borrar, es sólo de prueba
    def __str__(self):
        datos = self.consultar_libros()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux
    
    # Consultar Libros
    def consultar_libros(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        seleccionar_tabla = 'SELECT * FROM libro'
        cursor.execute(seleccionar_tabla)
        datos = cursor.fetchall()
        cursor.close()    
        conn.close()
        return datos
        
    def buscar_libro_conexion(self, isbn):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM libro WHERE isbn = {}".format(isbn)
        cursor.execute(sql)
        datos = cursor.fetchone()
        cursor.close()    
        conn.close()
        return datos
    
    # Conseguir los datos del libro para la tabla préstamo
    
    def get_datos_libro(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        cursor.execute("SELECT isbn, titulo, precio_reposicion, estado FROM libro ORDER BY isbn ASC")
        libro_data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return [libro.Libro(isbn, titulo, precio_reposicion, estado) for isbn, titulo, precio_reposicion, estado in libro_data]
    
    # Registrar Alta Libro
    
    # Paráms de Libro a insertar: isbn, titulo, precio_reposicion, estado

    def insertar_libro(self, libro):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db', isolation_level=None)
        cursor = conn.cursor()
        sql='''INSERT INTO libro (isbn, titulo, precio_reposicion, estado) 
        VALUES('{}', '{}', '{}', '{}')'''.format(libro.isbn, libro.titulo, libro.precio_reposicion, 
                                                 libro.estado)
        cursor.execute(sql)
        n = cursor.rowcount
        conn.commit()    
        cursor.close()
        conn.close()
        return n    

    # Registrar Baja Libro
    def eliminar_libro(self, id_libro):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = "DELETE FROM libro WHERE id = ?"
        cursor.execute(sql, (id_libro,))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount  

    
    def borrar_todo_libro(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        
        sql_delete_all = 'DELETE FROM libro'
        cursor.execute(sql_delete_all)
        
        sql_reset_auto_increment = 'DELETE FROM sqlite_sequence WHERE name="libro"'
        cursor.execute(sql_reset_auto_increment)
        
        n = cursor.rowcount

        conn.commit()
        cursor.close()
        conn.close()
        return n

    # Actualizar Libro
    def modificar_libro(self, id_libro, nuevo_isbn, nuevo_titulo, nuevo_precio, nuevo_estado):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = """UPDATE libro
                SET isbn = ?, titulo = ?, precio_reposicion = ?, estado = ?
                WHERE id = ?"""
        cursor.execute(sql, (nuevo_isbn, nuevo_titulo, nuevo_precio, nuevo_estado, id_libro))
        conn.commit()
        cursor.close()
        conn.close()

    # Métodos Query Específicos - Préstamo

    def insertar_prestamo(self, prestamo):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db', isolation_level=None)
        cursor = conn.cursor()

        # Check if the number of existing loans for the given numeroDocumento is less than 3
        sql_count_loans = f"SELECT COUNT(*) FROM prestamo WHERE numeroDocumento = '{prestamo.numeroDocumento}'"
        cursor.execute(sql_count_loans)
        existing_loans = cursor.fetchone()[0]

        # Check if the socio has any book in the estado 'Extraviado'
        sql_check_extraviado = f'''
            SELECT COUNT(*) FROM prestamo 
            JOIN libro ON prestamo.isbn = libro.isbn 
            WHERE prestamo.numeroDocumento = '{prestamo.numeroDocumento}' 
            AND libro.estado = 'Extraviado' OR libro.estado = 'Prestado'
        '''
        cursor.execute(sql_check_extraviado)
        books_extraviado = cursor.fetchone()[0]

        if existing_loans < 3 or books_extraviado == 0:
            # Insert the new Prestamo record
            sql_insert_prestamo = f'''
                INSERT INTO prestamo (numeroDocumento, isbn, fechaPrestamo, fechaDevolucion, cantidadDias) 
                VALUES ('{prestamo.numeroDocumento}', '{prestamo.isbn}', 
                        '{prestamo.fechaPrestamo}', '{prestamo.fechaDevolucion}', '{prestamo.cantidadDias}')
            '''
            cursor.execute(sql_insert_prestamo)

            # Update the Libro estado to 'Prestado'
            sql_update_libro = f"UPDATE libro SET estado = 'Prestado' WHERE isbn = '{prestamo.isbn}'"
            cursor.execute(sql_update_libro)

            n = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return n
        else:
            # If the limit is reached or books are extraviado, return a message or handle accordingly
            cursor.close()
            conn.close()
            return 0
        
    def get_socio_by_numeroDocumento(self, numero_documento):
        # Fetch Socio based on document number
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = f"SELECT * FROM socio WHERE numeroDocumento = {numero_documento}"
        cursor.execute(sql)
        socio_data = cursor.fetchone()
        cursor.close()
        conn.close()

        # If Socio is found, create a Socio object and return it
        if socio_data:
            # Assuming you have a Socio class
            # You might need to modify this based on your actual Socio class implementation
            return socio.Socio(numeroDocumento=socio_data[0], nombre=socio_data[1], apellido=socio_data[2], tipoDocumento=socio_data[3])

        # If Socio is not found, return None or raise an exception as needed
        return None
    
    
    def get_libro_by_isbn(self, isbn):
        # Fetch Libro based on ISBN
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = f"SELECT * FROM libro WHERE isbn = {isbn}"
        cursor.execute(sql)
        libro_data = cursor.fetchone()
        cursor.close()
        conn.close()

        # If Libro is found, create a Libro object and return it
        if libro_data:
            # Assuming libro_data[3] is the column index for estadoLibro in the libro table
            estado_libro = libro_data[3]

            # Create an instance of the Estado class
            estado_instance = estado.Estado(estado_libro)

            # Create a Libro object with _estado attribute
            return libro.Libro(isbn=libro_data[0], titulo=libro_data[1], precio_reposicion=libro_data[2], estado_libro=estado_instance)

        # If Libro is not found, return None
        return None

    def consultar_prestamos(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        seleccionar_tabla = 'SELECT * FROM prestamo'
        cursor.execute(seleccionar_tabla)
        datos = cursor.fetchall()
        cursor.close()    
        conn.close()
        return datos

    def borrar_todo_prestamo(self):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        
        sql_delete_all = 'DELETE FROM prestamo'
        cursor.execute(sql_delete_all)
        
        sql_reset_auto_increment = 'DELETE FROM sqlite_sequence WHERE name="prestamo"'
        cursor.execute(sql_reset_auto_increment)
        
        n = cursor.rowcount

        conn.commit()
        cursor.close()
        conn.close()
        return n