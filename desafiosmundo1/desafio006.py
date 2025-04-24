numero = int(input('Diga um número: '))
print('O dobro de \33[1;31m{}\33[m é \33[1;32m{}\33[m, o seu triplo é \33[32m{}\33[m e sua raiz quadrada é \33[32m{:.2f}\33[m'.format(numero, numero * 2, numero * 3, pow(numero, (1/2))))
# Formatação com raiz quadrada, só o basic