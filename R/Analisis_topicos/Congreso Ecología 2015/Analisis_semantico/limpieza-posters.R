a <- gregexpr("(?<=19459!).*?(?=24275! )", texto, perl=T)
posters <- regmatches(texto, a)
write(posters, "posters.txt", sep = "")



# Elimina número de página y salto de página [[1-9]+[:space:]*]?\f 
# y saltos de página sueltos por ahí.
posters <- gsub("[1-9]+[:space:]+\f", "\n", posters, perl=T)
posters <- gsub("[[:space:]+]?\f", "\n", posters, perl=T)

# Elimina números de línea
posters <- gsub("[0-9]+!", "", posters, perl=T)

# Elimina un espacio al inicio del texto
posters <- gsub("^ ", "", posters, perl=T)

# Elimina membrete de Congreso Mexicano de Ecologia
#(ID:[1-9]+)[ a-zA-Z,0-9áéíóóñ:]+[_ ]+(! ! [0-9]+ Congreso Mexicano de Ecología V[ ]+)
# [[:alnum:] :,]+[_ ]+(! ! [0-9]+ Congreso Mexicano de Ecología V[ ]+)
posters <- gsub("(ID:[1-9]+)[ ]+(lunes|martes|miércoles|jueves), (20|21|22|23) de abril de 2015  Mampara [0-9]+ Eje temático: [[:alpha:] ]*", "\\1\n", posters, perl=T)
#posters <- gsub("(! ! [0-9]+ Congreso Mexicano de Ecología V[ ]+)", "\\1\n", posters, perl=T)
#posters <- gsub("Congreso[ \n]+Mexicano[ \n!]+Vde[ \n]+Ecología", " ", posters, perl=T)

# Elimina series de espacios al principio de línea
posters <- gsub("([ ]{60,}|[ ]*[_]{40,})([ ]*[!]*[ ]*[\f]?[ ]*[!]*[ ]*)", "\n", posters, perl=T)

# Separa el título ([“”\u \.,;:\-\\(\\)]{17,})!?[[ ]+]?
posters <- gsub("([[:upper:][:punct:][:digit:][:blank:]]{10,})[ ]*![ ]*", "\nResumen:\n\\1\nautoresini", posters, perl=T)
posters <- gsub("([[:upper:][:punct:][:digit:][:blank:]]{10,})[ ]{4,}",   "\nResumen:\n\\1\nautoresini", posters, perl=T)

#Separa el texto de interés que inicia tras el email
posters <- gsub("[[:alnum:]\\.-_]+@[[:alnum:]\\.]+[[:alnum:]]+[\\.[:alnum:]*]?", "autoresfin", posters, perl=T)

# Elimina colección de autores (inicia con 517 lineas)
posters <- gsub("autoresini.*autoresfin", "", posters, perl=T) 

# Separa bloque de palabras clave y retiene sólo las palabras (517 lineas)
posters <- gsub("Palabras clave: ", "\n", posters, perl=T)

# Separa el identificador de la ponencia (883 lineas)
posters <- gsub("[[:space:][:punct:]!]*(ID:[ ]*[0-9]+)", "\n\\1 iniMarcaFechaLugarEje", posters, perl=T)

# Elimina fecha, lugar, eje, etc. (922 lineas)
posters <- gsub("[ ]?iniMarcaFechaLugarEje.*[[:space:]]*(Resumen:)[ ]?", "\n\\1", posters, perl=T)

# Limpia las marcas al final del documento
posters <- gsub("[ ]?iniMarcaFechaLugarEje[[:alnum:][:punct:][:space:]]+", "", posters, perl=T)

# Elimina espacios múltiples entre palabras
#posters <- gsub("^[ ]?(Resumen:) ", "\\1", posters, perl=T)
#posters <- gsub("[ ]{2,}", " ", posters, perl=T)

write(posters, "posters.txt", sep = "") # 928 líneas final

