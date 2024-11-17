from random import choice, shuffle
from tabulate import tabulate
import os

def ingresar_jugador():
    '''Registra el nombre de jugador, con el . no juega y solo muestra el ranking'''
    print('\n' * 2)
    jugador = input('Ingrese su nombre (Enter para salir): ').strip().upper()
    return jugador


def elegir_nivel():
    '''Permite selecccionar entre dos niveles de dificultad.'''
    while True:
        nivel = input('\nTipee una letra para seleccionar el nivel de dificultad (Benigno o Maligno): ')
        if not nivel:
            continue
        nivel = nivel.strip().upper()[0]
        if nivel in 'BM':
            break
        else:
            print('Se acepta solo la letra inicial del nivel!')
    return nivel


def elegir_tema():
    '''Permite elegir el tema con el que va a jugar.'''
    menu = {}
    indice = 1
    for archivo in os.listdir():
        if archivo.endswith('.lst'):
            menu[indice] = archivo
            indice += 1
    menu[99] = 'salir.lst'      

    while True:
        os.system('clear')
        comando_so = 'toilet TEMAS -f bigmono9 -F gay -t'
        os.system(comando_so) 
        for opcion in menu:
            print(opcion, '-', menu[opcion][:-4].upper())

        eleccion = input('\nTipee un número de tema: ')
        try:
            eleccion = int(eleccion)
        except:
            continue

        if int(eleccion) not in menu.keys():
            print('\n')
            pausa = input('No disponible, reintente con las alternativas mostradas!. ENTER para continuar')
            continue
        else:
            print(menu[eleccion].upper()[:-4])
            return menu[eleccion]


def leer_palabras(tematica):
    '''Abre el archivo y leer todas las palabras del mismo.'''
    with open(tematica, 'r') as archivo:
        lista_de_palabras = archivo.readlines()
        return lista_de_palabras


def escribir_puntaje(jugador, tematica, palabras, puntos):
   '''Recibe 4 argumentos y escribe el archivo que si no existe lo crea'''
   with open('puntajes.csv', 'a') as archivo:
       archivo.write(jugador + ',' + tematica + ',' + palabras + str(puntos) + '\n')
       return


def determinar_largo_min_max_palabra(lista_completa_palabras):
    '''Devuelve la cantidad de caracteres de la palabra mas corta y mas larga del archivo'''
    largo_max_palabra, largo_min_palabra = 0, 0
    for palabra in lista_completa_palabras:
        if len(palabra) > largo_max_palabra:
            largo_max_palabra = len(palabra)
        elif len(palabra) < largo_min_palabra:
          largo_min_palabra = len(palabra)   
    return largo_min_palabra, largo_max_palabra


def definir_limites_por_nivel(minimo, maximo, nivel_elegido):
    '''Obtiene min/max del nivel elegido.'''
    separador = int((maximo - minimo) / 2)
    if nivel_elegido == 'B':
        return minimo, minimo + separador
    else:
        return minimo + separador, maximo


def obtener_listado_por_nivel(lista_completa, nivel, min, max):
    '''Arma listado de palabras recortado por nivel.'''
    lista_palabras_recortada_por_nivel = []
    for palabra in lista_completa:
        if len(palabra) >= min and len(palabra) <= max:
            lista_palabras_recortada_por_nivel.append(palabra.upper()[:-1])
    return lista_palabras_recortada_por_nivel
        

def elegir_palabra(lista_palabras):
    '''Elige al azar una palabra y la retorna tanto normal como revuelta'''
    palabra_elegida = choice(lista_palabras).upper()
    palabra_elegida_formato_lista = list(palabra_elegida)
    while True:
        shuffle(palabra_elegida_formato_lista)
        palabra_revuelta = ''.join(palabra_elegida_formato_lista)
        if palabra_elegida == palabra_revuelta:
            continue
        else:
            break
    return palabra_elegida, palabra_revuelta


