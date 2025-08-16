"""
Convertidor de Unidades:
Descripción: Convierte entre unidades comunes (ej. Celsius a Fahrenheit, metros a pies).
Características: Consola, funciones simples, manejo de diferentes tipos de conversión.
"""
def convertir_miligramos_a_gramos(miligramos:int):
	gramos = miligramos / 1000
	print(f"{miligramos} mg son {gramos} g.")
	input()

def convertir_miligramos_a_kilogramos(miligramos:int):
	kilogramos = miligramos / 1000000
	print(f"{miligramos} mg son {kilogramos} kg.")
	input()

def convertir_gramos_a_miligramos(gramos:int):
	miligramos = gramos * 1000
	print(f"{gramos} g son {miligramos} mg.")
	input()

def convertir_gramos_a_kilogramos(gramos:int):
	kilogramos = gramos / 1000
	print(f"{gramos} g son {kilogramos} kg.")
	input()

def convertir_kilogramos_a_miligramos(kilogramos:int):
	miligramos = kilogramos * 1000000
	print(f"{kilogramos} kg son {miligramos} mg.")
	input()

def convertir_kilogramos_a_gramos(kilogramos:int):
	gramos = kilogramos * 1000
	print(f"{kilogramos} kg son {gramos} g.")
	input()

def datos_miligramos(opcion:int):
	continuar_proceso:bool = False
	miligramos:int
	while not continuar_proceso:
		try:
			miligramos = int(input("\nIngrese la cantidad de miligramos: "))
			if opcion == 1:
				convertir_miligramos_a_gramos(miligramos)
			elif opcion == 2:
				convertir_miligramos_a_kilogramos(miligramos)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Miligramos.")

def datos_gramos(opcion:int):
	continuar_proceso:bool = False
	gramos:int
	while not continuar_proceso:
		try:
			gramos = int(input("\nIngrese la cantidad de gramos: "))
			if opcion == 3:
				convertir_gramos_a_miligramos(gramos)
			elif opcion == 4:
				convertir_gramos_a_kilogramos(gramos)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Gramos.")

def datos_kilogramos(opcion:int):
	continuar_proceso:bool = False
	kilogramos:int
	while not continuar_proceso:
		try:
			kilogramos = int(input("\nIngrese la cantidad de kilogramos: "))
			if opcion == 5:
				convertir_kilogramos_a_miligramos(kilogramos)
			elif opcion == 6:
				convertir_kilogramos_a_gramos(kilogramos)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Kilogramos.")

def opciones_de_conversion_de_masa() -> int:
	opcion:int = 0
	continuar:bool = False
	while not continuar:
		print(" +-----------------------------------+\n",
		      "| Seleccione la conversión de masa: |\n",
		      "+-----------------------------------+")
		print(" | 1. Miligramos a Gramos            |\n",
		      "| 2. Miligramos a Kilogramos        |\n",
		      "| 3. Gramos a Miligramos            |\n",
		      "| 4. Gramos a Kilogramos            |\n",
		      "| 5. Kilogramos a Miligramos        |\n",
		      "| 6. Kilogramos a Gramos            |\n",
		      "| 7. Salir                          |\n",
		      "+-----------------------------------+\n")
		try:
			opcion = int(input("\nIndique la opción deseada: "))
			continuar = True
		except ValueError:
			print("\nPor favor, ingrese un número válido.")
	return opcion

def convertir_masa():
	opcion:int
	continuar:bool = False
	while not continuar:
		opcion = opciones_de_conversion_de_masa()
		if opcion == 1 or opcion == 2:
			datos_miligramos(opcion)
		elif opcion == 3 or opcion == 4:
			datos_gramos(opcion)
		elif opcion == 5 or opcion == 6:
			datos_kilogramos(opcion)
		elif opcion == 7:
			print("\nSaliendo del convertidor de masa...")
			continuar = True
		else:
			print("\nOpción no válida. Por favor, intente de nuevo.")

def convertir_kilometros_a_milimetros(kilometros:int):
	milimetros = kilometros * 1000000
	print(f"{kilometros} km son {milimetros} mm.")
	input()

def convertir_kilometros_a_centimetros(kilometros:int):
	centimetros = kilometros * 100000
	print(f"{kilometros} km son {centimetros} cm.")
	input()

def convertir_kilometros_a_metros(kilometros:int):
	metros = kilometros * 1000
	print(f"{kilometros} km son {metros} m.")
	input()

def convertir_metros_a_milimetros(metros:int):
	milimetros = metros * 1000
	print(f"{metros} m son {milimetros} mm.")
	input()

def convertir_metros_a_centimetros(metros:int):
	centimetros = metros * 100
	print(f"{metros} m son {centimetros} cm.")
	input()

