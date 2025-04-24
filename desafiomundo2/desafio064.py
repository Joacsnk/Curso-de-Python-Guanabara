numero = contagem_numeros = soma = 0
while numero != 999:
    numero = int(input("Digite um número inteiro: "))
    if numero == 999: #flag == 999
        break
    else:
        contagem_numeros += 1 #contagem
        soma += numero #soma
print(f"\n\nQuantidade de números digitados: {contagem_numeros}\nSoma dos números digitados: {soma}")