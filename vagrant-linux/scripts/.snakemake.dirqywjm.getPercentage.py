
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0bX\x17\x00\x00\x00./data/sorted_data2.txtq\x0ca}q\rh\x07}q\x0esbX\x07\x00\x00\x00threadsq\x0fK\x01X\t\x00\x00\x00wildcardsq\x10csnakemake.io\nWildcards\nq\x11)\x81q\x12}q\x13h\x07}q\x14sbX\x06\x00\x00\x00paramsq\x15csnakemake.io\nParams\nq\x16)\x81q\x17}q\x18h\x07}q\x19sbX\x03\x00\x00\x00logq\x1acsnakemake.io\nLog\nq\x1b)\x81q\x1c}q\x1dh\x07}q\x1esbX\x04\x00\x00\x00ruleq\x1fX\x05\x00\x00\x00getGCq X\x06\x00\x00\x00configq!}q"X\t\x00\x00\x00resourcesq#csnakemake.io\nResources\nq$)\x81q%(K\x01K\x01e}q&(X\x06\x00\x00\x00_nodesq\'K\x01h\x07}q((h\'K\x00N\x86q)X\x06\x00\x00\x00_coresq*K\x01N\x86q+uh*K\x01ubub.')
######## Original script #########
from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
import numpy as np


def gcPercentage():
    try:
        file = open(snakemake.input[0], "r")
    except IOError:
        print("File broken")

    percentages = []
    for line in file.readlines():
        line = line.split("\t")
        seq = line[5]
        gen = line[0]
        gcseq = GC(seq)
        percentages.append([gen, gcseq])

    return percentages


def plotPercentage(gc):
    plt.style.use('ggplot')
    i = 0


    for x in range(0,len(gc),25):
        end = x + 25
        gene = []
        gcList = []
        atList = []
        for x in gc[x:end]:
            gene.append(x[0])
            gcList.append(x[1])
            atList.append(100-x[1])


        gcPerc = np.array(gcList)
        atPerc = np.array(atList)

        ind = [x for x, _ in enumerate(gene)]

        plt.bar(ind, gcPerc, width=0.5, label='GC %', color='yellow', bottom=atPerc)
        plt.bar(ind, atPerc, width=0.5, label='AT %', color='black')

        plt.xticks(ind, gene)
        plt.ylabel("Percentage")
        plt.xlabel("GeneID")
        plt.legend(loc="upper right")
        plt.title("GC % per GeneID")
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

        
        
        #plt.show()
        plt.savefig(snakemake.output[i])
		i += 1
        plt.close()

def main():
    gc = gcPercentage()
    plot = plotPercentage(gc)

main()
