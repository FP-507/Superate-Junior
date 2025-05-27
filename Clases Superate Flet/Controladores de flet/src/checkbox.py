import flet as ft

def main(page: ft.Page):
    page.title = "Checkbox Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    def on_checkbox_change(e):
        if e.control.value:
            page.add(ft.Text("Checkbox is checked!"))
        else:
            page.add(ft.Text("Checkbox is unchecked!"))

    
    checkbox1 = ft.Checkbox(
        label="Accept Terms and Conditions",
        value=False,
        on_change=on_checkbox_change,
        width=300,
    )

    page.add(
        checkbox1,
    )


ft.app(target=main)