import flet as ft

def build_home_view() -> ft.Control:
    return ft.Column([
        ft.Text("Home", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ft.Text("Bienvenido a la tienda de ejemplo", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
    ], 
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    expand=True,
    )