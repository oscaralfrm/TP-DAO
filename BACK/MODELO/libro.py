from BACK.MODELO import estado

class Libro:
    
    def __init__(self, isbn, titulo, precio_reposicion, estado_libro):
        self._isbn = isbn
        self._titulo = titulo
        self._precio_reposicion = precio_reposicion
        self._estado = estado.Estado(estado_libro)
        
    def __str__(self):
        return 'ISBN: ' + str(self._isbn) + ' | Título: ' + str(self._titulo) +\
            ' | Precio de Reposición: ' + str(self._precio_reposicion) + \
                str(self._estado._estadoLibro)
                
    # Métodos Accesores
    
    # Getters
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def precio_reposicion(self):
        return self._precio_reposicion
    
    @property
    def estado(self):
        return self._estado

    
    # Setters
    
    @isbn.setter
    def isbn(self, nuevoIsbn):
        self._isbn = nuevoIsbn
        
    @titulo.setter
    def titulo(self, nuevoTitulo):
        self._titulo = nuevoTitulo
        
    @precio_reposicion.setter
    def precio_reposicion(self, nuevoPrecioReposicion):
        self._precio_reposicion = nuevoPrecioReposicion
        
    @estado.setter
    def estado(self, nuevoEstado):
        self._estado = nuevoEstado
        