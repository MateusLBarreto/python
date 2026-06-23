# Questao 30
n = int(input("Digite um valor: "))
nDiv = n
if n <= 1:
    print("Valor invalido.")
else:
    while nDiv > 1:
        nDiv -= 1
        if n % nDiv == 0:
            nPrimo = False
            nDiv = 1
        else:
            nPrimo = True
            nDiv -= 1
    print (nPrimo)