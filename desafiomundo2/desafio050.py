y = 0
for i in range (0, 6):
    x = int(input("Diga um número: "))
    if x % 2 == 0: # Separando o par
        y += x
print(f'Os valores somados foram, no total, {y}') 