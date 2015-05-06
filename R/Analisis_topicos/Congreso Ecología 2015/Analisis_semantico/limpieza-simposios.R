
limpieza <- function (tx)
{
  # Limpieza -------------
  
  # Elimina Congreso Mexicano de Ecologia
  tx <- gsub("Congreso[ \r\n]+Mexicano[ \r\n!]+Vde[ \r\n]+Ecología", " ", tx, perl=T)
  
  # Elimina rótulo sección:  Parte 1 
  tx <- gsub(" Parte [1-9]+", "\n", tx, perl=T)
  
  # Elimina números de línea
  tx <- gsub("[0-9]+!", " ", tx, perl=T)
  #write(tx, "test.txt", sep = "")
  
  #Separa el texto de interés que inicia tras el email
  tx <- gsub("[[:alnum:]\\.\\-]+@[[:alnum:]\\.]+[[:alnum:]\\.]+[[:alnum:]]*", "autoresfin\n", tx, perl=T)
  
  # Separa el título
  tx <- gsub("([ [:upper:][:punct:][:digit:]]*)!", "\nResumen: \n\\1\nautoresini", tx, perl=T)
  
  # Elimina colección de autores
  tx <- gsub("autoresini[[:space:]1-9[:alpha:][:punct:]]*autoresfin", "", tx, perl=T)
  
  # Elimina pleca de "-"
  tx <- gsub("[–]{2,}", "\n", tx, perl=T)
  
  # Elimina espacios sucesivos
  tx <- gsub("[ ]{2,}", "", tx, perl=T)
    
  # Agrega final de línea tras el identificador de la ponencia
  tx <- gsub("(ID:[0-9]+)", "\n\\1\n", tx, perl=T)
  
  # Elimino un patron de números "!!5 5 2 2 0 2 , 21 1" o "5 5 2 2 0 2 , 21 28"
  tx <- gsub("[!]*[ ]*[0-9][ ]+[0-9][ ]+[0-9][ ]+[0-9][ ]+[0-9][ ]+[0-9][ ]+\\,[ ]+[0-9]+[ ]+[0-9]+[ ]*\f", "\n", tx, perl=T)
  
  # Elimina "!" sueltos que quedan por ahí precedidos o seguidos o no de espacio.
  tx <- gsub("[ ]*![ ]*", "", tx, perl=T)
  
  # Corrije algunos resumenes que quedan con un espacio al inicio
  tx <- gsub("\n[ ]+", "\n", tx, perl=T)
  
  # Separa bolque de palabras clave y retiene sólo las palabras
  tx <- gsub("Palabras clave: ", "\n", tx, perl=T)
  
  # Elimina doble salto de línea
  tx <- gsub("[\n]{2,}", "\n", tx, perl=T)
  
  # Elimina identificador con fecha y datos de página
  tx <- gsub("(ID:[[:digit:]]+\n)[\f[:alnum:][:blank:][:punct:]]+(\nResumen:)", "\\1\\2\n", tx, perl=T)
  tx <- gsub("(ID:[[:digit:]]+\n)[\f[:alnum:][:blank:][:punct:]]+\n[[:alnum:][:blank:][:punct:]]+(\nResumen:)", "\\1\\2\n", tx, perl=T)
  
  # Elimina espacio antes de salto de línea
  tx <- gsub("[[:blank:]][\n]{1,}", "\n", tx, perl=T)
  
  # Elimina doble salto de línea
  tx <- gsub("[\n]{2,}", "\n", tx, perl=T)
  
  # Arreglo textos específicos que no supe como arreglar de otro modo
  tx <- gsub(" (DIVERSIDAD GENÉTICA DE LA PAPAYA SILVESTRE EN MÉXICO\n)(Resumen:\n)", "\\2\\1", tx, perl=T)
  
  # Elimino una fecha y texto que sobra al final
  tx <- gsub("miércoles, 22 de abril de 2015, 12:00:00 PM, Sala: 13tx: Resiliencia y conservación de ecosistemas ribereños en zonas áridas\n", "", tx, perl=T)

  # Elimina marcadores de "form feed" que quedan en el texto
  tx <- gsub("\f\n", "", tx, perl=T)
  
}
