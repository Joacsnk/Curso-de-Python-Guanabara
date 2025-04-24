print('\33[34m---Comparador---')
# pegando dados...
n1 = int(input('Diga o primeiro valor: '))
n2 = int(input('Diga o segundo valor: '))
# comparando os valores
if n1 > n2:
    print(f'\33[33mO número {n1} é maior que {n2}\33[m')
elif n2 > n1:
    print(f'\33[36mO número {n2} é maior que {n1}\33[m')
else:
    print(f'\33[35mO número {n1} é igual ao número {n2}\33[m')
    