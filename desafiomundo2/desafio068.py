from random import randint, choice #sem mota explicação, um par ou ímpar
vitorias = 0
while True:
    print("-------------------------")
    numero = int(input("Digite um número: "))
    while True:
        escolha_P_I = str(input("Escolha entre par ou ímpar [P/I]: ")).lower()
        if escolha_P_I == 'i' or escolha_P_I == 'p':
            break
    numero_pc = randint(0, 29)
    if escolha_P_I == 'p':
        if (numero_pc + numero) % 2 == 0:
            print(f"\nVocê venceu! O número que a máquina escolheu foi {numero_pc} e o resultado foi {numero_pc+numero}\n")
            vitorias += 1 
        else:
            break
    else:
        if (numero_pc + numero) % 2 == 1:
            print(f"\nVocê venceu! O número que a máquina escolheu foi {numero_pc} e o resultado foi {numero_pc+numero}\n")
            vitorias += 1
        else:
            break
print(f"\nVocê perdeu! O número que a máquina escolheu foi {numero_pc} e o resultado foi {numero_pc+numero}\n")
print(f"Você venceu {vitorias} vezes")
        
    
            