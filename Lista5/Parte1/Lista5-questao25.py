# Questao 25
valor = input("Digite um valor: ")
casa = len(valor)
valor = int(valor)
contCasa = 0
while contCasa < casa:
    digito = valor // 10 ** contCasa % 10
    contCasa += 1
    print(end=f"{digito}")
print()