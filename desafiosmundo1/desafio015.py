dias = int(input('Dias que o carro foi alugado: '))
km = float(input('Km rodados pelo carro: '))
print('Valor total: \33[31;1mR${:.2f}\33[m'.format((dias * 60) + (km * 0.15)))
# Cálculo de carro alugado, easy