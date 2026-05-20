assentos = [["Livre" for i in range(3)] for i in range(3)]
print("Assentos:",assentos[0],assentos[1],assentos[2],sep="\n")
print("Escolha uma linha:")
linha = int(input())
print("Escolha uma coluna:")
coluna = int(input())
assentos[linha][coluna] = "Ocupado"
print("Assentos:",assentos[0],assentos[1],assentos[2],sep="\n")
