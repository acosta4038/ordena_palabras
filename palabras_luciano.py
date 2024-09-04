from random import choice, shuffle
def crear_archivo(ruta_de_archivo):
    """La función crea y cierra un archivo de texto"""    
    try:
        crear_archivo_personas = open(ruta_de_archivo, "x")
        crear_archivo_personas.close()
    except:
        print("El archivo ya fue creado")
    return

def buscar_palabras(bienvenido,leer_archivo):
    """Abre el archivo en modo lectura y busca el total de letras, el minimo, maximo y el promedio."""
    bienvenido = True
    leer_archivo
    largo_minimo = set({})
    largo_maximo = set({})
    letras_totales = set({})
    largo_promedio = ()
    while bienvenido:
        lectura = leer_archivo.readlines()
        if not lectura:
            break    
        for numeros in lectura:
            letras_totales.add(len(numeros))
        for numeros in lectura:
            if len(numeros) <= 5:
                largo_minimo.add(len(numeros))
        for numeros in lectura:
            if len(numeros) >= 15:
                largo_maximo.add(len(numeros))
        for numeros in lectura:
            largo_promedio = 86061 / len(numeros)     
    leer_archivo.close()
    return letras_totales, largo_minimo, largo_maximo, largo_promedio 

def juego(buscar_en_archivo):
    while True:
        palabra = choice(buscar_en_archivo.read().splitlines()).upper()
        x = list(palabra)
        shuffle(x)
        palabra_elegida = palabra
        buscar_en_archivo.close()
        return palabra_elegida, x
def final():
    final = print("Que tenga un buen día", "las veces jugadas fueron:",veces_jugadas , "\nLas veces acertadas fueron:",veces_acertadas,"\n Los reintentos fueron: ", reintentos, "\n sus puntos fueron", puntos)
    return
#cuerpo
veces_acertadas = 0
veces_jugadas = 0
reintentos = 0
ruta_de_archivo = "/home/luci/Documentos/python/logica/palabras/spanish.lst"
crear_archivo(ruta_de_archivo)
leer_archivo = open(ruta_de_archivo,"r")
vidas = 5
bienvenido = input("Bienvendio muchas gracias por probar este juego ¿Quieres continuar? ").strip()
if bienvenido:
    letras_totales,largo_minimo,largo_maximo,largo_promedio = buscar_palabras(bienvenido,leer_archivo)
    print(letras_totales)
    print(largo_minimo)
    print(largo_maximo)
    print(largo_promedio)
    buscar_en_archivo = open(ruta_de_archivo,"r")
    palabra_elegida, palabra_desordenada = juego(buscar_en_archivo)
    print(palabra_desordenada)
    while True:
        veces_jugadas += 1
        resolver = input("Por favor ordena esta palabra: ").upper().strip()
        if resolver == palabra_elegida:
            puntos = vidas * len(palabra_elegida)
            veces_acertadas +=1
            print("\nMuy bien",palabra_elegida)
            final()
            break
        elif vidas == 0 :
            print("\nperdiste (T_T)", palabra_elegida)
            puntos = vidas * len(palabra_elegida)
            final()
            break
        elif resolver != palabra_elegida:
            print("\nerror vuelva a intentar ordenar:", palabra_desordenada, "te quedan", vidas )
            vidas -= 1
            reintentos +=1
            continue
else:
    puntos = 0
    final()
