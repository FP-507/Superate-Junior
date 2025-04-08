frase = input("Dime una frase: ")
letra_buscada= input("Dime una letra de tu frase: ")


contador_letra_buscada = 0

for letra in frase:
    if letra.lower == letra_buscada:
        contador_letra_buscada+=1

print(f"tu letra se repite {contador_letra_buscada} veces en tu frase")