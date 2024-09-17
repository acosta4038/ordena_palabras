import random

def cargar_palabras(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        palabras = archivo.read().splitlines()
    return palabras

def elegir_palabra_azar(palabras):
    return random.choice(palabras)

def desordenar_palabra(palabra):
    letras = list(palabra)
    random.shuffle(letras)
    return ''.join(letras)

def jugar(palabras):
    palabra = elegir_palabra_azar(palabras)
    palabra_desordenada = desordenar_palabra(palabra)
    
    print(f"Palabra desordenada: {palabra_desordenada}")
    
    intentos = 0
    while True:
        respuesta = input("Escribe la palabra correctamente: ")
        intentos += 1
        if respuesta.lower() == palabra.lower():
            print(f"¡Correcto! Lo lograste en {intentos} intento(s).")
            break
        else:
            print("Incorrecto. Intenta de nuevo.")

# Ejecutar el juego
if __name__ == "__main__":
    ruta_archivo = '/home/noahavila/Escritorio/programación/palabras_revueltas.lst' 
    palabras = cargar_palabras(ruta_archivo)
    
    jugar(palabras)