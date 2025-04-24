from datetime import date
nome = str(input('\33[1;42mDiga seu nome:\33[m\33[32m ')) # estilo
nascimento = int(input('\33[1;42mDiga seu ano de nascimento:\33[0m\33[32m ')) # dado para cálculo
anoatual = date.today() # puxando ano atual
idade = anoatual.year - nascimento # tranformando em iidade para facilitar os cálculos
if idade < 18:
    # ano atual menos os anos até fazer 18
    print('{} se alistará em \33[4m{}\33[0;32m, pois ainda é jovem\33[m'.format(nome, (18 - idade) + anoatual.year ))
elif idade > 18:
    # ano atual menos o excedente de 18 & o excedente sozinho 
    print('{} deveria se alistar em \33[4m{}\33[0;32m, porém passou do prazo.\nVocê está com \33[4m{}\33[0;32m ano(s) de atraso\33[m'.format(nome, anoatual.year - (idade - 18), idade - 18))
else:
    print('{} deverá se alistar nesse ano de \33[4m{}\33[m!!!'.format(nome, anoatual.year))

