import flet as ft

def main(page: ft.Page):
    page.title = "ElevatedButton Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_button_click(e):
        page.add(ft.Text("Button clicked!"))

    button1 = ft.ElevatedButton("Click Me", on_click=on_button_click, width=200, height=50, style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        color=ft.colors.BLUE,
        elevation=5,
        text_style=ft.TextStyle(
            size=20,
            weight=ft.FontWeight.BOLD
        )
    ))

    page.add(
        button1
    )

ft.app(target=main)

  