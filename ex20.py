estudantes = ["Bob","Bob2","Bob3","Bob4","Bob5"]
print("Lista de estudantes, do primeiro ao último a chegar:",estudantes)
contrario = []
for i in range(1,len(estudantes)+1):
    contrario.append(estudantes[-i])
print("Lista de estudantes, do último ao primeiro a chegar:",contrario)
