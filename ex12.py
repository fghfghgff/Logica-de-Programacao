n = int(input("Digite um número inteiro positivo: "))
fatorial = 1
for i in range(n):
    fatorial*=(n-i)
print(f"{n}! = {fatorial}")
