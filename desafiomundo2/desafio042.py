l1 = int(input('Diga a linha 1: '))
l2 = int(input('Diga a linha 2: '))
l3 = int(input('Diga a linha 3: '))
# Conferindo se é válido 
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    if l1 == l2 and l2 == l3:
        print('\nTriângulo válido. Tipo: \33[32mEquilátero\33[m')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('\nTriângulo válido. Tipo: \33[32mIsóceles\33[m')
    elif l1 != l2 and l2 != l3:
        print('\nTriângulo válido. Tipo: \33[32mEscaleno\33[m')
else:
    print('\n\33[31mNão é um triângulo válido\33[m')