#source('http://bioconductor.org/biocLite.R')

# biocLite('KEGGREST')
library('KEGGREST')

file = read.table(snakemake@input[[1]], sep="\t", quote = "") #input file
fileOut <-(snakemake@output[[1]]) #output file
output = file
lastcollum = ncol(output) +1
genes <- file[2]


for(i in 1:nrow(genes)){
  gene <- genes[i,1]
  try(query <- keggGet(c(paste('lpl:', gene, sep=''))), silent=F)
  if(exists('query')){
    pathways <- query[[1]]$PATHWAY
    if(!is.null(pathways)){
      
      outputpath <- toString(names(pathways))
      outputpath <- gsub(" ", "", outputpath)
    }
    else{
      outputpath = "-"
    }
    output[i,lastcollum] = outputpath
  }
}

write.table(output, fileOut, sep="\t", row.names = FALSE, col.names = FALSE, quote = FALSE)