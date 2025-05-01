from modules.shared import shared_state
import json
# Módulo de "Quién va primero"
def buscar(prioridad, lista):
	for palabra in prioridad:
		if palabra in lista:
			return palabra
	return None

"""
PALABRAS CONFLICTIVAS
¿está? ¿ésta? esta ésta está
¿cómo?
¿dónde?
¿cuál?
¿esa?
¿qué?
ok okay
¿seguro?
"""

dicc = {
	"PRÓXIMA": 3, "VOY": 2, "PRIMERO": 6, "HAYA": 2, "VAYA": 6,
	"espera": 5, "RÁPIDO": 4, "MONITOR": 6, "ÚLTIMA": 3, "SÍ": 6,
	"HAY": 4, "OTRA": 5, "BIEN": 5, "PALABRA": 6, "NADA": 4,
	"LISTO": 4, "OKAY": 4, "BUENO": 1, "NO": 6, "ALLÁ": 5,
	"AHÍ": 3, "HALLA":6, "VALLA": 2, "OTRO": 6,
}

dicc2 = {
	"HAYA H":"HAYA", "HALLA H":"HAYA", "ALLÁ H":"HAYA",
	"VAYA V":"VAYA", "BAYA V":"VAYA",
	"VAYA B":"BAYA", "BAYA B":"BAYA",
	"AHÍ A":"AHÍ", "HAY A":"AHÍ",
	"AHÍ H":"HAY", "HAY H":"HAY",
	"OKAY L":"OKAY", "OKAY":"OK"
}

def idGrupo(texto):
	palabras = texto.upper().split()
	if len(palabras) == 2:
		cod = palabras[1]
		cod = cod[:1].upper()
		if palabras[0] + " " + cod in dicc2:
			return dicc2[palabras[0] + " " + cod]
		else:
			return False
	else:
		if palabras[0] == "HALLAR":
			return "HALLA"
		try:
			return palabras[0]
		except KeyError:
			return False


def identificar(texto):
	"""Esto va a quitar las tildes para que sea más maniobrable, si el TTS escribe como u cómo, etc"""
	tildes = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
	texto = texto.translate(tildes)
	ok_formas = {"OK", "OKEY", "OKAY"}
	partes = texto.upper().split("DESPUES")
	resultado = []
	for grupo in partes:
		grupo = grupo.split()
		if any(p in ok_formas for p in grupo):
			if "LARGO" in grupo:
				pal = "OKAY"
			else:
				pal = "OK"
		elif "TILDE" in grupo and grupo.count("TILDE") == 1:
			pal = "ÉSTA"
		elif "TILDE" in grupo and grupo.count("TILDE") == 2:
			pal = "ESTÁ"
		else:
			pal = grupo[0]
		if "PREGUNTA" in grupo:
			pal = f"¿{pal}?"
		resultado.append(pal)
	return resultado

def identificarPrimera(texto):
	texto = texto.upper()


def quienvaprimero(texto, grupo):
	"""Se debe identificar el botón y devolver la primera palabra de la lista. Formato: Palabra TILDE TILDE PREGUNTA Siguiente
	12
	34 Orden
	56"""
	grp = idGrupo(grupo)
	palabras = identificar(texto)
	print (grp)
	print (palabras)
	if not grp in dicc:
		return False
	pos = dicc[grp]
	word = palabras[pos-1]
	with open("data/primero.json", "r", encoding="UTF-8") as f:
		data = json.load(f)
	lista = data[word]
	resultado = buscar(lista, palabras)
	return f"Pulsa {resultado}"
