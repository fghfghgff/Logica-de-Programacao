palavra = input("Digite uma palavra: ")
letras = [*palavra]
contrario = ""
for i in range(1,len(letras)+1):
    contrario=contrario+letras[-i]
if contrario==palavra:
    print("Sua palavra é um palíndromo!")
else:
    print("Sua palavra não é um palíndromo...")
