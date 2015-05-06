archivos.txt <- dir(directorio.actual, pattern = ".txt")

archivo.txt.clp <- paste0(directorio.actual, "/", archivos.txt[2], sep="")

# Lee el archivo completo
texto.clp <- paste0(scan(archivo.txt.clp, what = character(), encoding = "UTF-8"), collapse = " ")

# Recorta sección de resúmenes de contribuciones en simposio
# Útilizo los números de línea en formato "###!" para recortar
gregexpr("\\b19488!", texto.clp)
a <- gregexpr("(?<=\\b19459!).*?(?=\\b19488!)", texto.clp, perl=T)
posters <- regmatches(texto, a)
#posters <- limpieza(posters) 

# Elimina membrete de Congreso Mexicano de Ecologia
posters <- gsub("Congreso[ \r\n]+Mexicano[ \r\n!]+Vde[ \r\n]+Ecología", " ", posters, perl=T)

write(posters, "poster-clp.txt", sep = "")
