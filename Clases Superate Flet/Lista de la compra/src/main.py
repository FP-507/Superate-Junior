import flet as ft 

def main(page: ft.Page):
    page.title = "Lista de la compra"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_500


    def agregar_al_carrito(producto):
        carrito.append(producto)
        page.open(ft.SnackBar(ft.Text(f"{producto} añadido al carrito.")))
        page.update()

    
    def pagar_carrito(e):
        page.open(ft.SnackBar(ft.Text(f"Se ha procesado el pago de {carrito} exitosamente")))
        page.update()

    search_input = ft.TextField(
    label="Buscar producto",
    label_style=ft.TextStyle(size=16, color=ft.colors.GREY_700, weight=ft.FontWeight.W_500),
    hint_text="¿Qué buscas comprar?",
    width=400, 
    bgcolor=ft.colors.WHITE,
    border_color=ft.colors.BLUE_GREY_500,
    focused_border_color=ft.colors.BLUE_GREY_700,
    text_size=ft.TextStyle(size=16, color=ft.colors.BLUE_GREY_700),
    focused_border_width=2,
)

    search_button = ft.ElevatedButton(
        text="Buscar",
        on_click=lambda e: page.update(),
        bgcolor=ft.colors.BLUE_GREY_600,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.BLUE_GREY_700,
            elevation=2,
            shadow_color=ft.colors.BLUE_GREY_900,
        )
    )

    boton_pagar = ft.ElevatedButton(
        text="Pagar carrito",
        on_click=pagar_carrito,
        bgcolor=ft.colors.GREEN_600,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.GREEN_700,
            elevation=2,
            shadow_color=ft.colors.GREEN_900,
        )
    )

    productos = ["Pan", "Leche", "Huevos", "Arroz", "Queso"]
    carrito = []

    lista_productos = ft.ListView(spacing=10, padding=10, width=400, height=300, auto_scroll=True)

    for item in productos:
        fila = ft.Row(
            controls=[
                ft.Checkbox(label=item, value=False),
                ft.IconButton(
                    icon=ft.icons.ADD_SHOPPING_CART,
                    icon_color=ft.colors.BLUE_GREY_300,
                    on_click=lambda e, producto=item: agregar_al_carrito(producto),

                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        lista_productos.controls.append(fila)


    layout = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    search_input,
                    search_button
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Text("Lista de productos disponibles:", color=ft.colors.WHITE, size=20, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
            lista_productos,
            boton_pagar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page.add(layout)

ft.app(target=main)            