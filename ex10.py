cadastrados = ["Bob","Bob2"]
print("Insira um nome.")
nome = input()
if nome in cadastrados:
    print("Esse nome já está cadastrado!")
else:
    print("Esse nome não está cadastrado.")
