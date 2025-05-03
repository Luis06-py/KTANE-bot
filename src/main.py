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
from modules.bombModules.simón import Simón
from modules.bombModules.contraseñas import bruteforceCol, getCol
from modules.bombModules.teclados import identificarT
from modules.bombModules.morse import decodeMorse
from modules.bombModules.secuencia import secuenciaCables
from modules.bombModules.laberinto import resolverLaberinto
from modules.bombModules.perillas import getPerPos

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

def STT():
	texto = grabar() 
	#texto = input("Tú: ")
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
	with open("data/config.json", "r", encoding="UTF-8") as f:
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
			elif texto == "módulo de Simón":
				while True:
					TTS("Dime la secuencia")
					s = STT()
					if s == "fallo":
						try:
							shared_state.data["fallo"] += 1
						except KeyError:
							shared_state.data["fallo"] = 1
						TTS("Hecho.")
					elif s == "salir":
						TTS("Salir.")
						break
					else:
						sim = Simón(s)
						if sim:
							TTS(sim)
						else:
							TTS("No he entendido lo que has dicho")
			elif texto == "módulo de contraseña" or texto == "módulo de contraseñas":
				for i in range(1, 6):
					TTS("Dí la secuencia.")
					s = STT()
					if s == "hecho":
						break
					else:
						getCol(s, i)
				res = bruteforceCol()
				if res:
					TTS("La contraseña es "+res)
				else:
					TTS("No he podido.")
			elif texto == "módulo de teclados" or texto == "módulo de teclados":
				TTS("Dí los símbolos.")
				s = STT()
				if s:
					r = identificarT(s)
					if r:
						TTS(r)
					else:
						TTS("Símbolos incorrectos.")
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "módulo de morse" or texto == "módulo de Morse":
				TTS("Dí la secuencia.")
				m = STT()
				if m:
					f = decodeMorse(m)
					if f:
						TTS(f)
					else:
						TTS("No he entendido lo que has dicho.")
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "módulo de secuencia":
				while True:
					TTS("Dí la secuencia.")
					s = STT()
					if s == "salir":
						TTS("Hecho.")
						break
					else:
						se = secuenciaCables(s)
						if se:
							TTS(se)
						else:
							TTS("No he entendido lo que has dicho.")
			elif texto == "módulo de laberinto" or texto == "módulo del laberinto":
				TTS("Círculo verde.")
				c = STT()
				TTS("Cuadrado.")
				ori = STT()
				TTS("Triángulo.")
				des = STT()
				if c and ori and des:
					ruta = resolverLaberinto(c, ori, des)
					if ruta:
						TTS("Allá voy.")
						for i in range(0, len(ruta), 3):
							subgrupo = ruta[i:i+3]
							tad = ' '.join(subgrupo)
							TTS(tad)
					else:
						TTS("No he entendido lo que has dicho.")
				else:
					TTS("No he entendido lo que has dicho.")
			elif texto == "módulo de perillas":
				TTS("Dí las luces")
				p = STT()
				if p:
					pos = getPerPos(p)
					if pos:
						TTS(pos)
					else:
						TTS("No he entendido lo que has dicho.")
				else:
					TTS("No he entendido lo que has dicho")
			# Fin de comandos
			elif texto == "salir":
				TTS("Hasta pronto.")
				break
			else:
				TTS("No he entendido lo que has dicho.")