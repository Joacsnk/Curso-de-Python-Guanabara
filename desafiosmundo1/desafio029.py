velocidade = float(input('Velocidade: '))
if velocidade > 80:
    # Se ele passar de 80, ele calcula
    print('\33[1;30;41mLimite de velocidade atingido\33[m \n\33[1;30;41mVocê foi multado\33[m')
    multa = (velocidade - 80)* 7.00
    print('\33[1;30;41mO valor da multa é de R${:.2f}\33[m'.format(multa))
else:
    print('\33[1;30;42mVeículo no limite de velocidade :)\33[m')