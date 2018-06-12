
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00getGCq\x04X\x07\x00\x00\x00threadsq\x05K\x01X\t\x00\x00\x00resourcesq\x06csnakemake.io\nResources\nq\x07)\x81q\x08(K\x01K\x01e}q\t(X\x06\x00\x00\x00_nodesq\nK\x01X\x06\x00\x00\x00_namesq\x0b}q\x0c(X\x06\x00\x00\x00_coresq\rK\x00N\x86q\x0eh\nK\x01N\x86q\x0fuh\rK\x01ubX\t\x00\x00\x00wildcardsq\x10csnakemake.io\nWildcards\nq\x11)\x81q\x12}q\x13h\x0b}q\x14sbX\x06\x00\x00\x00paramsq\x15csnakemake.io\nParams\nq\x16)\x81q\x17}q\x18h\x0b}q\x19sbX\x06\x00\x00\x00configq\x1a}q\x1bX\x05\x00\x00\x00inputq\x1ccsnakemake.io\nInputFiles\nq\x1d)\x81q\x1e}q\x1fh\x0b}q sbX\x03\x00\x00\x00logq!csnakemake.io\nLog\nq")\x81q#}q$h\x0b}q%sbX\x06\x00\x00\x00outputq&csnakemake.io\nOutputFiles\nq\')\x81q(X\x17\x00\x00\x00./data/sorted_data2.txtq)a}q*h\x0b}q+sbub.')
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
