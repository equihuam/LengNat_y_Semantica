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
import csv

# --------------------  Expresión Regular -----------------------------
# Prepara el código de expresión regular para la selección del título
# Es un conjunto de caracteres en mayúscula. Hay que evitar leer el año 
# y la hora y unas NOM o NMX, que caben como un patrón válido, así como 
# unos agradecimientos al PAPIIT (ya los borré).La r antes de las
# comillas indica interpretación directa ("raw") del texto.

# Gracias a consejo de sln en http://stackoverflow.com/questions/30142018
# "(?<![A-Z0-9ÁÉÍÓÚÑ:;¿?()+.,])((?!(?:NOM-059-SEMARNAT|NOM-059 SEMARNAT 2010:|DAP-|GATA|NOM-059-2010-SEMARNAT))[A-ZÁÉÍÓÚÑ¿\"](?:(?!(?:[-]{2,}|-2010|GATA|NOM\-059\-SEMARNAT))[A-Z0-9ÁÉÍÓÚÑ&:;¿?()´\-+. ,\"]){19,}(?<=[A-ZÁÉÍÓÚÑ?&\"\-´ ]))(?![a-z])"

# No es necesaria esta separación de componentes, pero es didáctico aquí!!!
# Construcción de la expresión regular para recuperar títulos
# Ve (hacia atras, sin seleccionar: "?<") - Que no ("!") inicie en medio de algo
RE_capturaTitulo = (
  r"(?<![A-Z0-9ÁÉÍÓÚÑÇÃ×:;¿?()+.,])" + # No hay nada antes del texto
  r"(" + # Inicia la construcción del grupo 1
     r"(?!" + # Ve hacia adelante que no inicie con nada como lo que sigue
        r"(?:" + # Agrupa sin capturar lo que sigue (añadir lo necesario)
           # Colección de términos y frases a omitir de la captura 
           r"MATERIALES Y METODOS|MATERIALES Y MÉTODOS.|NOM-059-SEMARNAT|" +
           r"NOM-059 SEMARNAT 2010:|DAP-|GATA|NOM-059-2010-SEMARNAT|ICRR|" + 
           r"NOM- 059- ECOL-2001.|AS: 10-6M, 10-7M, 10-8|CONAFOR-CONACYT" +
     r"))" + # Cierra la exploración y el grupo de cosas por evitar

     # Define como empieza la captura: Inicia con una letra incluso con acento
     # o comillas o abre interrogación
     r"[A-ZÁÉÍÓÚÑÇÃ×¿\"]" + # Inicia la captura con alguno de estos caracteres

     # Inicia el grupo de captura 
     r"(?:"  + # agrupa sin capturar lo que sigue (al menos 19 veces)
        # El grupo de captura no puede contener lo que se anota en este conjunto
        r"(?!" + # ve hacia adelante que no haya lo que sigue
           r"(?:" + # agrupa sin capturar lo que hay que evitar
              r"[-]{2,}|-2010|GATA40|GATA16|IAN873,|IAN710,|RRIM600,|PB260" + 
              r"NOM\-059\-SEMARNAT|NOM\- 059\- ECOL-2001.|ICRR" + # Omitir esto
        r"))" + # cierra el grupo de cosas a evitar y el conjunto que lo define
        r"[A-Z0-9ÁÉÍÓÚÑÇÃ×&:;¿?()´\-+. ,\"]" + # Esto es lo que hay que capturar
     r"){19,}" + # Cierra agrupa 2 y captura repetida al menos 19 veces.
   r"(?<=[A-ZÁÉÍÓÚÑÇÃ×?&\"\-´ ])" + # ve hacia atras que el grupo incluya alguno de estos
   r")" + # Termina el grupo de captura 
   r"(?![a-záéíóú])") # El patrón concluye al encontrar una minúscula tras la captura

# Prepara la captura del título
regExpTitulo = re.compile(RE_capturaTitulo) 

# Expresión regular para capturar el identificador del resumen
regExpID = re.compile(r"(ID:[ 0-9]+)") 

# Expresión regular para capturar las palabras clave
regExpClv = re.compile(r"(?<=Palabras clave: ).*?(?=ID:)") 

# Recupera el título del simposio como equivalente a "eje temático"
regExpSimp = re.compile(r"(?<=Simposio: )(.*?)(?=(?:[ A-Z]{4,}|Parte [0-9]|  Congreso|[ -]{4,}))")

# Recortar el bloque de texto que está entre el correo electrónico 
# del autor correspondiente e ID:
regExpTexto = re.compile(r"(?<=@).*?(?= Palabras clave: )")

# Recupera el eje temático de presentaciones orales y carteles
regExpEje = re.compile(r"(?<=Eje temático: )(.*?)(?=(?:[ A-Z]{4,}|  Congreso|[ -]{4,}))")

# ------------------- Localización de archivos de texto --------------------
# Los archivos de datos están en:
# Software-github/LengNat_y_Semantica/Datos y textos
# Abrie el archivo y carga en "texto"
os.getcwd() # directorio actual
rutaBase = "C:/Users/Miguel/Documents/0 Versiones/1 Personales/Software-github/"
rutaTextos = "LengNat_y_Semantica/Datos y textos"
os.chdir(rutaBase + rutaTextos)
archivosTexto = os.listdir(rutaBase + rutaTextos)
archivosTexto.index("memorias_en_edicion_doc.txt")
archivo = open("memorias_en_edicion_doc.txt",'r')
texto = archivo.readlines()
archivo.close()

# ---------  Segmentación por bloques de contenido ---------------------
# -------- presentación, simposios, orales y carteles ------------------

# Corta los bloques de  interés 
presentacion = texto[148:166]
simposios = texto[1591:10611]
orales = texto[10712:33043]
carteles = texto[33152:60329]

