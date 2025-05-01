from modules.shared import shared_state
# Reconocimiento de etiquetas (número de serie, color, etc.)
def palabraANumero(palabra):
	listNumeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
	if palabra.lower() in listNumeros:
		return str(listNumeros.index(palabra.lower()))
	return palabra[0].upper()

def serialNumber(texto):
	"""El número de serie puede contener letras y números, el último siempre es un número."""
	palabras = texto.strip().split()
	abrv = "".join([palabraANumero(palabra) for palabra in palabras])
	shared_state.data["serial"] = abrv

def indicador(texto):
	"""Los posibles indicadores son: SND, CLR, CAR, IND, FRQ, SIG, NSA, MSA, TRN, BOB, FRK, esto se hará con fonética (Alfa delta, etc. usando "HECHO" para separar)"""
	#indicadores = ["SND", "CLR", "CAR", "IND", "FRQ", "SIG", "NSA", "MSA", "TRN", "BOB", "FRK"]
	palabras = texto.split()
	ind = []
	for i in range(0, len(palabras), 4):
		bloque = palabras[i:i+4]
		if len(bloque) == 4:
			bloque.pop()
		iniciales = ''.join([palabra[0].upper() for palabra in bloque[:3]])
		if iniciales:
			ind.append(iniciales)
	# Voy a omitir la comprobación de errores
	shared_state.data["indicador"] = ind

def baterías(texto):
	"""Las baterías pueden ser AA o D, formato: cantidad_A cantidad_D"""
	palabras = texto.strip().split()
	if len(palabras) != 3:
		return False
	try:
		shared_state.data["baterías"] = {"A": palabraANumero(palabras[0]), "D": palabraANumero(palabras[2])}
		return True
	except:
		return False

def conectores(texto):
	"""Los conectores pueden ser: DVI (DVI-D) paralelo PS (PS/2) RJ (RJ-45) serial stereo/Estereo (Estéreo RCA)"""
	conectores = ["DVI", "PAR", "PS", "RJ", "SER", "EST"]
	con = []
	palabras = texto.strip().split()
	for palabra in palabras:
		if palabra.upper() == "ESTÉREO" or palabra.upper() == "STEREO":
			con.append("EST")
		elif palabra.upper() == "PARALELO":
			con.append("PAR")
		elif palabra.upper() == "SERIAL":
			con.append("SER")
		elif palabra.upper() in conectores:
			con.append(palabra.upper())
	shared_state.data["conectores"] = con
