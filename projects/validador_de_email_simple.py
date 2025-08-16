"""
Validador de Email Simple:
Descripción: Verifica si una cadena de texto tiene el formato básico de un email (contiene '@' y '.').
Características: Consola, validación de cadenas, uso de in para caracteres.
"""

correo:str = input("Introduce un correo electrónico: ")
if ('@' in correo) and (("gmail.com" in correo) or ("hotmail.com" in correo)):
	print("El correo electrónico es válido.")
else:
	print("El correo electrónico no es válido.")
