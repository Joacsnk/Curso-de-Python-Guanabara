km = float(input('Diga a distância por KM: '))
# Calculando o preco pela distância 
if km <= 200:
    passagem = km * 0.5
    print('Valor da passagem: \33[31mR${:.2f}\33[m'.format(passagem))
else:
    passagem = km * 0.45
    print('Valor da passagem: \33[31mR${:.2f}\33[m'.format(passagem))