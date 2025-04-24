media_idade = 0
maior_idade = 0
menos_20 = 0
nome_mais_velho = ""
for i in range(1, 5):
    print(f'\nPessoa {i}\n')
    nome = str(input('Diga o nome: '))
    idade = int(input('Diga a idade: '))
    sexo = int(input('Diga o sexo (Masculino[1] Feminino[2]): '))
    media_idade += idade #média das idades
    if sexo == 1 and idade > maior_idade:
        nome_mais_velho = [nome, idade] #Homem mais velho
    if sexo == 2 and idade < 20:
        menos_20 += 1 #Mulher com menos de 20 anos
media_idade = media_idade / 4
print(f'\nMédia de idade :{media_idade}')
print(f'Homem mais velho, com {nome_mais_velho[1]} anos: {nome_mais_velho[0]}')
print(f'Mulheres com menos de 20 anos: {menos_20}')