altura = float(input('Diga a altura: '))
peso = float(input('Diga seu peso: '))
# Cálcuo: peso dividido pela altura dupla 
imc = peso / (altura ** 2)
print('O seu \33[33mIMC\33[m (\33[33mÍndice de Massa Corporal\33[m) é de \33[33m{:.2f}\33[m'.format(imc))
if imc < 18.5:
    print('Você está \33[35mabaixo do peso\33[m')
elif imc >= 18.5 and imc < 25:
    print('Você está no \33[32mpeso ideal\33[m')
elif imc >= 25 and imc < 30:
    print('Você está com \33[37;1msobrepeso\33[0m')
elif imc >= 30 and imc < 40:
    print('Você está com \33[31mobesidade\33[m')
elif imc > 40:
    print('Você está com \33[31;1mobesidade mórbida\33[0m')



    

    
