# Keep Talking And Nobody Explodes BOT
Este proyecto es un bot diseñado para asistir en el juego *Keep Talking and Nobody Explodes* (KTANE). Su objetivo es proporcionar ayuda rápida y precisa para resolver los módulos del juego.

## Características
- Asistencia en tiempo real para resolver módulos.
- Compatible con múltiples módulos del juego.
- Interfaz fácil de usar.

## Requisitos
- Python 3.8 o superior.
- Librerías necesarias (ver archivo `requirements.txt`).

## Instalación
1. Clona este repositorio:

2. Instala las dependencias:
	```bash
	pip install -r requirements.txt
	```

## Ejemplo de uso
Primero configura el archivo JSON.
```json
{"calib": true}
```
En el caso de que el micrófono no reconozca la primera o última palabra, se puede decir "clave" y el bot descartará la palabra, por ejemplo si se dice **clave hola mundo**, interpretará **hola mundo**, pero si interpreta "clave", el bot eliminará la palabra.

Ejecuta el bot con el siguiente comando:
```bash
python main.py
```
Dentro el usuario se comunicará con el Bot y deberá proporcionarle indicaciones sobre los módulos para desactivar las bombas.
Se usará el abecedario fonético (es decir, Alpha, Bravo, Charlie... pero en español). Módulos:

### Etiquetado
#### Número de serie
- Comando: número de serie
- Se debe indicar el número de serie después del comando de voz, por ejemplo "Alfa Bravo Delta Hotel Tango Siete".
- No es necesario dar el número entero, debido a que solo importa si hay vocales y el último número, con decir "alfa siete" valdría.

#### Indicador
- Comando: indicador
- Se deben indicar los indicadores que tienen tres palabras, debe decirse las tres letras y un "hecho", por ejemplo "Sierra Noviembre Delta Hecho Charlie Alfa Romeo Hecho" equivale a SND y CAR. En el caso de que no haya ninguno, se deberá decir cualquier cosa (por ejemplo Noviembre Uniforme Lima Hecho)

#### Baterías
- Comando: baterías
- Se debe decir dos números siendo "número1 luego número2", el primero correspondiente a la cantidad de baterías AA y el segundo a las baterías D

#### Conectores
- Comando: conectores
- Se deben indicar los conectores que tiene la bomba, se deben indicar de esta forma: DVI (DVI-D), Paralelo, PS (PS/2), RJ (RJ-45), Serial, y Estéreo (o Stereo)

### Módulo de cables
- Comando: número de cables
- Se deben decir los colores de los cables en el orden que aparecen. El bot repetirá lo que has dicho para detectar errores.

### Módulo de El Botón
- Comando: módulo de botón/módulo de botones
- Se deberá indicar el color del botón y el texto. Es necesario identificar baterías o indicadores. Si el botón debe ser mantenido, preguntará al usuario por el color de la franja, que se deberá indicar

### Módulo de memoria
- Comando: módulo de memoria
- Se deberá indicar primero el número grande y después en orden los cuatro números

### Módulo de Quién Va Primero
- Comando: módulo de primero
- Se debe indicar primero el grupo y después las palabras en este orden

|   |   |
|---|---|
| 1 | 2 |
| 3 | 4 |
| 5 | 6 |

#### Indicando el grupo
- Para indicar el grupo, se deben seguir unas reglas, esto es para evitar accidentes en palabras homófonas. Si se ve una letra se debe usar el abecedario fonético.

| Clave    | Valor  |
|----------|--------|
| HAYA H   | HAYA   |
| VAYA V   | VAYA   |
| VAYA B   | BAYA   |
| AHÍ A    | AHÍ    |
| AHÍ H    | HAY    |
| OKAY L   | OKAY   |
| OKAY     | OK     |
| HALLAR   | HALLA  |

- Nótese que esto es así porque el STT puede confundir *Baya* con *Valla*, entre otros.

#### Indicando las palabras
- Las palabras se deben indicar con este formato:
- Palabra **después** palabra *pregunta* **después**...
- En el caso de *esta*, se puede confundir con las tildes, para ello se debe decir **TILDE** dependiendo de su posición

| Clave            | Valor |
|------------------|-------|
| ESTA             | ESTA  |
| ESTA TILDE       | ÉSTA  |
| ESTÁ TILDE TILDE | ESTÁ  |

- En el caso de interrogaciones, se debe decir "PREGUNTA" al final

### Módulo de cables complicados
- Comando: módulo de complicados.
- Se deben indicar las características del cable (Estrella, Luz, Rojo y/o Azul) y después decir **después**.
- Deben estar indicadas las baterías y los puertos.

## Salida
```bash
$ python main.py
Iniciando bot de KTANE...
BOT: Estoy listo. ¿Qué necesitas?
Tú: conectores
BOT: Dímelo.
Tú: paralelo DVI estéreo
BOT: Hecho.
Tú: baterías
BOT: Dímelo.
Tú: dos luego uno
BOT: Hecho.
Tú: indicador
BOT: Dímelo.
Tú: noviembre uniforme Lima hecho
BOT: Hecho.
Tú: módulo de botón
BOT: Color y texto.
Tú: rojo mantener
BOT: Mantén el botón, ¿color de franja?
Tú: blanco
BOT: Suelta cuando haya un 1.
```

## Cosas a añadir:
- [ ] Módulo de teclados (jeroglíficos)
- [ ] Módulo de Simón Dice
- [ ] Módulo de Código Morse
- [ ] Módulo de Secuencia de Cables
- [ ] Módulo de Laberinto
- [ ] Módulo de Módulo de Contraseñas
- [ ] Módulo exigente de Perillas

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo [`LICENSE`](./LICENSE) para más detalles.