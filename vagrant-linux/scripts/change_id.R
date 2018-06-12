#install.packages("rentrez")
library("rentrez")


file = read.table(snakemake@input[[1]], header=TRUE) #input file
fileConn <-(snakemake@output[[1]]) #output file
testset = file[1:100,]

geneID <- 0
for (i in 1:nrow(testset)){
  id <- testset[i,1]
  r_search <- entrez_search(db="gene", term=id)
  geneID[i] <- r_search$ids
  
}
write.table(data.frame(geneID,testset[,1]), fileConn, sep="\t", row.names = FALSE, col.names = FALSE, quote = FALSE)

