
from dao.libro_dao import LibroDAO #/carpeta ./nombre del archvio/clase
from models.libro import Libro

def main():
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
if __name__ == "__main__":
    main()
    