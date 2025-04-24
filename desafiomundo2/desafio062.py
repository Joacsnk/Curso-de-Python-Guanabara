termo1 = int(input("Diga o primeiro termo da PA: "))
razao = int(input('Diga a sua razão: '))
c = 0
x = 10
quant_termo = 0
while True:
    while c < x: #repetição while
        print(termo1, end=" ")
        termo1 += razao #Fazendo ela se repetir e somar
        c += 1
        quant_termo += 1
    print('PAUSA')
    x = int(input("Quantos termos você quer mostrar mais? "))
    if x == 0:
        print("Você viu {} quantidades de termos".format(quant_termo))
        break
    else:
        c = 0
