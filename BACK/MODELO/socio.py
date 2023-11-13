class Socio:
    def __init__(self, nombre, apellido, tipoDocumento, numeroDocumento):
        self._nombre = nombre
        self._apellido = apellido
        self._tipoDocumento = tipoDocumento
        self._numeroDocumento = numeroDocumento
        
    def __str__(self) -> str:
        return 'Nombre: ' + str(self._nombre) +\
            ' | Apellido: ' + str(self._apellido) + ' | Tipo de Documento: ' + str(self._tipoDocumento) +\
                ' | Número de Documento: ' + str(self._numeroDocumento) 
                
    # Métodos Accesores
    
    # Getters
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def tipoDocumento(self):
        return self._tipoDocumento
    
    @property
    def numeroDocumento(self):
        return self._numeroDocumento

    
    # Setters
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre
        
    @apellido.setter
    def apellido(self, nuevoApellido):
        self._apellido = nuevoApellido
        
    @tipoDocumento.setter
    def tipoDocumento(self, nuevoTipoDocumento):
        self._tipoDocumento = nuevoTipoDocumento
        
    @numeroDocumento.setter
    def numeroDocumento(self, nuevoNumeroDocumento):
        self._numeroDocumento = nuevoNumeroDocumento
        
    
    
    