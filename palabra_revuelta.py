"""Se adjunta un archivo de texto con mas de 86 mil palabras en castellano. 
Tenemos que hacer un programa que pueda leer las mismas y cargarlas en memoria principal. 
En síntesis el programa deberá elegir al azar alguna de ellas y mostrarla desordenada. 
El jugador deberá tipearla en forma correcta. 
Vayan pensando como puntuar, si por tiempo, por largo de palabra,
por una combinación de ambos o por otro criterio.
Ese será el juego que haremos para la jornada.


Requisitos básicos:
Cuál es el mínimo de largo de palabra?
Cuál es el máximo de largo de palabra?
Cuál es el largo promedio de palabra (redondeado a 1 entero)?
Que el programa elija una palabar al azar.
Que la muestre en mayúsculas en su orden natural y la muestre desordenada."""

"""NUEVOS REQUERIMIENTOS:

    1- Dificultades: facil, intermedio, dificil. 
       Mayor cantidad de letras por nivel
       y mayor nivel de puntos por dificultad.

    2- Intentos maximos, 5 por ejemplo. Mayor cantidad de puntos
       mientras se utilicen menos intentos.

    3- Tematica de palabras, que haya 10 archivos diferentes por ejemplo. 
       Que cada uno tenga una tematica con palabras diferentes.
       Por ejemplo: futbol, países, comida.

    4- Crear 9 archivos con tematicas de palabras entre 50 y 100.
"""

import random

def desordenar_palabra(palabra_a_desordenar):
    """Esta def se encarga de desordenar las palabras aleatorias."""

    palabra_original = palabra_a_desordenar
    palabra_a_desordenar = list(palabra_a_desordenar)
    random.shuffle(palabra_a_desordenar)
    palabra_a_desordenar = "".join(palabra_a_desordenar)
    print(f"Esta es la palabra en subcadenas {palabra_a_desordenar}")
    te_toca(palabra_original)

def te_toca(palabra_original):
    """Esta def se encarga de verificar si la palabra que ingreso el usuario es correcta o no."""

    intentos = 5
    print("¡Intenta armar que palabra es la que se muestra! Tienes 5 intentos.")
    while intentos != 0:
        ordenar_palabra = input("Ingresar palabra ordenada: ")
        if ordenar_palabra == palabra_original:
            print("¡Ganaste!")
            break
        else:
            intentos = intentos - 1
            print("¡Ups, palabra incorrecta!")
            print(f"Intentos restantes: {intentos}")
        if intentos == 0:
            print("¡Perdiste! Suerte la proxima.")

def dificultad_seleccionada(nivel_de_dificultad):
    """Conecta la ejecucion del programa entre distintas partes."""

    nivel_de_dificultad = nivel_de_dificultad.upper()
    if nivel_de_dificultad == "FACIL" or nivel_de_dificultad == "INTERMEDIO" or nivel_de_dificultad == "DIFICIL":
        puntaje(nivel_de_dificultad)
    else:
        respuesta_valida()
    
    return nivel_de_dificultad.upper()

def puntaje(nivel_de_dificultad):
    """Segun la dificultad elegira una palabra de un listado o de otro y la manda a desordenar."""

    nivel_de_dificultad = nivel_de_dificultad.upper()

    if nivel_de_dificultad == "FACIL":
        palabra_random = random.choice(listado_de_palabras_faciles)
        print(f"La palabra facil es {palabra_random}")
        desordenar_palabra(palabra_random)

    if nivel_de_dificultad == "INTERMEDIO":
        palabra_random = random.choice(listado_de_palabras_intermedias)
        print(f"La palabra intermedia es {palabra_random}")
        desordenar_palabra(palabra_random)

    if nivel_de_dificultad == "DIFICIL":
        palabra_random = random.choice(listado_de_palabras_dificiles)
        print(f"La palabra dificil es {palabra_random}")
        desordenar_palabra(palabra_random)

def promedio_de_palabras(promedio_facil, promedio_intermedio, promedio_dificil):
    """Esta def calcula el promedio de las palabras segun la dificultad."""

    promedio_facil = promedio_facil / len(listado_de_palabras_faciles)
    print(f"El promedio es de palabras faciles es {round(promedio_facil)}")
    promedio_intermedio = promedio_intermedio / len(listado_de_palabras_intermedias)
    print(f"El promedio es de palabras intermedias es {round(promedio_intermedio)}")
    promedio_dificil = promedio_dificil / len(listado_de_palabras_dificiles)
    print(f"El promedio es de palabras dificiles es {round(promedio_dificil)}")

def respuesta_valida():
    """Verificar que la dificultad ingresada sea valida."""

    while True:
        print("La respuesta ingresada no es valida.")
        dificultad = input("Ingrese la dificiltad con la que deseas jugar(Facil, Intermedio, Dificil): ").upper()
        if dificultad == "FACIL" or dificultad == "INTERMEDIO" or dificultad == "DIFICIL":
            return dificultad_seleccionada(dificultad)
        else:
            continue

#Cuerpo del programa

revuelto = open("spanish.lst", "r")
listado_de_palabras_faciles = []
listado_de_palabras_intermedias = []
listado_de_palabras_dificiles = []
contador = 0
promedio_facil = 0
promedio_intermedio = 0
promedio_dificil = 0

for palabra in revuelto:
    #Este contador y este if contador, son para que el programa no agarre las 86 mil palabras jaja, y
    #agarre las que le indiquemos nosotros
    contador = contador + 1
    if contador > 200:
        print("Llegamos hasta aqui.")
        break
    palabra = palabra.strip()

    if 0 <= len(palabra) <= 5:
        listado_de_palabras_faciles.append(palabra)
        promedio_facil = promedio_facil + len(palabra)

    elif 5 <= len(palabra) <= 10:
        listado_de_palabras_intermedias.append(palabra)
        promedio_intermedio = promedio_intermedio + len(palabra)
    
    elif 10 <= len(palabra) <= 15:
        listado_de_palabras_dificiles.append(palabra)
        promedio_dificil = promedio_dificil + len(palabra)

#Calcular el promedio de palabras de las distintas dificultades
promedio_de_palabras(promedio_facil, promedio_intermedio, promedio_dificil)

#A partir de aca tenemos la seleccion de dificultad
dificultad = input("Ingrese la dificultad con la que queire jugar(Facil, Intermedio, Dificil): ")
dificultad_seleccionada(dificultad)


revuelto.close()
#<
#>