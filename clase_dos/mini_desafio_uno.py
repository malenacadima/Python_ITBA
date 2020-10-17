'''
Mini-desafío: floats
Crear:

Una función que convierta grados Celsius a grados Farenheit (https://es.wikipedia.org/wiki/Grado_Fahrenheit)
Una función que convierta grados Celsius a grados Kelvin (https://es.wikipedia.org/wiki/Kelvin)
El usuario debe ingresar una temperatura en grados Celsius y el programa debe mostrar las conversiones a Farenheit y Kelvin utilizando las funciones. Si la temperatura ingresada es inferior al cero absoluto, el programa debe mostrar un mensaje de advertencia.

Pueden leer aqui sobre como hacer las conversiones.
'''

def celsius_a_farenheit(num):
	return num * 9 / 5 + 32

def celsius_a_kelvin(num):
	return num + 273.15

grados = float(input('temperatura: '))

print(celsius_a_farenheit(grados))
print(celsius_a_kelvin(grados))