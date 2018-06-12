
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00getGCq\x04X\x06\x00\x00\x00outputq\x05csnakemake.io\nOutputFiles\nq\x06)\x81q\x07X\x16\x00\x00\x00./data/sorted_data.txtq\x08a}q\tX\x06\x00\x00\x00_namesq\n}q\x0bsbX\x06\x00\x00\x00paramsq\x0ccsnakemake.io\nParams\nq\r)\x81q\x0e}q\x0fh\n}q\x10sbX\x03\x00\x00\x00logq\x11csnakemake.io\nLog\nq\x12)\x81q\x13}q\x14h\n}q\x15sbX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18}q\x19h\n}q\x1asbX\t\x00\x00\x00resourcesq\x1bcsnakemake.io\nResources\nq\x1c)\x81q\x1d(K\x01K\x01e}q\x1e(X\x06\x00\x00\x00_coresq\x1fK\x01h\n}q (h\x1fK\x00N\x86q!X\x06\x00\x00\x00_nodesq"K\x01N\x86q#uh"K\x01ubX\t\x00\x00\x00wildcardsq$csnakemake.io\nWildcards\nq%)\x81q&}q\'h\n}q(sbX\x06\x00\x00\x00configq)}q*X\x07\x00\x00\x00threadsq+K\x01ub.')
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
