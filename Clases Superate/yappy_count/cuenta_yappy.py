class Usuario:  # Clase Usuario para manejar la información del usuario
    """ Clase Yappy para manejar las operaciones de la cuenta """
    def __init__(self, usuario, saldo):  # Método Constructor
        self.__saldo = saldo
        self.usuario = usuario

    # Funciones get
    def get_saldo(self):  # Método para obtener el saldo
        return self.__saldo

    def get_usuario(self):  # Método para obtener el usuario
        return self.usuario

    # Funciones set
    def set_usuario(self, usuario):
        self.usuario = usuario

    # Métodos de clase
    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Se han depositado {cantidad}.")
        

    def enviar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han enviado {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Saldo insuficiente para enviar.")

    def estado(self):
        print(f"Usuario: {self.get_usuario()} tiene un saldo de: {self.get_saldo()}")

   
   
