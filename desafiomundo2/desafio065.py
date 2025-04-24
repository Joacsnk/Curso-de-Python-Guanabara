media = contagem = 0
decisao = "x"
while decisao != "N":
    numero = int(input("DIGITE UM NÚMERO INTEIRO: "))
    decisao = str(input("DESEJA CONTINUAR? [S/N]: ")).upper()
    media += numero # media
    contagem += 1 
    if contagem == 1: #se for a primeira vez
        menor = numero
        maior = 0
    else:
        if maior < numero: #maior
            maior = numero
        if menor > numero: #menor
            menor = numero
print(f"\n\nMédia dos números: {media / contagem}")
print(f"\nMaior número digitado: {maior}")
print(f"\nMenor número digitado: {menor}")