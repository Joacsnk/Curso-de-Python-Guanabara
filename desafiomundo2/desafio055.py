maior = 0
menor = 0
for i in range(1, 6): #Contando até 5
    peso = float(input(f'Diga o peso da pessoa {i}: '))
    if i == 1: #Colocando valor base
        maior = peso
        menor = peso
    elif peso > maior: #Definindo o maior
        maior = peso
    elif peso < menor:#Definindo o menor
        menor = peso
print(f'\nO maior peso foi de {maior} e o menor foi {menor}')