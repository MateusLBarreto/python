# Questao 31
cont = 0
vetorNotas = []
while cont < 10:
    n = int(input("Digite uma nota: "))
    if 0 <= n <= 10:
        vetorNotas.append(n)
    else:
        print("Valor invalido.")
    cont += 1
media= sum(vetorNotas) / 10
print("A media dessas notas é igual a: ",media)
if media >= 7:
    print("Aluno aprovado.")
elif 5 >= media > 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")