def jugar(jugador, palabra_elegida, palabra_revuelta, tema, jugada):
    '''Jugada que devuelve el puntaje'''
    intento = 1
    intentos_restantes = 4
    largo_palabra_elegida = len(palabra_elegida)
    while True:

        os.system('clear')
        print('Jugador:', jugador)
        print('Tema   :', tema.upper()[:-4])
        print('Modo   :', modo_jugada[nivel])
        print('Jugada :', jugada, 'de 3')
        print('Intento:', intento, 'de 4')
        print('Puntuación ideal:',intentos_restantes * palabra_elegida)
        print('Palabra elegida revuelta:', palabra_revuelta)
        comando_so = 'toilet ' + palabra_revuelta + ' -f bigmono9 -F metal -t'
        os.system(comando_so)

        if intento == intentos_restantes:
            print('Intentos agotados! La palabra era:', palabra_elegida)
            comando_so = 'toilet ' + palabra_elegida + ' -f bigmono9 -F gay -t'
            os.system(comando_so)            
            pausa = input('Pulse ENTER para continuar.')
            intentos_restantes = 0
            break

        ayuda = False
        while True:
            if not ayuda:
                palabra_tipeada = input('Tipee la palabra (? para ayudín, pero te reduciré los puntos a la mitad): ').strip().upper()
            else:
                palabra_tipeada = input('Tipee la palabra: ').strip().upper()

            if palabra_tipeada == '?' and not ayuda:
                ayuda = True
                print('El primer caracter es:', palabra_elegida[0])
                continue
            else:
                break

        if palabra_tipeada == palabra_elegida:
            #print('Correcto!')
            comando_so = 'toilet ' + 'Correcto!' + ' -f bigmono9 -F gay -t'
            os.system(comando_so)
            pausa = input('Pulse ENTER para continuar.')
            break
        else:
            intento += 1
            intentos_restantes = intentos_restantes - 1
            comando_so = 'toilet No es! -f bigmono9 -t'
            os.system(comando_so)          
            pausa = input('Pulse ENTER para continuar.')

    if ayuda:
        puntos = int(largo_palabra_elegida * intentos_restantes / 2) 
    else:
        puntos = largo_palabra_elegida * intentos_restantes

    return puntos


def ranking():
    '''Lee puntajes, ordena e imprime el topten.'''
    with open('puntajes.csv', 'r') as archivo:
        lista_archivo = archivo.readlines()
        ranking = []
        for linea in lista_archivo:
            lista_linea = linea.split(',')
            jugador = lista_linea[0]
            puntos  = int(lista_linea[5])
            ranking.append([0, jugador, puntos])

        ranking_ordenado = sorted(ranking, key=lambda pts: pts[2])
        ranking = ranking_ordenado[::-1]
        for i in range(10):
            ranking.append((0, '', 0))
        os.system('clear')
        comando_so = 'toilet Top-Ten -f bigmono9 -F metal -t'
        os.system(comando_so)
        i = 0
        topten = []

        for r in ranking:
            topten.append([i+1, ranking[i][1], ranking[i][2]])
            i += 1

        topten = topten[:10]
        print(tabulate(topten, headers=['Posición', 'Jugador/Equipo', 'Puntos'], tablefmt='fancy_grid'))
        pausa = input('Pulse ENTER para terminar.')

    return
    

#programa principal
while True:

    modo_jugada = {'B':'Benigno', 'M':'Maligno'}
    os.system('clear')
    print('\n'*6)
    comando_so = 'toilet Palabra Revuelta -f bigmono9 -F gay -t'
    os.system(comando_so)
    jugador = ingresar_jugador()
    if not jugador:
        break
    elif jugador == '.':
        ranking()
        break

    tema = elegir_tema()
    if tema == 'salir.lst':
        ranking()
        break

    nivel = elegir_nivel()
    palabras_por_3 = ''

    lista_palabras_completa = leer_palabras(tema)
    minimo, maximo  = determinar_largo_min_max_palabra(lista_palabras_completa)
    desde, hasta = definir_limites_por_nivel(minimo, maximo, nivel)
    lista_palabras_por_nivel = obtener_listado_por_nivel(lista_palabras_completa, nivel, desde, hasta)
    del lista_palabras_completa
    
    puntaje_total = 0
    for jugada in (1, 2, 3):
        palabra_elegida, palabra_revuelta = elegir_palabra(lista_palabras_por_nivel)
        os.system('clear')
        palabra_elegida, palabra_revuelta = elegir_palabra(lista_palabras_por_nivel)
        print('Palabra elegida revuelta:', palabra_revuelta)
        comando_so = 'toilet ' + palabra_revuelta + ' -f bigmono9 -F metal -t'
        os.system(comando_so)
        puntaje = jugar(jugador, palabra_elegida, palabra_revuelta, tema, jugada)
        print('Puntaje obtenido por esta jugada:', puntaje)
        puntaje_total += puntaje
        lista_palabras_por_nivel.remove(palabra_elegida)
        palabras_por_3 = palabras_por_3 + palabra_elegida + ','

    escribir_puntaje(jugador.upper(), tema.upper()[:-4], palabras_por_3, puntaje_total)
    print('\n' + '-' * (50 + len(jugador)))
    print(jugador + ',', 'Puntaje obtenido sumando todas las jugadas:', puntaje_total)
    print('-' * (50 + len(jugador)) + '\n')

    if jugador != '.':
        pausa = input('Pulse ENTER para ver el ranking')
        ranking()