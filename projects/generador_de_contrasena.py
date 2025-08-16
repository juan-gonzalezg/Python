"""
Generador de Contraseñas:
Descripción: Pide al usuario la longitud y genera una contraseña aleatoria con letras, números y símbolos.
Características: Consola, imperativo, módulos random y string.
"""
import random
import string

num:int = input("Indica la longitud para la contraseña: ")
if num.isdigit():
	longitud:int = int(num)
	caracteres:str = string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()_-+={}[]|\\\"'<,>.?/\'"
	cantidad:int = 1
	clave:str = ""
	while cantidad <= longitud:
		clave += random.choice(caracteres)
		cantidad += 1
	print(clave)
else:
	print("Valor incorrecto!")