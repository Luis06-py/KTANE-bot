from modules.shared import shared_state
# Módulo del gran botón

def botón(content):
	"""El botón puede ser de varios colores y con un texto determinado, se deben identificar las pilas e indicadores"""
	content = content.strip().split()
	if len(content) != 2:
		return "No he entendido lo que has dicho.", False
	texto = content[1]
	color = content[0]
	texto = texto.upper()
	color = color.upper()
	try:
		b = shared_state.data["baterías"]
		i = shared_state.data["indicador"]
	except:
		return "Necesito el número de baterías e indicadores.", False
	if color == "rojo" and texto == "ABORTAR":
		return "Mantén el botón, ¿color de franja?", True
	elif texto == "DETONAR":
		if int(b["A"]) + int(b["D"]) >= 1:
			return "Pulsa y suelta.", False
	elif color == "BLANCO":
		if "CAR" in i:
			return "Mantén el botón, ¿número de franja?", True
	elif int(b["A"]) + int(b["D"]) >= 2 and "FRK" in i:
		return "Pulsa y suelta.", False
	elif color == "AMARILLO" or (color == "ROJO" and texto == "MANTENER"): # Se han juntado dos instrucciones para simplificar
		return "Mantén el botón, ¿color de franja?", True
	else:
		return "Mantén el botón, ¿color de franja?", True
	

def franja(color):
	"""El color de la franja puede ser azul, blanca, amarilla o de otro color"""
	color = color.upper()
	if color == "AZUL":
		return "Suelta cuando haya un 4."
	elif color == "AMARILLO":
		return "Suelta cuando haya un 5."
	else: # Blanco o otro color
		return "Suelta cuando haya un 1."
	