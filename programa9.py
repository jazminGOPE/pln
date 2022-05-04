'''
Parcial 2
Actividad 3
Jazmin Azucena Gonzalez Peredia
'''

#hapax es una palabra que aparece solo una vez en el texto.

import nltk
import matplotlib.pyplot as plt

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"
archivo_nombre = "doc_prog8.txt"

with open (carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()
print("--------------------------------------------------------------------")

tokens = nltk.word_tokenize(texto, "spanish")

tokens_conjunto = set(tokens)
palabras_total = len(tokens)
palabras_diferentes = len(tokens_conjunto)

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto_nltk)
print("palabras totales: ", palabras_total)
print("Palabras diferentes: ", palabras_diferentes)

print("--------------------------------------------------------------------")
hapaxes = distribucion.hapaxes()
for hapax in hapaxes:
    print(hapax)

from matplotlib import rcParams
rcParams.update({"figure.autolayout": True})
distribucion.plot(cumulative=True)
distribucion.plot(40, cumulative=True)
