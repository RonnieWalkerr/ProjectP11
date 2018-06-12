with open(snakemake.input[0],"r") as file:
    pmSplitDic = {}
    datalist = []
    for x in file:
        datalist.append(x)

    for j in range(len(datalist)):
        swapped = False
        i = 0
        while i<len(datalist)-1:
            pmline1 = len(datalist[i].split("\t")[3].split(","))
            pmline2 = len(datalist[i+1].split("\t")[3].split(","))
            if pmline1 > pmline2:
                 datalist[i], datalist[i+1] = datalist[i+1], datalist[i]
                 swapped = True
            i += 1
        if swapped == False:
             break
    print(datalist)

with open(snakemake.output[0], "w") as outfile:
    for x in datalist:
        outfile.write(x)
