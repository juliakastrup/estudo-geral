"""
Faça um programa que leia 5 números e informe o maior número.
"""

num1 = input('Digite o número 1: ')
num2 = input('Digite o número 2: ')
num3 = input('Digite o número 3: ')
num4 = input('Digite o número 4: ')
num5 = input('Digite o número 5: ')

maiornum = '-inf'

if num1 > maiornum:
	maiornum = num1

if num2 > maiornum:
	maiornum = num2

if num3 > maiornum:
	maiornum = num3

if num4 > maiornum:
	maiornum = num4

if num5 > maiornum:
	maiornum = num5

print(f'O maior número é {maiornum}')