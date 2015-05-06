# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es archivo temporal
"""

# Inicializa la librería nltk
import nltk

# descarga los anexos del libro de "Natural Language Processing"

nltk.download()

# Ejemplo de búsqueda de palabras en contexto
text1
text1.concordance("monstrous")
text1.concordance("sea")
text4.concordance("environment")
text4.concordance("earth")
text4.concordance("clean")

# Ejemplo de búsqueda de términos "similares"
text1.similar("monstrous")

# Se puede buscar el contexto que tienen en común un conjunto de términos
text2.common_contexts(["monstrous", "very"])

# Gráfica de dispersión de un términos. En qué posición aparecen en relación
# con el inicio del documento en una colección de documentos pegados en uno.
# Por ejemplo se puede explorar el uso de palabras en los últimos 220 años 
# en un texto construido artificialmente uniendo los textos de los discursos
# inaugurales de principio a fin uno detras de otro.
text4.dispersion_plot(["climate", "environment", "health", "earth", "clean"])

# Longitud de un texto
len(text3)

# Vocabulario de un texto
set(text3)
sorted(set(text3))
len(set(text3))

# Uso promedio de cada palabra
len(text3)/len(set(text3))

#Conteo del uso de una palabra o "token"
text3.count("smote")

# Definición de una función para calcular la probabilidad de uso de
# palabras en un texto






