# Questao 19
NdeValores = int(input("Digite o numero de valores: "))
inicio = int(input("Digite um valor inicial: "))
razao = int(input("Digite o valor da razão: "))
NdeValoresInicial = 1
print(inicio)
while NdeValoresInicial < NdeValores:
    inicio += razao
    NdeValoresInicial += 1
    print(inicio)