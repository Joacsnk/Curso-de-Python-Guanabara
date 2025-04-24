contador = soma = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 999: #flag para parar
        break
    contador += 1
    soma += n
print(f'\nVocê digitou {contador} números que, somados, resulta em {soma}')