valor = float(input("Qual o valor do livro? "))
if valor>80:
    desconto = valor*0.1
    final = valor-desconto
    print("Desconto: ",desconto)
    print("Valor final: ",final)
else:
    print("Valor final: ",valor)
