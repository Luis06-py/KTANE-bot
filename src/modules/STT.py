import speech_recognition as sr
r = sr.Recognizer()

def grabar():
	# Loop en caso de que no se reconozca la voz
	while True:
		try:
			with sr.Microphone() as source2:
				r.adjust_for_ambient_noise(source2, duration=0.5)
				audio2 = r.listen(source2)
				texto = r.recognize_google(audio2, language="es-ES")
				return texto
		except sr.RequestError:
			print("No se pudo conectar al servicio de reconocimiento de voz.")
			return
		except sr.UnknownValueError:
			# print("No se pudo entender el audio.")
			return

def output(text):
	print ("Texto reconocido:", text)

if __name__ == "__main__":
	while True:
		text = grabar()
		if text:
			print("Texto reconocido:", text)
			output(text)
		else:
			print("No se reconoció ningún texto.")