# Programa que procura se a pessoa tem Silva no nome

nome = str(input("Digite o seu nome completo: ")).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))