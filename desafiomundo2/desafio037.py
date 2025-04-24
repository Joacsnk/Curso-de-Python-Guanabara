decimal = int(input('\33[4mDiga um número para a conversão: '))
# Escolha da conversão: 
anwser = int(input('\33[0m\33[1mEscolha sua conversão\nBinário (1)\nOctal(2)\nHexadecimal(3)\nDigite aqui: '))
if anwser == 1:
    conversao = bin(decimal)
    print('\n\33[0;33mO número {} convertido para binário é equivalente ao {}\33[m'.format(decimal, conversao))
elif anwser == 2:
    conversao = oct(decimal)
    print('\n\33[0;35mO número {} convertido para octal é equivalente ao {}\33[m'.format(decimal, conversao))
elif anwser == 3:
    conversao = hex(decimal)
    print('\n\33[0;34mO número {} convertido para hexadecimal é equivalente ao {}\33[m'.format(decimal, conversao))
else:
    print('\n\33[31;1mErro!!! Número inválido\33[m')