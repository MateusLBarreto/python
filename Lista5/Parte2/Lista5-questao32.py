# Questao 32
n = int(input("Digite um valor: "))
nDiv = n
while nDiv > 0:
    if n % nDiv == 0:
        print(end=f"{nDiv}, ")
    nDiv -= 1