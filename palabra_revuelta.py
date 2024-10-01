import os
import random
import csv
def inicio ():
     while True:
        inicio = input("Ingrese 1 para iniciar o 2 para salir: ") 
        if  not inicio :
            print("Ingrese una opcion valida")
            continue 

        elif inicio == "1":
           
            return True
        elif inicio == "2":
            print("Fin del juego")
            return False 
            
        else :
            print("Opcion invalida")

def ingresar_nombre():
     while True:
        alias_jugador = input("Ingrese nombre o alias: ").lower()
        if not alias_jugador:
            continue
        elif alias_jugador:
            
            return alias_jugador
              
def elegir_tema():
    '''Permite elegir el tema con el que va a jugar.'''
    while True:
        temas = []
        for archivo in os.listdir():
            if archivo.endswith('.lst'):
                temas.append(archivo)
        menu = {}
        indice = 1
        for tema in temas:
            menu[indice] = tema
            indice += 1
        print('\nTEMAS DISPONIBLES PARA ELEGIR')
        print('-----------------------------')
        indice = 1
        opciones_disponibles = []
        for tema in temas:
            print(indice, '-', tema.upper()[:-4])
            opciones_disponibles.append(str(indice))
            indice += 1    
        eleccion = input('Seleccione un número de tema: ')
        if eleccion not in opciones_disponibles:
            pausa = input('No disponible, reintente con las alternativas mostradas!. ENTER para continuar')
            continue
        else:
            eleccion = int(eleccion)
            print(menu[eleccion].upper()[:-4])
            return menu[eleccion]

def leer_palabras(tematica):
    '''Abre el archivo y leer todas las palabras del mismo.'''
    with open(tematica, 'r') as archivo:
        lista_de_palabras = archivo.readlines()
        return lista_de_palabras

def lectura(lista_de_palabras):
    """"Selecciona palabras que tenga mas de 4 letras y menos de 12"""
    filtro_lista = []
    while True:
        try:
            eleccion_dificultad = int(input("Seleccione la dificultad, 1: benigno 2: maligno: "))
            if eleccion_dificultad == 1:
                for palabra in lista_de_palabras:
                    palabra = palabra.strip().lower()
                    if len(palabra) > 4 and len(palabra) < 12:
                        filtro_lista.append(palabra)
                break
            
            elif eleccion_dificultad == 2:
                for palabra in lista_de_palabras:
                    palabra = palabra.strip()
                    if len(palabra) > 13 and len(palabra) < 20:
                        filtro_lista.append(palabra)
                break        
        except ValueError:
            print("Eleccion invalida")
            continue           

    return filtro_lista  

def desordenar_letras(filtro_lista): 
    """"Desordena una palabra seleccionada aleatoriamente del archivo y elimina la palabra escogida de la lista"""
    palabra_random = []
    caracteres = []
    
    palabra_alazar = random.choice(filtro_lista)
    palabra_random.append(palabra_alazar)
    filtro_lista.remove(palabra_alazar)
   
    for letra in palabra_alazar:
            caracteres.append(letra)
    random.shuffle(caracteres)
    palabra_desordenada = "".join(caracteres)
    
    while True:
        
        if palabra_alazar == palabra_desordenada:
            for letra in palabra_alazar:
                caracteres.append(letra)
            random.shuffle(caracteres)
            palabra_desordenada= "".join(caracteres)
            continue
        else:
            break
            
    return  palabra_alazar,palabra_desordenada

def chances(palabra_alazar,palabra_desordenada,puntos = 0):
     # Verificar si la plabra ingresada es correcta y calcular los puntos.
    oportunidades = 3
    print(palabra_alazar)
    print(palabra_desordenada)
    for i in range (oportunidades):
         
        adivinar = input("Ingrese la palabra ordenada: ").lower().strip()            
        if not adivinar:
                print("Ingrese algo")
                continue
        elif adivinar == palabra_alazar:
            print("Bien hecho")
            puntos += (oportunidades - i) * len(palabra_alazar) 
            break
        elif adivinar != palabra_alazar:
            intentes_restantes= oportunidades - i
            print(f"Fallaste, te quedan {intentes_restantes} oportunidades.")
       
    return palabra_alazar, palabra_desordenada, puntos




                   
                
              
#Cuerpo de programa inicial
puntos = 0 

alias_jugador = ingresar_nombre()
arranque = inicio() 
eligir_tematica = elegir_tema()
tema_sin_extension= eligir_tematica [3:-4]
leer_lista = leer_palabras(eligir_tematica)
dificultad = lectura(leer_lista)
contador = 0
almacenamiento_csv= []
palabras_elegidas = [] 

while True:
    if contador == 3 :
        break
        11
    if arranque == True:
        palabra_alazar,caracteres = desordenar_letras(dificultad)
        contador = contador + 1
        palabra_alazar,palabra_desordenada, puntos = chances(palabra_alazar,caracteres,puntos)
        palabras_elegidas.append(palabra_alazar)
        tup_resultado = alias_jugador,puntos
        continue
        
    elif arranque == False:
        break 
print("fin del juego")
almacenamiento_csv.append(tup_resultado)    

with open ("puntajes.lst","a") as archivo:
    writer = csv.writer(archivo)
    resultado = f"El puntaje del jugador: {alias_jugador} fue: {puntos}.Palabras elegidas: {palabras_elegidas}.\n"
    archivo.write(resultado)

with open ("ranking.csv",mode ="a", newline = "") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(almacenamiento_csv)

with open ("ranking.csv",mode = "r",newline = "" ) as archivo:
    reader = csv.reader(archivo)
    renglones =  list(reader)

datos_ordenados = sorted(renglones, key=lambda x: int(x[1]), reverse=True)
   
with open ("ranking.csv",mode ="w", newline = "") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos_ordenados)



    