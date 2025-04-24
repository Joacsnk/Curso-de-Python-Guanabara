while True:
    sexo = str(input("Diga seu sexo [M/F]: ")).upper().strip()
    if sexo != "M" and sexo != "F":
        print("Sexo errado, insira novamente\n") #Verifica se é F ou M
    else:
        break
print("Fim")