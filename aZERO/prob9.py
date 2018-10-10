cond = False

while not cond:
	nota = input('Digite uma nota entre 0 e 10: ')
	if nota.isdigit():
		if float(nota) >= 0 and float(nota) < 11:
			cond = True
	print('Olá, insira um valor válido')

print(f'Você inseriu {nota}, um valor válido')

