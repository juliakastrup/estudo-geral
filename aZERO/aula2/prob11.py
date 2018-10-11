"""
Exercício # 11
Faça um programa que itere em uma string e toda vez que uma vogal aparecer
na sua string print o seu nome entre as letras
string = bananas
b
eduardo
n
eduardo
n
...
"""


word = input('Type a word: ')
name = input('Digite seu nome: ')

for i in word:
	if i in 'aeiou':
		print(name)
	else:
		print(i)
	


vowels = 'aeiou'

word = input('Type a word: ')
word = list(word)

for l in word:
	if l not in vowels:
		print(l)
	else:
		print('Júlia')