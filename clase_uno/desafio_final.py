def lothar(num):
	if num % 2 == 0:
		return num / 2
	elif num % 2 != 0:
		return num * 3 + 1

#---> main()

numero = int(input('Digite un número: '))
secuencia = [numero]
while lothar(numero) != 1:
	numero = lothar(numero)
	secuencia.append(numero)

print('secuencia', secuencia)
print('cantidad de veces: ', len(secuencia))