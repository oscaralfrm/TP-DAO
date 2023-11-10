import sqlite3

class Conexion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conexion, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('TP-DAO/BBDD/daoBBDD.sqlite')
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    # Getters que permitirán conseguir de forma única la conexión y definir el cursor:

    @property
    def getConexion(self):
        return self.conn

    @property
    def getCursor(self):
        return self.cursor

# Ejemplo de uso:
db_instance = Conexion()
conn = db_instance.getConexion()
cursor = db_instance.getCursor()

# Realiza operaciones con la base de datos usando 'conn' y 'cursor'

# Cierra la conexión y el cursor cuando hayas terminado
cursor.close()
conn.close()




