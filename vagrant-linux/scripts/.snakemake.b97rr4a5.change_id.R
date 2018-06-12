
######## Snakemake header ########
library(methods)
Snakemake <- setClass(
    "Snakemake",
    slots = c(
        input = "list",
        output = "list",
        params = "list",
        wildcards = "list",
        threads = "numeric",
        log = "list",
        resources = "list",
        config = "list",
        rule = "character"
    )
)
snakemake <- Snakemake(
    input = list('data/RNA-Seq-counts.txt'),
    output = list('data/output_newIDs.txt'),
    params = list(),
    wildcards = list(),
    threads = 1,
    log = list(),
    resources = list(),
    config = list(),
    rule = 'ID_transfer'
)
######## Original script #########
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