# ------------------------ Presentación  ---------------------------
# Elimina saltos de línea y junta todo en una sola línea de texto
espacioSep = " "
presentacion = espacioSep.join(linea.strip() for linea in presentacion)

presentacionDatos = [r"presentacion", r"ID:0", r"Presentación", r"Presentacion", r"Fronteras de la Ecología, Mundo Globalizado", presentacion]

# Escribe el bloque de orales al disco en formato csv
with open(u"presentación.csv", "wb") as f:
        w = csv.writer(f, dialect = "excel-tab")
        w.writerow(presentacionDatos)

# Limpieza y segmentación de los resumenes título, texto, palClv e ID
# Empieza por eliminar marcas de formato y espacios ed relleno
simposios = [linea.lstrip("[0123456789* \t\n") for linea in simposios]
orales = [linea.lstrip("^0123456789* \t\n") for linea in orales]
carteles = [linea.lstrip("^0123456789* \t\n") for linea in carteles]

# Hubo 33 sesiones de simposio
# Se reportan los siguientes números de presentaciones:
# 192 en simposio , 478 orales y 553 carteles
# Pero recupero del documento de resumenes:
# 186 en simposio, 451 orales y 547 carteles

# --------------- Simposios ----------------

# Concatenación de la lista en un solo bloque de texto corrido
simpTexto = espacioSep.join(linea.strip() for linea in simposios)

# Uso expresiones regulares para extraer los bloques de interés
# del texto corrido de simposios contenido en simpTexto

# Recupera el identificador del resumen 
simpID =  regExpID.findall(simpTexto)

# Recupera las palabras clave
simpPalClv = regExpClv.findall(simpTexto)

# Recupera el eje temático
simpTema = regExpSimp.findall(simpTexto)

# Selección del título: usa la expresión regular preparada al principio!
simpTitulos =  regExpTitulo.findall(simpTexto)

# Recortar el bloque de texto del resumen
simpResumen =  regExpTexto.findall(simpTexto)

# Elimina el residuo de email que quedó al inicio de los resumenes
simpResumen = [re.sub("^[a-z\. ]+", "", t) for t in simpResumen]

# Combina los datos en una lista anidada
simpDatos = zip(simpID, simpTema, simpTitulos, simpPalClv, simpResumen)
simpDatos = [["simposio"]+list(fila) for fila in simpDatos]

# Escribe el bloque de simposios al disco en formato csv
with open("simposios.csv", "wb") as f:
        w = csv.writer(f, dialect = "excel-tab")
        for fila in simpDatos:        
           w.writerow(fila)
        

# --------------- orales ----------------

# Concatenado de los textos en un solo bloque corrido de orales
oralTexto = espacioSep.join(linea.strip() for linea in orales)

# Recupera el identificador del resumen 
oralID =  regExpID.findall(oralTexto)

#Extrae las palabras clave
oralPalClv = regExpClv.findall(oralTexto)

# Recupera el eje temático
oralEje = regExpEje.findall(oralTexto)

# Recupera los títulos de los resúmenes
oralTitulos =  regExpTitulo.findall(oralTexto)
oralTitulos = [t.strip() for t in oralTitulos]

# Extrae los textos de los resumenes
oralResumen =  regExpTexto.findall(oralTexto)

# Elimina el residuo de email que quedó al inicio de los resumenes
oralResumen = [re.sub("^[a-z\. ]+", "", t) for t in oralResumen]

# Combina los datos en una lista anidada
oralDatos = zip(oralID, oralEje, oralTitulos, oralPalClv, oralResumen)
oralDatos = [["oral"]+list(fila) for fila in oralDatos]

# Escribe el bloque de orales al disco en formato csv
with open("orales.csv", "wb") as f:
        w = csv.writer(f, dialect = "excel-tab")
        for fila in oralDatos:        
           w.writerow(fila)

# --------------- Carteles ----------------

# Inicia en línea 33153 del documento fuente
# Concatenado de los textos en un solo bloque corrido de orales
cartelTexto = espacioSep.join(linea.strip() for linea in carteles)

# Recupera el identificador del resumen 
cartelID =  regExpID.findall(cartelTexto)

# Recupera las palabras clave
cartelPalClv = regExpClv.findall(cartelTexto)

# Recupera el eje temático
cartelEje = regExpEje.findall(cartelTexto)

# Selección del título: usa la expresión regular preparada al principio!
cartelTitulos =  regExpTitulo.findall(cartelTexto)

# Recortar el bloque de texto
# Está entre el correo electrónico del autor correspondiente e ID:
cartelResumen =  regExpTexto.findall(cartelTexto)

# Elimina el residuo de email que quedó al inicio de los resumenes
# Probelmas identificado: -noroeste.org (línes 258)  
#                         165edu.mx (línea 95)
cartelResumen = [re.sub("^[a-z0-9\-\. ]+", "", t) for t in cartelResumen]

# Combina los datos en una lista anidada
cartelDatos = zip(cartelID, cartelEje, cartelTitulos, cartelPalClv, cartelResumen)
cartelDatos = [["cartel"]+list(fila) for fila in cartelDatos]

# Escribe el bloque de carteles al disco en formato csv
with open("carteles.csv", "wb") as f:
        w = csv.writer(f, dialect = "excel-tab")
        for fila in cartelDatos:        
           w.writerow(fila)

#  --------------------------   Todo Junto  -------------------------------

# Junta todos los bloques en uno solo
todoDatos = [presentacionDatos] + simpDatos + oralDatos + cartelDatos

# Escribe el paquete completo con todo junto al disco en formato csv
with open("todo.csv", "wb") as f:
        w = csv.writer(f, dialect = "excel-tab")
        for fila in todoDatos:        
           w.writerow(fila)
