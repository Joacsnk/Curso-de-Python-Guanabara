frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece \33[32m{}\33[m vezes na frase'.format(frase.count('a')))
print('A primeira letra A aparece na posição \33[36m{}\33[m'.format(frase.find('a') + 1))
# Só aqui que entendi dps, dá para colocar um r no find
print('A última letra A aparece na posição \33[30;43m{}\33[m'.format(frase.rfind('a') + 1))