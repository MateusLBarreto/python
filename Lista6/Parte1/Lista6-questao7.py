# Questao 7
rep = int(input())
lista = []
for item in range(0, rep):
    valor = int(input())
    if item == rep - 1:
        lista.insert(0, valor)
    else:
        lista.append(valor)
print(lista)