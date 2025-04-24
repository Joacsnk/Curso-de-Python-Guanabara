from math import pow, sqrt
oposto = float(input('\33[4;33mCateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente, 2))
print('\33[0;33mO valor da hipotenusa é de \33[30m{:.2f}\33[m'.format(hipotenusa))
# Cálculo de triângulo