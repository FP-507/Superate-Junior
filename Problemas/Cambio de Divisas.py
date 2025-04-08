#creamos un diccionario con las divisas : su valor en dolares
divisas = {"Dolar":1, "Yen":0.0067, "Euro": 1.09,"Soles":0.28,"Pesos Mexicanos": 0.5}


print("""Aqui cambiamos tus divisas a balboas, que divisa quieres cambiar
      1. Dolares
      2. Yenes
      3. Euros
      4. Soles
      5.Pesos Mexicanos
      Elija uno por favor""")

eleccion = input()

print("Cuanto dinero quieres cambiar")

tu_dinero = int(input())

cambio = tu_dinero*divisas[eleccion]

print(f"Okey, aqui tiene su dinero, tiene {cambio} Balboas")