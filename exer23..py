#leitura de nome completo, contagem de quantidades de letras ...

nome_completo = str(input("Digite o seu nome completo :")).strip()
dividido = nome_completo.split()
print("Seu nome em maiúscula é", nome_completo.upper())
print("Seu nome em minúscula é", nome_completo.lower())
print("O seu nome ao todo tem {} letras" .format(len(nome_completo) - nome_completo.count(' ')))
print("Seu primeiro nome é", dividido[0], "e ele tem", len(dividido[0]), "letras")
