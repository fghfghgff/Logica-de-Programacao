nums = []
pares = []
print("Insira 10 números:")
for i in range(10):
    n = int(input())
    nums.insert(i,n)
    if n%2==0:
        pares.insert(i,n)
print("Quantidade de pares:",len(pares))
