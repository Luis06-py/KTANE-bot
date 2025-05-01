from modules.STT import grabar
from modules.shared import shared_state
import pyttsx3, json

# Módulos de la bomba
from modules.bombModules.etiquetas import serialNumber, indicador, baterías, conectores
from modules.bombModules.cables import cables
from modules.bombModules.botón import botón, franja
from modules.bombModules.memoria import etapa1, etapa2, etapa3, etapa4, etapa5
from modules.bombModules.primero import quienvaprimero
from modules.bombModules.complicados import cablesComplicados

# Este es un BOT de KTANE (Keep Talking And Nobody Explodes) que utiliza TTS y STT para interactuar con el usuario.
# El bot ayuda al usuario a resolver el juego de KTANE, proporcionando pistas y consejos sobre cómo desactivar las bombas.

engine = pyttsx3.init()

def TTS(text):
	engine.say(text)
	try:
		print ("BOT: " + text)
	except:
		print ("BOT: ???") # Esto es un error, pero no se puede evitar, buscar el origen del error
	engine.runAndWait()

def STT(): # Reemplazar por STT (Speech to Text)
	texto = grabar() # input("Tú: ")
	if texto:
		if shared_state.data["calib"]:
			texto.replace("clave ","")
			texto.replace(" clave","")
			texto.replace("clave","")
		print ("Tú: " + texto)
		return texto
	else:
		print ("Tú: ???")
		return "???"

if __name__ == "__main__":
	with open("data/config.json", "r") as f:
		data = json.load(f)
	shared_state.data["calib"] = data["calib"] # La palabra de calibración es CLAVE
	print ("Iniciando bot de KTANE...")
	TTS("Estoy listo. ¿Qué necesitas?")
	while True:
		texto = STT()
		if not texto:
			TTS("No he entendido lo que has dicho.")
		else:
			if texto == "fallo":
				try:
					shared_state.data["fallo"] += 1
				except KeyError:
					shared_state.data["fallo"] = 1
				TTS("Hecho.")
			# Etiquetas
			elif texto == "número de serie":
				TTS("Dímelo.")
				serial = STT()
				if serial:
					serialNumber(serial)
					TTS("Hecho.")
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "indicador":
				TTS("Dímelo.")
				ind = STT()
				if ind:
					indicador(ind)
					TTS("Hecho.")
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "baterías":
				TTS("Dímelo.")
				bat = STT()
				if bat:
					y = baterías(bat)
					if y:
						TTS("Hecho.")
					else:
						TTS("No he entendido lo que has dicho.")
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "conectores":
				TTS("Dímelo.")
				con = STT()
				if con:
					conectores(con)
					TTS("Hecho.")
				else:
					TTS("No he entendido lo que has dicho.")
			
			# Módulos:
			elif texto == "módulo de cables":
				TTS("Dímelo.")
				cab = STT()
				if cab:
					TTS(cab)
					rec = cables(cab)
					TTS(rec)
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "módulo de botón" or texto == "módulo de botones":
				TTS("Color y texto.")
				texto = STT()
				bot = botón(texto)
				TTS(bot[0])
				if bot[1] == True:
					texto = STT()
					fr = franja(texto)
					TTS(fr)
			elif texto == "módulo de memoria":
				TTS("Dímelo.")
				mem = STT()
				if mem:
					et1 = etapa1(mem)
					if et1:
						TTS(et1)
						TTS("Etapa dos, dímelo.")
						mem2 = STT()
						et2 = etapa2(mem2)
						if et2:
							TTS(et2)
							TTS("Etapa tres, dímelo.")
							mem3 = STT()
							et3 = etapa3(mem3)
							if et3:
								TTS(et3)
								TTS("Etapa cuatro, dímelo.")
								mem4 = STT()
								et4 = etapa4(mem4)
								if et4:
									TTS(et4)
									TTS("Etapa cinco, dímelo.")
									mem5 = STT()
									et5 = etapa5(mem5)
									if et5:
										TTS(et5)
										TTS("Hecho.")
									else: # E5 devuelve False
										TTS("No he entendido lo que has dicho.")
								else: # E4 devuelve False
									TTS("No he entendido lo que has dicho.")
							else: # E3 devuelve False
								TTS("No he entendido lo que has dicho.")
						else: # E2 devuelve False
							TTS("No he entendido lo que has dicho.")
					else: # E1 devuelve False
						TTS("No he entendido lo que has dicho.")
				else: # E1
					TTS("No he entendido lo que has dicho.")
			elif texto == "módulo de primero":
				TTS("Dime el grupo.")
				gr = STT()
				if gr:
					TTS("Dime las palabras.")
					ide = STT()
					a = quienvaprimero(ide, gr)
					if a:
						TTS(a)
					else:
						TTS("No he entendido lo que has dicho.")
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "módulo de complicados":
				TTS("Dime los cables.")
				cab = STT()
				cb = cablesComplicados(cab)
				if cb:
					TTS(cb)
				else:
					TTS("No he entendido lo que has dicho")
				

			else:
				TTS("No he entendido lo que has dicho.")
			
				


		
	# texto = grabar()
	# TTS(texto)
