"""
Juego de Adivina el Número:
Descripción: La computadora elige un número y el usuario intenta adivinarlo, recibiendo pistas ("más alto", "más bajo").
Características: Consola, bucles, condicionales, validación de entrada entera.
"""
import random
import string

digitos:list = [1,2]
uno_o_dos_digitos:int = random.choice(digitos)
numeros:str = string.digits
numero_seleccionado:int = 1
numero_a_adivinar:int = 0

if uno_o_dos_digitos == 1:
	numero_a_adivinar = random.choice(numeros)
else:
	digito1=0
	while digito1 == 0:
		digito1 = random.choice(numeros)
	numero_a_adivinar = int(digito1+random.choice(numeros))

print("\t\tBienvenido a Adivina El Número!\nA continuación tendras que adivinar el número en el que estoy pensando.\nSuerte!\n\n")
while numero_seleccionado != numero_a_adivinar:
	numero_seleccionado = int(input("Ingrese el número que crea que estoy pensando: "))
	print()
	if numero_seleccionado > numero_a_adivinar:
		print("El número es más bajo al seleccionado. Intentalo de nuevo\n")
	elif numero_seleccionado < numero_a_adivinar:
		print("El número es más alto al seleccionado. Intentalo de nuevo\n")
	else:
		print("Adivinastes el número. Felicidades!")