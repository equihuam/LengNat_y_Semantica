# Usa el archivo basado en "doc"
texto <- paste0(scan(archivo.txt, what = character(), encoding = "UTF-8"), collapse = " ")

# Recorta sección de resúmenes de contribuciones en simposio
# Útilizo los números de línea en formato "###\t" para recortar
gregexpr(pattern = "12\t", text = texto, perl=T)

a <- gregexpr("(?<=12\t).*?(?=\b5596)", texto, perl=T)
simposio <- regmatches(texto, a)
simposio <- limpieza(simposio) 
write(simposio, "test.txt", sep = "")
nchar(texto)

grep("12\t", texto)
