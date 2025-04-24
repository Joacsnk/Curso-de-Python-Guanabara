cidade = str(input('Em qual cidade você nasceu? '))
# Aqui eu tiro os espaços, Coloco como capitalizado e divido (salvando na var)
divisao = cidade.lstrip().capitalize().split()
# Agora é só comparar
print('\33[4m', divisao[0] == 'Santo', '\33[m')