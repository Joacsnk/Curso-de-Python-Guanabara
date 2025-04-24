n1 = int(input('diga o primeiro número: ' ))
n2 = int(input('diga o segundo número: ' ))
n3 = int(input('diga o terceiro número: ' ))
# Coloquei em uma lista e usei funções para facilitar e diminuir o tamanho
numeros = [n1, n2, n3]
print('O \33[32mmaior\33[m número é o \33[32m{}\33[m e o \33[31mmenor\33[m número é \33[31m{}\33[m'.format(max(numeros), min(numeros)))