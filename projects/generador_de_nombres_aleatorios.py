"""
Generador de Nombres Aleatorios:
Descripción: Combina una lista de nombres y apellidos predefinidos para generar nombres completos aleatorios.
Características: Consola, listas, random.choice.
"""
import random

nombres:tuple = ("Sofía", "Mateo", "Valentina", "Sebastián", "Isabella", "Alejandro", "Camila", "Diego", "Lucía", "Nicolás", "Emma", "Daniel", "Valeria", "Pablo", "Martina", "Javier", "Emilia", "Samuel", "Antonella", "Fernando")
apellidos:tuple = ("Salazar", "Medina", "Morales", "Rojas", "Castro", "Vargas", "Díaz", "Ramírez", "Torres", "Flores", "Rivera", "Gómez", "García", "Rodríguez", "Martínez", "Hernández", "López", "González", "Pérez", "Sánchez")
nombre_completo:str
continuar:bool = False

print("Generador de Nombres Aleatorios")
while not continuar:
	print(" +----------------------------------------------------------------+\n",
	      "| 1. Generar Nombre Completo Corto (Un nombre y un apellido)     |\n",
	      "| 2. Generar Nombre Completo Largo (Dos nombres y dos apellidos) |\n",
	      "| 3. Salir                                                       |\n",
	      "+----------------------------------------------------------------+\n")
	try:
		opcion:int = int(input("Indique una opción: "))
		continuar = True
	except ValueError:
		print("Por favor, ingrese un número válido.\n")

if opcion == 1:
	nombre_completo = random.choice(nombres) + " " + random.choice(apellidos)
	print(f"\nNombre Completo Corto: {nombre_completo}")
elif opcion == 2:
	nombre_completo = random.choice(nombres) + " " + random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)
	print(f"\nNombre Completo Largo: {nombre_completo}")
elif opcion == 3:
	print("\nSaliendo del generador de nombres aleatorios.")
else:
	print("\nOpción no válida. Por favor, intente de nuevo.")
