# Questao 28
contValor = 1
while 1 <= contValor < 30:
    if contValor % 3 == 0:
        print ("Fizz")
    elif contValor % 5 == 0:
        print ("Buzz")
    else:
        print(contValor)
    if contValor % 15 == 0:
        print ("FizzBuzz")
    contValor += 1