from datetime import date
print('---CNN---')
nascimento = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year - nascimento # pegando ano atual
if anoatual <= 9:
    categoria = '\33[30mMIRIM\33[m'
elif anoatual > 9 and anoatual <= 14:
    categoria = '\33[33mINFANTIL\33[m'
elif anoatual > 14 and anoatual <= 19:
    categoria = '\33[34mJUNIOR\33[m'
elif anoatual == 20:
    categoria = '\33[32mSÊNIOR\33[m'
elif anoatual > 20:
    categoria = '\33[31mMASTER\33[m'
print(f'\nSUA CATEGORIA É {categoria}!!!')

