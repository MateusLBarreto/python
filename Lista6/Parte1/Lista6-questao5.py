# Questao 5
rep = int(input())
lista = []
for i in range(0, rep):
    valor = int(input())
    lista.insert(-i, valor)
print(lista)