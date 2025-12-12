# Calculo de alugel de carro
quantidade = float(input("Qual a quantidade de Km percorridos ?"))
dia = float(input("Qual a quantidade do dia alugado ?"))
preco = 60 * dia
rodada = 0.15 * quantidade
total = preco + rodada

print("O preço a ser pago é de {} R$." .format(total))