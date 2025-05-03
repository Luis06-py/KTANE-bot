from modules.shared import shared_state
# Módulo de ejemplo para el juego de la bomba
# Este módulo contiene funciones de ejemplo que no hacen nada en particular.

def funcióndeEjemplo(texto):
	"""Esta es una función de ejemplo que no hace nada."""
	# Aquí puedes poner el código que quieras
	palabras = texto.strip().split()
	shared_state.data["dato"] = palabras # Almacena el dato en el shared_state
	# Puedes hacer lo que quieras con el dato, por ejemplo, imprimirlo