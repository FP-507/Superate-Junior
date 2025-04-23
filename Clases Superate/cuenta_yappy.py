# Definición de la clase 'usuario' que representa a un usuario con un nombre y una cantidad de dinero.
class usuario: 
    # Método constructor que inicializa el nombre y el dinero del usuario.
    def __init__(self, nombre, dinero):
        self.__nombre = nombre  # Atributo privado que almacena el nombre del usuario.
        self.__dinero = dinero  # Atributo privado que almacena la cantidad de dinero del usuario.
    
    # Método para recibir dinero. Incrementa el saldo del usuario.
    def recibir(self, cant_recibida): 
        self.__dinero += cant_recibida  # Suma la cantidad recibida al saldo actual.
    
    # Método para enviar dinero. Disminuye el saldo del usuario si tiene suficiente dinero.
    def enviar(self, cant_enviada): 
        if self.__dinero > 0:  # Verifica que el saldo sea mayor a 0 antes de descontar.
            self.__dinero -= cant_enviada  # Resta la cantidad enviada del saldo actual.
    
    # Método para visualizar los datos del usuario (nombre y saldo).
    def ver(self): 
        print(f'Usuario: {self.__nombre} \n Dinero: {self.__dinero}')  # Imprime el nombre y el saldo del usuario.

# Creación de una instancia de la clase 'usuario' con el nombre 'Fidel' y un saldo inicial de 5000.
user_1 = usuario('Fidel', 5000)

# Muestra los datos iniciales del usuario.
print(user_1.ver())

# El usuario recibe 300$.
user_1.recibir(300)

# Muestra los datos del usuario después de recibir dinero.
print(user_1.ver())

# El usuario envía 200$
user_1.enviar(200)

# Muestra los datos del usuario después de enviar dinero.
print(user_1.ver())