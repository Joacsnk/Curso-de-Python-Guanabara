numero = int(input('Digite um número: '))
c = 0 #contador de divisões
for i in range(1, numero + 1):
    if numero % i == 0: #verificando as divisões e salvando
        print('\033[31m{}'.format(i), end=' ')
        c += 1
    else:
        print('\033[33m{}'.format(i), end=' ')
print('\n\033[mO número {} tem {} divisores'.format(numero, c))
if c == 2: #verificando se é primo
    print('Por isso o número É PRIMO!')
else:
    print('Por isso o número NÃO É PRIMO!')