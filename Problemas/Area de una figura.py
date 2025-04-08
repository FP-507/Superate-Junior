"""Vamos a cacular el area de una figura"""

figura = int(input("""De que figura quiere obtener su area: 
               1. Triangulo
               2. Rectangulo 
               3. Cuadrado
               4. Circulo
               """))

if figura==1: 
    base= int(input("Cual es la base de tu triangulo: "))
    altura= int(input("Cual es la altura de tu triangulo: "))
    area = (base*altura)/2
elif figura == 2: 
    base= int(input("Cual es la base de tu rectaangulo: "))
    altura= int(input("Cual es la altura de tu rectangulo: "))
    area= base*altura
elif figura == 3: 
    lado = int(input("cuanto mide uno de los lados de tu cuadrado: "))
    area = lado**2
elif figura == 4: 
    radio = int(input("cual es el radio de tu circulo: "))
    area = radio**2 * 3.14
else: 
    print("Has elegido una opcion incorrecta")

print(f"El area es de {area}")