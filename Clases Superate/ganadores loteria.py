ganadores = []
for i in range(5):
    print("di un numero ganador de la loteria")
    ganadores.append(int(input()))
    
ganadores = sorted(ganadores)

print(f"Okey, los ganadores de la loteria entonces son {ganadores}")