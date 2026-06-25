# Questao 4
rep = int(input())
lista = []
lista_maior = []
for _ in range(0, rep):
    valor = int(input())
    lista.append(valor)
media = sum(lista) / rep
for item in lista:
    if item > media:
        lista_maior.append(item)
print(len(lista_maior))