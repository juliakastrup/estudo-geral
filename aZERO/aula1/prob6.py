"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

prod1 = input('Digite o preço do produto 1: ')
prod2 = input('Digite o preço do produto 2: ')
prod3 = input('Digite o preço do produto 3: ')


if prod1 == prod2 and prod3 > prod1:
	print('Tanto faz levar o produto 1 ou o 2')
else:
	if prod1 == prod3 and prod2 > prod1:
		print('Tanto faz levar o produto 1 ou o 3')
	else:
		if prod2 == prod3 and prod2 > prod1:
			print('Tanto faz levar o produto 2 ou o 3')
		else:
			if prod1 == prod2 == prod3 :
				print('Todos os produtos têm o mesmo preço. Escolha com o coração!')
			else:
				if prod1 < prod2:
					if prod1 < prod3:
						print('Compre o produto 1')
					else:
						print('Compre o produto 3')
				else:
					if prod2 < prod1:
						print('Compre o produto 2')
					else:
						print('Compre o produto 3')
				