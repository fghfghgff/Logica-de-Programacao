print("Insira o nome do produto.")
nome = input()
print("Qual a quantidade atual?")
atual = int(input())
print("Qual a quantidade vendida?")
vendida = int(input())
print("Estoque restante:",atual-vendida)
if atual-vendida<0:
    print("Estoque negativo!")
