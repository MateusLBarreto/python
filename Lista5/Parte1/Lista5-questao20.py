# Questao 20
valor = int(input("Digite um valor: "))
contadorValor = 1
contador = 1
while contador < valor:
    contador += 1
    contadorValor += 1 / contador
print(contadorValor)