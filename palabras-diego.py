import random
    
def crear_archivo(ruta_de_archivo):
    """La función crea y cierra un archivo de texto"""    
    try:
        crear_archivo_= open(ruta_de_archivo, "x")
        crear_archivo_.close()
    except:
        print("El archivo ya fue creado")
    return

def desordenar(lista): 
    palabra_random = random.choice(lista)
    lista_palabras = list(palabra_random)
    random.shuffle(lista_palabras)
    return ''.join(lista_palabras), palabra_random

ruta_de_archivo = "/home/diego/Documentos/logica_y_estructura/palabra/spanish.lst"
archivo_de_palabras = open(ruta_de_archivo, "r")
palabras = []

for palabra in archivo_de_palabras:
    palabras.append(palabra[:-1])

def resultado(correctas, veces_jugadas, incorrectos,puntos):
    resultados = print("las respuestas correctas fueron: ", correctas, "\nla cantidad de veces jugadas fueron: ", veces_jugadas, "\nlas respuestas incorrectas fueron: ", incorrectos, " \nlos puntos obtenidos fueron", puntos)
    return

#cuerpo del programa# 
correctas = 0
veces_jugadas = 0
incorrectos = 0
puntos = 0

nombre = input(" Ingrese su nombre para registrarse: ").strip()
if not nombre:
    print("\nError! Debe ingresar un nombre.") 
#da la bienvenida al usuario y suma una jugada 
print("\nbienvenido al juego ORDENA TU PALABRA", nombre, "espero la pases muy bien!!")
veces_jugadas +=1
while True:     
    palabra_desordenada, palabra_ordenada = desordenar(palabras)

#da la palabra random desordenada
    while True: 
        print("la palabra para ordenar es: ")
        print(palabra_desordenada)

        #se le pide la palabra ordenada al usuario y se corrobora si esta correcta, ademas de sumar un punto por respuesta correcta
        respuesta = input("ingresar la palabra ordenada para sumar puntos: ").upper().strip()
        if respuesta == palabra_ordenada.upper():
            print("felicitaciones, la palabra fue ingresada correctamente, sumaste un punto")
            correctas +=1
            puntos +=1
            jugar_nuevamente = input("¿jugar de nuevo? ingresar: [S] [N]:").upper().strip()
            if jugar_nuevamente == 'S':
                break
            else: 
                print("los resultados son los siguientes: ")
                resultado(correctas, veces_jugadas, incorrectos,puntos)
                break  
        elif respuesta != palabra_ordenada:
            incorrectos +=1
            print("no has logrado ordenar la palabra correctamente")   
            error = input("¿desea volver a intentarlo? ingresar, [S] [N]: ").strip().upper()
            if error == "S": 
                continue    
            elif error == "N":
                print ("\ngracias por jugar a ORDENA TU PALABRA, abajo van a estar todos los resultados")  
                resultado(correctas, veces_jugadas, incorrectos,puntos)
                
    continue            
                
    