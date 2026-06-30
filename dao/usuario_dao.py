# DAO: Data Access Object
# usuario_dao: Objeto de acceso a datos de la tabla usuario

from database.conexion import Conexion    # Carpeta/archivo/clase 
from models.usuario import Usuario

class UsuarioDAO:
# SELECT * FROM usuario
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM vista_usuarios")  # tabla virtual
        registros = cursor.fetchall() # nombre de la tabla/el resultado de cursor fetchall
        
        usuarios = [] # lista vacia
        for registro in registros:  # crea un nuevo usuario con nueva info
            usuario = Usuario(
                id=registro[0],
                nombre=registro[1],
                matricula=registro[2],
                correo=registro[3],  
                carrera=registro[4]   
            )
            usuarios.append(usuario)

        cursor.close()
        conexion.close()
        return usuarios

    # Crear insertar
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor() # Conexion es la clase conexion es la variable

        # El SQL espera las columnas de la BD: id, nombre, matricula, carrera, correo
        sql = """
        INSERT INTO usuario(id, nombre, matricula, carrera, correo)
        VALUES(%s, %s, %s, %s, %s)
        """
        cursor.execute(
            sql,
            (usuario.id,
             usuario.nombre,
             usuario.matricula,
             usuario.carrera, 
             usuario.correo)  
        )

        conexion.commit()
        cursor.close()
        conexion.close()
        

    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor() # C

        # Modifica por ID en la BD
        sql = """ 
        UPDATE usuario
        SET nombre = %s, matricula = %s, carrera = %s, correo = %s
        WHERE id = %s  
        """
        cursor.execute(
            sql,
            (usuario.nombre,
             usuario.matricula,
             usuario.carrera, 
             usuario.correo,  
             usuario.id)
        )

        conexion.commit() 
        cursor.close()
        conexion.close()


    # eliminar un registro
    def eliminar(self, usuario_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor() # C

        cursor.execute(
            "DELETE FROM usuario WHERE id = %s",
            (usuario_id,)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM usuario ORDER BY id DESC")
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]