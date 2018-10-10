"""
Exercício #7
Faça um programa que receba uma string e responda se ela tem alguma vogal,
se sim, quais são? E também diga se ela é uma frase ou não.
"""

frase = input('Digite algo: ')

if 'a' or 'e' or 'i' or 'o' or 'u' in frase:
	print('Contém vogal!')
elif 'a' or 'e' or 'i' or 'o' or 'u' not in frase:
	print('Não contém vogais! Você é polonês?')   # Não está funcionando. Sempre diz que tem vogal. Rever.

if 'a' in frase:
	print('Contém a letra a')

if 'e' in frase:
	print('Contém a letra e')

if 'i' in frase:
	print('Contém a letra i')

if 'o' in frase:
	print('Contém a letra o')

if 'u' in frase:
	print('Contém a letra u')

if ' ' in frase:
	print('Isso é uma frase! :)')
else:
	print('Isso não é uma frase!')








