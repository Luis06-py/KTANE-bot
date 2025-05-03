from modules.shared import shared_state
# Módulo de Secuencia de cables

apariciones = {
	"R":{
		"1": ["C"], "2": ["B"], "3": ["A"], "4": ["A", "C"],
		"5": ["B"], "6": ["A", "C"], "7": ["A", "B", "C"], "8": ["A", "B"], "9": ["B"]
	},
	"A":{
		"1": ["B"], "2": ["A", "C"], "3": ["B"], "4": ["A"],
		"5": ["B"], "6": ["B", "C"], "7": ["C"], "8": ["A", "C"], "9": ["A"]
	},
	"N":{
		"1": ["A", "B", "C"], "2": ["A", "C"], "3": ["B"], "4": ["A", "C"],
		"5": ["B"], "6": ["B", "C"], "7": ["A", "B"], "8": ["C"], "9": ["C"]
	}

}

def incrementar(color):
	try:
		shared_state.data[color] += 1
	except:
		shared_state.data[color] = 2

def getCount(color):
	try:
		x = shared_state.data[color]
		return str(x)
	except:
		return "1"

def secuenciaCables(texto):
	"""Formato: color letra después, se tomará la primera letra (colores: R A N), conectado a fonético."""
	texto = texto.upper()
	secciones = texto.split("DESPUÉS")
	lista = []
	for parte in secciones:
		palabras = parte.strip().split()
		iniciales = [p[0] for p in palabras]
		lista.append(" ".join(iniciales))
	
	for cable in lista:
		col = cable[0]
		if not col in apariciones:
			print ("No superó la comprobación de errores")
			return False
	# Esto es una verificación de errores

	sec = ""

	for cable in lista:
		col = cable[0]
		cont = getCount(col)
		con = cable[2]
		incrementar(col)
		try:
			if con in apariciones[col][cont]:
				sec += " sí"
			else:
				sec += " no"
		except Exception as e:
			return False
	
	return sec[1:]