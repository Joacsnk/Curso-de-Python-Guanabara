celcius = float(input("Temperatura em celcius: "))
print('\33[1;46m{}ºC\33[m é equivalente a \33[1;46m{:.1f}ºF\33[m'.format(celcius, celcius * 9 / 5 + 32))
# Cálculo mais complicado, não sabia de cabeça