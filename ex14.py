cadastrados = []
for i in range(5):
    print("Cadastre um usuário.")
    usuario = input()
    cadastrados.insert(i,usuario)
print("Usuários cadastrados: ",cadastrados)
