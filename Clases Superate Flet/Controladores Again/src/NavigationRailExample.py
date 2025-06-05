import flet as ft

from views.home_view import build_home_view
from views.cart_view import build_cart_view
from views.profile_view import build_profile_view

def main(page: ft.Page):
    """Example using only NavigationBar."""
    page.title = "Ejemplo NavigationBar"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.BLUE_GREY_700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    current_view = ft.Container(expand=True)
    views = [build_home_view, build_cart_view, build_profile_view]
    current_view.content = views[0]()

    def on_change(e: ft.ControlEvent):
        current_view.content = views[e.control.selected_index]()
        page.update()

    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART, label="Cart"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
        ],
        on_change=on_change,
    )

    page.add(ft.Column([nav, current_view], expand=True))

if __name__ == "__main__":
    ft.app(target=main)