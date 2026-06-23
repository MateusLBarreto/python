# Questao 21
n = int(input("Digite o número de notas: "))
contador = 0
vetorNotas = []
while contador < n:
    nota = int(input("Digite a nota:"))
    vetorNotas.append(nota)
    # .append pode ser usado para incluir uma variavel em um vetor
    contador += 1
print (max(vetorNotas))