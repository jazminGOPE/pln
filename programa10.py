'''
Parcial 2
Actividad 4
Jazmin Azucena Gonzalez Peredia
'''

#Implementar 3 funciones nuevas

#Obtener sinonimos y antonimos.

'''Esta funcion se trabaja unicamente con el modulo corpus, con la funcion wordnet
WordNet es una base de datos creada para el procesamiento del lenguaje natural. 
Incluye un grupo de sinónimos y una breve definición de algunas palabras.
'''

from nltk.corpus import wordnet

#Definicion y ejemplos de pain (dolor)
syn = wordnet.synsets('pain')
print(syn[0].definition())
print(syn[0].examples())

#El resultado será:
'''
a symptom of some physical hurt or disorder
['the patient developed severe pain and distension']
'''

    # Obtener sinónimos de computer (computadora)
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

#El resultado será:
'''
['computer', 'computing_machine', 'computing_device', 'data_processor', 'electronic_computer',
'information_processing_system', 'calculator', 'reckoner', 'figurer', 'estimator', 'computer']
'''

    # Obtener antónimos de small (pequeño)
antonyms = []
for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)

#El resultado será:
'''
['large', 'big', 'big']
'''
