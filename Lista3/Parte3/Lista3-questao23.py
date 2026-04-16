# Questao 23
from Valores import n1, n2
D = True
print(D and n2 or n1) # Retorna 10, porque True and 10 = 10 e 10 or 4 = 10
D = False
print(D and n2 or n1) # Retorna 4, ja que False and 10 = False e False or 4 = 4