'''Mini-desafío If y While
Implementar un programa que muestre la siguiente secuencia:

1, 2, 3, 4, 5, 4, 3, 2, 1, 0

Para un desafío mayor: Utilizar un solo while, un solo if y un solo else
'''
flag = 0
x = 1
while x >= 0:
	if x<5 and flag == 0:
		print(x)
		x = x + 1
	else:
		flag = 1
		print(x)
		x = x - 1
