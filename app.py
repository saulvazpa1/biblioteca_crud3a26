
from dao.libro_dao import LibroDAO #/carpeta ./nombre del archvio/clase
from models.libro import Libro

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
    





def main():
    print("====BIBLIOTECA UNI===")
    print("Menu de opciones")
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



    

    
if __name__ == "__main__":
    main()
    