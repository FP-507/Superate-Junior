def area_circulo(radio):
    #la formula para el area de un ciculo es A=r**2*pi 
    area = radio**2*3.14 
    print(f"el area de tu circulo es {area}")

def volumen_cilindro(radio,altura):
    #la formula para el volumen de un cilindro es Volumen = pi*r**2*h
    volumen= 3.14*radio**2*altura
    print(f"el volumen de tu cilindro es {volumen}")

area_circulo(5)

volumen_cilindro(6,3)