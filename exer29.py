#Jogo de advinha
import random
from time import sleep
usuario = int(input("Advinha um número de 0 à 5: "))
print("PROCESSANDO...")
sleep(3)
computador = [random.randint(0,5)]
print(computador)

if usuario == computador:
    print("Você venceu")
else:
    print("Você perdeu")