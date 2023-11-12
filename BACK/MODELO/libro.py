class Libro:
    def __init__(self, isbn, titulo, precio_reposicion, estado):
        self._isbn = isbn
        self._titulo = titulo
        self._precio_reposicion = precio_reposicion
        self._estado = estado
        
    def __str__(self) -> str:
        return 'ISBN: ' + str(self.isbn) + ' | Título: ' + str(self.titulo) +\
            ' | Precio de Reposición: ' + str(self.precio_reposicion) + \
                ' | Estado: ' + str(self.estado) 
                
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
        