"""
Reglas del juego:

El jugador puede elegir entre las temáticas disponibles.
Cada temática será un archivo que contiene una lista de palabras.

Requisitos del juego:

Los archivos de palabras deben ser de texto plano, una palabra por linea y deben tener la extensión .lst
Por cada jugada se debe guardar en puntajes.csv una linea con 6 datos: jugador, tematica, palabra1, palabra2, palabra3, puntos.
Cuando termina el juego se debe mostrar un ranking ordenado por puntos con las 10 primeras posiciones: Puesto, Jugador, Tema, Puntaje

"""

import random
import time
import threading

def desordenar_palabra(palabra_a_desordenar):
    """Esta def se encarga de desordenar las palabras aleatorias y que no se queden identicas a la original."""

    palabra_original = palabra_a_desordenar
    palabra_a_desordenar = list(palabra_a_desordenar)
    random.shuffle(palabra_a_desordenar)
    palabra_a_desordenar = "".join(palabra_a_desordenar)
    while palabra_a_desordenar == palabra_original:
        palabra_a_desordenar = list(palabra_a_desordenar)
        random.shuffle(palabra_a_desordenar)
    print(f"Esta es la palabra desordenada {palabra_a_desordenar}\n")
    te_toca(palabra_original)

def te_toca(palabra_original):
    """Esta def se encarga de verificar si la palabra que ingreso el usuario es correcta o no."""

    intentos = 4
    print("¡Intenta armar que palabra es la que se muestra! Tienes 4 intentos.")
    while intentos != 0:
        ordenar_palabra = input("Ingresar palabra ordenada: ").lower()
        if ordenar_palabra == palabra_original:
            if 1 <= len(palabra_original) <= 12:
                puntos = intentos * len(palabra_original)
                global puntos_totales
                puntos_totales = puntos_totales + puntos

            elif 13 <= len(palabra_original) <= 20:
                puntos = intentos * len(palabra_original)
                puntos_totales = puntos_totales + puntos

            print("¡Correcto!")
            print(f"Los puntos obtenidos son {puntos}\n")
            break
        else:
            intentos = intentos - 1
            print("¡Ups, palabra incorrecta!")
            print(f"Intentos restantes: {intentos}\n")
        if intentos == 0:
            puntos = 0
            print("¡Se terminaron los intentos!")
            print("0 puntos obtenidos.\n")
    return print(f"Los puntos totales obtenidos {puntos_totales}\n")

def dificultad_seleccionada(nivel_de_dificultad):
    """Conecta la ejecucion del programa entre distintas partes."""

    if nivel_de_dificultad == "1" or nivel_de_dificultad == "2":
        palabra_random_segun_dificultad(nivel_de_dificultad)
    else:
        respuesta_valida()

def palabra_random_segun_dificultad(nivel_de_dificultad):
    """Segun la dificultad elegira una palabra de un listado o de otro y la manda a desordenar."""

    inicio = 0
    fin = 3
    if nivel_de_dificultad == "1":
        for i in range(inicio, fin):
            palabra_random = random.choice(listado_de_palabras_faciles)
            while palabra_random in lista_anti_repeticion:
                palabra_repetida = palabra_random
                palabra_random = random.choice(listado_de_palabras_faciles)
                if palabra_repetida == palabra_random:
                    continue
                else:
                    lista_anti_repeticion.append(palabra_random)
                    print(f"\nLa palabra BENIGNA es {palabra_random}")
                    desordenar_palabra(palabra_random)
                    break
         
            lista_anti_repeticion.append(palabra_random)
            print(f"\nLa palabra BENIGNA es {palabra_random}")
            desordenar_palabra(palabra_random)

    if nivel_de_dificultad == "2":
        for i in range(inicio, fin):
            palabra_random = random.choice(listado_de_palabras_intermedias)
            while palabra_random in lista_anti_repeticion:
                palabra_repetida = palabra_random
                palabra_random = random.choice(listado_de_palabras_intermedias)
                if palabra_repetida == palabra_random:
                    continue
                else:
                    lista_anti_repeticion.append(palabra_random)
                    print(f"\nLa palabra BENIGNA es {palabra_random}")
                    desordenar_palabra(palabra_random)
                    break
         
            lista_anti_repeticion.append(palabra_random)
            print(f"\nLa palabra BENIGNA es {palabra_random}")
            desordenar_palabra(palabra_random)

