ano = int(input('DESCUBRA SE O ANO É BISSEXTO\nQual é o ano de consulta? '))
# Como é ano bissexto, vou dividir por quatro e ver o resto
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano \33[32mÉ BISSEXTO!!!\33[m')
else:
    print('o ano \33[31mNÃO É BISSEXTO :(:(:(:(\33[m')