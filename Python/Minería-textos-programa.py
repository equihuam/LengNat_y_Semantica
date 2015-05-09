# -*- coding: utf-8 -*-
"""
Minería de texto para capturar los textos de los resumenes
del V Congreso Mexicano de Ecología (
San Luis Potosí abril-2015

Autor: Miguel Equihua Zamora
email: equihuam@gamil.com

"""

# Inicializa la librerías
import nltk
import re
import os # biblioteca de acceso a sistema operativo

# Abrir el archivo y leerlo en "texto"
# Los archivos de datos están en:
# Software-github/LengNat_y_Semantica/Datos y textos
os.getcwd() # directorio actual
rutaTextos = "C:/Users/Miguel/Documents/0 Versiones/1 Personales/Software-github/LengNat_y_Semantica/Datos y textos"
os.chdir(rutaTextos)
archivosTexto = os.listdir(rutaTextos)
archivo = open(archivosTexto[9],'r')
texto = archivo.readlines()
archivo.close()

# Lee linea por linea en texto hasta encontrar "Presentación" para separar
# el texto respectivo.
presentacion = texto[148:164]

# Elimina saltos de línea y junta todo en una sola línea de texto
espacioSep = " "
presentacion = espacioSep.join(linea.strip() for linea in presentacion)

# Corta los bloques de resumenes de  interés 
simposios = texto[1591:10608]
orales = texto[10710:33040]
carteles = texto[33150:60312]

# Limpieza y segmentación de los resumenes título, texto, palClv e ID
# Empieza por eliminar marcas de formato y espacios ed relleno
simposios = list((linea.strip("0123456789* \t\n") for linea in simposios))
orales = list((linea.strip("0123456789* \t\n") for linea in orales))
carteles = list((linea.strip("0123456789* \t\n") for linea in carteles))


# Concatenación de la lista en un solo bloque de texto corrido
simp = espacioSep.join(linea.strip() for linea in simposios)

# Uso de expresiones regulares para extraer los bloques de interés
# Selección del título
# Es un conjunto de caracteres en mayúscula. Hay que evitar leer el año 
# y la hora y unas NOM o NMX, que caben como un patrón válido, así como 
# unos agradecimientos al PAPIIT (ya los borré). Hay algunos títulos que 
# queda con una mayúscula suelta al final del texto. La r antes de las
# comillas indica interpretación directa ("raw") del texto.
regExp_sec = re.compile(r"(?! |IN207615|2015|,|[0-9]|AM|\n|[- ]{2,})([A-Z0-9ÁÉÍÓÚÑ:;¿\?\(\)\-\+\. ,]{25,})") 
ms =  regExp_sec.findall(simp)
titulosEnSimposios = list((linea[:-1].strip() for linea in ms))

# Elimino la mayúscula sueltaque queda al final de algunos títulos.
for i in range(len(titulosEnSimposios)):
    a = re.search(" +[A-Z]$", titulosEnSimposios[i])
    if a:
      titulosEnSimposios[i] = re.sub(a.group(0), "", titulosEnSimposios[i])

# Recortar el bloque de texto
# Está entre el correo electrónico del autor correspondiente e ID:
regExp_sec = re.compile(r"([\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}") 
regExp_sec = re.compile(r"(?<=@).*?(?= Palabras clave: )")
textosEnSimposios =  regExp_sec.findall(simp)


