'''
Jazmin Azucena Gonzalez Peredia
Profesor: Oswaldo Carrillo Zepeda
'''

'''Obtener el vocabulario de todos los documentos'''

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"
archivo_nombre = "texto2.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
        texto = archivo.read()

simbolos = ["(", ")", ",", ".", ";", ":", '""', '.', "-", "\""]

for simbolo in simbolos:
    texto = texto.replace (simbolo, " ")

palabras_lista = texto.split()

palabras_unicas = []

for palabra in palabras_lista:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)
print(palabras_unicas)
num = len(palabras_unicas)
print("Numero de palabras unicas en el documento: ", num)
num2 = len(palabras_lista)  
print("Numero de palabras de todo el documento: ", num2)  
