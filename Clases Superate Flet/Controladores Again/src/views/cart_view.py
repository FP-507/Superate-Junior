import flet as ft

def build_cart_view() -> ft.Control:

    return ft.Column(
        controls=[
            ft.Text('carrito', size=24, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
            ft.Text('Aqui van los productos agregados', size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )