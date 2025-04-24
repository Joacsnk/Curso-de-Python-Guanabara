# Ultilizando o randint para fazer o pc escolher 
from random import randint
numero = int(input('Tente acertar o número '))
numeropc = randint(0, 5)
# Comparando os números 
if numero == numeropc:
    print('\33[32mPARABENS, VOCÊ ACERTOU!!!!\33[m')
else:
    print('\33[31mVocê errou... :(\33[m')

