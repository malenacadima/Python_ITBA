'''Mini-desafio if
1. Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4) utilizando un if/else. La nota será ingresada por el usuario usando input().

2. Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F de acuerdo a la siguiente conversión:

A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: 0–59
'''

print('Ingrese 1 para el primer programa o 2 para el segundo')

programa = int(input('Programa: '))

if programa == 1:
	print('Programa #1')
	nota = int(input('Ingrese nota: '))
	if nota >= 4:
		print('aprobado')
	else:
		print('desaprobado')
elif programa == 2:
	print('Programa #2')
	nota = int(input('Ingrese nota: '))
	if nota <= 100 and nota >= 90:
		print('Nota A')
	elif nota < 90 and nota >= 80:
		print('Nota B')
	elif nota < 80 and nota >= 70:
		print('Nota C')
	elif nota < 70 and nota >= 60:
		print('Nota D')
	elif nota < 60:
		print('Nota F')

