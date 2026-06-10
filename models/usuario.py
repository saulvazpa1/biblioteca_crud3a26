class Usuario:

    #constructor
    def __init__(self,id_usuario,nombre,matricula,email,carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.matricula= matricula
        self.email = email
        self.carrera= self.carrera
        self.activo= True
    def activar(self):
        self.activo = True

    def desactivat(self):
        self.activo =False

    def mostrar_info(self):
        return f"Usuario id{self,self.id_usuario},Nombre:{self.nombre},Matricula:{self.matricula},Email:{self.email},Carrera:{self.carrera},Activo:{'Si'if self.activo else 'No'}"
        