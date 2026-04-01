# Questao 8
import math
tempo = float(input("Digite o tempo em horas: "))
tempoHoras = math.floor(tempo)
tempoMinutos = math.floor((tempo - tempoHoras) * 60)
print (f"O tempo : {tempoHoras} horas e {tempoMinutos} minutos.")