print("Nota 1:")
nota1 = float(input())
print("Nota 2:")
nota2 = float(input())
print("Nota 3:")
nota3 = float(input())
media = (nota1+nota2+nota3)/3
print("Média: "+str(media))
if media>=7:
    print("Aprovado!")
elif media>=5:
    print("Recuperação!")
else:
    print("Reprovado!")
