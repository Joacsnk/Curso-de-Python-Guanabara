n = int(input("Diga um número: ")) #fibonacci
a = 0
b = 1
contador = 0
while contador != n: #caso 1
    if n == 1:
        print(a)
        break
    elif n == 2: #caso 2
        print(a)
        print(b)
        break
    else:
        if contador == 0: #mostra os dois primeiros e faz a sequência
            print(a)
            print(b)
            contador = 2
        c = a + b
        print(c)
        a = b
        b = c
        contador += 1
        