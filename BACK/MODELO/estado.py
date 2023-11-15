class Estado:
    def __init__(self, estadoLibro):
        self._estadoLibro = estadoLibro
    
    def __str__(self) -> str:
        return str(self._estadoLibro)
    
        # Métodos Accesores
    
    # Getters
    
    @property
    def estadoLibro(self):
        return self._estadoLibro
    
    # Setters
    
    @estadoLibro.setter
    def estadoLibro(self, nuevoEstadoLibro):
        self._estadoLibro = nuevoEstadoLibro