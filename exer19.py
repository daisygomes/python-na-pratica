# Seno, Cosseno e tangente de um ângulo
import math
angulo = float(input("Digite valor de um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {}º, tem seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}" .format(angulo, seno, cosseno, tangente))