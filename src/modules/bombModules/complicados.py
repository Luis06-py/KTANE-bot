from modules.shared import shared_state
# Módulo de cables complicados

# Estrella Rojo Azul LED
dic = {
	"----":"C",
	"E---":"C",
	"ER--":"C",
	"E-A-":"N",
	"ERA-":"P",
	"ERAL":"N",
	"E-AL":"P",
	"E--L":"B",
	"ER-L":"B",
	"-R--":"S",
	"-RA-":"S",
	"--A-":"S",
	"---L":"N",
	"--AL":"P",
	"-RAL":"S",
	"-R-L":"B"
}

def transform(ins):
	if ins == "C":
		return "corta"
	elif ins == "N":
		return "no"
	elif ins == "S":
		try:
			ser = shared_state.data["serial"]
			if ser %2 != 0:
				return "corta"
			else:
				return "no"
		except:
			return False
	elif ins == "P":
		try:
			con = shared_state.data["conectores"]
			if "PAR" in con:
				return "corta"
			else:
				return "no"
		except:
			return False
	elif ins == "B":
		try:
			bat = shared_state.data["baterías"]
			count = int(bat["A"])
			if count > 1:
				return "corta"
			else:
				return "no"
		except:
			return False

def cablesComplicados(texto):
	"""Esta es la funcion de cables complicados"""
	texto = texto.upper()
	cables = texto.strip().split("DESPUÉS")
	cab = []
	for cable in cables:
		x = cable.strip()
		cod = ["-", "-", "-", "-"]
		if "ESTRELLA" in x:
			cod[0] = "E"
		if "ROJO" in x:
			cod[1] = "R"
		if "AZUL" in x:
			cod[2] = "A"
		if "LUZ" in x:
			cod[3] = "L"
		cod = ''.join(cod)
		cab.append(cod)
	ord = []
	for cable in cab:
		ord.append(transform(dic[cable]))
	if False in cab:
		return False
	else:
		resultado = ' '.join(ord)
		return resultado