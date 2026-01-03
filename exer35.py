# Programa que calcule o salário de um funcionario e aumento

salario = float(input("Digite o seu salário: "))
if salario > 1250:
    aumento = salario + (salario * 0.10)
    print("Quem ganhava R${}, passa a ganhar R${}".format(salario, aumento))
else:
    aumento2 = salario + (salario * 0.15)
    print("Quem ganhava R${}, passa a ganhar R${}".format(salario, aumento2))
