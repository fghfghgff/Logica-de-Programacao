octeto = int(input("Digite o primeiro octeto de um endereço IP: "))
if octeto>=1 and octeto<=126:
    print("Classe A")
elif octeto>=128 and octeto <=191:
    print("Classe B")
elif octeto >= 192 and octeto<= 223:
    print("Classe C")
else:
    print("Valor inválido")
