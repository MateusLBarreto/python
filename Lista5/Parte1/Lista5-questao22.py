# Questao 22
n = int(input("Digite o número de notas: "))
contador = 0
vetorNotas = []
while contador < n:
    nota = int(input("Digite a nota:"))
    vetorNotas.append(nota)
    contador += 1
print (min(vetorNotas))