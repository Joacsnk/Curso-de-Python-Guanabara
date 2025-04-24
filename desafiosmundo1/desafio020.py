from random import shuffle
aluno1 = input('aluno 1: ')
aluno2 = input('aluno 2: ')
aluno3 = input('aluno 3: ')
aluno4 = input('aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('\n A ordem de apresentação será: \33[30;1m\n{}\33[m'.format(alunos))
# Agora usando para embaralhar
