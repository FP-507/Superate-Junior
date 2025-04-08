movimiento_rober = ["O","N","N","N","O", "S", "E", "E", "E"]
x=0
y=0

for mov in movimiento_rober:   
    if mov == "O": 
        x+=1 
    elif mov == "E":
        x-=1
    elif mov == "N":
        y+=1 
    elif mov == "S":
        y-=1

print(f"La posicion del rober marciano es de y:{y} y x:{x}")  