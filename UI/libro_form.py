import flet as ft
def libro_form(regresar):
    titulo_input = ft.TextField(
        label="Titulo del libro:",
        width=400 
    )

    autor_input = ft.TextField(
        label="Autor del libro:",
        width= 400
    )

    isbn_input =  ft.TextField(
        label="ISBN:",
        width= 400
    )

    mensaje = ft.Text(
        "",
        color= ft.Colors.GREEN
    )

    #crear la funcion para el boton
    def guardar_libro(e):
        titulo=titulo_input.value#recuperar los valores de TEXTFIELD
        autor = autor_input.value#nombre_text_field.value
        isbn = isbn_input.value

        #validacion de datos 

        if titulo ==" " or autor== "" or isbn=="":
            mensaje.value="Todos los cmapos son obligatorios"
            mensaje.color= ft.Colors.RED
        else:
            mensaje.value=f"Libro'{titulo}'listo para insertar"
            print(f"Titulo:'{titulo}',Autor:'{autor}',ISBN:'{isbn}'")#para ver en consola si funciona
            mensaje.color=ft.Colors.GREEN
            #limpiar campos
            titulo_input.value=""
            autor_input.value=""
            isbn_input.value=""
            
        e.page.update()
    return ft.Container(
        padding= 30,
        content= ft.Column(#crear lista necesita controls
            controls=[
                ft.Text(
                    "Registrar nuevo libro",
                    size=24,
                    weight= ft.FontWeight.BOLD,
                    color =ft.Colors.BLUE_GREY_800
                   
                ),
                ft.Text(
                    "Captura los datos basicos del libro",
                    size=14,
                    color = ft.Colors.BLUE_GREY_600
                ), #las comas los separar cada elemento
                
                
                titulo_input,
                autor_input,
                isbn_input,

                ft.Row(
                    controls=[


                        ft.ElevatedButton(
                            "Registrar libro",
                            icon=ft.Icons.SAVE,
                            on_click=guardar_libro
                        ),
                        ft.OutlinedButton(
                            "Regresar",
                            icon = ft.Icons.ARROW_BACK,
                            on_click= lambda e: regresar()
                        )
                    ]
                ),
                mensaje
               
            ],

            
            spacing=15
        )
    )