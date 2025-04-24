from random import choice
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('\nO aluno escolhido para apagar o quadro é \33[32m{}\33[m'.format(choice(alunos)))
# Usando uma biblioteca para randomizar