mais_18 = homens = mulheres_menos_20 = 0
while True: #cadastro com while
    print('\n--------Cadastramento--------\n')
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo [F/M]: ')).lower()
        if sexo == 'f' or sexo == 'm':
            break
    while True:
        r = str(input('Deseja continuar? [S/N]: ')).lower()
        if r == 'n' or r == 's':
            break
    if idade > 18:
        mais_18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1
    if r == 'n':
        break
print(f'\n\nPessoas com mais de 18 cadastradas: {mais_18}\nHomens cadastrados: {homens}\nMulheres com menos de 20 anos cadastradas: {mulheres_menos_20}')
    