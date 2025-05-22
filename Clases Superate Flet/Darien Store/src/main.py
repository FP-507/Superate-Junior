import flet as ft

def main(page: ft.Page):
    page.title = "Darien Store"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_500
    page.window.maximized = True


    carrito = []

    productos = [
        {"nombre": "Laptop HP", "imagen": "assets//laptopHP.jpg", "categoria": "Tecnología"},
        {"nombre": "Audífonos JBL", "imagen": "assets//bocinaJBL.jpg", "categoria": "Tecnología"},
        {"nombre": "Camisa Blanca", "imagen": "assets//camisaBlanca.jpg", "categoria": "Ropa"},
        {"nombre": "Zapatos Deportivos", "imagen": "assets//zapatillasDeportivas.jpg", "categoria": "Ropa"},
    ]

    filtro_categoria = ft.Dropdown(
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Tecnología"),
            ft.dropdown.Option("Ropa"),
        ],
        value="Todos",
        label="Filtrar por categoría"
    )

    barra_busqueda = ft.TextField(label="Buscar producto...")

    lista_productos = ft.ListView(expand=True, spacing=10)
    
    def mostrar_productos():
        lista_productos.controls.clear()
        texto = barra_busqueda.value.lower()
        cat = filtro_categoria.value

        for p in productos:
            if texto in p["nombre"].lower() and (cat == "Todos" or p["categoria"] == cat):
                lista_productos.controls.append(
                    ft.Card(
                        content=ft.Row(
                            [
                                ft.Image(src=p["imagen"], width=90, height=90),
                                ft.Text(p["nombre"], size=20),
                                ft.Text(p["categoria"], size=16),
                                ft.ElevatedButton(
                                    text="Agregar al carrito",
                                    on_click=lambda e, producto=p: agregar_al_carrito(producto)
                                )
                                
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        width=400,
                        height=100,
                        margin=10,
                    )
                )
        page.update()

    def agregar_al_carrito(nombre):
        carrito.append(nombre)
        page.open(ft.SnackBar(ft.Text(f"{nombre} añadido al carrito")))
        page.update()
    

    def procesar_pago(e):
        if carrito:
            carrito.clear()
            page.open(ft.SnackBar(
                content=ft.Row([
                    ft.Icon(name=ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN),
                    ft.Text("Se ha procesado el pago correctamente", color=ft.Colors.GREEN)
                ]),
                bgcolor=ft.Colors.WHITE
            ))
        else:
            page.open(control=ft.SnackBar(
                content=ft.Text(value="Tu carrito está vacío!", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.RED
            ))
        page.update()

    
    filtro_categoria.on_change = lambda e: mostrar_productos()
    barra_busqueda.on_change = lambda e: mostrar_productos()

    page.add(
        ft.Column(controls=[
            barra_busqueda,
            filtro_categoria,
            lista_productos,
            ft.ElevatedButton(text="Pagar carrito", icon=ft.Icons.PAYMENT, on_click=procesar_pago)
        ])
    )

    mostrar_productos()
  
ft.app(target=main)