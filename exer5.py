n1 = int(input('Digite um número :'))
n2 = int(input('Digite um outro número :'))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
e = n1**n2
r = n1 % n2
print("A soma é {}, a subtração é {}, a divisão é {} e a multiplicação é {}" .format(soma, sub, div, mult) )
print("A exponenciação é {}, e o resto da divisão é {}" .format(e , r))