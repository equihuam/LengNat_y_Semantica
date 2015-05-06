#*****************************************************************
#
# Análisis de contribuciones Congreso Mexicano Ecologia 2015
#
# Autor: Miguel Equihua
# Correo: equihuam@gmail.com
# Institución: Instituto de Ecología, AC
# 
#*****************************************************************

library("plyr")
library("reshape2")
library("ggplot2")
library ("tm")

# Lectura de datos y contenido ------------------------------------------
# ubicación de documentos en formato txt

directorio.actual <- getwd()
archivos.txt <- dir(directorio.actual, pattern = ".txt")

archivo.txt <- paste0(directorio.actual, "/", archivos.txt[4], sep="")

# Lee el archivo completo
texto <- paste0(scan(archivo.txt, what = character()), collapse = " ")

# Recorta sección de resúmenes de contribuciones en simposio
# Útilizo los números de línea en formato "###!" para recortar
a <- gregexpr("(?<=12!).*?(?= 5596!)", texto, perl=T)
simposio <- regmatches(texto, a)
simposio <- limpieza(simposio) 
write(simposio, "test.txt", sep = "")

# Organiza datos: título, textos, palabras clave e ID separados -------------
simposio.res <- strsplit(simposio, split = "Resumen:\n", perl = T)
simposio.res.df <- lapply(simposio.res, function (x) strsplit(x, "\n"))

# Usa "las pinzas plyR" para recuperar los datos en un data.frame
simposio.res.df <- ldply(simposio.res.df[[1]], 
                         function(x) c(tit=x[1], txt=x[2], clv=x[3], id=x[4]))
simposio.res.df <- simposio.res.df[-1,]
row.names(simposio.res.df) <- NULL
simposio.res.df[1,c(1,3,4)]
write.table(simposio.res.df, "simposio.dat", sep = "\t")

orales.res.df <- orales.res.df[-1,]
row.names(orales.res.df) <- NULL
orales.res.df[437,c(1,3,4)]

# simposio.res.df[[1]][grepl("MONITOREO BIOLÓGICO", simposio.res.df[[1]])]

# Recorta sección de resúmenes de contribuciones orales
# Útilizo los números de línea en formato "###!" para recortar
a <- gregexpr("(?<=5609!).*?(?=19445!)", texto, perl=T)
orales <- regmatches(texto, a)
orales <- limpieza.orales(orales) 
write(orales, "orales.txt", sep = "")

# Organiza datos: título, textos, palabras clave e ID separados -------------
orales.res <- strsplit(orales, split = "Resumen:\n", perl = T)
orales.res.df <- lapply(orales.res, function (x) strsplit(x, "\n"))

# orales.res.df[[1]][grepl("SÍNDROMES DE POLINIZACIÓN DE UNA", orales.res.df[[1]])]

# Usa "las pinzas plyR" para recuperar los datos en un data.frame
orales.res.df <- ldply(orales.res.df[[1]], 
                         function(x) c(tit=x[1], txt=x[2], clv=x[3], id=x[4]))
orales.res.df <- orales.res.df[-1,]
row.names(orales.res.df) <- NULL
orales.res.df[1,c(1,3,4)]
write.table(orales.res.df, "orales.dat", sep = "\t")


# Recorta sección de resúmenes de carteles. El bloque parece ser
# demasiado largo asi que lo divido en dos porciones.
# Útilizo los números de línea en formato "###!" para recortar
#gregexpr("(?<=19459!).*?(?=25276!)", texto, perl = T)
#gregexpr("36127!", texto, perl = T)

a <- gregexpr("(?<=19459!).*?(?=25276! )", texto, perl=T)
posters <- regmatches(texto, a)
#posters <- limpieza.posters(posters) 
write(posters, "posters.txt", sep = "")

# Organiza datos: título, textos, palabras clave e ID separados -------------
posters.res <- strsplit(posters, split = "Resumen:\n", perl = T)
posters.res.df <- lapply(posters.res, function (x) strsplit(x, "\n"))

# posters.res.df[[1]][grepl("SÍNDROMES DE POLINIZACIÓN DE UNA", posters.res.df[[1]])]
