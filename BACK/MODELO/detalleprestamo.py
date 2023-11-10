class DetallePrestamo:
    def __init__(self, numeroPrestamo, cantidadDiasPrestamo):
        self.numeroPrestamo = numeroPrestamo
        self.cantidadDiasPrestamo = cantidadDiasPrestamo
        
    def __str__(self) -> str:
        return 'Número del Préstamo: ' + str(self.numeroPrestamo) + \
            ' | Cantidad de Días del Préstamo: ' + str(self.cantidadDiasPrestamo)