def promedio_de_palabras(promedio_facil, promedio_intermedio):
    """Esta def calcula el promedio de las palabras segun la dificultad."""

    promedio_facil = promedio_facil / len(listado_de_palabras_faciles)
    print(f"El promedio es de palabras BENIGNAS es {round(promedio_facil)}")
    promedio_intermedio = promedio_intermedio / len(listado_de_palabras_intermedias)
    print(f"El promedio es de palabras MALIGNAS es {round(promedio_intermedio)}\n")

def ingresar_nombre():
     """Toma el nombre del usuario y valida que ingrese algo."""
     while True:
        alias_jugador = input("Ingrese nombre o alias: ").lower()
        if not alias_jugador:
            continue
        elif alias_jugador:

            return alias_jugador 

def respuesta_valida():
    """Verificar que la dificultad ingresada sea valida."""

    while True:
        print("La respuesta ingresada no es valida.")
        dificultad = input("Ingrese la dificiltad con la que deseas jugar BENIGNO(1) o MALIGNO(2): ").upper()
        if dificultad == "1" or dificultad == "2":
            return dificultad_seleccionada(dificultad)
        else:
            continue

#Cuerpo del programa

revuelto = open("spanish.lst", "r")
listado_de_palabras_faciles = []
listado_de_palabras_intermedias = []
contador = 0
promedio_facil = 0
promedio_intermedio = 0
puntos_totales = 0
lista_anti_repeticion = []

print("¡BIENVENIDO A PALABRA REVUELTA!\n\nA continuacion podras seleccionar la dificultad.\nLos puntajes de cada dificultad son:\n\nBENIGNO = 3 puntos.\nMALIGNO = 5 puntos.\n")
print("El valor de puntos de dificultad se multiplicara por la cantidad de intentos.\nPor cada intento fallido, obtendras menos puntos.\n")
print("¡Buena suerte!\n")

for palabra in revuelto:
    #Este contador y este if contador, son para que el programa no agarre 
    # las 86 mil palabras jaja, y agarre las que le indiquemos nosotros.
    contador = contador + 1
    if contador > 200:
        break
    palabra = palabra.strip()

    if 1 <= len(palabra) <= 12:
        listado_de_palabras_faciles.append(palabra)
        promedio_facil = promedio_facil + len(palabra)
    
    elif 13 <= len(palabra) <= 20:
        listado_de_palabras_intermedias.append(palabra)
        promedio_intermedio = promedio_intermedio + len(palabra)
        
#Calcular el promedio de palabras de las distintas dificultades.
promedio_de_palabras(promedio_facil, promedio_intermedio)

while True:
    #A partir de aca tenemos el comienzo y la seleccion de dificultad y de ahi todo el programa.
    jugar = input("Ingrese 1 para jugar o ENTER para salir: ")
    if jugar == "1":
        ingresar_nombre()
        dificultad = input("Ingrese la dificiltad con la que deseas jugar BENIGNO(1) o MALIGNO(2): ")
        dificultad_seleccionada(dificultad)
    elif jugar == "":
        print("Hasta luego :D")
        break
    else:
        while True:
            print("Opcion ingresada no valida.")
            jugar = input("Ingrese 1 para jugar o ENTER para salir: ")
            if jugar == "1":
                ingresar_nombre()
                dificultad = input("Ingrese la dificiltad con la que deseas jugar BENIGNO(1) o MALIGNO(2): ")
                dificultad_seleccionada(dificultad)
                break
            elif jugar == "":
                print("Hasta luego :)")
                exit()
            else:
                continue

revuelto.close()
#<
#>