def convertir_metros_a_kilometros(metros:int):
	kilometros = metros / 1000
	print(f"{metros} m son {kilometros} km.")
	input()

def convertir_centimetros_a_milimetros(centimetros:int):
	milimetros = centimetros * 10
	print(f"{centimetros} cm son {milimetros} mm.")
	input()

def convertir_centimetros_a_metros(centimetros:int):
	metros = centimetros / 100
	print(f"{centimetros} cm son {metros} m.")
	input()

def convertir_centimetros_a_kilometros(centimetros:int):
	kilometros = centimetros / 100000
	print(f"{centimetros} cm son {kilometros} km.")
	input()

def convertir_milimetros_a_centimetros(milimetros:int):
	centimetros = milimetros / 10
	print(f"{milimetros} mm son {centimetros} cm.")
	input()

def convertir_milimetros_a_metros(milimetros:int):
	metros = milimetros / 1000
	print(f"{milimetros} mm son {metros} m.")
	input()

def convertir_milimetros_a_kilometros(milimetros:int):
	kilometros = milimetros / 1000000
	print(f"{milimetros} mm son {kilometros} km.")
	input()

def datos_milimetros(opcion:int):
	continuar_proceso:bool = False
	milimetros:int
	while not continuar_proceso:
		try:
			milimetros = int(input("\nIngrese la cantidad de milímetros: "))
			if opcion == 1:
				convertir_milimetros_a_centimetros(milimetros)
			elif opcion == 2:
				convertir_milimetros_a_metros(milimetros)
			elif opcion == 3:
				convertir_milimetros_a_kilometros(milimetros)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Milimetros.")

def datos_centimetros(opcion:int):
	continuar_proceso:bool = False
	centimetros:int
	while not continuar_proceso:
		try:
			centimetros = int(input("\nIngrese la cantidad de centímetros: "))
			if opcion == 4:
				convertir_centimetros_a_milimetros(centimetros)
			elif opcion == 5:
				convertir_centimetros_a_metros(centimetros)
			elif opcion == 6:
				convertir_centimetros_a_kilometros(centimetros)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Centimetros.")

def datos_metros(opcion:int):
	continuar_proceso:bool = False
	metros:int
	while not continuar_proceso:
		try:
			metros = int(input("\nIngrese la cantidad de metros: "))
			if opcion == 7:
				convertir_metros_a_milimetros(metros)
			elif opcion == 8:
				convertir_metros_a_centimetros(metros)
			elif opcion == 9:
				convertir_metros_a_kilometros(metros)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Metros.")

def datos_kilometros(opcion:int):
	continuar_proceso:bool = False
	kilometros:int
	while not continuar_proceso:
		try:
			kilometros = int(input("\nIngrese la cantidad de kilómetros: "))
			if opcion == 10:
				convertir_kilometros_a_milimetros(kilometros)
			elif opcion == 11:
				convertir_kilometros_a_centimetros(kilometros)
			elif opcion == 12:
				convertir_kilometros_a_metros(kilometros)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Kilometros.")

def opciones_de_conversion_de_longitud() -> int:
	opcion:int = 0
	continuar = False
	while not continuar:
		print(" +---------------------------------------\n+",
		      "| Seleccione la conversión de longitud: |\n",
		      "+---------------------------------------+")
		print(" | 1. Milímetros a Centímetros           |\n",
		      "| 2. Milímetros a Metros                |\n",
		      "| 3. Milímetros a Kilómetros            |\n",
		      "| 4. Centímetros a Milímetros           |\n",
		      "| 5. Centímetros a Metros               |\n",
		      "| 6. Centímetros a Kilómetros           |\n",
		      "| 7. Metros a Milímetros                |\n",
		      "| 8. Metros a Centímetros               |\n",
		      "| 9. Metros a Kilómetros                |\n",
		      "| 10. Kilómetros a Milímetros           |\n",
		      "| 11. Kilómetros a Centímetros          |\n",
		      "| 12. Kilómetros a Metros               |\n",
		      "| 13. Salir                             |\n",
		      "+---------------------------------------+\n")
		try:
			opcion = int(input("\nIndique la opción deseada: "))
			continuar = True
		except ValueError:
			print("\nPor favor, ingrese un número válido.")
	return opcion

def convertir_longitud():
	opcion:int
	continuar:bool = False
	while not continuar:
		opcion = opciones_de_conversion_de_longitud()
		if opcion == 1 or opcion == 2 or opcion == 3:
			datos_milimetros(opcion)
		elif opcion == 4 or opcion == 5 or opcion == 6:
			datos_centimetros(opcion)
		elif opcion == 7 or opcion == 8 or opcion == 9:
			datos_metros(opcion)
		elif opcion == 10 or opcion == 11 or opcion == 12:
			datos_kilometros(opcion)
		elif opcion == 13:
			print("\nSaliendo del convertidor de longitud...")
			continuar = True
		else:
			print("\nOpción no válida. Por favor, intente de nuevo.")

