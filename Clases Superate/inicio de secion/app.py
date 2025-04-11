import csv 

def Autenticar(user,password): 

    with open('Clases Superate\inicio de secion\BaseDeDatos.csv', 'r') as archivo: 
        lector = csv.DictReader(archivo)
        
        for fila in lector:

            if fila["username"] == user and fila["password"] == password:

                return True
        
        return False


usuario = input('Cual es tu nombre de usuario: ')

contrasena = input('Cual es tu contraseña: ')

if Autenticar(usuario,contrasena):

    print("Bienvenido al programa")
else:

    print("Usuario o contrasena incorrectas")
      
