import flet as ft

def main(page: ft.Page):
    page.title = "RadioGroup Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    def on_radio_change(e):
        page.add(ft.Text(f"Selected: {e.control.value}"))

    radio_group = ft.RadioGroup(
        on_change=on_radio_change,
        content= ft.Column(
            controls=[
                ft.Radio(value="Option 1", label="Option 1"),
                ft.Radio(value="Option 2", label="Option 2"),
                ft.Radio(value="Option 3", label="Option 3"),
            ],
        ),
    )

    page.add(
        radio_group,
    )


    
ft.app(target=main) 