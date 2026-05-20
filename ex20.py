vendas = [10,2,150,89,4]
print("Maior venda:",max(vendas))
print("Menor venda:",min(vendas))
total = 0
for i in vendas:
    total+=i
print("Total vendido:",total)
print("Média:",total/len(vendas))
