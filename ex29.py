vendas = [
 [120, 300, 250],
 [400, 150, 600]
]
total = 0
totais = []
maior = 0
for i in vendas:
    totallinha = 0
    for j in i:
        total+=j
        totallinha+=j
        if maior<j:
            maior=j
    totais.append(totallinha)
print("Total:",total)
print("Total por linha:",totais)
print("Maior venda:",maior)
