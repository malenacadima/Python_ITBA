'''
Mini-desafío: Operaciones con strings
Hacer un programa que permita ingresar un nombre y un apellido usando dos veces la función input( ). Luego debe crear la variable nombre_y_apellido que contenga ambos datos separados por un espacio. Un fabricante de tarjetas admite la impresión de hasta 26 caracteres para el nombre del dueño de la tarjeta, el programa debe imprimir "Nombre admitido" si nombre_y_apellido cumple con esta restricción y "Nombre no admitido" en caso contrario (el espacio cuenta como uno de los 26 caracteres disponibles).

Para un desafío mayor: Si nombre_y_apellido cumple la restricción, mostrar el nombre y apellido. En caso contrario nombre_y_apellido debe valer la inicial del nombre y luego el apellido separado por un espacio. Si todavía no se cumple la restricción entonces el valor será la inicial del nombre y las primeras 24 letras del apellido. Mostrar el nombre resultante.
'''

def fabricante_de_tarjetas(nom_y_ape):
	if len(nom_y_ape) <= 26:
		print('Nombre admitido')
	else:
		print('Nombre no admitido')

def mayor_desafio(nommbre, apellido):
	if len(nombre + ' ' + apellido) <= 26:
		print(nombre + ' ' + apellido)
	else:
		print(nombre[0] + ' ' + apellido[:24])


nombre = input('nombre: ')
apellido = input('apellido: ')

nombre_y_apellido = nombre + ' ' + apellido

fabricante_de_tarjetas(nombre_y_apellido)

mayor_desafio(nombre, apellido)
