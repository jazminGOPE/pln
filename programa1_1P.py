'''
Jazmin Azucena Gonzalez Peredia
Profesor: Oswaldo Carrillo Zepeda
Parcial 1
Actividad 1
'''

print("Procesamiento del lenguaje natural")

suma = 7 + 5
resultado = suma * 5

print(suma)
print("Resultado =", resultado)

print("-----------------------------------------------------")
archivo = open("/home/jazmin/Documentos/pln/prog123/prog.txt")
print(archivo.read())
archivo.close()

archivo2 = open("/home/jazmin/Documentos/pln/prog123/document.txt", "w")
cadena1 = "primer clase de programación python en procesamiento"
archivo2.write(cadena1)

archivo2 = open("/home/jazmin/Documentos/pln/prog123/document.txt")
print(archivo2.read())
archivo2.close()