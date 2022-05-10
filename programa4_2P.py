'''
Parcial 2
Actividad 4
Jazmin Azucena Gonzalez Peredia
'''

#Implementar 3 funciones nuevas

import nltk

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"
archivo_nombre = "doc_prog8.txt"

with open (carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")
texto_nltk = nltk.Text(tokens)
print("-------------------------------------------------------------\n")

'''
Imprime colocaciones derivadas del texto, ignorando palabras vacías. 
'''
print("Colocaciones: ")
texto_nltk.collocations()
texto_nltk.collocations(num=10, window_size=2)
print("-------------------------------------------------------------\n")

'''
Imprime texto aleatorio, generado usando un modelo de lenguaje de trigramas.
'''

print("Generar: ")
texto_nltk.generate(length=100, text_seed=None, random_seed=42)
print("-------------------------------------------------------------\n")

'''
Encuentra instancias de la expresión regular en el texto. El texto es una lista de tokens y un patrón de
expresión regular para que coincida una sola ficha debe estar rodeada por corchetes angulares.
'''

print("Encontrar todo: ")
texto_nltk.findall("<se.*>{2,}")
print("-------------------------------------------------------------\n")

