import flet as ft 

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_700

    # Crear un campo de texto
    txt_numero = ft.Text(value="0", size=30, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, width=100)
    # Crear una función para incrementar el número  
    def incrementar(cant):
        # Obtener el valor actual del campo de texto
        numero_actual = int(txt_numero.value)
        # Incrementar el número
        numero_incrementado = numero_actual + cant
        # Actualizar el campo de texto con el nuevo valor
        txt_numero.value = str(numero_incrementado)
        # Redibujar la página para mostrar el nuevo valor
        page.update()

    # Crear un botón para incrementar el número
    btn_incrementar = ft.IconButton(icon=ft.icons.ARROW_UPWARD, icon_color=ft.colors.GREEN, on_click=lambda e: incrementar(1))

    # Crear un botón para decrementar el número
    btn_disminuir = ft.IconButton(icon=ft.icons.ARROW_DOWNWARD, icon_color=ft.colors.RED, on_click=lambda e: incrementar(-1))


    layout = ft.Row(
        controls=[
            btn_incrementar,
            txt_numero,
            btn_disminuir
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    # Agregar los controles a la página
    page.add(layout)

ft.app(target=main)