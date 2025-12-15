#Leitura de um número real qualquer, com a sua porção inteira
import math
numero = float(input("Digite um número real: "))
print("O número {}, tem a sua parte inteira {}." .format(numero, math.floor(numero)))