def convertir_dias_a_segundos(dias:int):
	segundos = dias * 86400
	print(f"{dias} días son {segundos} segundos.")
	input()

def convertir_dias_a_minutos(dias:int):
	minutos = dias * 1440
	print(f"{dias} días son {minutos} minutos.")
	input()

def convertir_dias_a_horas(dias:int):
	horas = dias * 24
	print(f"{dias} días son {horas} horas.")
	input()

def convertir_horas_a_segundos(horas:int):
	segundos = horas * 3600
	print(f"{horas} horas son {segundos} segundos.")
	input()

def convertir_horas_a_minutos(horas:int):
	minutos = horas * 60
	print(f"{horas} horas son {minutos} minutos.")
	input()

def convertir_horas_a_dias(horas:int):
	dias = horas / 24
	print(f"{horas} horas son {dias} días.")
	input()

def convertir_minutos_a_segundos(minutos:int):
	segundos = minutos * 60
	print(f"{minutos} minutos son {segundos} segundos.")
	input()

def convertir_minutos_a_horas(minutos:int):
	horas = minutos / 60
	print(f"{minutos} minutos son {horas} horas.")
	input()

def convertir_minutos_a_dias(minutos:int):
	dias = minutos / 1440
	print(f"{minutos} minutos son {dias} días.")
	input()

def convertir_segundos_a_minutos(segundos:int):
	minutos = segundos / 60
	print(f"{segundos} segundos son {minutos} minutos.")
	input()

def convertir_segundos_a_horas(segundos:int):
	horas = segundos / 3600
	print(f"{segundos} segundos son {horas} horas.")
	input()

def convertir_segundos_a_dias(segundos:int):
	dias = segundos / 86400
	print(f"{segundos} segundos son {dias} días.")
	input()

def datos_segundos(opcion:int):
	continuar_proceso:bool = False
	segundos:int
	while not continuar_proceso:
		try:
			segundos = int(input("\nIngrese la cantidad de segundos: "))
			if opcion == 1:
				convertir_segundos_a_minutos(segundos)
			elif opcion == 2:
				convertir_segundos_a_horas(segundos)
			elif opcion == 3:
				convertir_segundos_a_dias(segundos)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Segundos.")

def datos_minutos(opcion:int):
	continuar_proceso:bool = False
	minutos:int
	while not continuar_proceso:
		try:
			minutos = int(input("\nIngrese la cantidad de minutos: "))
			if opcion == 4:
				convertir_minutos_a_segundos(minutos)
			elif opcion == 5:
				convertir_minutos_a_horas(minutos)
			elif opcion == 6:
				convertir_minutos_a_dias(minutos)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Minutos.")

def datos_horas(opcion:int):
	continuar_proceso:bool = False
	horas:int
	while not continuar_proceso:
		try:
			horas = int(input("\nIngrese la cantidad de horas: "))
			if opcion == 4:
				convertir_horas_a_segundos(horas)
			elif opcion == 5:
				convertir_horas_a_minutos(horas)
			elif opcion == 6:
				convertir_horas_a_dias(horas)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Horas.")

def datos_dias(opcion:int):
	continuar_proceso:bool = False
	dias:int
	while not continuar_proceso:
		try:
			dias = int(input("\nIngrese la cantidad de días: "))
			if opcion == 4:
				convertir_dias_a_segundos(dias)
			elif opcion == 5:
				convertir_dias_a_minutos(dias)
			elif opcion == 6:
				convertir_dias_a_horas(dias)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la cantidad de Días.")

def opciones_de_conversion_de_tiempo() -> int:
	opcion:int = 0
	continuar:float = False
	while not continuar:
		print(" +-------------------------------------+\n",
		      "| Seleccione la conversión de tiempo: |\n",
		      "+-------------------------------------+")
		print(" | 1. Segundos a Minutos               |\n",
		      "| 2. Segundos a Horas                 |\n",
		      "| 3. Segundos a Días                  |\n",
		      "| 4. Minutos a Segundos               |\n",
		      "| 5. Minutos a Horas                  |\n",
		      "| 6. Minutos a Días                   |\n",
		      "| 7. Horas a Segundos                 |\n",
		      "| 8. Horas a Minutos                  |\n",
		      "| 9. Horas a Días                     |\n",
		      "| 10. Días a Segundos                 |\n",
		      "| 11. Días a Minutos                  |\n",
		      "| 12. Días a Horas                    |\n",
		      "| 13. Salir                           |\n",
		      "+-------------------------------------+\n")
		try:
			opcion = int(input("\nIndique la opción deseada: "))
			continuar = True
		except ValueError:
			print("\nPor favor, ingrese un número válido.")
	return opcion

