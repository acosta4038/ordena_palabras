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

def temas(ruta_temas):
    """muestra una lista de temas"""
    lista_de_temas = listdir(ruta_temas)
    lista = list([])
    chdir(ruta_temas)
    medio = "\n"
    for i, temas in enumerate(lista_de_temas):
        temas_a_elegir = (f"{i}:{temas}")
        lista.append(temas_a_elegir), medio
    print(lista,"\n")
    return lista


def elegir_tema(temas_a_elegir,ruta_de_jugador):
    while True:
        elegir_tema = input("Ingrese el numero del tema: ").strip()
        if not elegir_tema:
            print("Por favor elija un tema")
            continue
        elif int(elegir_tema) <= 9:
            tema_elegido = temas_a_elegir[int(elegir_tema)]
            print("El tema elegido fue: ",tema_elegido)
            with open(ruta_de_jugador,"a")as dato_jugador:
                dato_jugador.write(str(tema_elegido[2:-4]) + ",")
            ruta_tema_elegido = getcwd()+ "/" + str(tema_elegido[2:])
            print(ruta_tema_elegido)
            return ruta_tema_elegido
        elif int(elegir_tema) >= 10:
            tema_elegido = temas_a_elegir[int(elegir_tema)]
            print("El tema elegido fue: ",tema_elegido)
            with open(ruta_de_jugador,"a")as dato_jugador:
                dato_jugador.write(str(tema_elegido[3:-4]) + ",")
            ruta_tema_elegido = getcwd()+ "/" + str(tema_elegido[3:])
            print(ruta_tema_elegido)
            return ruta_tema_elegido
        else:
            print("error elija uno de estos numeros")

def promedio(ruta_tema_elegido):
    tema_elegido = open(ruta_tema_elegido,"r").read().splitlines()
    minimo = 1
    maximo = 1
    for numero in tema_elegido:
        if len(numero) > maximo:
            maximo = len(numero)
        elif len(numero) < minimo:
            minimo = len(numero)    
    x = maximo - minimo
    medio = x / 2
    print(minimo,maximo,medio)
    return int(medio), maximo, minimo

def mesclar_palabra(ruta_tema_elegido, ruta_de_jugador,promedio,minimo):
    while True:
        lista_palabras =open(ruta_tema_elegido,"r").read().splitlines()

        dificultad = input("Escribe una dificultas <F> o <D>: ").strip().upper()
        if not dificultad:
            print("\n Por favor elija una")
            continue
        elif dificultad == "FACIL" or dificultad == "F":
                while True:
                    palabra = choice(lista_palabras)
                    if len(palabra) >= minimo <= int(promedio):
                        x = list(palabra)
                        shuffle(x)
                        palabra_elegida = palabra
                        with open(ruta_de_jugador,"a")as dato_jugador:
                            dato_jugador.write(palabra_elegida + ",")
                        lista_palabras.remove(palabra_elegida)
                        return (palabra_elegida).upper(), x
                    else:
                        continue
        elif dificultad == "DIFICIL" or dificultad == "D":
                while True:
                    palabra = choice(lista_palabras)
                    if len(palabra) >= int(promedio):
                        x = list(palabra)
                        shuffle(x)
                        palabra_elegida = palabra
                        with open(ruta_de_jugador,"a")as dato_jugador:
                            dato_jugador.write(palabra_elegida + ",")
                        lista_palabras.remove(palabra_elegida)
                        return (palabra_elegida).upper(), x
                    else:
                        continue
        else:
            continue    

def juego_1(palabra_elegida, palabra_desordenada):
    intentos = 4
    print(palabra_desordenada)
    while intentos != 0:
        print(palabra_elegida)
        resolver = input("\n Por favor ordena esta palabra: ").upper().strip()
        if resolver == palabra_elegida:
            puntos = intentos * len(palabra_elegida)
            print("\nMuy bien",palabra_elegida)
            return puntos
        elif resolver != palabra_elegida:
            intentos -= 1
            print("\n Error vuelva a intentar ordenar:", palabra_desordenada, "te quedan", intentos)
            continue
        else:
            print("\nfin del juego")
            return
    puntos = intentos * len(palabra_elegida)
    print("\nperdiste (T_T) la palabra era:", palabra_elegida, "Tus puntso fueron", puntos)
    return puntos
    
def ranking(ruta_de_jugadores):
    lista_jugadores = open(ruta_de_jugadores,"r").readlines()
    nombre = list()
    tema = list()
    puntos = list()
    for jugadores in lista_jugadores:
        separador = jugadores.split(",")
        nombre.append(separador[0])
        tema.append(separador[1])
        puntos.append(separador[5])

    datos = {"participantes": nombre,
             "tema": tema,
             "puntos": puntos}
    
    df = pd.DataFrame(datos)
    df = df.sort_values(by= "puntos", ascending=False).reset_index(drop=True)
    df.drop(df.index[11:100], inplace=True)
    df["ranking_puntos"] = df["puntos"].rank(method="min")
    print("\n  Mejores jugadores \n",df,"\n")
    
    



#Cuerpo principal#
#palabras/temas/marcas de autos.lst
ruta_de_jugador = "/home/luci/Documentos/python/logica/archivo_jugador.csv"
ruta_temas = "ordena_palabras/temas"
crear_archivo(ruta_de_jugador)
while True:
    while True:
        nombre_jugador = input("Bienvenido por favor ingrese su nombre o aprete <ENTER> para salir: ").strip()
        if len(nombre_jugador) == 0:
            print("\nSe a salido con exito")
            exit()
        elif nombre_jugador:
            with open(ruta_de_jugador,"a")as dato_jugador:
                dato_jugador.write(nombre_jugador + ",")
            lista = temas(ruta_temas)
            break
        else:
            print("\nPor favor ingrese un nombre\n")
            continue
    ruta_tema_elegido = elegir_tema(lista,ruta_de_jugador)
    medio, maximo, minimo = promedio(ruta_tema_elegido)
    contador = 0
    puntajes = 0
    while True:
        if contador != 3:
            palabra_elegida, x = mesclar_palabra(ruta_tema_elegido, ruta_de_jugador,medio,minimo)
            puntos = juego_1(palabra_elegida, x)
            puntajes = puntajes + puntos
            contador +=1
            continue
        else:
            with open(ruta_de_jugador,"a")as dato_jugador:
                dato_jugador.write(str(puntajes) + "\n")
            ranking(ruta_de_jugador)
            pausa = input("Precione <ENTER> para continuar")
            break
    while True:
        volver_a_jugar = input("¿Quieres volver a jugar? ingrese <S> o <N>: ").upper().strip()
        if not volver_a_jugar:
            print("Por favor eliga una de las oppciones\n")
            continue
        elif volver_a_jugar == "S" or volver_a_jugar == "N":
            break
        else:
            print("\nPor favor elija una de las oppciones")
    
    if volver_a_jugar == "S":
        continue
    elif volver_a_jugar == "N":
        exit()