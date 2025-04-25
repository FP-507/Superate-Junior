"""Vamos a calcular el área de una figura"""

# Solicitar al usuario que elija una figura para calcular su área
figura = int(input("""De que figura quiere obtener su area: 
               1. Triangulo
               2. Rectangulo 
               3. Cuadrado
               4. Circulo
               """))

# Verificar qué figura eligió el usuario y calcular el área correspondiente
if figura == 1: 
    # Cálculo del área de un triángulo
    base = int(input("Cual es la base de tu triangulo: "))
    altura = int(input("Cual es la altura de tu triangulo: "))
    area = (base * altura) / 2  # Fórmula del área del triángulo
elif figura == 2: 
    # Cálculo del área de un rectángulo
    base = int(input("Cual es la base de tu rectangulo: "))
    altura = int(input("Cual es la altura de tu rectangulo: "))
    area = base * altura  # Fórmula del área del rectángulo
elif figura == 3: 
    # Cálculo del área de un cuadrado
    lado = int(input("Cuánto mide uno de los lados de tu cuadrado: "))
    area = lado ** 2  # Fórmula del área del cuadrado
elif figura == 4: 
    # Cálculo del área de un círculo
    radio = int(input("Cuál es el radio de tu círculo: "))
    area = radio ** 2 * 3.14  # Fórmula del área del círculo (usando π ≈ 3.14)
else: 
    # Mensaje de error si el usuario elige una opción incorrecta
    print("Has elegido una opción incorrecta")

# Mostrar el resultado del área calculada
print(f"El área es de {area}")