class Meeseeks_Box:
    def __init__(self,nombre, fuerza, rapidez, inteligencia, agilidad, mision):
        self.nombre = nombre
        self.fuerza = fuerza
        self.rapidez = rapidez
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.mision = mision
    
    def presentarse(self): 
        print(f"""Hola!! Soy {self.nombre} MIRAMEEE!!
Mi mision es {self.mision}""")
        
    def pelear(enemigo, self): 
        puntaje = 0
        puntaje_enemigo = 0
        if self.fuerza> enemigo.fuerza: 
            puntaje+=1
        else: 
            puntaje_enemigo += 1
        
        if self.rapidez> enemigo.rapidez: 
            puntaje+=1
        else: 
            puntaje_enemigo += 1

        if self.inteligencia> enemigo.inteligencia: 
            puntaje+=1
        else: 
            puntaje_enemigo += 1

        if self.agilidad> enemigo.agilidad: 
            puntaje+=1
        else: 
            puntaje_enemigo += 1

        if puntaje>puntaje_enemigo: 
            print(f'{self.nombre} Gana')
        elif puntaje==puntaje_enemigo:
            print('Hay un empate')
        else: 
            print(f'{enemigo} Gana')
        
mr_Meeseeks1 = Meeseeks_Box("Sr.Azul", 30,40,20,35, "Aprobar el Toeic")
mr_Meeseeks1.presentarse()

mr_Meeseeks2 = Meeseeks_Box("Chocolate", 50, 50000, 70, 1500, "ganar una carrera de relevo")
mr_Meeseeks2.presentarse()

mr_Meeseeks1.pelear(mr_Meeseeks2)