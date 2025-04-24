print("-----CAIXA ELETRÔNICO-----\n")
valor = int(input("Digite o valor para ser sacado: ")) #notas do maior ao menor com while
nota_50 = nota_20 = nota_10 = nota_1 = 0
while True:
    if (valor - 50) >= 0:
        nota_50 += 1
        valor -= 50
    else:
        break
while True:
    if (valor - 20) >= 0:
        nota_20 += 1
        valor -= 20
    else:
        break
while True:
    if (valor - 10) >= 0:
        nota_10 += 1
        valor -= 10
    else:
        break
while True:
    if (valor - 1) >= 0:
        nota_1 += 1
        valor -= 1
    else:
        break
print(f'Notas necessárias:')
if nota_50 > 0:
    print(f'Notas de 50: {nota_50}')
if nota_20 > 0:
    print(f'Notas de 20: {nota_20}')
if nota_10 > 0:
    print(f'Notas de 10: {nota_10}')
if nota_1 > 0:
    print(f'Notas de 1: {nota_1}')