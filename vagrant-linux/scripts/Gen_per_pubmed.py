

with open(snakemake.input[0],"r") as file:
    pmSplitDic = {}
    for line in file:
        line = line.split("\t")
        geneID = line[0]
        pubmedIDs = line[3].split(",")
        for pm in pubmedIDs:
            if pm in pmSplitDic.keys():
                geneList = pmSplitDic[pm]
                geneList.append(geneID)
                pmSplitDic[pm] = geneList
            else:
                geneList = [geneID]
                pmSplitDic[pm] = geneList

with open(snakemake.output[0] ,"w") as outfile:
    for key in pmSplitDic.keys():
        pubmed = key
        genes = pmSplitDic[key]
        outfile.write(key + "\t")
        for x in genes:
            outfile.write(x + ",")
        outfile.write("\n")
