valor = float(input('\33[30;0mValor do produto: \33[30;4m'))
fpag = int(input('\33[30;0mDinheiro (1)   Cheque (2)     Cartão (3)\nForma de pagamento: \33[30;4m'))
# Dinheiro ou cheque
if fpag == 1 or fpag == 2:
    desconto = valor * 10 / 100
    print('\n\33[30;0mO valor final foi de \33[32mR${:.2f}\33[30m, com \33[32;1mR${:.2f}\33[0;30m de desconto'.format(valor + desconto, desconto))
# Cartão
elif fpag == 3:
    fpag = int(input('\n\33[30;0mDébito (1)   Crédito (2)\nForma de pagamento: \33[30;4m'))
    # Débito
    if fpag == 1:
        desconto = valor * 5 / 100
        print('\33[30;0mO valor final foi de \33[32R${:.2f}\33[m, com \33[32;1mR${:.2f}\33[30;0m de desconto'.format(valor + desconto, desconto)) 
    # Crédito   
    elif fpag == 2:
        fpag = int(input('\33[30;0mÀ vista (1)   2 vezes (2)     3 vezes(3)       4 vezes(4)     5 vezes(5)\nForma de pagamento: \33[30;4m'))
        # À vista
        if fpag == 1:
            desconto = valor * 5 / 100
            print('\n\33[30;0mO valor final foi de \33[32mR${:.2f}\33[30;0m, com \33[32;1mR${:.2f}\33[30;0m de desconto'.format(valor + desconto, desconto)) 
        # 2x    
        elif fpag == 2:
            print('\n\33[30;0mO valor final foi 2 vezes de \33[32mR${:.2f}\33[30;0m, sem nenhum desconto'.format(valor / 2) )
        # 3x
        elif fpag == 3:
            acrescimo = valor * 20 / 100
            print('\n\33[30;0mO valor final foi 3 vezes de \33[32mR${:.2f}\33[30;0m, com um acréscimo de \33[31;1mR${:.2f}\33[30;0m'.format((valor + acrescimo) / 3, acrescimo))
        # 4x
        elif fpag == 4:
            acrescimo = valor * 20 / 100
            print('\n\33[30;0mO valor final foi 4 vezes de \33[32mR${:.2f}\33[30;0m, com um acréscimo de \33[31;1mR${:.2f}\33[30;0m'.format((valor + acrescimo) / 4, acrescimo))
        # 5x
        elif fpag == 5:
            acrescimo = valor * 20 / 100
            print('\n\33[30;0mO valor final foi 5 vezes de \33[32mR${:.2f}\33[30;0m, com um acréscimo de \33[31;1mR${:.2f}\33[30;0m'.format((valor + acrescimo) / 5, acrescimo))
        else:
            print('\n\33[1;31mOPCÃO INVÁLIDA!\33[0m')
    else:
        print('\n\33[1;31mOPCÃO INVÁLIDA!\33[0m')   
else:
    print('\n\33[1;31mOPCÃO INVÁLIDA!\33[0m')