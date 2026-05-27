itens = []
while True:
    item = input("Digite o nome de um item de supermercado, ou digite 'sair' para encerrar: ")
    if item=="sair":
        break
    else:
        itens.append(item)
print("Lista de itens:",itens)
