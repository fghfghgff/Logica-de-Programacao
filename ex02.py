tamanho = int(input("Qual o tamanho do arquivo em Megabytes? "))
velocidade = int(input("Qual a velocidade da internet em Megabits por segundo? "))
tamanho_bits = tamanho*8
tempo = tamanho_bits/velocidade
print(f"Tempo aproximado de download: {tempo} segundos.")
