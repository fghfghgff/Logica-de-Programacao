produtos = []
def cadastrar_produto():
    print("Qual produto deseja cadastrar?")
    produto = input()
    produtos.append(produto)
    print("Produto cadastrado.")

def listar_produtos():
    print("Produtos:",produtos)

def buscar_produto():
    print("Qual produto deseja buscar?")
    produto = input()
    if produto in produtos:
        print("Esse produto está cadastrado.")
    else:
        print("Esse produto não está cadastrado.")

def remover_produto():
    print("Qual produto deseja remover?")
    produto = input()
    produtos.remove(produto)
    print("Produto removido.")

def salvar():
    with open("produtos.txt","w", encoding="utf-8") as arq:
        arq.write(", ".join(produtos))
        print("Lista de produtos salva em arquivo.")

def ler():
    with open("produtos.txt","r", encoding="utf-8") as arq:
        print("Conteúdo do arquivo:",arq.read())

while True:
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Remover produto")
    print("5 - Salvar em arquivo")
    print("6 - Ler arquivo")
    print("0 - Sair")
    n=input()
    if n=="1":
        cadastrar_produto()
    elif n=="2":
        listar_produtos()
    elif n=="3":
        buscar_produto()
    elif n=="4":
        remover_produto()
    elif n=="5":
        salvar()
    elif n=="6":
        ler()
    elif n=="0":
        break
