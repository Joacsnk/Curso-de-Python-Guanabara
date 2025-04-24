frase = str(input('Digite uma frase: ')).strip().upper() # colocando a frase em maiúsculas e sem espaços
palavras = frase.split() #dividindo em listas
junto = ''.join(palavras) #juntando sem espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1): #pegando letra por letra
    inverso += junto[letra]
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo')