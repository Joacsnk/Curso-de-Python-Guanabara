while True:
    numero = int(input("Digite um número para a tabuada: "))
    print("\n")
    if numero < 0:
        break
    for i in range(1, 11): #tabuada formatada
        print(f'{numero} X {i} = {numero*i}')
    print('\n')