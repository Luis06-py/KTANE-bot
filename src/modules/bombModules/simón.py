from modules.shared import shared_state
# Módulo de Simón Dice
vocal = {
	"ROJO": ["AZUL", "AMARILLO", "VERDE"],
	"AZUL": ["ROJO", "VERDE", "ROJO"],
	"VERDE": ["AMARILLO", "AZUL", "AMARILLO"],
	"AMARILLO": ["VERDE", "ROJO", "AZUL"]
}

noVocal = {
	"ROJO": ["AZUL", "ROJO", "AMARILLO"],
	"AZUL": ["AMARILLO", "AZUL", "VERDE"],
	"VERDE": ["VERDE", "AMARILLO", "AZUL"],
	"AMARILLO": ["ROJO", "VERDE", "ROJO"]
}

def Simón(texto):
	"""Secuencia de Simón Dice, deben decirse lo(s) colores, y también asignado el número de serie"""
	sec = texto.upper().split()
	try:
		serial = shared_state.data["serial"]
	except:
		print ("NO HAY")
		return False
	try:
		fallos = int(shared_state.data["fallo"])
	except:
		fallos = 0
	voc = any(letra in "aeiouAEIOU" for letra in serial)
	sec2 = []
	if voc:
		for color in sec:
			sec2.append(vocal[color][fallos])
	else:
		for color in sec:
			sec2.append(noVocal[color][fallos])
	resultado = " ".join(sec2)
	return resultado