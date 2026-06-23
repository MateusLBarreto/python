# Questao 29
NdeValores = int(input("Digite o numero de valores que serão digitados:"))
contValor = 1
somaPositiva = 0
somaNegativa = 0
while 1 <= contValor <= NdeValores:
    valor = int(input("Digite um valor: "))
    if valor > 0:
        somaPositiva += valor
    elif valor < 0:
        somaNegativa += valor
    contValor += 1
print ("A soma dos valores positivos é igual a:",somaPositiva)
print ("A soma dos valores negativos é igual a:",somaNegativa)
# vetorPositivo = []
# vetorNegativo = []
# while 1 <= contValor <= NdeValores:
#     valor = int(input("Digite um valor: "))
#     if valor > 0:
#         vetorPositivo.append(valor)
#     elif valor < 0:
#         vetorNegativo.append(valor)
#     contValor += 1
# print ("A soma dos valores positivos é igual a: ",sum(vetorPositivo))
# print ("A soma dos valores negativos é igual a: ",sum(vetorNegativo))