notas = []
print("Insira as notas de 10 alunos:")
for i in range(10):
    nota = int(input())
    notas.insert(i,nota)
print("Ordem crescente:",sorted(notas))
print("Ordem descrescente:",sorted(notas,reverse=True))
