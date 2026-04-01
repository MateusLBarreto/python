# Questao 10
import math
x = float(input("Digite um valor positivo: "))
raiz = math.sqrt(x)
raizTeto = math.ceil(raiz)
raizChao = math.floor(raiz)
print (f"A raiz quadrada de {x} é: {raiz}\nO arredontamento dessa raiz para cima é: {raizTeto}\nO arredondamento dessa raiz para baixo é: {raizChao}")