from models.libro import Libro

class  Prestamo:

    #constructor
    def __init__(self,id_prestamo,usuario,libro,fecha_prestamo,fecha_devolucion):
        self.id_prestamo=id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False

    def registrar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()
    
    def mostrar_info(self):
        return f"Prestamo ID: {self.id_prestamo},Usuario: {self.usuario.nombre},Libro:{self.libro.titulo},Fecha de Prestamo{self.fecha_prestamo},fecha de Devolucion:{self.fecha_devolucion},Devuelto:{'si'if self.devuelto else 'No'}"
