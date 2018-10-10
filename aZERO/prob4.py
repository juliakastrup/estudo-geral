"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
"""

numint1 = float(input('Digite um número inteiro: '))
numint2 = float(input('Digite outro número inteiro: '))
numreal = float(input('Digite um número real: '))

letraA = int((numint1*2)*(numint2/2))
letraB = (numint1*3) + numreal
letraC = numreal**3


print(f'O produto do dobro do primeiro com metade do segundo é {letraA}')
print(f'A soma do triplo do primeiro com o terceiro é {letraB}')
print(f'O terceiro elevado ao cubo é {letraC}')