# Questao 17
a = int(input("Digite um valor: "))
b = int(input("Digite um valor maior que o anterior: "))
if a < b:
    while a <= b:
        print(a)
        a += 1
else:
    print("Valores invalidos.")