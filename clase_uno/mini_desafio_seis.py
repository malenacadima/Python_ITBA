'''Mini-desafío funciones
Escribir una función que chequee los siguientes usuarios y contraseñas:

Usuario: Juan - Contraseña: 12345_
Usuario: Pablo - Contraseña: xDcFvGbHn
La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.
'''
def validar (usuario, contraseña):
	if usuario == 'Juan' and contraseña == '12345':
		return True
	elif usuario == 'Pablo' and contraseña == 'xDcFvGbHn':
		return True
	else:
		return False

#--> Main()

print(validar(input('Usuario: '), input('Contraseña: ')))
