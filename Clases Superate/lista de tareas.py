import flet as ft

def main(page: ft.Page):
    page.title = "Tablero de notas"

    #los temas se usa para elegir un tema de la computadora (dark/light) ya que let se guia por este para el uso de alunos colores como puede ser el color de las letras
    page.theme_mode = 'Light'
    page.padding = 20
    page.bgcolor = ft.colors.BLUE_GREY_800
    
    # Funcion para crear nuevas notas
    def add_note(e): 
        new_note= create_note("Nueva Tarea")
        grid.controls.append(new_note)
        page.update()

    # Funcion para eliminar notas
    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    #grid.controls.... te permite acceder al grid como si fuera una lista y realizar distintas funciones


    def create_note(text): 

        #un TextField en resumen son inputs o cuadros de texto que el usuario puede modificar
        note_content = ft.TextField(value=text, multiline= True, bgcolor= ft.colors.BLUE_GREY_50)
        note_btns = ft.Row(controls=[
                #flet pemite usar iconos como botones y trae algunos iconos por defecto
                 #se usa un lambda para llamar a la funcion de borrar notas
                 ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: delete_note(note)), 
                 ft.Checkbox(on_change=None), 
                 ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_UP, on_click=lambda _: change_priority(int(1), note)),
                 ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN, on_click=lambda _: change_priority(int(-1), note)),])
    
        #se crea un contenedor que en este caso es el postit
        note = ft.Container(
            #se crea en columna para tener la distrubucion deseada
            content=ft.Column(
                [note_content, 
                 note_btns
                 ]
                ),
                #caracteristicas del contenedor casi identicas a como se colocan e CSS
                width= 200,
                height= 300,
                bgcolor= ft.colors.BLUE_GREY_100,
                border_radius= 7,
                padding= 4,
            )

        #usamos return para decir el resultado de la funcion
        return note
    
    def change_priority(delta,note): 
        posicion_inical = int(grid.controls.index(note))
        posicion_final = posicion_inical - delta
        item = grid.controls.pop(posicion_inical)
        grid.controls.insert(posicion_final,item)
        page.update()


    #un grid es como si usaramos flex box pero mucho mas simple de usar
    grid = ft.GridView(
        expand= True,
        max_extent= 220,
        child_aspect_ratio=1, #hace que el alto y anco sea iguales

        #los espaciados a los lados 
        spacing= 10,
        run_spacing= 100,
    )

    notes = [
        'Comprar Leche',
        'Reunion de Expo 3pm',
        'Estudiar Ingles'
    ]

    for note in notes: 
        grid.controls.append(create_note(note))

    #usamos page.add para mostrar todo en la aplicacion
    page.add(ft.Row #esta fila sera lo que nos funcione como titulo o zona superior de la aplicacion
             ([
                 ft.Text('Mis notas Adhesivas', size= 24, weight="bold", color= ft.colors.WHITE ),
                 ft.IconButton(ft.icons.ADD, on_click= add_note, icon_color=ft.colors.WHITE)
             ], alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
             ,grid)
    

ft.app(target=main)