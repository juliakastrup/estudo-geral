"""
Faça um programa que receba uma data de nascimento (15/07/87) e imprima
'Você nasceu em <dia> de <mes> de <ano>'
"""


data = input('Digite sua data de nascimento, no formato dd/mm/aa, por favor: ')

data = data.split('/')

print(f'Você nasceu em {data[0]} de {data[1]} de {data[2]}')
