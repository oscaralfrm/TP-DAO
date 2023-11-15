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
        sql_count_loans = "SELECT COUNT(*) FROM prestamo WHERE numeroDocumento = ?"
        cursor.execute(sql_count_loans, (prestamo.numeroDocumento,))
        existing_loans = cursor.fetchone()[0]

        # Check if the socio has any book in the estado 'Extraviado' or 'Prestado'
        sql_check = '''
            SELECT COUNT(*) FROM prestamo 
            JOIN libro ON prestamo.isbn = libro.isbn 
            WHERE prestamo.numeroDocumento = ? 
            AND (libro.estado = 'Extraviado' OR libro.estado = 'Prestado')
        '''
        cursor.execute(sql_check, (prestamo.numeroDocumento,))
        books_extraviado_or_prestado = cursor.fetchone()[0]

        if existing_loans < 3 and books_extraviado_or_prestado == 0:
            # Check if the book is not already borrowed
            sql_check_borrowed = "SELECT estado FROM libro WHERE isbn = ?"
            cursor.execute(sql_check_borrowed, (prestamo.isbn,))
            libro_estado = cursor.fetchone()

            if libro_estado and libro_estado[0] == 'Disponible':
                # Insert the new Prestamo record
                sql_insert_prestamo = '''
                    INSERT INTO prestamo (numeroDocumento, isbn, fechaPrestamo, fechaDevolucion, cantidadDias) 
                    VALUES (?, ?, ?, ?, ?)
                '''
                cursor.execute(sql_insert_prestamo, (
                    prestamo.numeroDocumento,
                    prestamo.isbn,
                    prestamo.fechaPrestamo,
                    prestamo.fechaDevolucion,
                    prestamo.cantidadDias
                ))

                # Update the Libro estado to 'Prestado'
                sql_update_libro = "UPDATE libro SET estado = 'Prestado' WHERE isbn = ?"
                cursor.execute(sql_update_libro, (prestamo.isbn,))

                n = cursor.rowcount
                conn.commit()
                cursor.close()
                conn.close()
                return n
            else:
                # If the book is already borrowed, return a message or handle accordingly
                cursor.close()
                conn.close()
                return 0
        else:
            # If the limit is reached or books are extraviado or prestado, return a message or handle accordingly
            cursor.close()
            conn.close()
            return 0

        
    def get_socio_by_numeroDocumento(self, selected_socio_numeroDocumento):
            # Fetch Socio based on document number
            conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
            cursor = conn.cursor()
            sql = "SELECT nombre, apellido, tipoDocumento, numeroDocumento FROM socio WHERE numeroDocumento = ?"
            cursor.execute(sql, (selected_socio_numeroDocumento,))
            socio_data = cursor.fetchone()
            cursor.close()
            conn.close()

            # If Socio is found, create a Socio object and return it
            if socio_data:
                return socio.Socio(
                    nombre=socio_data[0],
                    apellido=socio_data[1],
                    tipoDocumento=socio_data[2],
                    numeroDocumento=socio_data[3]
                )

            # If Socio is not found, return None or raise an exception as needed
            return None

    def get_libro_by_isbn(self, selected_libro_isbn):
        # Fetch Libro based on ISBN
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
        cursor = conn.cursor()
        sql = "SELECT isbn, titulo, precio_reposicion, estado FROM libro WHERE isbn = ?"
        cursor.execute(sql, (selected_libro_isbn,))
        libro_data = cursor.fetchone()
        cursor.close()
        conn.close()

        # If Libro is found, create a Libro object and return it
        if libro_data:
            estado_libro = libro_data[3]
            return libro.Libro(
                isbn=libro_data[0],
                titulo=libro_data[1],
                precio_reposicion=libro_data[2],
                estado_libro=estado_libro  # Use _estado instead of estado
            )

        # If Libro is not found, return None or raise an exception as needed
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