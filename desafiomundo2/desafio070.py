total_gasto = mais_1k = c = 0
while True:
    print("\n--------------------")
    print("--------LOJA--------\n") #basciamente um outro cadastro com while
    nome_produto = str(input("Digite o nome do produto: ")).lower().strip()
    preco_produto = float(input(f"Digite o preço do {nome_produto}: R$"))
    total_gasto += preco_produto
    if c == 0:
        menor_preco = preco_produto
        c = 1
    if preco_produto > 1000:
        mais_1k += 1
    if preco_produto < menor_preco:
        menor_preco = preco_produto
        nome_menor_preco = nome_produto
    while True:
        opcao = str(input("Deseja continuar? [S/N]")).upper()
        if opcao == "S" or opcao == "N":
            break
    if opcao == "N":
        break
print(f"\n\nTotal gasto: R${total_gasto}")
print(f'Quantidade de produtos maiores que R$1000: {mais_1k}')
print(f'O {nome_menor_preco} foi o produto mais barato, custando R${menor_preco:.2f}')

    