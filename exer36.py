# ANALISANDO O TRIÂNGULO

print('-=' *15)
print("ANALISADOR DE TRIÂNGULOS")
print('-=' *15)

r1 = float(input("Primeiro segemento: "))
r2 = float(input("Segundo segemento: "))
r3 = float(input("Terceiro segemento: "))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")