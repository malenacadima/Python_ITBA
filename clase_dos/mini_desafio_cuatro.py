'''
Mini-desafío: Diccionarios
Realizar un programa que pida al usuario un número de legajo y el nombre completo, luego lo guarde en un diccionario.

Usar dos celdas de codigo, en una crear el diccionario, y en la otra agregar el nombre y legajo, mostrar el contenido. La idea es que cuando se ejecute varias veces la segunda celda se agrege un nuevo nombre y legajo a lo que ya había sido almacenado en el diccionario.
'''

def cargar_datos():
	legajo = int(input('legajo: '))
	nombre = input('nombre completo: ')
	diccionario = {
	'legajo' : legajo
	'nombre completo' : nombre
	}
	return diccionario

list_diccionarios = []
nuevo_diccionario = cargar_datos()
list_diccionarios.append(nuevo_diccionario)
