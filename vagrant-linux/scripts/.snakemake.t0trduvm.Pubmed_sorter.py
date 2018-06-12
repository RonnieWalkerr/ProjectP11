
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0bX\x16\x00\x00\x00./data/sorted_data.txtq\x0ca}q\rh\x07}q\x0esbX\x07\x00\x00\x00threadsq\x0fK\x01X\t\x00\x00\x00resourcesq\x10csnakemake.io\nResources\nq\x11)\x81q\x12(K\x01K\x01e}q\x13(X\x06\x00\x00\x00_coresq\x14K\x01X\x06\x00\x00\x00_nodesq\x15K\x01h\x07}q\x16(h\x15K\x00N\x86q\x17h\x14K\x01N\x86q\x18uubX\x06\x00\x00\x00configq\x19}q\x1aX\x05\x00\x00\x00inputq\x1bcsnakemake.io\nInputFiles\nq\x1c)\x81q\x1d}q\x1eh\x07}q\x1fsbX\x06\x00\x00\x00paramsq csnakemake.io\nParams\nq!)\x81q"}q#h\x07}q$sbX\x03\x00\x00\x00logq%csnakemake.io\nLog\nq&)\x81q\'}q(h\x07}q)sbX\x04\x00\x00\x00ruleq*X\t\x00\x00\x00sort_dataq+ub.')
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
