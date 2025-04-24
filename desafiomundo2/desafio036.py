print('---EMPRÉSTIMO HIPOTECÁRIO----\n')
# Pegando valores base para o cálculo
nome = str(input('\33[1mNome do beneficiário: '))
casa = float(input('Valor da hipoteca requerida: '))
salario = float(input('Salário do beneficiário: '))
tempodepagar = int(input('Tempo de pagamento (em anos): '))
# Cálculo para saber quantas parcelas ele(a) pagará
prestacao = casa / (tempodepagar * 12)
# Caso maior que 30% do salário, ele negará. Senão, mostrará os dados
if prestacao > (salario * 30 / 100):
    print('\33[31;1mEMPRÉSTIMO NEGADO!!! O valor da sua parcela é equivalente mais de 30% do seu salário\33[m')
else:
    print('\33[mO senhor(a) {} pagará por {} anos o valor de {}R${:.2f}{} por mês, \33[32msem juros e anuidade\33[m'.format(nome, tempodepagar, '\33[32m', prestacao, '\33[m'))
