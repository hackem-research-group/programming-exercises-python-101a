def compararNumeros(numero1, numero2):
	'''
	Funcion que imprime el numero mayor y menor de 2 datos ingresados
	'''
	#Usamos una estructura if-elif-else
	if numero1 > numero2:
		print "El numero mayor es", numero1
		print "El numero menor es", numero2
	elif numero1 == numero2:
		print "Los numeros son iguales:", numero1, numero2
	else:
		print "El numero mayor es", numero2
		print "El numero menor es", numero1
