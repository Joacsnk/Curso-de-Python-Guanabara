numero = int(input('\33[34mEscreva um número de 0 até 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
# Preciso de mais conhecimento matemático, eu não sabia dessa
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}\33[m'.format(m))
