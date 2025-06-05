import flet as ft

def build_profile_view() -> ft.Control:

    return ft.Column([
        ft.Text("Perfil", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ft.Text("Información del usuario",size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
    ], 
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    expand=True,
    )