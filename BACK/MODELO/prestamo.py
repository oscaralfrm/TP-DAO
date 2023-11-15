from BACK.MODELO import socio
from BACK.MODELO import libro

class Prestamo:
    
    def __init__(self, socio, libro, fechaPrestamo, fechaDevolucion, cantidadDias):
        self._socio = socio
        self._libro = libro
        self._fechaPrestamo = fechaPrestamo
        self._fechaDevolucion = fechaDevolucion
        self._cantidadDias = cantidadDias
        
    def __str__(self) -> str:
        return 'Número de Documento del Socio: ' + str(self._socio.numeroDocumento) + \
            ' | ISBN del Libro: ' + str(self._libro.isbn) +\
            ' | Fecha del Préstamo (Alta): ' + str(self._fechaPrestamo) + \
                ' | Fecha de Devolución (Baja): ' + str(self._fechaDevolucion)  + \
                    ' | Cantidad de Días del Préstamo: ' + str(self._cantidadDias)
                
    # Métodos Accesores
    
    # Getters
    
    @property
    def numeroDocumento(self):
        return self._socio.numeroDocumento
    
    @property
    def isbn(self):
        return self._libro.isbn
    
    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo
    
    @property
    def fechaDevolucion(self):
        return self._fechaDevolucion

    @property
    def cantidadDias(self):
        return self._cantidadDias
    
    # Setters
    # Menos el de socio.numeroDocumento y el de libro.isbn, porque esa data ya la tenemos
    # en otra parte del código y NO se debería poder modificar en el selector.
        
    @fechaPrestamo.setter
    def fechaPrestamo(self, nuevaFechaPrestamo):
        self._fechaPrestamo = nuevaFechaPrestamo
        
    @fechaDevolucion.setter
    def fechaDevolucion(self, nuevaFechaDevolucion):
        self._fechaDevolucion = nuevaFechaDevolucion
    
    @cantidadDias.setter
    def cantidadDias(self, nuevaCantidadDias):
        self._cantidadDias = nuevaCantidadDias