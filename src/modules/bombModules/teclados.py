from modules.shared import shared_state
import json

sec = {
	"A":["1", "6", "11", "16", "21", "26", "15"],
	"B":["2", "1", "15", "17", "18", "26", "24"],
	"C":["27", "7", "17", "22", "23", "11", "18"],
	"D":["3", "8", "13", "21", "22", "24", "9"],
	"E":["4", "9", "13", "19", "8", "25", "20"],
	"F":["3", "2", "10", "12", "4", "14", "5"]
}

# Módulo del teclado (jeroglíficos)
def identificarT(cadena):
	"""Esto sirve para identificar una cadena de cuatro símbolos, siendo SÍMBOLO después SÍMBOLO"""
	partes = cadena.upper().split("DESPUÉS")
	partes = [parte.strip() for parte in partes]
	with open("data/config.json", "r", encoding="UTF-8") as f:
		data = json.load(f)
	sím = []
	try:
		for parte in partes:
			sím.append(data["símbolos"][parte])
	except:
		return False
	
	opor = list(sec.keys())
	for símbolo in sím:
		for clave in list(opor):
			if símbolo not in sec[clave]:
				opor.remove(clave)

	if not len(opor) == 1:
		return False
	
	
	cadCorr = sec[opor[0]]
	sam = data["símbolos"]
	invertido = {v: k for k, v in sam.items()}
	# sím
	
	ordenado = sorted(sím, key=lambda x: cadCorr.index(x) if x in cadCorr else len(cadCorr))
	resultado = [invertido.get(elem, "") for elem in ordenado]
	resultado_str = " DESPUÉS ".join(resultado)
	return resultado_str.lower()
	
# bravo mayúscula después euro después pieza después cara
	