def convertir_tiempo():
	opcion:int
	continuar:bool = False
	while not continuar:
		opcion = opciones_de_conversion_de_tiempo()
		if opcion == 1 or opcion == 2 or opcion == 3:
			datos_segundos(opcion)
		elif opcion == 4 or opcion == 5 or opcion == 6:
			datos_minutos(opcion)
		elif opcion == 7 or opcion == 8 or opcion == 9:
			datos_horas(opcion)
		elif opcion == 10 or opcion == 11 or opcion == 12:
			datos_dias(opcion)
		elif opcion == 13:
			print("\nSaliendo del convertidor de tiempo...")
			continuar = True
		else:
			print("\nOpción no válida. Por favor, intente de nuevo.")

def convertir_fahrenheit_a_celsius(fahrenheit:float):
	celsius = (fahrenheit - 32) * 5/9
	print(f"{fahrenheit}°F es igual a {celsius}°C")
	input()

def convertir_celsius_a_fahrenheit(celsius:float):
	fahrenheit = (celsius * 9/5) + 32
	print(f"{celsius}°C es igual a {fahrenheit}°F")
	input()

def datos_celsius():
	continuar_proceso:bool = True
	celsius: float
	while not continuar_proceso:
		try:
			celsius = float(input("\nIngrese la temperatura en Celsius (sin grados \"°C\"): "))
			convertir_celsius_a_fahrenheit(celsius)
			continuar_proceso = True
		except ValueError:
			print("Por favor, ingrese un número válido para la temperatura en Celsius.")

def datos_fahrenheit():
	continuar_proceso:bool = True
	fahrenheit:float
	while not continuar_proceso:
		try:
			fahrenheit = float(input("\nIngrese la temperatura en Fahrenheit (sin grados \"°F\"): "))
			convertir_fahrenheit_a_celsius(fahrenheit)
			continuar_proceso = True
		except ValueError:
			print("\nPor favor, ingrese un número válido para la temperatura en Fahrenheit.")

def opciones_de_conversion_de_temperatura() -> int:
	opcion:int = 0
	continuar:bool = False
	while not continuar:
		print(" +------------------------------------------+\n",
		      "| Seleccione la conversión de temperatura: |\n",
		      "+------------------------------------------+")
		print(" | 1. Celsius a Fahrenheit                  |\n",
		      "| 2. Fahrenheit a Celsius                  |\n",
		      "| 3. Salir                                 |\n",
		      "+------------------------------------------+\n")
		try:
			opcion = int(input("Indique la opción deseada: "))
			continuar = True
		except ValueError:
			print("\nPor favor, ingrese un número válido.")
	return opcion

def convertir_temperatura():
	opcion:int
	continuar:bool = False
	while not continuar:
		opcion = opciones_de_conversion_de_temperatura()
		if opcion == 1:
			datos_celsius()
		elif opcion == 2:
			datos_fahrenheit()
		elif opcion == 3:
			print("\nSaliendo del convertidor de temperatura...")
			continuar = True
		else:
			print("\nOpción no válida. Por favor, intente de nuevo.")

def opciones_de_conversion_de_unidades() -> int:
	opcion:int = 0
	continuar:bool = False
	while not continuar:
		print(" +-----------------------------------+\n",
		      "| Seleccione el tipo de conversión: |\n",
		      "+-----------------------------------+")
		print(" | 1. Masa                           |\n",
		      "| 2. Longitud                       |\n",
		      "| 3. Tiempo                         |\n",
		      "| 4. Temperatura                    |\n",
		      "| 5. Salir                          |\n",
		      "+-----------------------------------+\n")
		try:
			opcion = int(input("Indique la opción deseada: "))
			continuar = True
		except ValueError:
			print("\nPor favor, ingrese un número válido.")
	return opcion

def convertir_unidades():
	opcion:int
	continuar:bool = False
	while not continuar:
		opcion = opciones_de_conversion_de_unidades()
		if opcion == 1:
			convertir_masa()
		elif opcion == 2:
			convertir_longitud()
		elif opcion == 3:
			convertir_tiempo()
		elif opcion == 4:
			convertir_temperatura()
		elif opcion == 5:
			print("\nSaliendo del convertidor de unidades. Gracias por usarlo.")
			continuar = True
		else:
			print("\nOpción no válida. Por favor, intente de nuevo.")

def main():
	print("Bienvenido al Convertidor de Unidades")
	convertir_unidades()

main()