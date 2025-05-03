#from modules.shared import shared_state
import re
# Módulo de Código Morse

morse_a_texto = {
	".-": "A", "-...": "B", "-.-.": "C",
	"-..": "D", ".": "E", "..-.": "F",
	"--.": "G", "....": "H", "..": "I",
	".---": "J", "-.-": "K", ".-..": "L",
	"--": "M", "-.": "N", "---": "O",
	".--.": "P", "--.-": "Q", ".-.": "R",
	"...": "S", "-": "T", "..-": "U",
	"...-": "V", ".--": "W", "-..-": "X",
	"-.--": "Y", "--..": "Z"
}

frecuencias = {
	'FRENOFRENO': '3.505 MHZ', 
	'HONGOSHONGOS': '3.515 MHZ', 
	'LENTESLENTES': '3.522 MHZ', 
	'BIELABIELA': '3.532 MHZ', 
	'RESTARESTA': '3.535 MHZ', 
	'TRATOTRAO': '3.542 MHZ', 
	'VOLARVOLAR': '3.545 MHZ', 
	'VUELTAVUELTA': '3.552 MHZ', 
	'LLAVESLLAVES': '3.555 MHZ', 
	'TABLATABLA': '3.565 MHZ', 
	'TRONCOTRONCO': '3.572 MHZ', 
	'BOMBABOMBA': '3.575 MHZ', 
	'SANTOSSANTOS': '3.582 MHZ', 
	'SENSOSENSO': '3.592 MHZ', 
	'RATASRATAS': '3.595 MHZ', 
	'TRENESTRENES': '3.600 MHZ'} 
# Se repite para que funcionen las posibilidades de REGEX
# Ejemplos para "TRENES"
# *TREN*
# *ENES*
# *RENE*
# *STRE*

def traducir(morse_lista):
    return [morse_a_texto.get(simbolo, '?') for simbolo in morse_lista]

# punto DESPUÉS punto punto punto DESPUÉS punto línea punto punto DESPUÉS punto
def decodeMorse(texto): 
	"""Se debe indicar una serie de números (4 mínimo) separado de DESPUÉS."""
	print (texto)
	texto = texto.upper()
	texto = texto.replace('PUNTO', '.').replace('LÍNEA', '-').replace('GUION', '-')
	lista = texto.split('DESPUÉS')
	lista = [item.strip().replace(' ', '') for item in lista]
	lista = traducir(lista)
	regex = ''.join([re.escape(c) for c in lista])
	regex = f".*{regex}.*"
	print (regex)
	for clave in frecuencias.keys():
		if re.search(regex, clave):
			x = frecuencias[clave]
			return x
	return False

	
