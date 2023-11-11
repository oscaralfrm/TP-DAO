import sqlite3

# Usamos el Patrón Singleton...

class Conexion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conexion, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('BBDD\\tp-dao.db')
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    # Getters que permitirán conseguir de forma única la conexión y definir el cursor:

    @property
    def getConexion(self):
        return self.conn

    @property
    def getCursor(self):
        return self.cursor

    def run_query(self, query, parameters = ()):
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
            return result


