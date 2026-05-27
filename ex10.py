valor = float(input("Qual o valor atual da bolsa do estagiário? "))
if valor < 1000:
    aumento = valor*0.15
    print("Valor final:",valor+aumento)
else:
    aumento = valor*0.1
    print("Valor final:",valor+aumento)
