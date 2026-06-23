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

       
        
        cursor.execute("SELECT * FROM vista_libros")  #tabla virtual
        registros=cursor.fetchall() #nombre de la tabla/el resultado de cursor fetchall
        
        libros =[] #lsita vacia
        for registro in registros:  #crea un nuevo libro con nueva info
            libro = Libro(
            id=registro[0],
            titulo=registro[1],
            autor=registro[2],
            isbn=registro[3],
            disponible=registro[4]
            )
            libros.append(libro)
           

        cursor.close()
        conexion.close()
        return libros
    #Crear insertar

    def insertar(self,libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()#Conexion es la clase conexion es la varibale

#recibe parametro %s
        sql="""
        INSERT INTO libro(id,titulo,autor,isbn,disponible)
        VALUES(%s,%s,%s,%s,%s)
        """
        cursor.execute(
            sql,

            (libro.id,
             libro.titulo,
             libro.autor,
             libro.isbn,
             libro.disponible)
        )

        conexion.commit()
        cursor.close()
        conexion.close()
        

    def actualizar(self,libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()#C

        #modifique por ID 
        sql=""" 
        UPDATE libro
        SET titulo = %s,autor = %s,isbn= %s ,
        disponible = %s
        WHERE id = %s  

         """
        cursor.execute(
            sql,
            (libro.titulo,
             libro.autor,
             libro.isbn,
             libro.disponible,
             libro.id)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    #eliminar un regsitro
    def eliminar(self,libro_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()#C

        cursor.execute(
            "DELETE FROM libro WHERE id = %s",
             (libro_id,)
             )
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM libro ORDER BY id DESC")
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]


