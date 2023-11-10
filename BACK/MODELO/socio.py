class Socio:
    def __init__(self, numeroSocio, nombre, apellido, tipoDocumento, numeroDocumento, prestamo):
        self.numeroSocio = numeroSocio
        self.nombre = nombre
        self.apellido = apellido
        self.tipoDocumento = tipoDocumento
        self.numeroDocumento = numeroDocumento
        self.prestamo = prestamo
        
    def __str__(self) -> str:
        return 'Número de Socio: ' + str(self.numeroSocio) + ' | Nombre: ' + str(self.nombre) +\
            ' | Apellido: ' + str(self.apellido) + ' | Tipo de Documento: ' + str(self.tipoDocumento) +\
                ' | Número de Documento: ' + str(self.numeroDocumento) + ' | Préstamo: ' + str(self.prestamo)
                
    # Métodos Accesores
    
    # Getters
    
    @property
    def nombre(self):
        return self.nombre
    
    # Setters
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.nombre = nuevoNombre
    
    
    