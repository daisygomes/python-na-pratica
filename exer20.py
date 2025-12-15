# Sorteio

import math
import random
aluno1 = input("Digite o nome: ")
aluno2 = input("Digite o nome: ")
aluno3 = input("Digite o nome: ")
aluno4 = input("Digite o nome: ")
alunos = (aluno1, aluno2, aluno3, aluno4)
sorteio = random.choice(alunos)
print("O sorteado foi {}" .format(sorteio))
