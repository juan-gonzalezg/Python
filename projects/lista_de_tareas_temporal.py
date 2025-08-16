"""
Lista de Tareas (Temporal):
Descripción: Permite al usuario añadir, ver y eliminar tareas. Los datos se pierden al cerrar el programa.
Características: Consola, lista de Python para almacenar tareas, sin persistencia.
"""

tareas:list = []
salida:bool = False

while not salida:
	continuar:bool = False
	opcion:int = 0

	print(" +--------------------------+\n",
	"|\tLista de Tareas (Temporal)\t|\n",
	"+--------------------------+\n",
	"|\t1. Añadir Tarea\t\t\t|\n",
	"|\t2. Ver Tareas\t\t\t|\n",
	"|\t3. Eliminar Tarea\t\t|\n",
	"|\t4. Salir\t\t\t\t|\n",
	"+--------------------------+\n")

	while not continuar:
		try:
			opcion = int(input("Seleccione una opción: "))
			continuar = True
		except ValueError:
			print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

	if opcion == 1:
		tarea_a_agregar:str = input("Ingrese la tarea a añadir: ")
		tareas.append(tarea_a_agregar)
		print(f"Tarea '{tarea_a_agregar}' añadida exitosamente.")
		input("Presiona Enter para continuar...")
	elif opcion == 2:
		if tareas:
			print("Tareas actuales:")
			for tarea in tareas:
				print(f"- {tarea}")
			print()
		else:
			print("No hay tareas en la lista.\n")
		input("Presiona Enter para continuar...")
	elif opcion == 3:
		if tareas:
			tarea_a_eliminar:str = input("Ingrese la tarea a eliminar: ")
			if tarea_a_eliminar in tareas:
				tareas.remove(tarea_a_eliminar)
				print(f"Tarea '{tarea_a_eliminar}' eliminada exitosamente.\n")
			else:
				print(f"Tarea '{tarea_a_eliminar}' no encontrada en la lista.\n")
		else:
			print("No hay tareas para eliminar.\n")
		input("Presiona Enter para continuar...")
	elif opcion == 4:
		print("Saliendo del programa. ¡Hasta luego!")
		salida = True
	else:
		print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.\n")
		input("Presiona Enter para continuar...")