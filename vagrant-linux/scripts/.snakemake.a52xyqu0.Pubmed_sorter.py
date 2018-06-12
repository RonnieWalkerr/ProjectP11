
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_coresq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x07K\x00N\x86q\x0bh\x08K\x01N\x86q\x0cuubX\x06\x00\x00\x00configq\r}q\x0eX\x06\x00\x00\x00outputq\x0fcsnakemake.io\nOutputFiles\nq\x10)\x81q\x11X\x16\x00\x00\x00./data/sorted_data.txtq\x12a}q\x13h\t}q\x14sbX\x03\x00\x00\x00logq\x15csnakemake.io\nLog\nq\x16)\x81q\x17}q\x18h\t}q\x19sbX\x07\x00\x00\x00threadsq\x1aK\x01X\t\x00\x00\x00wildcardsq\x1bcsnakemake.io\nWildcards\nq\x1c)\x81q\x1d}q\x1eh\t}q\x1fsbX\x06\x00\x00\x00paramsq csnakemake.io\nParams\nq!)\x81q"}q#h\t}q$sbX\x05\x00\x00\x00inputq%csnakemake.io\nInputFiles\nq&)\x81q\'}q(h\t}q)sbX\x04\x00\x00\x00ruleq*X\t\x00\x00\x00sort_dataq+ub.')
######## Original script #########
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
