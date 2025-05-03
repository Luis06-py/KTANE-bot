from modules.shared import shared_state
import itertools, re
# Módulo de contraseñas

contraseñas = ['ABAJO', 'ALTAR', 'BAJAR', 'BOMBA', 'BUENO', 'CABLE', 'CERCA', 'CORTO', 'DELTA', 'DONDE', 'ESTAR', 'FALTA', 'GOMAS', 'GRASA', 'HOGAR', 'HUESO', 'LISTO', 'LUGAR', 'MAGIA', 'MIEDO', 'MUNDO', 'NUNCA', 'OTROS', 'PASAR', 'PASOS', 'PERCA', 'PLATA', 'PUNTO', 'QUESO', 'RONDA', 'SALTO', 'SUENA', 'TASAR', 'TRABA', 'VALOR']

def getCol(texto, num):
	"""Almacenar en los datos una columna"""
	palabras = texto.strip().split()
	palabras = [p[0].upper() for p in texto.strip().split()]
	try:
		shared_state.data["cont"][str(num)] = palabras
	except KeyError:
		shared_state.data["cont"] = {}
		shared_state.data["cont"][str(num)] = palabras

def bruteforceCol():
	"""Fuerza bruta para identificar la contraseña. En el caso de que haya dos posibilidades, se dirá la primera."""
	cols = len(shared_state.data["cont"])
	if cols >= 2:
		columns = [shared_state.data["cont"][str(i)] for i in range(1, cols + 1)]
		regex = ''.join(f"[{''.join(c)}]" for c in columns)
		regex += '.' * (5 - cols)
		# print (regex) Por si se quiere ver la secuencia REGEX
		for password in contraseñas:
			if re.fullmatch(regex, password):
				return password
	return False

