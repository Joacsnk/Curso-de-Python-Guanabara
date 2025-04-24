nome = str(input('Digite seu nome completo ')).title().strip()
print('\33[42mSeja bem vindo\33[m')
# Aqui eu divido os nomes em uma lista
nome = nome.split()
print('Seu primeiro nome é \33[32m{}\33[m'.format(nome[0]))
# Aqui eu pego o ultimo elemento da lista (que é a quantidade de elementos da lista menos - 1)
print('Seu último nome é \33[32m{}\33[m'.format(nome[len(nome) - 1]))