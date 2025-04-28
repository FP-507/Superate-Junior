import csv 
import os

class ConsultaBD: 
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena
        self.archivo = 'cuenta_yappy.csv' 

    def autenticar(self):
        with open(self.archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila['usuario'] == self.usuario and fila['contrasena'] == self.contrasena:
                    return True
        print("Usuario o contraseña incorrectos.")
        return False
    
    def registrar(self):
        campos = ['usuario', 'contrasena', 'saldo']

        base_datos_real = os.path.exists(self.archivo)

        if base_datos_real:
            with open(self.archivo, 'r') as archivo:    
                lector = csv.DictReader(archivo)
                for fila in lector:
                    if fila['usuario'] == self.usuario:
                        print("El usuario ya existe.")
                        return
            
        with open(self.archivo, 'a', newline='') as archivo:
             escritor = csv.DictWriter(archivo, fieldnames=campos)

             if not base_datos_real:
                    escritor.writeheader()
             escritor.writerow({'usuario': self.usuario, 'contrasena': self.contrasena, 'saldo': 0})
        print("Usuario registrado exitosamente.")