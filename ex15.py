frase = input("Digite uma frase: ")
letras = [*frase]
vogais = ["a","e","i","o","u"]
quant_vogais = 0
for letra in letras:
    if letra in vogais:
        quant_vogais+=1
print("Quantidade de vogais em sua frase:",quant_vogais)
