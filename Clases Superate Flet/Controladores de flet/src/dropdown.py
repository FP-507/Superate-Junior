import flet as ft

def main(page: ft.Page):
    page.title = "Dropdown Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    def on_dropdown_change(e):
        page.add(ft.Text(f"Selected: {e.control.value}"))
    
    dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Option 1"),
            ft.dropdown.Option("Option 2"),
            ft.dropdown.Option("Option 3"),
        ],
        label="Select an option",
        on_change=on_dropdown_change,
        width=300,
    )
    page.add(
        dropdown,
    )

    
ft.app(target=main)