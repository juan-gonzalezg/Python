"""
Calculadora Simple:
Descripción: Una calculadora que realiza operaciones básicas (suma, resta, multiplicación, división) ingresadas por el usuario.
Características: Interfaz de consola, programación imperativa, datos en memoria, validación básica de entrada numérica.
"""

print(" +--------------------------+\n",
"|\tOperaciones:\t\t\t|\n",
"+--------------------------+\n",
"|\t1. Suma (+)\t\t\t\t|\n",
"|\t2. Resta (-)\t\t\t|\n",
"|\t3. Multiplicación (*)\t|\n",
"|\t4. División (/)\t\t\t|\n",
"+--------------------------+\n")
option_elegida = input("Opción: ")

if option_elegida.isdigit():
	option = int(option_elegida)
	numero1=float(input("Ingrese el numero: "))
	numero2=float(input("Ingrese el numero: "))
	if option==1:
		print(f"Resultado de la suma: {numero1+numero2}")
	elif option==2:
		print(f"Resultado de la resta: {numero1-numero2}")
	elif option==3:
		print(f"Resultado de la multiplicación: {numero1*numero2}")
	elif option==4:
		print(f"Resultado de la división: {numero1/numero2}")
else:
	print("\nOpción incorrecta!")