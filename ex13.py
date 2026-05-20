while True:
    print("Insira uma senha.")
    senha = input()
    if len(senha) >= 8:
        print("Senha válida!")
        break
    else:
        print("Senha inválida!")
