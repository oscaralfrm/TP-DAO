class Socio:
    def __init__(self, nombre, apellido, tipoDocumento, numeroDocumento):
        self.nombre = nombre
        self.apellido = apellido
        self.tipoDocumento = tipoDocumento
        self.numeroDocumento = numeroDocumento
        
    def __str__(self) -> str:
        return 'Nombre: ' + str(self.nombre) +\
            ' | Apellido: ' + str(self.apellido) + ' | Tipo de Documento: ' + str(self.tipoDocumento) +\
                ' | Número de Documento: ' + str(self.numeroDocumento) 
                
    # Métodos Accesores
    
    # Getters
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def apellido(self):
        return self.apellido
    
    @property
    def tipoDocumento(self):
        return self.tipoDocumento
    
    @property
    def numeroDocumento(self):
        return self.numeroDocumento

    
    # Setters
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        
    @apellido.setter
    def nombre(self, nuevoApellido):
        self.apellido = nuevoApellido
        
    @tipoDocumento.setter
    def nombre(self, nuevoTipoDocumento):
        self.tipoDocumento = nuevoTipoDocumento
        
    @numeroDocumento.setter
    def nombre(self, nuevoNumeroDocumento):
        self.numeroDocumento = nuevoNumeroDocumento
        
    
    
    