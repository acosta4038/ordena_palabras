import re

import random
  
def lectura(archivo):
    """"Selecciona palabras que tenga mas de 4 letras y menos de 12"""
    filtro_lista = []
    for palabra in archivo:
        palabra = palabra.strip()
        if len(palabra) > 4 and len(palabra) < 12 :
            filtro_lista.append(palabra)
    return filtro_lista      

def desordenar_letras (filtro_lista): 
    """"Desordena la palabra seleccionada del archivo"""
    caracteres =[] 
    
    palabra_alzar= random.choice(filtro_lista)
    for letra in palabra_alzar:
        caracteres.append(letra)
        
    random.shuffle(caracteres)
    cadena= "".join(caracteres)
    print(cadena)
    
    return len(cadena)

def promedio (cant_total,contador):
    """"Calcula la cantidad de palabras leidas"""
    if contador == 0:
        return 0

    promedio= cant_total/ contador
        
    pro_redondeado= round(promedio)
    return pro_redondeado



#Cuerpo de programa inicial

contador = 0 
cant_caracteres = 0

with open("spanish.lst","r") as archivo:
    archivo_contenido = archivo.readlines()
    
    while True:
        inicio = input("Enter para iniciar: ")
        if inicio == "":
            filtro =  lectura(archivo_contenido)
            total_letras = desordenar_letras(filtro)
            contador += 1
            cant_caracteres += total_letras
            continue
        elif inicio == "esc".lower():
            resultado= promedio(cant_caracteres,contador)
            print(f"El promedio es: {resultado}")
            print("Fin de programa")
            break
        else:
            print("Opcion incorrecta")        
    







