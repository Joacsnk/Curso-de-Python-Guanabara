numero = int(input('Digite um numero: '))
# Verificando se o resto da divisão é 0 ou 1
numero = numero % 2
if numero == 0:
    print('O número é \33[33mPAR\33[m')
else:
    print('O número é \33[34mÍMPAR\33[m')
