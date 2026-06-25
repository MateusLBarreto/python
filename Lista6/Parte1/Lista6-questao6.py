# Questao 6
rep = int(input())
lista = [0] * rep
for item in range(0, rep):
    valor = int(input())
    if item == 0:
        lista[-1] = valor
    else:
        lista[item - 1] = valor
print(lista)