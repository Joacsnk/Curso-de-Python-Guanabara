salario = float(input('Qual é o seu salário?: '))
# Calculando porcentagem de acordo com o salario
if salario <= 1250:
    salario += salario * 15 / 100
else:
    salario += salario * 10 / 100
print('Seu salário atual é de \33[30;1;42mR${:.2f}\33[m'.format(salario))