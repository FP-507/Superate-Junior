import csv

class usuario: 
    def __init__(self, nombre, saldo=0):

        with open('cuenta_yappy.csv', 'a') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                self.__usuario = fila['usuario']
                self.__saldo = fila['saldo']
    
    def recibir(self, cant_recibida): 
        with open('cuenta_yappy.csv', 'a') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila['usuario'] == self.__usuario:
                    self.__saldo += cant_recibida
                    fila['saldo'] = self.__saldo
        
    
    def enviar(self, cant_enviada):
         with open('cuenta_yappy.csv', 'a') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila['usuario'] == self.__usuario: 
                    if fila['saldo'] > 0:
                        fila['saldo'] -= cant_enviada
    
    def cuenta(self): 
        with open('cuenta_yappy.csv', 'r') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila['usuario'] == self.__usuario: 
                    print(f'Usuario: {self.__usuario} \n Dinero: {self.__saldo}')

        

