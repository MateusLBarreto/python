# Questao 27
contValor = 0
Npositivo = 0
Nnegativo = 0
Nzero = 0
while contValor < 10:
    valor = int(input("Digite um valor: "))
    if valor > 0:
        Npositivo += 1
    elif valor < 0:
        Nnegativo += 1
    else:
        Nzero += 1
    contValor += 1
print(f"Nessa lista de valores, {Npositivo} valores sao positivos, {Nnegativo} valores sao negativos e {Nzero} valores sao iguais a zero.")