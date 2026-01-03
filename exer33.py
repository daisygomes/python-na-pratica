# Ano comum e ano bissexto
from datetime import date
ano = int(input("Digite um ano para ver se é comum ou bissexto: "))
if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
    ano = date.today().year
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano não é bissexto".format(ano))