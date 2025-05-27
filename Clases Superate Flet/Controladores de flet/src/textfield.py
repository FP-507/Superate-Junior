import flet as ft

def main(page: ft.Page):
    page.title = "TextField Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_field = ft.TextField(label="Enter your name", hint_text="Type here...", autofocus=True, width=300)
    text_field2 = ft.TextField(label="Enter your email", hint_text="Type here...", width=300, multiline=True)
    text_field3 = ft.TextField(label="Password", hint_text="Type your password...", password=True, width=300)

    page.add(
        text_field,
        text_field2,
        text_field3
    )

ft.app(target=main)
