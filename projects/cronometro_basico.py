"""
Cronómetro Básico:
Descripción: Un cronómetro que se inicia, detiene y reinicia.
Características: Consola, módulo time, manejo de estados.
"""
import time

tiempo:int = 0
continuar:bool = False
reiniciar:str = ""
while not continuar:
	while not continuar:
		try:
			tiempo = int(input("Ingrese el tiempo en segundos de espera para detener: "))
			continuar = True
		except ValueError:
			print("Por favor, ingrese un número entero válido.\n")
	print("Cronómetro iniciado!")
	iniciar = time.time()
	for i in range(tiempo):
		print(".", end = "")
		time.sleep(1)
	detener = time.time()
	print("Cronómetro detenido!\n")
	print(f"Trascurrieron {(detener-iniciar):.2f} segundos.\n")

	continuar_reinicio:bool = False
	while not continuar_reinicio:
		reiniciar = input("¿Desea reiniciar el cronómetro? (s/n): ").strip().lower()
		if reiniciar == "s":
			print("\nReiniciando cronómetro...\n")
			continuar_reinicio = True
		elif reiniciar == "n":
			print("\nCronómetro finalizado.")
			continuar_reinicio = True
		else:
			print("Opción no válida. Por favor, ingrese 's' para reiniciar o 'n' para finalizar.\n")
	if reiniciar == "n":
		continuar = True
		print("Gracias por usar el cronómetro.")
	else:
		continuar = False