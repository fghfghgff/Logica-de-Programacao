alice = 0
bob = 0
while True:
    print("Vote 1 para Alice, 2 para Bob, ou digite 0 para sair.")
    voto = input()
    if voto=="1":
        alice+=1
    elif voto=="2":
        bob+=1
    elif voto=="0":
        break
print("Votos da Alice:",alice)
print("Votos do Bob:",bob)
