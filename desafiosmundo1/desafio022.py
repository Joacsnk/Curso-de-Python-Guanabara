nome = str(input('Diga o seu nome: ')).strip()
print('analisando nome...')
# Colocando em maiúsculo e minúsculo
print('Seu nome em maiúsculo é \33[32m{}\33[m'.format(nome.upper()))
print('Seu nome em minúsculo é \33[31m{}\33[m'.format(nome.lower()))
# Dividindo, separando o primeiro nome, juntando novamente e exibindo (Contando) as letras
nome = nome.split()
inicio = nome[0]
nome = ''.join(nome)
print('Seu nome tem \33[32m{}\33[m letras ao todo'.format(len(nome)))
print('Seu primeiro nome tem \33[31m{}\33[m letras'.format(len(inicio)))