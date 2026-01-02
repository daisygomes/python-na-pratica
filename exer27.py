frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A apareceu {} vezes" .format(frase.count('A')))

print("A posição que A aparece pela primeira vez é {}" .format(frase.find("A") + 1))
print("A posição que A aparece pela ultima vez é {}" .format(frase.rfind('A') + 1))