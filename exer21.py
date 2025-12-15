# Sorteio 2
import random
aluno1 = input("Digite o nome: ")
aluno2 = input("Digite o nome: ")
aluno3 = input("Digite o nome: ")
aluno4 = input("Digite o nome: ")
apresentacao = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(apresentacao)
print("A ordem de apresentação será {}" .format(apresentacao))