class Animal:
    def __init__(self, nombre='Desconocido', numero_patas=0, color='Desconocido', habitat='Desconocido', tipo_alimentacion='Desconocido', sonido='Desconocido'):
        self.__nombre = nombre
        self.__numero_patas = numero_patas
        self.__color = color
        self.__habitat = habitat
        self.__tipo_alimentacion = tipo_alimentacion
        self.__sonido = sonido

    def sonido(self):
        print(f"El sonido de {self.__nombre} es: {self.__sonido}")

    def caminar(self):
        print(f"{self.__nombre} camina con {self.__numero_patas} patas.")

    def comer(self):
        print(f"{self.__nombre} se alimenta de {self.__tipo_alimentacion}.")


class Serpiente(Animal):
    def __init__(self, veneno):
        # Llamar al constructor de la clase base para inicializar atributos heredados
        super().__init__(nombre='Leticia', numero_patas=0, tipo_alimentacion='estudiantes de Abel Bravo', sonido='ssssss')
        self.__veneno = veneno

    def morder(self):
        if self.__veneno:
            print(f"{self._Animal__nombre} muerde con veneno.")
        else:
            print(f"{self._Animal__nombre} muerde sin veneno.")

    def caminar(self):
        print(f"{self._Animal__nombre} se desliza en lugar de caminar.")


# Crear una instancia de la clase Serpiente
serpiente = Serpiente(True)

# Llamar a los métodos de la instancia
serpiente.caminar()
serpiente.sonido()
serpiente.morder()
serpiente.comer()