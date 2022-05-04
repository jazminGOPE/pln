'''
Jazmin Azucena Gonzalez Peredia
Profesor: Oswaldo Carrillo Zepeda
'''

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"
archivo_nombre = "servidor.txt"
palabra = input("Escribe la palabra a buscar en el documento: ")


'''palabra1 = "acuerdo"
palabra2 = "RESOLUCION"'''

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

    if palabra in texto:
        print("La palabra: ", palabra, "fue encontrada en el texto")

    else:
        print("La palabra: ", palabra, "no fue encontrada en el texto")