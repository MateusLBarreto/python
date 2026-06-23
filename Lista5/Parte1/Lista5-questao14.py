# Questao 14
base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
contador = 1
poten = 1
while expoente >= contador:
    poten = poten * base
    contador += 1
print (poten)