from modules.STT import grabar
import pyttsx3

# Módulos de la bomba
from modules.bombModules.etiquetas import serialNumber

# Este es un BOT de KTANE (Keep Talking And Nobody Explodes) que utiliza TTS y STT para interactuar con el usuario.
# El bot ayuda al usuario a resolver el juego de KTANE, proporcionando pistas y consejos sobre cómo desactivar las bombas.

engine = pyttsx3.init()

def TTS(text):
	engine.say(text)
	print ("BOT: " + text)
	engine.runAndWait()

def STT():
	texto = grabar()
	if texto:
		print ("Tú:" + texto)
		return texto
	else:
		print ("Tú: ???")
		return None

if __name__ == "__main__":
	texto = grabar()
	TTS(texto)