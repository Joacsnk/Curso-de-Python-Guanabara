l1 = int(input('Diga a linha 1: '))
l2 = int(input('Diga a linha 2: '))
l3 = int(input('Diga a linha 3: '))
# É só comparar se uma reta é menor que as outras duas juntas
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('É UM \033[32mTRIÂNGULO VÁLIDO!!!\033[m')
else:
    print('\33[31mNão é um triângulo válido\33[m')