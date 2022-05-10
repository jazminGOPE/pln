'''
Parcial 2
Actividad 2
Jazmin Azucena Gonzalez Peredia
'''

import nltk

carpeta_nombre = "/home/jazmin/Documentos/pln/documentos/"
archivo_nombre = "doc_prog8.txt"

with open (carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")
'''for token in tokens:
    print(token)'''

palabras_total = len(tokens)
print("palabras totales: ", palabras_total)

tokens_conjunto = set(tokens)
palabras_diferentes = len(tokens_conjunto)
print("Palabras diferentes: ", palabras_diferentes)

riqueza_lexica = palabras_diferentes/palabras_total
print("Riqueza lexica: ", riqueza_lexica)
riqueza_lexicap = 100*palabras_diferentes/palabras_total
print("Riqueza lexica: ", riqueza_lexicap, "%", "\n")
print("-------------------------------------------------------------")

texto_nltk = nltk.Text(tokens)
palabra = input("Escribe la palabra a buscar en el documento: " )

print("CONCORDANCE: \n")
texto_nltk.concordance(palabra)
print("-------------------------------------------------------------")

print ("PALABRAS SIMILARES: \n")
texto_nltk.similar(palabra)
print("-------------------------------------------------------------")

conteo_individual = tokens.count(palabra)
print("Numero de veces que se encuentra la palabra: '", palabra, "'en el texto: ", conteo_individual)