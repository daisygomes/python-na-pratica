# Leitura de número de 0 a 9999 e contando unidade, dezena, centena e milhares

numero = int(input("Informe um número: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analisando o númro {}" .format(numero))
print("Unidade: {}" .format(u))
print("Dezena: {}" .format(d))
print("Centena: {}" .format(c))
print("Milhar: {}" .format(m))