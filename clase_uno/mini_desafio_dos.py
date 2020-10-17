'''Mini-desafio
Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, y que muestra en pantalla a qué día de la semana corresponde mediante un número de 0 a 6 (mostrar el número 0 si corresponde a Lunes y 6 si es Domingo)

Suponemos que el día 0 del año cae un Lunes.

Pista (seleccionar texto para ver): Los días múltiplos de 7 corresponden a 0 (Lunes), los días que tienen resto 1 en la división por 7 corresponden a 1 (Martes), los días que tienen resto 2 en la división por 7 corresponden a 2 (Miércoles), etc.
'''

dia = int(input('dia: '))

print('lunes\t\t', dia % 7 == 0)
print('martes\t\t', dia % 7 == 1)
print('miercoles\t', dia % 7 == 2)
print('jueves\t\t', dia % 7 == 3)
print('viernes\t\t', dia % 7 == 4)
print('sabado\t\t', dia % 7 == 5)
print('domingo\t\t', dia % 7 == 6)


