cadastrados = []
while True:
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")
    n = input()
    if n=="1":
        print("Cadastre um usuário:")
        usuario = input()
        cadastrados.insert(-1,usuario)
    elif n=="2":
        print("Usuários cadastrados:",cadastrados)
    elif n=="3":
        break
