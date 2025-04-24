# Ultilizando o randint para fazer o pc escolher 
from random import randint
tentativas = 0
numeropc = randint(0, 10)
while True:
    numero = int(input('Tente acertar o número '))
    if numero == numeropc:
        print('\33[32mPARABENS, VOCÊ ACERTOU!!!!\33[m')
        break
    else:
        print('\33[31mVocê errou... :(, tente novamente\n\33[m')
        tentativas += 1 #Contando tentativas
        if numero < numeropc:
            print('O número é maior que {}'.format(numero))
        else:
            print('O número é menor que {}'.format(numero))
print("\nVocê fez {} tentativas antes de conseguir!!".format(tentativas))

