from random import randint
# interface kkk
print('\33[34m----------JO KEN PO----------\nDigite ''10'' para parar\n\33[m')
jogo = True #importante para o looping, para que fique jogando até parar
while jogo:
    jogada = int(input('\33[34mEscolha sua jogada: Pedra (1)  Papel(2)  Tesoura(3): '))
# randomizando a jogada 
    jogadapc = randint(1, 3)
# definindo as jogadas em str para facilitar na escrita (jogador)
    if jogada == 1:
        jogada01 = 'pedra'
    elif jogada == 2:
        jogada01 = 'papel'
    else:
        jogada01 = 'tesoura'
# definindo as jogadas em str para facilitar na escrita (máquina)
    if jogadapc == 1:
        jogadapc01 = 'pedra'
    elif jogadapc == 2:
        jogadapc01 = 'papel'
    else:
        jogadapc01 = 'tesoura'
# caso de eencerramento do jogo
    if jogada == 10:
        jogo = False
# caso de empate 
    elif jogada == jogadapc:
        print('\n\33[33mEMPATE!! Os dois jogadores escolheram {}\n\33[m'.format(jogada01))
# caso a máquina ganhe 
    elif (jogada == 1 and jogadapc == 2) or (jogada == 2 and jogadapc == 3) or (jogada == 3 and jogadapc == 1):
        print('\n\33[31mVocê perdeu!!\33[m Você escolheu \33[31m{}\33[m e a máquina escolheu \33[32m{}\n\33[m'.format(jogada01, jogadapc01))
# caso a máquina perca 
    elif (jogada == 1 and jogadapc == 3) or (jogada == 3 and jogadapc == 2) or (jogada == 2 and jogadapc == 1):
        print('\n\33[32mVocê ganhou!!\33[m Você jogou \33[32m{}\33[m e a máquina jogou \33[31m{}\n\33[m'.format(jogada01, jogadapc01))
# caso o número digitado seja errado
    else:
        print('\n\33[31;1mCOMANDO INVÁLIDO!!!\n\33[0m')
print('\33[34m\nFIM DO JOGO!!\33[m')
