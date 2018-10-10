"""
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

área = int(input('Digite o tamanho da área a ser pintada, em m²: '))

totallitros = área/3

if totallitros < 18:
	print('Será necessária apenas uma lata.')
	print('Total: R$80,00')
else:
	if área%18!=0 and área%3!=0:
		qtslatas = (totallitros // 18) + 1
		custototal = qtslatas * 80
		print(f'Você precisará comprar {qtslatas}, ao custo total de {custototal}')
	else:
		qtslatas = (totallitros // 18)
		custototal = qtslatas * 80
		print(f'Você precisará comprar {qtslatas}, ao custo total de {custototal}')

