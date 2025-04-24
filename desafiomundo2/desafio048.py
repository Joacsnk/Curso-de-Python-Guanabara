x = 0
for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0: # caso for ímpar e múltiplo de 3
        x += i #soma
print(f'\nA soma é igual a {x}')