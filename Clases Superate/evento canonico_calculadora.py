def caclular(operador, numero1, numero2): 
    if operador == 1: 
        resultado = numero1 + numero2
    elif operador == 2: 
        resultado = numero1 - numero2
    elif operador == 3: 
        resultado = numero1 * numero2
    elif operador == 4: 
        resultado = numero1 / numero2
    elif operador == 5: 
        resultado = numero1 ** numero2

    return resultado

try:
    numero1 = input('dime el primer numero ')
    numero2= input('dime el segundo numero ')
    operacion= input("""Dime que operacion deseas realizar
                    1. suma 
                    2. resta
                    3. multiplicacion
                    4. division
                    5. exponenciacion
                     """)
    if numero2 == ''   or numero1 == '' or operacion == '': 
        raise ValueError
except ValueError:
     print(("Lo siento no puedes ingresar un campo vacio"))
except: 
    print("disculpa no nos es posible calcular tus valores")
else: 
    try:
        print(caclular(int(operacion),float(numero1), float(numero2)))
    except: 
        print('has ingresado valores incorrectos, no se pueden calcular')