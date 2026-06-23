# Questao 24
valor = input("Digite um valor: ")
casa = len(valor)
valor = int(valor)
contCasa = 0
vetorDigito = []
while contCasa < casa:
    digito = valor // 10 ** contCasa % 10
    vetorDigito.append(digito)
    contCasa += 1
print(sum(vetorDigito))