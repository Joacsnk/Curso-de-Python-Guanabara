from math import sin, cos, tan, radians
angulo = float(input('\33[36mDigite um ângulo: '))
print('\33[30;4mSeno: {:.2f}'.format(sin(radians(angulo))))
print('Coseno: {:.2f}'.format(cos(radians(angulo))))
print('Tangente: {:.2f}\33[m'.format(tan(radians(angulo))))
# Transformação de graus - radiano e radiano - sen, cos e tan