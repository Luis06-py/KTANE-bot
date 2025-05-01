from modules.shared import shared_state
# Módulo de cables

def cables(texto):
	"""Los cables pueden ser Rojo, Azul, Blanco, Amarillo, Negro"""
	cables = texto.upper().split()
	cantidad = len(cables)
	
	if cantidad == 3:
		if not "ROJO" in cables:
			return "Corta el segundo cable."
		elif cables[2] == "BLANCO":
			return "Corta el último cable."
		elif cables.count("AZUL") > 1:
			return "Corta el último cable azul."
		else:
			return "Corta el último cable."
	elif cantidad == 4:
		if cables.count("ROJO") > 1:
			try:
				serial = shared_state.data["serial"]
				if serial[-1].isdigit() and int(serial[-1]) % 2 != 0: # Impar
					return "Corta el último cable rojo."
			except KeyError:
				return "Necesito el número de serie."
			except Exception as e:
				return e
		if cables[3] == "AMARILLO" and not "ROJO" in cables:
			return "Corta el primer cable."
		elif cables.count("AZUL") == 1:
			return "Corta el primer cable."
		elif cables.count("AMARILLO") > 1:
			return "Corta el último cable."
		else:
			return "Corta el segundo cable."
	elif cantidad == 5:
		if cables[4] == "NEGRO":
			try:
				serial = shared_state.data["serial"]
				if serial[-1].isdigit() and int(serial[-1]) % 2 != 0:
					return "Corta el cuarto cable."
			except KeyError:
				return "Necesito el número de serie."
		if cables.count("ROJO") == 1 and cables.count("AMARILLO") > 1:
			return "Corta el primer cable."
		elif not "NEGRO" in cables:
			return "Corta el segundo cable."
		else:
			return "Corta el primer cable."
	elif cantidad == 6:
		if not "AMARILLO" in cables:
			try:
				serial = shared_state.data["serial"]
				if serial[-1].isdigit() and int(serial[-1]) % 2 != 0:
					return "Corta el cuarto cable."
			except KeyError:
				return "Necesito el número de serie."
		if cables.count("AMARILLO") == 1 and cables.count("BLANCO") > 1:
			return "Corta el cuarto cable."
		elif not "ROJO" in cables:
			return "Corta el último cable."
		else:
			return "Corta el cuarto cable."
	else:
		return "No puedo ayudar con eso."