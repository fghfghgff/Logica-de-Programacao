nomes = []
emails = []
def cadastrar_nome(nome):
    nomes.insert(-1,nome)
def cadastrar_email(email):
    emails.insert(-1,email)
def validar_idade(idade):
    if idade>=18:
        print("Cadastrado com sucesso!")
    else:
        print("Idade  mínima: 18.")
print("Qual seu nome?")
cadastrar_nome(input())
print("Qual seu email?")
cadastrar_email(input())
print("Qual sua idade?")
validar_idade(int(input()))
