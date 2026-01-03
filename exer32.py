# Programa que calcula o preço da viagem de acordo com a distância

distancia = float(input("Qual é a distância da sua viagem? "))


if distancia <= 200:
    cobranca = distancia * 0.50
    print("Você está preste a começar uma viagem de {} Km" .format(distancia))
    print("E o preço da sua passagem será de R${}." .format(cobranca))
else:
    cobranca2 = distancia * 0.45
    print("Você está preste a começar uma viagem de {} Km".format(distancia))
    print("E o preço da sua passagem será de R${}.".format(cobranca2))