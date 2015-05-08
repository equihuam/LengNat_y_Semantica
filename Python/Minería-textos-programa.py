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
rutaTextos = "C:/Users/Miguel/Documents/0 Versiones/1 Personales/Software-github\LengNat_y_Semantica\Datos y textos"
os.chdir(rutaTextos)
archivosTexto = os.listdir(rutaTextos)
archivo = open(archivosTexto[9],'r')
texto = archivo.readlines()

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

simp = espacioSep.join(linea.strip() for linea in simposios)
s = re.sub("^[A-Z0-9ÁÉÍÓÚÑ ,:]+","\1{tit}" simp)

"ID:" in simposios[25] 

# Separa los títulos
titulo = []
lineasConsecutivas = False 
for i in range(len(simposios)):
    if simposios[i].isupper() and "ID:" not in simposios[i]:
        if lineasConsecutivas:
            texto = texto + " " + simposios[i]
        titulo.append(simposios[i])  
        lineasConsecutivas = not lineasConsecutivas


