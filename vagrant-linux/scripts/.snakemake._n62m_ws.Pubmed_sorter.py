
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00outputq\x04csnakemake.io\nOutputFiles\nq\x05)\x81q\x06X\x16\x00\x00\x00./data/sorted_data.txtq\x07a}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\t\x00\x00\x00resourcesq\x0bcsnakemake.io\nResources\nq\x0c)\x81q\r(K\x01K\x01e}q\x0e(X\x06\x00\x00\x00_coresq\x0fK\x01X\x06\x00\x00\x00_nodesq\x10K\x01h\t}q\x11(h\x10K\x00N\x86q\x12h\x0fK\x01N\x86q\x13uubX\x05\x00\x00\x00inputq\x14csnakemake.io\nInputFiles\nq\x15)\x81q\x16}q\x17h\t}q\x18sbX\x03\x00\x00\x00logq\x19csnakemake.io\nLog\nq\x1a)\x81q\x1b}q\x1ch\t}q\x1dsbX\x06\x00\x00\x00configq\x1e}q\x1fX\x06\x00\x00\x00paramsq csnakemake.io\nParams\nq!)\x81q"}q#h\t}q$sbX\x04\x00\x00\x00ruleq%X\t\x00\x00\x00sort_dataq&X\t\x00\x00\x00wildcardsq\'csnakemake.io\nWildcards\nq()\x81q)}q*h\t}q+sbub.')
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
