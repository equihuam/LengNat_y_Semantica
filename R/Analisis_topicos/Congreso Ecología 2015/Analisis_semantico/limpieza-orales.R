limpieza.orales <- function (tx)
{
  
  # Elimina membrete de Congreso Mexicano de Ecologia
  tx <- gsub("Congreso[ \r\n]+Mexicano[ \r\n!]+Vde[ \r\n]+Ecología", " ", tx, perl=T)
  
  # Elimina números de línea
  tx <- gsub("[0-9]+!", " ", tx, perl=T)
  
  # Elimina series de espacios al principio de línea
  tx <- gsub("([ ]{60,}|[ ]*[–]{40,})([ ]*[!]*[ ]*[\f]*[ ]*[!]*[ ]*)", "\n", tx, perl=T)
  
  # Separa el título
  tx <- gsub("([[:upper:][:punct:][:digit:][:blank:]]{10,})[ ]*![ ]*", "\nResumen: \n\\1\nautoresini", tx, perl=T)
  tx <- gsub("([[:upper:][:punct:][:digit:][:blank:]]{10,})[ ]{4,}", "\nResumen: \n\\1\nautoresini", tx, perl=T)
  
  #Separa el texto de interés que inicia tras el email
  tx <- gsub("[[:alnum:]\\.\\-]+@[[:alnum:]\\.]+[[:alnum:]\\.]+[[:alnum:]]*[ ]*", "autoresfin", tx, perl=T)
  
  # Elimina colección de autores
  tx <- gsub("autoresini[[:space:]1-9[:alpha:][:punct:]]*autoresfin", "", tx, perl=T)
  
  # Separa bloque de palabras clave y retiene sólo las palabras
  tx <- gsub("Palabras clave: ", "\n", tx, perl=T)
  
  # Separa el identificador de la ponencia
  tx <- gsub("[[:space:][:punct:]!]*(ID:[ ]*[0-9]+)", "\n\\1 iniMarcaFechaLugarEje", tx, perl=T)
  
  # Elimina fecha, lugar, eje, etc.
  tx <- gsub("[ ]*iniMarcaFechaLugarEje.*[\n]*(Resumen:)[ ]?", "\n\\1", tx, perl=T)
  
  # Limpia las marcas al final del documento
  tx <- gsub("[ ]?iniMarcaFechaLugarEje[[:alnum:][:punct:][:blank:]]+", "", tx, perl=T)
  
  # Elimina espacios múltiples entre palabras
  tx <- gsub("^[[:space:]]{2,}(Resumen:) ", "\\1", tx, perl=T)
  tx <- gsub("[ ]{2,}", " ", tx, perl=T)
}
