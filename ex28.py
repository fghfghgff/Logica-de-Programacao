notas = {}
aprovados = []
for i in range(5):
    print("Nome:")
    nome = input()
    print("Nota:")
    nota = int(input())
    notas[nome] = nota
    if nota >=7:
        aprovados.insert(-1,nome)
print("Aprovados:",aprovados)
