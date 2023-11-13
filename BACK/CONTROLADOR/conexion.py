import sqlite3
from BACK.MODELO import libro
from BACK.MODELO import socio

# Usamos el Patrón Singleton...

class Conexion:
    '''
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conexion, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('BBDD\\tp-dao.db')
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    Si trabajamos luego con el patrón Singleton, tenemos que usar luego:
    
        conexion_instance = Conexion()        
        conn = conexion_instance.conn  
        cursor = conexion_instance.cursor


    # Getters que permitirán conseguir de forma única la conexión y definir el cursor:

    @property
    def getConexion(self):
        return self.conn

    @property
    def getCursor(self):
        return self.cursor

    '''
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
    
    # Registrar Alta Libro
    
    # Paráms de Socio: Id, nombre, apellido, tipoDocumento, numeroDocumento
    
    def insertar_socio(self, socio):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
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

    # Registrar Baja Libro
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

    # Actualizar Libro
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
    
    # Registrar Alta Libro
    
    # Paráms de Libro a insertar: isbn, titulo, precio_reposicion, estado

    
    def insertar_libro(self, libro):
        conn = sqlite3.connect('TPDAO\BBDD\TPDAO.db')
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
