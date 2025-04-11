#creamos un nuevo documento, si elegimos un documento ya creado, borrara todo lo que contenga
file = open('Clases Superate\manejo de archivos\miArchivo.txt', "w")

#abrimos el documento y escribimos en este
file.write('Fidel y Joel son buenos amigos')
file.close()

#de esta forma revisamos si mi nombre esta en el archivo y si lo esta te dice 'usuario aceptado'
file = open('Clases Superate\manejo de archivos\miArchivo.txt', "r")
user = file.read()
file.close()

if 'Fidel' in user:
    print('Usuario correcto' )

#forma de abrir archivos profesional 

with open('Clases Superate\manejo de archivos\miArchivo.txt', "r") as file:
    user = file.read()
    if 'Fidel' in user:
        print('Usuario correcto')
    