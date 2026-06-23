# Questao 3
rep = int(input())
lista = []
for _ in range(0, rep):
    valor = int(input())
    if valor % 2 == 0:
        lista.append(valor)
print(len(lista))