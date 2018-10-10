nota1 = float(input('Qual foi sua nota 1? '))
nota2 = float(input('Qual foi sua nota 2? '))

media = sum([nota1,nota2])/2

if media == 10:
	print('Aprovado com distinção')
elif media >= 7:
	print('Aprovado')
else: 
	print('Reprovado')
