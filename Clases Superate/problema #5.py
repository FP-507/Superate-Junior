""" Escribe un programa y regrese el reverso de esa palabra, ademas qeu guarde cadda letra en una lista y se retorne al usuario"""

def Reverso(palabra): 
    palabra_reverso = reversed(palabra)
    list_palabra = [palabra]

    print(palabra_reverso)
    print(list_palabra)

Reverso("ojo")