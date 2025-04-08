ingreidentes_vegetarianos = ["tofu", "pimiento"]
ingreidentes_carnivoros = ["peperoni", "jamon", "salmon"]

print("""Bienvenido a la Pizzeria Veganapoli
Quiere menu Vegetariano? si o no""")
eleccion = input()
ingrediente = None

while not(ingrediente in ingreidentes_carnivoros or ingrediente in ingreidentes_vegetarianos):
    if eleccion == "si":
        print(f"Ha elegido nuestro menu vegetariano este menu contiene {ingreidentes_vegetarianos} elija uno, ademas de lo que elijas llevara Salsa de Tomate y queso Mozarella ")
        ingrediente = input()

    elif eleccion == "no":
        print(f"Ha elegido nuestro menu no vegetariano este menu contiene {ingreidentes_carnivoros} elija uno, ademas de lo que elijas llevara Salsa de Tomate y queso Mozarella ")
        ingrediente = input()

    if not(ingrediente in ingreidentes_carnivoros or ingrediente in ingreidentes_vegetarianos):
        print("elija una opcion correcta")

print(f"Okey su pizza tendra Queso Mozarella, Salsa de Tomate y {ingrediente}")



