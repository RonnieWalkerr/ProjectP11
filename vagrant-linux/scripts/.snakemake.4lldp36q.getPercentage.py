
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00wildcardsq\tcsnakemake.io\nWildcards\nq\n)\x81q\x0b}q\x0ch\x07}q\rsbX\x06\x00\x00\x00paramsq\x0ecsnakemake.io\nParams\nq\x0f)\x81q\x10}q\x11h\x07}q\x12sbX\x06\x00\x00\x00outputq\x13csnakemake.io\nOutputFiles\nq\x14)\x81q\x15X\x17\x00\x00\x00./data/sorted_data2.txtq\x16a}q\x17h\x07}q\x18sbX\x04\x00\x00\x00ruleq\x19X\x05\x00\x00\x00getGCq\x1aX\x06\x00\x00\x00configq\x1b}q\x1cX\x05\x00\x00\x00inputq\x1dcsnakemake.io\nInputFiles\nq\x1e)\x81q\x1f}q h\x07}q!sbX\t\x00\x00\x00resourcesq"csnakemake.io\nResources\nq#)\x81q$(K\x01K\x01e}q%(X\x06\x00\x00\x00_nodesq&K\x01X\x06\x00\x00\x00_coresq\'K\x01h\x07}q((h&K\x00N\x86q)h\'K\x01N\x86q*uubX\x07\x00\x00\x00threadsq+K\x01ub.')
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
