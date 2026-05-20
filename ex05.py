print("Qual o seu nome de usuário?")
nome = input()
print("Qual é a sua senha?")
senha = input()
if nome=="admin" and senha=="1234":
    print("Login realizado com sucesso")
else:
    print("Credenciais inválidas")
