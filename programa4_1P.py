'''
Jazmin Azucena Gonzalez Peredia
Profesor: Oswaldo Carrillo Zepeda
Parcial 1
Actividad 4
'''

'''El ejercicio consiste en unir todos los documentos en uno solo'''

import os

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"
carpeta_salida = "/home/jazmin/Documentos/pln/documentos/"

archivo_salida = "UNION.txt"

archivos_lista = os.listdir(carpeta_nombre)

union = ""
for archivo_nombre in archivos_lista:
    archivo = open(carpeta_nombre + archivo_nombre)
    texto = archivo.read()
    archivo.close()
    union += texto


    with open(carpeta_salida + archivo_salida, "w") as salida:
        salida.write(union)

