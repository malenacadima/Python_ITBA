'''
Mini-desafío: listas
1. Crear una lista con los números pares menores a 50.

2. Crear una lista con el nombre de los días de la semana. Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, que determine a qué día de la semana corresponde mediante un número de 0 (Lunes) a 6 (Domingo) y luego muestre en pantalla el elemento correspondiente de la lista, o sea, el día de la semana en forma de texto (suponemos que el día 0 del año es Lunes).

Ejemplos:

calcularDia(1) => 'Martes' (Ya que el día 0 es Lunes)

calcularDia(10) => 'Jueves' (Ya que el día 7 también es Lunes)

3. Realizar un programa que ordena nombres alfabeticamente. Primero debe pedir al usuario que ingrese el número de nombres que serán ingresados, luego debe pedir al usuario que ingrese un nombre y repetir ese pedido la cantidad de veces indicada. Los nombres se deben ir agregando a una lista. Por último, ordenar la lista alfabéticamente y mostrar en pantalla de a uno por vez los nombres ordenados (usando un for).
'''

def ordenar_nombres():
	tamaño_lista = int(input('cuántos nombres va a ingresar: '))
	lista_nombres = []
	for i in range(tamaño_lista):
		nombre = input('nombre: ')
		lista_nombres.append(nombre)
	lista_nombres.sort()
	for i in range(tamaño_lista):
		print(lista_nombres[i])

def lista_numeros_pares():
	lista = []
	for num in range(50):
		if not num % 2:
			lista.append(num)
	print(lista)

def calcularDia(num):
	dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
	if num % 7 == 0:
		return dias[0]
	elif num % 7 == 1:
		return dias[1]
	elif num % 7 == 2:
		return dias[2]
	elif num % 7 == 3:
		return dias[3]
	elif num % 7 == 4:
		return dias[4]
	elif num % 7 == 6:
		return dias[6]

lista_numeros_pares()
print(calcularDia(int(input('numero de dia: '))))
ordenar_nombres()