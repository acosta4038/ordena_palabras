from random import choice, shuffle
import pandas as pd
from os import listdir, system , chdir, getcwd
def crear_archivo(ruta_de_jugador):
    """Crea un archivo para guardar la informacion de los jugadores o participantes"""
    try:
        archivo_jugador = open(ruta_de_jugador, "x")
        print("Creaste un archivo")
    except:
        print(" El archivo ya fue creado")
    return

def temas(ruta_temas,ruta_de_jugador):
    """muestra una lista de temas"""
    lista_de_temas = listdir(ruta_temas)
    chdir(ruta_temas)
    ranking_temas = {"Elige un tema": lista_de_temas}
    df = pd.DataFrame(ranking_temas)
    print(df)
    return elegir_tema(df,ruta_de_jugador)

def elegir_tema(df,ruta_de_jugador):
    while True:
        elegir_tema = input("Ingrese el numero del tema: ").strip()
        if not elegir_tema:
            print("Por favor elija un tema")
            continue
        elif elegir_tema:
            tema_elegido = df.loc[int(elegir_tema):int(elegir_tema)]
            with open(ruta_de_jugador,"a")as dato_jugador:
                dato_jugador.write(str(tema_elegido) + ",")
            ruta = getcwd()
            cambiar = chdir(str(ruta) + "/" + str(tema_elegido)[0])
            ruta_tema_elegido = getcwd()
            print(ruta_tema_elegido)
            return promedio(ruta_tema_elegido, ruta_de_jugador)
        else:
            print("error elija uno de estos numeros")

def promedio(tema_elegido, ruta_de_jugador):
    minimo = 1
    maximo = 1
    for numero in tema_elegido:
        if numero > maximo:
            maximo = numero
        elif numero > minimo < maximo:
            numero = minimo
    suma = minimo + maximo
    promedio = suma / 2
    return mesclar_palabra(promedio, maximo, tema_elegido, ruta_de_jugador)

def mesclar_palabra(promedio, maximo, tema_elegido,ruta_de_jugador):
    contador = 1
    while contador != 3:
        dificultad = input("Escribe una dificultas <FACIL> o <DIFICIL>: ").strip().upper()
        if not dificultad:
            print("Por favor elija una")
            continue
        elif dificultad == "FACIL":
            while contador:
                palabra = choice(tema_elegido).upper()
                if palabra <= promedio:
                    x = list(palabra)
                    shuffle(x)
                    palabra_elegida = palabra
                    contador += 1
                    with open(ruta_de_jugador,"a")as dato_jugador:
                        dato_jugador.write(palabra_elegida, + ",")
                    return juego_1(palabra_elegida, x, ruta_de_jugador)
                else:
                    continue
        elif dificultad == "DIFICIL":
             while contador:
                palabra = choice(tema_elegido).upper()
                if palabra <= maximo and palabra >= promedio:
                    x = list(palabra)
                    shuffle(x)
                    palabra_elegida = palabra
                    contador +=1
                    with open(ruta_de_jugador,"a")as dato_jugador:
                        dato_jugador.write(palabra_elegida + ",")
                    return juego_1(palabra_elegida, x,ruta_de_jugador)
                else:
                    continue

def juego_1(palabra_elegida, palabra_desordenada, ruta_de_jugador):
    intentos = 4
    contador = 1
    print(palabra_desordenada)
    if contador != 3:
        while True:
            resolver = input("Por favor ordena esta palabra: ").upper().strip()
            if resolver == palabra_elegida:
                puntos = intentos * len(palabra_elegida)
                print("\nMuy bien",palabra_elegida)
                contador += 1
                return mesclar_palabra()
            elif intentos == 0 :
                print("\nperdiste (T_T) la palabra era:", palabra_elegida)
                puntos = intentos * len(palabra_elegida)
                contador += 1
                return mesclar_palabra()
            elif resolver != palabra_elegida:
                intentos -= 1
                print("\nerror vuelva a intentar ordenar:", palabra_desordenada, "te quedan", intentos)
                continue
    else:
        print("fin del juego")
        return ranking(puntos, ruta_de_jugador)
    
def ranking(puntos, ruta_de_jugadores):
    with open(ruta_de_jugador,"a")as dato_jugador:
        dato_jugador.write(puntos)
    mejores_jugadores = open(ruta_de_jugadores,"r").readline()
    mejores_jugadores.split(",")
    nombre = mejores_jugadores[0]
    tema = mejores_jugadores[1]
    puntos = mejores_jugadores[5]
    for jugadores in mejores_jugadores:
        jugadores = list(nombre + tema + puntos)
        for jugadores in jugadores,range(10):
            jugadores.sort[2]
            enumerate(jugadores)
            print(jugadores)
        pausa = input("Precione <ENTER> para continuar")
        return



#Cuerpo principal#
#palabras/temas/marcas de autos.lst
ruta_de_jugador = "/home/luci/Documentos/python/logica/palabras/archivo_jugador.lst"
ruta_temas = "/home/luci/Documentos/python/logica/palabras/temas"
crear_archivo(ruta_de_jugador)
while True:
    nombre_jugador = input("Bienvenido por favor ingrese su nombre o aprete <ENTER> para salir: ").strip()
    if len(nombre_jugador) == 0:
        print("\nSe a salido con exito")
        exit()
    elif nombre_jugador:
        with open(ruta_de_jugador,"a")as dato_jugador:
            dato_jugador.write(nombre_jugador + ",")
        temas(ruta_temas, ruta_de_jugador)
    else:
        print("\nPor favor ingrese un nombre\n")
        continue