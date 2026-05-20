for i in range(3):
    print("Usuário:")
    usuario = input()
    print("Senha:")
    senha = input()
    if usuario=="admin" and senha=="1234":
        print("Login realizado com sucesso!")
        break
    else:
        print("Login incorreto.")
else:
    print("Conta bloqueada.")
