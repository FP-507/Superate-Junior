
this_year = 2025

try:
    birth_year = int(input("En que año naciste"))
    if birth_year == '': 
        raise ValueError
except ValueError:
     print(("Lo siento no puedes ingresar un campo vacio"))
except: 
    print("disculpa no nos es posible calcular tu edad")
else: 
        calculo_edad = this_year - birth_year
       
        print(f'tu edad es {calculo_edad}')
finally: 
     print('Muchas gracias por participar')



    

