import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Hola Mundo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Crear un campo de texto
    txt_nombre = ft.TextField(label="Nombre", autofocus=True)

    # Crear un botón
    btn_saludo = ft.ElevatedButton(text="Saludar", on_click=lambda e: page.add(ft.Text(f"Hola, {txt_nombre.value}!")))

    # Agregar los controles a la página
    page.add(txt_nombre, btn_saludo)

ft.app(target=main)