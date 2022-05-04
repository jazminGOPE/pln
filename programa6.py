'''
Jazmin Azucena Gonzalez Peredia
Profesor: Oswaldo Carrillo Zepeda
'''

import os

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"

archivos_lista = os.listdir(carpeta_nombre)

for archivo_nombre in archivos_lista:
    print("\n", archivo_nombre)
    archivo = open(carpeta_nombre+archivo_nombre)
    lineas_lista= archivo.readlines()
    archivo.close()
    longitud = len(lineas_lista)
    print("El archivo", archivo_nombre, "tiene", longitud, "lineas")

    archivo = open(carpeta_nombre+archivo_nombre)
    texto = archivo.read()
    archivo.close()

    simbolos = ["(", ")", ",", ".", ";", ":", "/", "\""]
    for simbolo in simbolos:
        texto = texto.replace(simbolo," ")
    
    palabras_lista = texto.split()
    palabras_lista.sort()
    for palabra in palabras_lista:
        print(palabra)
    