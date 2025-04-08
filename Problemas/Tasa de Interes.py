def calcular_interes(capital,años):
    porcentaje_interes = 3.5/100

   
    capital_actual = capital *  ((1+porcentaje_interes)**años)

    print(f"""{años} años mas tarde....
Hola, actualmente tienes {capital_actual}
       """)

print("""Buen dia, nuestro banco posee un porcentaje de interes del 3.5%.
Cuanto dinero desea ingresar""")

capital_input = int(input())

print("""Por cuanto tiempo desea dejarlo en nuestro banco""")
años_input = int(input())

calcular_interes(capital=capital_input,años=años_input)