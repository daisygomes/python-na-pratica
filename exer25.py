#Uma programa que analisa se o nome da cidade começa com santo ou não

cidade = str(input("Digite o nome da sua cidade: ")).strip()
print(cidade[:5].upper() == 'SANTO')
