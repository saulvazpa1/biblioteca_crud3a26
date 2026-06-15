#DAO: Data Acces Object
#libro_dao: Objeto de acceso a datos de la tabla libro


from database.conexion import Conexion    #Carpeta/archivo/clase 
from models.libro import Libro

class LibroDAO:
#SELECT * FROM libro
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
      #obejto para mysql 
        cursor = conexion.cursor()
        #que comando ejecutar
        cursor.execute("SELECT * FROM libro")
        registros=cursor.fetchall() #nombre de la tabla/el resultado de cursor fetchall
        
        libros =[] #lsita vacia
        for registro in registros:  #crea un nuevo libro con nueva info
            libro = Libro(
            registro.id,
            registro.titulo,
            registro.autor,
            registro.isb,
            registro.disponible)
            libros.append(libro)

        cursor.close()
        conexion.close()
        return libros