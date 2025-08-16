"""
Piedra, Papel o Tijera:
Descripción: Juego clásico contra la computadora.
Características: Consola, random.choice, lógica de juego simple.
"""
import random

opciones_eleccion:list = ["piedra", "papel", "tijera"]
puntos:dict = {"jugador": 0, "maquina": 0}
opcion_maquina:str = random.choice(opciones_eleccion)
print("¡Bienvenido al juego de Piedra, Papel o Tijera!\n")
while puntos["jugador"]<3 and puntos["maquina"]<3:
	errores:int = 0
	correcto:bool = False
	while not correcto:
		opcion_jugador:str = input("Elige piedra, papel o tijera: ").lower()
		if opcion_jugador not in opciones_eleccion:
			print("\nOpción no válida. Inténtalo de nuevo.\n")
			errores += 1
			if errores == 1:
				print("Recuerda, las opciones válidas son: piedra, papel o tijera.")
				print(f"Nro de intentos restantes: {3 - errores}\n")
			elif errores == 2:
				print("Por favor, elige una de las opciones válidas.")
				print(f"Nro de intentos restantes: {3 - errores}\n")
			if errores == 3:
				print("Sus intentos se han agotado. La máquina gana esta ronda por defecto.")
				#puntos["maquina"] += 1
				correcto = True
		else:
			errores = 0
			print(f"\nHas elegido: {opcion_jugador}")
			print(f"La máquina eligió: {opcion_maquina}")
			correcto = True
	if opcion_jugador == opcion_maquina:
		print("\n¡Empate!")
	elif (opcion_jugador == "piedra" and opcion_maquina == "tijera") or \
		 (opcion_jugador == "papel" and opcion_maquina == "piedra") or \
		 (opcion_jugador == "tijera" and opcion_maquina == "papel"):
		puntos["jugador"] += 1
		print("\n¡Ganaste esta ronda!")
	else:
		puntos["maquina"] += 1
		print("\nLa máquina ganó esta ronda.")

	print(f"\nPuntuación - Jugador: {puntos['jugador']}, Máquina: {puntos['maquina']}\n")
	opcion_maquina = random.choice(opciones_eleccion)

if puntos["jugador"] >= 3:
	print("¡Felicidades! Has ganado el juego.")
else:
	print("\nLa máquina ha ganado el juego. ¡Inténtalo de nuevo!")
print("\nGracias por jugar Piedra, Papel o Tijera.")