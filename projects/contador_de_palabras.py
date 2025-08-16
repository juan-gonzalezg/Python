"""
Contador de Palabras:
Descripción: Pide al usuario un texto y cuenta la frecuencia de cada palabra.
Características: Consola, manipulación de cadenas, uso de diccionarios.
"""
import re

cadena:str = input("Intruduce un texto: ")
cadena.lower()
cadena_filtrada:str = re.sub(r'[^\w\s]', '', cadena)
palabras:list = cadena_filtrada.split()
contador_palabras:dict = {}

for palabra in palabras:
	if palabra in contador_palabras:
		contador_palabras[palabra] += 1
	else:
		contador_palabras[palabra] = 1

print("Frecuencia de palabras: ")
print("{'Palabra': 'Frecuencia'}")
print(contador_palabras)
