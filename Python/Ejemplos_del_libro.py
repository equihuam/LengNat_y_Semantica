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
def diversidad_lexico (text):
    return len(text) / len(set(text))

def proporcion (conteo, total):
    return 100 * conteo / total

diversidad_lexico(text3)

proporcion(4,80)
    
# Para el ejemplo hay listas de palabras de ejemplo para cada texto
sent1

juntas = sent1 + sent2

juntas.append("mi texto")

# Estas listas están indizadas, empezando en 0
juntas[1]
juntas.index("Sussex")

text5[16715:16735]

# Intervalos abirertos
lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho"]

#del inicio hasta el tercer elemento
lista[:3]

# de la posición 6 (indice empieza en 0) hasta el final
lista[5:]

# El penúltimo elemento
lista[-2]

saying = ['After', 'all', 'is', 'said', 'and', 'done',
'more', 'is', 'said', 'than', 'done']

# Cuáles son las 50 palabras más frecuentes en Moby Dick? Es la función
# FreqDist de NLTK!!!!
frec_dist = FreqDist(text1)
vocabulario = frec_dist.keys()
vocabulario[:50]
frec_dist["whale"]

# Gráfica de frecuencia de palabras
frec_dist.plot(50, cumulative=True)

# Palabras raras "hapaxes"
frec_dist.hapaxes()

# Palabras con longitudes específicas. Primero convierto la lista en "conjunto"
V = set(text1)

# Uso una función implícita para seleccionar las palabras.
palabrota = [w for w in V if len(w) > 15]

# Palabras largas y frecuentes!!!!!
sorted(p for p in set(text1) if len(p) > 10 and frec_dist[p] >15)








