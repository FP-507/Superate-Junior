import flet as ft

from views.home_view import build_home_view
from views.cart_view import build_cart_view
from views.profile_view import build_profile_view

def main(page: ft.Page):
    """Example using only NavigationRail."""
    page.title = "Ejemplo NavigationRail"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_700
    page.fonts = {
        "Roboto": "https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu4mxK.woff2",
        "RobotoMono": "https://fonts.gstatic.com/s/robotomono/v6/0Qw8c3b7a5k9f8d3e4c5f4c5f4c5f4c5.woff2",
    }

    current_view = ft.Container(expand=True, content=[])
    views = [build_home_view,build_cart_view,build_profile_view]
    current_view.content = views[0]()

    def on_change(e: ft.ControlEvent):
        current_view.content = views[e.control.selected_index]()
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home", ),
            ft.NavigationRailDestination(icon=ft.Icons.SHOPPING_CART, label="Cart", ),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Profile", ),
        ],
        on_change=on_change,
        bgcolor=ft.colors.BLUE_GREY_700,
        selected_label_text_style=ft.TextStyle(
            color=ft.colors.GREEN_ACCENT_400,
            size=16,
            font_family="Roboto",
            weight=ft.FontWeight.BOLD,
        ),
        unselected_label_text_style=ft.TextStyle(
            color=ft.colors.WHITE,
            size=14,
            font_family="RobotoMono",
            weight=ft.FontWeight.W_600,
        ),
    )

    page.add(ft.Row([rail, current_view], expand=True))


ft.app(target=main)
