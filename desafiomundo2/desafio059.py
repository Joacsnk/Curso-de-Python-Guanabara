sair = 0
while sair == 0:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("\nDigite o segundo número: ")) #Pegando os números
    while sair == 0:
        escolha = int(input("\nESCOLHA UMA OPÇÃO\n\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n"))
        match escolha:
            case 1: #soma
                soma = n1 + n2
                print(f"\nA soma de {n1} com {n2} é igual a {soma}")
            case 2: #multiplicação
                multiplicacao = n1 * n2
                print(f"\nA multiplicação de {n1} com {n2} é igual a {multiplicacao}")
            case 3: #maior que outro
                if n1 > n2:
                    print(f"\n{n1} é o maior número")
                elif n2 > n1:
                    print(f"\n{n2} é o maior número")
                else:
                    print("\nOs números são iguais")
            case 4: #repetir os números
                break
            case 5: #sair
                sair = 1
            