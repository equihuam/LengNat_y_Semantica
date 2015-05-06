# Ejemplo tomado de
# A Delicious Analysis! (aka topic modelling using recipes)
# February 17, 2014
#By inkhorn82
# http://www.r-bloggers.com/a-delicious-analysis-aka-topic-modelling-using-recipes/
#

library(tm)
library(topicmodels)

dir.recetas <- "C:/Users/equih_000/Documents/1 Versiones/3 Personales/Juls - Modelos/LDA/scirep-cuisines-detail/"
recipes <- readLines(paste(dir.recetas, "recipes combined.tsv", sep=""))

# Once I read it into R, I have to get rid of the /t
# characters so that it's more acceptable to the tm package

recipes.new <- apply(as.matrix(recipes), 1, function (x) gsub('\t',' ', x))

recipes.corpus <- Corpus(VectorSource(recipes.new))
recipes.dtm <- DocumentTermMatrix(recipes.corpus)

# Now I filter out any terms that have shown up in less than 10 documents

# recipes.dict = Dictionary(findFreqTerms(recipes.dtm,10)) ya no se usa en tm
# nueva solución
recipes.dict <- findFreqTerms(recipes.dtm, 10)
# inspect(DocumentTermMatrix(recipes.corpus, list(dictionary = recipes.dict)))
recipes.dtm.filtered <- DocumentTermMatrix(recipes.corpus, list(dictionary = recipes.dict))

# Here I get a count of number of ingredients in each document
# with the intent of deleting any documents with 0 ingredients

ingredient.counts <- apply(recipes.dtm.filtered, 1, function (x) sum(x))
recipes.dtm.filtered <- recipes.dtm.filtered[ingredient.counts > 0,]

# Here i get some simple ingredient frequencies so that I can plot them and decide 
# which I'd like to filter out

recipes.m <- as.matrix(recipes.dtm.filtered)
popularity.of.ingredients <- sort(colSums(recipes.m), decreasing=TRUE)
popularity.of.ingredients <- data.frame(ingredients = names(popularity.of.ingredients), num_recipes=popularity.of.ingredients)
popularity.of.ingredients$ingredients <- reorder(popularity.of.ingredients$ingredients, popularity.of.ingredients$num_recipes)

library(ggplot2)

ggplot(popularity.of.ingredients[1:30,], aes(x=ingredients, y=num_recipes)) + geom_point(size=5, colour="red") + coord_flip() +
  ggtitle("Recipe Popularity of Top 30 Ingredients") + 
  theme(axis.text.x=element_text(size=13,face="bold", colour="black"), 
        axis.text.y=element_text(size=13,colour="black", face="bold"), 
        axis.title.x=element_text(size=14, face="bold"), 
        axis.title.y=element_text(size=14,face="bold"),
        plot.title=element_text(size=24,face="bold"))

# Having found wheat, egg, and butter to be the three most frequent ingredients
# (and not caring too much about them as ingredients in general) I remove them 
# from the corpus and redo the document term matrix

recipes.corpus <- tm_map(recipes.corpus, removeWords, c("wheat","egg","butter"))  # Go back to line 6
recipes.dtm.final <- DocumentTermMatrix(recipes.corpus, list(dictionary = recipes.dict))

# Finally, I run the LDA and extract the 5 most
# characteristic ingredients in each topic... yummy!

recipes.lda <- LDA(recipes.dtm.filtered, 50)
t <- terms(recipes.lda,5)
t[,5]
