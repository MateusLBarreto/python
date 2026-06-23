valor = int(input("Digite um valor: "))
nPrimo = []
for j in range(2, valor + 1):
    jDiv = j
    jDiv -= 1
    while jDiv >= 1:
        jPrimo = []
        if j % jDiv == 0:
            jPrimo.append(False)
            jDiv = 1
        else:
            jPrimo.append(True)
            jDiv -= 1
        if all in jPrimo == True:
            nPrimo.append(j)
print(nPrimo)