'''
El ABC de Python
Aclaración: Este desafío es inventado, es posible que haya errores fácticos en cuanto a los alfabetos reales.

Encontramos una piedra antigua en una plaza de Buenos Aires cuyas inscripciones nos ayudan a decifrar nuevos alfabetos. Gracias a estas inscripciones descubrimos que las letras del alfabeto latino arcaico tienen una correspondencia con el alfabeto latino y vamos a crear un programa que nos ayude a traducir palabras de un alfabeto a otro.

Crear una función que recibe un string, transforma todos los caracteres del alfabeto latino arcaico en caracteres modernos, no modifica el resto de los caracteres (signos de puntuacion, espacios, etc.) y devuelve el resultado con return.

Ejemplos:

traducir( "𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏" ) => "ALFABETO"

traducir( "¡𐌐𐌄𐌓𐌃𐌉!" ) => "¡PERDI!

traducir( "¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉." ) => "¿SI O NO? MMM... SI."

Correspondencia entre alfabetos:

Arcaico : Moderno
'𐌀' : 'A',
'𐌁' : 'B',
'𐌂' : 'C',
'𐌃' : 'D',
'𐌄' : 'E',
'𐌅' : 'F',
'𐌆' : 'Z',
'𐌇' : 'H',
'𐌉' : 'I',
'𐌊' : 'K',
'𐌋' : 'L',
'𐌌' : 'M',
'𐌍' : 'N',
'𐌏' : 'O',
'𐌐' : 'P',
'𐌒' : 'Q',
'𐌓' : 'R',
'𐌔' : 'S',
'𐌕' : 'T',
'𐌖' : 'V',
'𐌗' : 'X'
'''

def traducir(palabra):
	diccionario = {
		'𐌀' : 'A',
		'𐌁' : 'B',
		'𐌂' : 'C',
		'𐌃' : 'D',
		'𐌄' : 'E',
		'𐌅' : 'F',
		'𐌆' : 'Z',
		'𐌇' : 'H',
		'𐌉' : 'I',
		'𐌊' : 'K',
		'𐌋' : 'L',
		'𐌌' : 'M',
		'𐌍' : 'N',
		'𐌏' : 'O',
		'𐌐' : 'P',
		'𐌒' : 'Q',
		'𐌓' : 'R',
		'𐌔' : 'S',
		'𐌕' : 'T',
		'𐌖' : 'V',
		'𐌗' : 'X'
	}

	flag = 0

	for letra in palabra:
		for llave, valor in diccionario.items():
			if letra == llave:
				flag = 1
				print(valor, end = '')
		if flag == 0:
			print(letra, end = '')
		flag = 0			
	print('')

texto = input()
traducir(texto)
