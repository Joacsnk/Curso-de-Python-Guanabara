fatorial = int(input("Digite um número para virar em fatorial: ")) #pegando fatorial input
multiplicacao = 1 #variável de auxílio
while fatorial > 1: #a multiplicação por 1 é desnecessária, então é até ser igual a 1
    multiplicacao = multiplicacao*fatorial # ele fará o fatorial vezes a multiplicação, e depois o fatorial diminui
    fatorial -= 1
print(multiplicacao)