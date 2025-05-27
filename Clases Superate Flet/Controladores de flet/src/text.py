import flet as ft

def main(page: ft.Page):
    page.title = "Text Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text1 = ft.Text("Hello, World!", size=30, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD)
    text2 = ft.Text("This is a Flet example.", italic=True, size=20, color=ft.colors.GREEN)

    page.add(text1, text2)

ft.app(target=main)