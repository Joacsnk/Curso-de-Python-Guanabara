menor = 0
maior = 0
for i in range(1, 8):
    ano = int(input(f'Ano da pessoa {i}: '))
    if ano > 2006: #Verifica se é maior ou menor de idade (ano de 2024)
        menor +=1
    else:
        maior +=1
print(f'{maior} pessoas são de maiores, enquanto {menor} são de menores')