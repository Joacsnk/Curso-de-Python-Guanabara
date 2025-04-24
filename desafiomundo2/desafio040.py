print('\33[37m-----MÉDIA FINAL-----\33[m')
nota1 = float(input('Nota do semestre I: '))
nota2 = float(input('Nota do semestre II: '))
media = (nota1 + nota2) / 2 # média e comparação
if media < 5:
    print('\33[31;1mALUNO REPROVADO!!!\33[0m')
elif media >= 5 and media <= 6.9:
    print('\33[33;1mALUNO EM RECUPERAÇÃO!!!\33[0m')
else:
    print('\33[32;1mALUNO APROVADO!!!\33[0m')

