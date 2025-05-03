# from modules.shared import shared_state
# Módulo exigente de de perilllas

dir = {
	("001011111101", "101010011011"): "Arriba",
	("011001111101", "101010010001"): "Abajo",
	("000010100111", "000010000110"): "Izquierda",
	("101111111010", "101100111010"): "Derecha",
}

def getPerPos(texto):
	"""Se deben decir las posiciones de ENCENDIDO o APAGADO"""
	palabras = ''.join(
		'1' if palabra.lower() == 'encendido' else '0'
		for palabra in texto.split()
	)
	direccion = None
	for clave, direccion in dir.items():
		if palabras in clave:
			return direccion
	if not direccion:
		return False