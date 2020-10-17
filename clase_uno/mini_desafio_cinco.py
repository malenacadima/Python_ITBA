'''Mini-desafío for
Mostrar la siguiente secuencia de datos utilizando la instrucción for y la instrucción if:

0, 1, 4, 9, 16, 25, 6, 7, 8, 9

'''

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ------------> i

# 0, 1, 4, 9, 16, 25, 36, 49, 64, 81  ----->  i * i


for i in range(10):
	if i < 6:
		print(i*i , end = ' ')
	else:
		print(i , end = ' ')
print('')