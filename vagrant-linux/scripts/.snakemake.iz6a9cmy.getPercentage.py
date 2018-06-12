
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05X\x17\x00\x00\x00./data/sorted_data2.txtq\x06a}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\x05\x00\x00\x00inputq\ncsnakemake.io\nInputFiles\nq\x0b)\x81q\x0c}q\rh\x08}q\x0esbX\t\x00\x00\x00resourcesq\x0fcsnakemake.io\nResources\nq\x10)\x81q\x11(K\x01K\x01e}q\x12(X\x06\x00\x00\x00_coresq\x13K\x01h\x08}q\x14(h\x13K\x00N\x86q\x15X\x06\x00\x00\x00_nodesq\x16K\x01N\x86q\x17uh\x16K\x01ubX\x06\x00\x00\x00paramsq\x18csnakemake.io\nParams\nq\x19)\x81q\x1a}q\x1bh\x08}q\x1csbX\t\x00\x00\x00wildcardsq\x1dcsnakemake.io\nWildcards\nq\x1e)\x81q\x1f}q h\x08}q!sbX\x03\x00\x00\x00logq"csnakemake.io\nLog\nq#)\x81q$}q%h\x08}q&sbX\x04\x00\x00\x00ruleq\'X\x05\x00\x00\x00getGCq(X\x07\x00\x00\x00threadsq)K\x01X\x06\x00\x00\x00configq*}q+ub.')
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
