"""Requisitos básicos:
Cuál es el mínimo de largo de palabra?
Cuál es el máximo de largo de palabra?
Cuál es el largo promedio de palabra (redondeado a 1 entero)?
Que el programa elija una palabar al azar.
Que la muestre en mayúsculas en su orden natural y la muestre desordenada."""

"""NUEVOS REQUERIMIENTOS:

1- Dificultades: facil y dificil. 
Mayor cantidad de letras por nivel y mayor nivel de puntos por dificultad.

2- Intentos maximos, 5 por ejemplo. Mayor cantidad de puntos mientras se utilicen menos intentos.

3- Tematica de palabras, que haya 10 archivos diferentes por ejemplo. 
Que cada uno tenga una tematica con palabras diferentes.
Por ejemplo: futbol, países, comida."""

import random

def desodenar_palabras(letras_desordenar): 
    """Este def se encarga de desordena las palabras aleatorias"""   
    palabra_inicial = letras_desordenar
    letras_desordenar = list(letras_desordenar) 
    random.shuffle(letras_desordenar)
    letras_desordenar == "".join(letras_desordenar)
    print(letras_desordenar)
    a_jugar(palabra_inicial)

def ingresar_nombre():
    print("Bienvenidos al juego")
    if nombre == "":
        nombre = input("Ingresar tu nombre o apodo: ")
        print("Incorrecto, ingrese un nombre o apodo") 
    
        
def a_jugar(palabra_inicial): 
    """Este def verifica si la palabra ingresada es correcta o no"""
    intentos = 5
    print("Intenta   ordenar la palabra desordenada, solo tienes 5 intentos ")
    while intentos != 0:
        ordenar_la_palabara = input("Ingresar la palabra ordenada: ")
        if ordenar_la_palabara == palabra_inicial:
            print("Muy bien, Felicitaciones Ganaste")
            break
        else:
            intentos = intentos -1
            print(f"Palabra incorrecta, intentos restantes: {intentos}")
        if intentos == 0:
            print(f"Has perdido, la palabra correcta es: {palabra_inicial}")
            print("Suerte la proxima")

    
def promedio_de_palabras(promedio):
    """Calcula el promedio de las palabras"""
    longitud_palabras = 86061
    largo_palabra = len(palabra_inicial)
    promedio = longitud_palabras / largo_palabra
    promedio = round(promedio)
    print (f"El promedio de la palabra es: {promedio}") 

#cuerpo principal 
ruta_de_archivo = "/home/michael04/Descargas/spanish.lst"
lista_de_palabra = open(ruta_de_archivo, "r") 
largo_maximo_palabra = 11
largo_minimo_palabra = 2
promedio = 0

ingresar_nombre()

for palabra in lista_de_palabra:
    lista_de_palabra = list(lista_de_palabra)
    lista_de_palabra = lista_de_palabra
    if len(palabra) <= largo_maximo_palabra:
        palabra_inicial = random.choice(lista_de_palabra)
        palabra_inicial = palabra_inicial.strip()
        print(f"La palabra es {palabra_inicial.upper()}")
        promedio_de_palabras(promedio)
        #Esta toma el promedio de la palabra
        desodenar_palabras(palabra_inicial)
        #Esta toma la palabra y la desordena
       



