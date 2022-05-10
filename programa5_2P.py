'''
Parcial 2
Actividad 5
Jazmin Azucena Gonzalez Peredia
'''

#Palabras funcionales 
#descargar el paquete “stopwords”

import nltk

print("Jazmin Azucena Gonzalez Peredia")

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"
archivo_nombre = "texto1.txt"

with open (carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()

print("------------------------------------------------------")
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    '''print(palabras_funcional)'''

print("------------------------------------------------------")
tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = []

for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)
        '''print(tokens_limpios)'''
print(len(tokens))
print(len(tokens_limpios))
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)