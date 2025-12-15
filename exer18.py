import math
c_oposto = float(input("Digite o cateto oposto: "))
c_adjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = math.sqrt((c_oposto**2) + (c_adjacente**2))
print("O comprimento da hipotenusa é {}." .format(hipotenusa))

# OU
# hip = math.hypot(co, ca)
#
