from modules.shared import shared_state
# Reconocimiento de etiquetas (número de serie, color, etc.)
def palabras_a_numeros(texto):
    listNumeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    resultado = ""
    for palabra in texto.lower().split():
        if palabra.isdigit():
            resultado += palabra
        elif palabra in listNumeros:
            resultado += str(listNumeros.index(palabra))
    return resultado

def etapa1(texto):
	"""Primera etapa del módulo de memoria. El primer número es grande."""	
	palabras = palabras_a_numeros(texto)
	if len(palabras) != 5:
		return False
	shared_state.data["etapa1"] = "-"+palabras[:1]
	shared_state.data["g1"] = palabras[0]
	if palabras[0] == "1":
		shared_state.data["pulsado1"] = palabras[1]
		shared_state.data["pos1"] = "1"
		return f"Pulsa el {palabras[1]}."
	elif palabras[0] == "2":
		shared_state.data["pulsado1"] = palabras[2]
		shared_state.data["pos1"] = "2"
		return f"Pulsa el {palabras[2]}."
	elif palabras[0] == "3":
		shared_state.data["pulsado1"] = palabras[3]
		shared_state.data["pos1"] = "3"
		return f"Pulsa el {palabras[3]}."
	elif palabras[0] == "4":
		shared_state.data["pulsado1"] = palabras[4]
		shared_state.data["pos1"] = "4"
		return f"Pulsa el {palabras[4]}."
	else:
		return False
	
def etapa2(texto):
	"""Segunda etapa del módulo de memoria. El primer número es grande."""	
	palabras = palabras_a_numeros(texto)
	if len(palabras) != 5:
		return False
	shared_state.data["etapa2"] = "-"+palabras[:1]
	shared_state.data["g2"] = palabras[0]
	if palabras[0] == "1":
		shared_state.data["pulsado2"] = "4"
		shared_state.data["pos2"] = palabras.index("4")
		return f"Pulsa el 4."
	elif palabras[0] == "2": # Misma posición etapa 1
		pos = shared_state.data["pos1"]
		pulsar = palabras[int(pos)]
		shared_state.data["pulsado2"] = pulsar
		shared_state.data["pos2"] = pos
		return f"Pulsa el {pulsar}."
	elif palabras[0] == "3":
		shared_state.data["pulsado2"] = palabras[1]
		shared_state.data["pos2"] = "1"
		return f"Pulsa el {palabras[1]}."
	elif palabras[0] == "4": #Misma posición etapa 1
		shared_state.data["pulsado4"] = palabras[4]
		pos = shared_state.data["pos1"]
		pulsar = palabras[int(pos)]
		shared_state.data["pulsado2"] = pulsar
		shared_state.data["pos2"] = pos
		return f"Pulsa el {pulsar}."
	else:
		return False
	
def etapa3(texto):
	"""Tercera etapa del módulo de memoria. El primer número es grande."""	
	palabras = palabras_a_numeros(texto)
	if len(palabras) != 5:
		return False
	shared_state.data["etapa3"] = "-"+palabras[:1]
	shared_state.data["g3"] = palabras[0]
	if palabras[0] == "1": # Misma etiqueta etapa 2
		shared_state.data["pulsado3"] = shared_state.data["pulsado2"]
		shared_state.data["pos3"] = palabras.index(str(shared_state.data["pulsado2"]))
		return f"Pulsa el {shared_state.data["pulsado3"]}."
	elif palabras[0] == "2": # Misma posición etapa 1
		shared_state.data["pulsado3"] = shared_state.data["pulsado1"]
		shared_state.data["pos3"] = palabras.index(str(shared_state.data["pulsado1"]))
		return f"Pulsa el {shared_state.data["pulsado3"]}."
	elif palabras[0] == "3":
		shared_state.data["pulsado3"] = palabras[3]
		shared_state.data["pos3"] = "3"
		return f"Pulsa el {palabras[3]}."
	elif palabras[0] == "4":
		shared_state.data["pulsado3"] = "4"
		shared_state.data["pos3"] = str(palabras.index("4"))
		return f"Pulsa el 4."
	else:
		return False

def etapa4(texto):
	"""Cuarta etapa del módulo de memoria. El primer número es grande."""	
	palabras = palabras_a_numeros(texto)
	if len(palabras) != 5:
		return False
	shared_state.data["etapa4"] = "-"+palabras[:1]
	shared_state.data["g4"] = palabras[0]
	if palabras[0] == "1": # Misma posición etapa 1
		shared_state.data["pulsado4"] = palabras[int(shared_state.data["pos1"])]
		shared_state.data["pos4"] = palabras.index(str(shared_state.data["pulsado4"]))
		return f"Pulsa el {shared_state.data["pulsado4"]}."
	elif palabras[0] == "2":
		shared_state.data["pulsado4"] = palabras[1]
		shared_state.data["pos4"] = "1"
		return f"Pulsa el {palabras[1]}."
	elif palabras[0] == "3": # Misma posición etapa 2
		shared_state.data["pulsado4"] = palabras[int(shared_state.data["pos2"])]
		shared_state.data["pos4"] = palabras.index(str(shared_state.data["pulsado4"]))
		return f"Pulsa el {shared_state.data["pulsado4"]}."
	elif palabras[0] == "4": # Misma posición etapa 2
		shared_state.data["pulsado4"] = palabras[int(shared_state.data["pos2"])]
		shared_state.data["pos4"] = palabras.index(str(shared_state.data["pulsado4"]))
		return f"Pulsa el {shared_state.data["pulsado4"]}."
	else:
		return False
	
def etapa5(texto):
	"""Quinta etapa del módulo de memoria. El primer número es grande."""	
	# Es redundante guardar la etapa 5, pero lo hago por si acaso
	palabras = palabras_a_numeros(texto)
	if len(palabras) != 5:
		return False
	shared_state.data["etapa5"] = "-"+palabras[:1]
	shared_state.data["g5"] = palabras[0]
	if palabras[0] == "1": # Misma etiqueta etapa 1
		shared_state.data["pulsado5"] = shared_state.data["pulsado1"]
		shared_state.data["pos5"] = palabras.index(str(shared_state.data["pulsado5"]))
		return f"Pulsa el {shared_state.data["pulsado5"]}."
	elif palabras[0] == "2": # Misma etiqueta etapa 2
		shared_state.data["pulsado5"] = shared_state.data["pulsado2"]
		shared_state.data["pos5"] = palabras.index(str(shared_state.data["pulsado5"]))
		return f"Pulsa el {shared_state.data["pulsado5"]}."
	elif palabras[0] == "3": # Misma etiqueta etapa 4
		shared_state.data["pulsado5"] = shared_state.data["pulsado4"]
		shared_state.data["pos5"] = palabras.index(str(shared_state.data["pulsado5"]))
		return f"Pulsa el {shared_state.data["pulsado5"]}."
	elif palabras[0] == "4": # Misma etiqueta etapa 3
		shared_state.data["pulsado5"] = shared_state.data["pulsado3"]
		shared_state.data["pos5"] = palabras.index(str(shared_state.data["pulsado5"]))
		return f"Pulsa el {shared_state.data["pulsado5"]}."
	else:
		return False