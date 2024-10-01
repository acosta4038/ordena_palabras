
def archivo_ordenado(tematica):

    with open(tematica,"r") as archivo:
        contenido = archivo.readlines()
        listaa = []

        for palabra in contenido:
            palabra_modificada = palabra.strip().replace(" ","-")
            listaa.append(palabra_modificada)
            lista_sin_repetir = list(set(listaa))
            
    for i in lista_sin_repetir:
        print(i)

