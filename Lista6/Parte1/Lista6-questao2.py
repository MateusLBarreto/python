# Questao 2
rep = int(input())
lista = []
for _ in range(0, rep):
    valor = int(input())
    lista.append(valor)
print(min(lista), max(lista))