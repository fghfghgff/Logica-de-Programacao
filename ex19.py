while True:
    porta = input("Qual porta deseja liberar? ")
    if porta=="80" or porta=="443":
        print("Porta liberada")
        break
    else:
        print("Porta bloqueada, tente outra")
