altura = float(input('Diga a altura: '))
largura = float(input('Diga a largura: '))
Area = altura * largura
print('Área: \33[36m{:.2f}\33[m\nQuantidade necessária de tinta: \33[36m{}L\33[m'.format(Area, Area / 2))
# Cálculo de área e de metro quadrado