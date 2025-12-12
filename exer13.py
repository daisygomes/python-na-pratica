#Leia o preço do produto com desconto
produto = int(input("Digite o preço do produto :"))
desconto = produto - (produto * 0.05)
print("O produto é {} R$, mas com desconto de 5% passa a ser {} R$." .format(produto, desconto))