# Programa para calcular velocidade e cobrar a multa

velocidade = float(input(" Informe a velocidade do carro: "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print("MULTADO! Você ultrapassou o limite permitido que é 80Km/h.")
    print("Você deve pagar uma multa de R${}." .format(multa))
print("Tenha um bom dia! Dirija com segurança.")
