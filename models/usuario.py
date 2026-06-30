class Usuario:

    #constructor
    def __init__(self,id,nombre,matricula,correo,carrera):
        self.id = id
        self.nombre = nombre
        self.matricula= matricula
        self.correo = correo
        self.carrera= carrera
        
        self.activo= True
    def activar(self):
        self.activo = True

    def desactivat(self):
        self.activo =False

    def mostrar_info(self):
        return f"Usuario id{self,self.id_usuario},Nombre:{self.nombre},Matricula:{self.matricula},Email:{self.correo},Carrera:{self.carrera},Activo:{'Si'if self.activo else 'No'}"
        