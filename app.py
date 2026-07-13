
import flet as ft


from dao.libro_dao import LibroDAO #/carpeta ./nombre del archvio/clase
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO #/carpeta ./nombre del archivo/clase
from models.usuario import Usuario
from ui.main_window import main_window



def ver_libros():
    try:
        libro_dao = LibroDAO() #tiene todo de Libro Dao

        libros = libro_dao.obtener_todos()

        print("===Libros en la Biblioteca ===")

    #si es que no hay libros  
        if len(libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in libros:
                print("-------------------------------------------")

                print(
                    f"ID:{libro.id},Titulo:{libro.titulo},"
                    f"Autor:{libro.autor},ISBN:{libro.isbn},"
                    f"Disponible:{'si' if libro.disponible else 'No'}"
                )
                print("-------------------------------------------")
        print("\n Conexion exitosa ala base de datos")
    except Exception as e:
        print("Error:")
        print(e)

#insertar
def insertar_libro():
    titulo = input("Escribe el titulo del nuevo libro:")
    autor = int(input("Escribe el id del autor:"))
    isbn = input("Escribe el isbn del nuevo libro")
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id,titulo,autor,isbn,disponible)
        libro_dao.insertar(libro)

        print("Insercion realizada con exito")
    except Exception as e :
        print("Error al insertar un nuevo libro")
        print(e)

def actualizar_libro():
    print("Selecciona el libro a actualizar")

    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int(input("Escribe el id del libro a actualizar:"))
        titulo=input("Escribe el nuevo titulo")
        autor = input("Escribe el nuevo autor")
        isbn = input("Escribe el nuevo ISBN")
        disponible = bool(input("Escribe el nuevo valor de disponible"))
        libro=Libro(id,titulo,autor,isbn,disponible)
        libro_dao.actualizar(libro)
        print(f"El libro {id} se ha actualizado exitosamente")

    except Exception as e:
        print(" Error al actualizar libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles:")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar"))
        libro_dao.eliminar(id)
        print("El libro {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar el libro{id}")
        print(e)


def ver_usuario():
    try:
        usuario_dao = UsuarioDAO() #tiene todo de Usuario Dao

        usuarios = usuario_dao.obtener_todos()

        print("=== Usuarios en la Biblioteca ===")

        #si es que no hay usuarios  
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print("-------------------------------------------")

                print(
                    f"ID:{usuario.id}, Nombre:{usuario.nombre},"
                    f" Matricula:{usuario.matricula}, Carrera:{usuario.carrera},"
                    f" Correo:{usuario.correo} "
                )
                print("-------------------------------------------")
        print("\n Conexion exitosa ala base de datos")
    except Exception as e:
        print("Error:")
        print(e)

#insertar USUARIOS
def insertar_usuario():
    nombre = input("Escribe el nombre del nuevo usuario: ")
    matricula = input("Escribe la matricula del nuevo usuario: ")
    carrera = int(input("Escribe el id de la carrera: "))
    correo = input("Escribe el correo del nuevo usuario: ")
    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        
       
        usuario = Usuario(id, nombre, matricula, correo, carrera)

        usuario_dao.insertar(usuario)
        print("Insercion realizada con exito")
    except Exception as e:
        print("Error al insertar un nuevo usuario")
        print(e)
def actualizar_usuario():
    print("Selecciona el usuario a actualizar")

    try:
        usuario_dao = UsuarioDAO()
        ver_usuario()
        id = int(input("Escribe el id del usuario a actualizar:"))
        nombre = input("Escribe el nuevo nombre:")
        matricula = input("Escribe la nueva matricula:")
        carrera = int(input("Escribe el nuevo id de la carrera:"))
        correo = input("Escribe el nuevo correo:")
        usuario = Usuario(id, nombre, matricula, correo, carrera)
        usuario_dao.actualizar(usuario)
        print(f"El usuario {id} se ha actualizado exitosamente")

    except Exception as e:
        print(" Error al actualizar usuario")
        print(e)

def eliminar_usuario():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles:")
        ver_usuario()
        id = int(input("Escribe el id del usuario a eliminar:"))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar el usuario {id}")
        print(e)
    
def menu_libros():
    print("1.ver todos los libros:")
    print("2. Insertar un nuevo libro:")
    print("3. Actualizar un libro disponible:")
    print("4. Eliminar un libro disponible:")

    opcion = int(input("Selecciona una opcion (1-4):"))
    match opcion:
        case 1:

            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4 :
           eliminar_libro()
    
def menu_usuarios():
    print("1.ver todos los Usuarios:")
    print("2. Insertar un nuevo Usuario:")
    print("3. Actualizar un Usuario disponible:")
    print("4. Eliminar un Usuario disponible:")

    opcion = int(input("Selecciona una opcion (1-4):"))
    match opcion:
        case 1:

            ver_usuario()
        case 2:
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4 :
           eliminar_usuario()

ft.app(target = main_window)


# def main():
#     print("==== BIBLIOTECA UNI ====")
#     print("1. Gestionar Libros")
#     print("2. Gestionar Usuarios")
    
#     try:
#         opcion = int(input("Selecciona una opción general (1-2): "))
#         match opcion:
#             case 1:
#                 menu_libros()
#             case 2:
#                 menu_usuarios()
#             case _:
#                 print("Opción no válida.")
#     except ValueError:
#         print("Por favor, introduce un número válido.")

    
# if __name__ == "__main__":
#     main()
    #control +k+c comentar todo